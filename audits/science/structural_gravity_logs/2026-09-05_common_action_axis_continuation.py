#!/usr/bin/env python3
"""Common-action continuation witness for the DSD-gravity radial axis branch.

Historical repository path keeps the earlier `structural_gravity_logs` name for
continuity. The model tested here is the reciprocal/common-action alternative to
the earlier scale-invariant axis-drive branch.

Dimensionless static energy (uniform sphere):

    E[U,a] = int_0^1 [s^2 p(a) U_s^2 - (3 eps/2) s^2 U^2] ds
             + (U(1)-1)^2
             + 1/(6 chi) int_0^1 [ell^2(s^2 a_s^2+6 a^2)+s^2 a^2] ds,

    p(a)=exp(-2 beta a/3),  0 <= a <= 1.

Euler equations in the interior are

    -s^-2 d/ds[s^2 p(a) U_s] = (3 eps/2) U,

    -ell^2(a_ss+2 a_s/s-6 a/s^2)+a = 2 beta chi p(a) U_s^2.

The exterior normalization is encoded by the natural boundary condition

    U(1)+p(1)U_s(1)=1.

This script supplies:
- bound-constrained alternating minimization for a stable equilibrium;
- the exact fully-saturated endpoint for a=1 almost everywhere;
- an unconstrained Newton stationary solver;
- pseudo-arclength continuation of the unsaturated stationary branch;
- the Schur-complement Hessian diagnostic before an axis bound activates.

This is a reproducibility/control calculation for a conditional specialization,
not a derivation of a universal gravity law.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np
from scipy.optimize import brentq, minimize, root


@dataclass
class Grid:
    s: np.ndarray
    h: float
    sm: np.ndarray
    w: np.ndarray


def make_grid(n: int) -> Grid:
    s = np.linspace(0.0, 1.0, n)
    h = 1.0 / (n - 1)
    sm = 0.5 * (s[:-1] + s[1:])
    w = np.full(n, h)
    w[[0, -1]] = h / 2.0
    return Grid(s=s, h=h, sm=sm, w=w)


def saturated_endpoint(beta: float) -> tuple[float, float, float]:
    """Exact endpoint for the limiting profile a=1 almost everywhere."""
    p = math.exp(-2.0 * beta / 3.0)

    def f(k: float) -> float:
        return (1.0 - p) * math.sin(k) + p * k * math.cos(k)

    k = brentq(f, math.pi / 2.0 + 1.0e-12, math.pi - 1.0e-12)
    epsilon = 2.0 * p * k * k / 3.0
    return p, k, epsilon


def field_matrix(a: np.ndarray, beta: float, epsilon: float, g: Grid):
    p = np.exp(-beta * (a[:-1] + a[1:]) / 3.0)
    c = p * g.sm * g.sm / g.h
    n = len(g.s)
    A = np.zeros((n, n))
    for i, ce in enumerate(c):
        A[i, i] += ce
        A[i, i + 1] -= ce
        A[i + 1, i] -= ce
        A[i + 1, i + 1] += ce
    A[np.arange(n), np.arange(n)] -= 1.5 * epsilon * g.w * g.s * g.s
    A[-1, -1] += 1.0
    return A, p, c


def axis_energy_gradient(
    x: np.ndarray,
    U: np.ndarray,
    beta: float,
    chi: float,
    ell: float,
    g: Grid,
):
    n = len(g.s)
    a = np.zeros(n)
    a[1:] = x
    p = np.exp(-beta * (a[:-1] + a[1:]) / 3.0)
    dU = np.diff(U)
    c = p * g.sm * g.sm / g.h
    da = np.diff(a)

    energy = np.sum(c * dU * dU)
    energy += (
        ell * ell * np.sum(g.sm * g.sm * da * da / g.h)
        + np.sum(g.w * (6.0 * ell * ell + g.s * g.s) * a * a)
    ) / (6.0 * chi)

    grad = np.zeros(n)
    edge_field = -(beta / 3.0) * c * dU * dU
    grad[:-1] += edge_field
    grad[1:] += edge_field

    edge_axis = ell * ell * g.sm * g.sm * da / (3.0 * chi * g.h)
    grad[:-1] -= edge_axis
    grad[1:] += edge_axis
    grad += g.w * (6.0 * ell * ell + g.s * g.s) * a / (3.0 * chi)
    return float(energy), grad[1:]


def total_energy(
    U: np.ndarray,
    a: np.ndarray,
    epsilon: float,
    beta: float,
    chi: float,
    ell: float,
    g: Grid,
) -> float:
    p = np.exp(-beta * (a[:-1] + a[1:]) / 3.0)
    c = p * g.sm * g.sm / g.h
    dU = np.diff(U)
    da = np.diff(a)
    energy = np.sum(c * dU * dU)
    energy -= 1.5 * epsilon * np.sum(g.w * g.s * g.s * U * U)
    energy += (U[-1] - 1.0) ** 2
    energy += (
        ell * ell * np.sum(g.sm * g.sm * da * da / g.h)
        + np.sum(g.w * (6.0 * ell * ell + g.s * g.s) * a * a)
    ) / (6.0 * chi)
    return float(energy)


def solve_bounded(
    epsilon: float,
    beta: float,
    chi: float,
    ell: float,
    grid: int,
    initial: str = "low",
    a0: np.ndarray | None = None,
    tolerance: float = 1.0e-7,
    max_iterations: int = 250,
):
    g = make_grid(grid)
    n = grid
    if a0 is not None:
        a = np.array(a0, copy=True)
    elif initial == "high":
        a = np.ones(n)
        a[0] = 0.0
    else:
        a = np.zeros(n)

    rhs = np.zeros(n)
    rhs[-1] = 1.0

    for iteration in range(max_iterations):
        A, _, _ = field_matrix(a, beta, epsilon, g)
        try:
            np.linalg.cholesky(A)
        except np.linalg.LinAlgError:
            return None, a, {
                "status": "field_not_positive_definite",
                "iterations": iteration,
            }

        U = np.linalg.solve(A, rhs)
        result = minimize(
            lambda x: axis_energy_gradient(x, U, beta, chi, ell, g)[0],
            a[1:],
            jac=lambda x: axis_energy_gradient(x, U, beta, chi, ell, g)[1],
            method="L-BFGS-B",
            bounds=[(0.0, 1.0)] * (n - 1),
            options={"ftol": 1.0e-13, "gtol": 2.0e-9, "maxiter": 1200},
        )
        a_new = np.zeros(n)
        a_new[1:] = result.x
        residual = float(np.max(np.abs(a_new - a)))
        if residual < tolerance:
            a = a_new
            A, _, _ = field_matrix(a, beta, epsilon, g)
            U = np.linalg.solve(A, rhs)
            return U, a, {
                "status": "ok",
                "iterations": iteration + 1,
                "residual": residual,
                "field_min_eigenvalue": float(np.linalg.eigvalsh(A)[0]),
                "energy": total_energy(U, a, epsilon, beta, chi, ell, g),
            }
        a = 0.5 * a + 0.5 * a_new

    return U, a, {
        "status": "max_iterations",
        "iterations": max_iterations,
        "residual": residual,
        "energy": total_energy(U, a, epsilon, beta, chi, ell, g),
    }


def full_gradient_hessian(
    x: np.ndarray,
    epsilon: float,
    beta: float,
    chi: float,
    ell: float,
    g: Grid,
    need_hessian: bool = True,
):
    n = len(g.s)
    U = x[:n]
    a = np.zeros(n)
    a[1:] = x[n:]
    p = np.exp(-beta * (a[:-1] + a[1:]) / 3.0)
    c = p * g.sm * g.sm / g.h
    dU = np.diff(U)

    grad_u = np.zeros(n)
    edge = 2.0 * c * dU
    grad_u[:-1] -= edge
    grad_u[1:] += edge
    grad_u -= 3.0 * epsilon * g.w * g.s * g.s * U
    grad_u[-1] += 2.0 * (U[-1] - 1.0)

    grad_a = np.zeros(n)
    edge_field = -(beta / 3.0) * c * dU * dU
    grad_a[:-1] += edge_field
    grad_a[1:] += edge_field
    da = np.diff(a)
    edge_axis = ell * ell * g.sm * g.sm * da / (3.0 * chi * g.h)
    grad_a[:-1] -= edge_axis
    grad_a[1:] += edge_axis
    grad_a += g.w * (6.0 * ell * ell + g.s * g.s) * a / (3.0 * chi)

    gradient = np.concatenate([grad_u, grad_a[1:]])
    if not need_hessian:
        return gradient

    m = 2 * n - 1
    H = np.zeros((m, m))

    for i, ce in enumerate(c):
        value = 2.0 * ce
        H[i, i] += value
        H[i, i + 1] -= value
        H[i + 1, i] -= value
        H[i + 1, i + 1] += value
    H[np.arange(n), np.arange(n)] -= 3.0 * epsilon * g.w * g.s * g.s
    H[n - 1, n - 1] += 2.0

    for i, ce in enumerate(c):
        du = dU[i]
        endpoints = [j for j in (i, i + 1) if j > 0]
        for j in endpoints:
            col = n + j - 1
            H[i, col] += 2.0 * beta * ce * du / 3.0
            H[i + 1, col] -= 2.0 * beta * ce * du / 3.0
            H[col, i] = H[i, col]
            H[col, i + 1] = H[i + 1, col]
        for j in endpoints:
            for k in endpoints:
                H[n + j - 1, n + k - 1] += beta * beta * ce * du * du / 9.0

    for i, sm in enumerate(g.sm):
        value = ell * ell * sm * sm / (3.0 * chi * g.h)
        if i > 0:
            H[n + i - 1, n + i - 1] += value
        H[n + i, n + i] += value
        if i > 0:
            H[n + i - 1, n + i] -= value
            H[n + i, n + i - 1] -= value

    for j in range(1, n):
        H[n + j - 1, n + j - 1] += (
            g.w[j] * (6.0 * ell * ell + g.s[j] * g.s[j]) / (3.0 * chi)
        )

    return gradient, H


def schur_minimum(H: np.ndarray, n: int) -> float:
    Huu = H[:n, :n]
    Hua = H[:n, n:]
    Haa = H[n:, n:]
    S = Huu - Hua @ np.linalg.solve(Haa, Hua.T)
    return float(np.linalg.eigvalsh(S)[0])


def epsilon_derivative(x: np.ndarray, g: Grid) -> np.ndarray:
    n = len(g.s)
    out = np.zeros(2 * n - 1)
    out[:n] = -3.0 * g.w * g.s * g.s * x[:n]
    return out


def newton_stationary(
    epsilon: float,
    x0: np.ndarray,
    beta: float,
    chi: float,
    ell: float,
    g: Grid,
):
    return root(
        lambda x: full_gradient_hessian(
            x, epsilon, beta, chi, ell, g, need_hessian=False
        ),
        x0,
        jac=lambda x: full_gradient_hessian(
            x, epsilon, beta, chi, ell, g, need_hessian=True
        )[1],
        method="hybr",
        options={"xtol": 1.0e-10, "maxfev": 1800},
    )


def pseudo_arclength_step(
    z_previous: np.ndarray,
    z_current: np.ndarray,
    ds: float,
    beta: float,
    chi: float,
    ell: float,
    g: Grid,
):
    tangent = z_current - z_previous
    tangent /= np.linalg.norm(tangent)
    predictor = z_current + ds * tangent
    m = len(z_current) - 1

    def residual(z):
        x = z[:m]
        epsilon = float(z[m])
        r = full_gradient_hessian(
            x, epsilon, beta, chi, ell, g, need_hessian=False
        )
        arc = float(np.dot(tangent, z - predictor))
        return np.concatenate([r, [arc]])

    def jacobian(z):
        x = z[:m]
        epsilon = float(z[m])
        _, H = full_gradient_hessian(x, epsilon, beta, chi, ell, g, True)
        re = epsilon_derivative(x, g)
        J = np.zeros((m + 1, m + 1))
        J[:m, :m] = H
        J[:m, m] = re
        J[m, :] = tangent
        return J

    return root(
        residual,
        predictor,
        jac=jacobian,
        method="hybr",
        options={"xtol": 1.0e-10, "maxfev": 1800},
    )


def print_point(args):
    g = make_grid(args.grid)
    U, a, info = solve_bounded(
        args.epsilon,
        args.beta,
        args.chi,
        args.ell,
        args.grid,
        initial=args.initial,
    )
    p_sat, k_sat, eps_sat = saturated_endpoint(args.beta)
    print(f"beta={args.beta:g} chi={args.chi:g} ell={args.ell:g}")
    print(f"epsilon={args.epsilon:.12f}")
    print(f"status={info['status']}")
    print(f"fully_saturated_p={p_sat:.12f}")
    print(f"fully_saturated_k={k_sat:.12f}")
    print(f"fully_saturated_endpoint={eps_sat:.12f}")
    if U is not None:
        print(f"U_max={np.max(U):.12f}")
        print(f"a_max={np.max(a):.12f}")
        print(f"saturation_fraction={np.mean(a > 1.0-1.0e-6):.6f}")
        print(f"energy={info['energy']:.12f}")
        if np.max(a) < 1.0 - 1.0e-6:
            x = np.concatenate([U, a[1:]])
            _, H = full_gradient_hessian(
                x, args.epsilon, args.beta, args.chi, args.ell, g, True
            )
            print(f"schur_minimum={schur_minimum(H, args.grid):.12e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--beta", type=float, default=0.5)
    parser.add_argument("--chi", type=float, default=0.5)
    parser.add_argument("--ell", type=float, default=0.1)
    parser.add_argument("--epsilon", type=float, default=0.9)
    parser.add_argument("--grid", type=int, default=61)
    parser.add_argument("--initial", choices=("low", "high"), default="low")
    parser.add_argument(
        "--saturated-endpoint",
        action="store_true",
        help="Print only the exact a=1 limiting endpoint.",
    )
    args = parser.parse_args()

    if args.saturated_endpoint:
        p, k, eps = saturated_endpoint(args.beta)
        print(f"beta={args.beta:g}")
        print(f"p_star={p:.12f}")
        print(f"k_star={k:.12f}")
        print(f"epsilon_star={eps:.12f}")
        return

    print_point(args)


if __name__ == "__main__":
    main()
