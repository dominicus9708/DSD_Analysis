#!/usr/bin/env python3
"""Numerical witness for the admissible radial axis/self-field threshold model.

Model
-----
Uniform spherical source, s=r/R in [0,1].

Field:
    -(1/s^2) d/ds [s^2 p(a) u_s] = lambda u,
    p(a) = exp(-2 beta a / 3),
    epsilon = 2 lambda / 3.

Axis response:
    -ell^2 (a_ss + 2 a_s/s - 6 a/s^2) + a
        = 2 beta chi (u_s/u)^2,
    0 <= a <= 1.

The default axis boundary condition is the variationally natural free boundary
(a_s(1)=0).  A compact Dirichlet control a(1)=0 is also available.
At the spectral endpoint, matching to U_out = 1 + c/s gives
    u(1) + p(1) u_s(1) = 0.

This script is a reproducibility/control tool, not a derivation of a universal
structural-gravity law.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq, minimize


BASELINE_EPSILON = math.pi**2 / 6.0


@dataclass
class Result:
    epsilon: float
    lam: float
    s: np.ndarray
    u: np.ndarray
    ylog: np.ndarray
    a: np.ndarray
    p: np.ndarray
    iterations: int
    residual: float

    @property
    def max_a(self) -> float:
        return float(np.max(self.a))

    @property
    def saturation_fraction(self) -> float:
        return float(np.mean(self.a > 1.0 - 1.0e-5))


def field_eigen(p_s: np.ndarray, s_grid: np.ndarray, lam_hint: float | None = None):
    """First radial eigenpair for a fixed positive p(s)."""
    p_interp = PchipInterpolator(s_grid, p_s)
    s0 = 1.0e-5

    def boundary_value(lam: float, return_sol: bool = False):
        p0 = float(p_interp(s0))
        u0 = 1.0 - lam * s0 * s0 / (6.0 * p0)
        flux0 = -lam * s0**3 / 3.0

        def rhs(s, state):
            u, flux = state
            p = float(p_interp(s))
            return flux / (s * s * p), -lam * s * s * u

        sol = solve_ivp(
            rhs,
            (s0, 1.0),
            (u0, flux0),
            rtol=2.0e-8,
            atol=1.0e-10,
            dense_output=return_sol,
            max_step=0.025,
        )
        value = sol.y[0, -1] + sol.y[1, -1]
        return (value, sol) if return_sol else value

    if lam_hint is not None:
        lo = max(1.0e-6, 0.7 * lam_hint)
        hi = 1.3 * lam_hint + 1.0e-4
        vlo = boundary_value(lo)
        vhi = boundary_value(hi)
    else:
        lo = 1.0e-6
        hi = 0.35
        vlo = boundary_value(lo)
        vhi = boundary_value(hi)

    if vlo * vhi > 0.0:
        lo = 1.0e-6
        vlo = boundary_value(lo)
        hi = 0.35
        vhi = boundary_value(hi)
        while vlo * vhi > 0.0 and hi < 12.0:
            lo, vlo = hi, vhi
            hi += 0.35
            vhi = boundary_value(hi)

    if vlo * vhi > 0.0:
        raise RuntimeError("Could not bracket the first radial eigenvalue.")

    lam = brentq(boundary_value, lo, hi, xtol=2.0e-10, rtol=2.0e-10)
    _, sol = boundary_value(lam, return_sol=True)
    values = sol.sol(np.maximum(s_grid, s0))
    u = values[0]
    flux = values[1]
    u[0] = 1.0
    flux[0] = 0.0

    u_s = np.zeros_like(s_grid)
    mask = s_grid > 0.0
    u_s[mask] = flux[mask] / (s_grid[mask] ** 2 * p_s[mask])
    ylog = u_s / u
    return lam, u, ylog


def axis_response(
    ylog: np.ndarray,
    s: np.ndarray,
    beta: float,
    chi: float,
    ell: float,
    bc: str,
    a0: np.ndarray | None = None,
):
    """Bound-constrained convex axis subproblem for fixed u_s/u."""
    drive = 2.0 * beta * chi * ylog * ylog
    n = len(s)
    h = s[1] - s[0]

    if ell == 0.0:
        a = np.clip(drive, 0.0, 1.0)
        a[0] = 0.0
        if bc == "dirichlet":
            a[-1] = 0.0
        return a

    if bc == "neumann":
        ids = np.arange(1, n)
    elif bc == "dirichlet":
        ids = np.arange(1, n - 1)
    else:
        raise ValueError("bc must be 'neumann' or 'dirichlet'")

    w = np.full(n, h)
    w[[0, -1]] = h / 2.0
    s_mid = 0.5 * (s[:-1] + s[1:])
    potential = 6.0 * ell * ell + s * s
    edge = ell * ell * s_mid * s_mid / h

    def assemble(x):
        a = np.zeros(n)
        a[ids] = x
        return a

    def energy_grad(x):
        a = assemble(x)
        da = np.diff(a)
        energy = (
            0.5 * np.sum(edge * da * da)
            + 0.5 * np.sum(w * potential * a * a)
            - np.sum(w * s * s * drive * a)
        )
        grad = w * (potential * a - s * s * drive)
        edge_grad = edge * da
        grad[:-1] -= edge_grad
        grad[1:] += edge_grad
        return energy, grad[ids]

    if a0 is None:
        x0 = np.clip(drive[ids], 0.0, 1.0)
    else:
        x0 = np.clip(a0[ids], 0.0, 1.0)

    result = minimize(
        lambda x: energy_grad(x)[0],
        x0,
        jac=lambda x: energy_grad(x)[1],
        method="L-BFGS-B",
        bounds=[(0.0, 1.0)] * len(ids),
        options={"ftol": 1.0e-12, "gtol": 2.0e-8, "maxiter": 800},
    )
    return assemble(result.x)


def solve_coupled(
    beta: float,
    chi: float,
    ell: float,
    bc: str = "neumann",
    grid: int = 321,
    relaxation: float = 0.25,
    tolerance: float = 1.0e-6,
    max_iterations: int = 220,
):
    s = np.linspace(0.0, 1.0, grid)
    a = np.zeros_like(s)
    lam_hint = None
    previous_residual = None

    for iteration in range(max_iterations):
        p = np.exp(-2.0 * beta * a / 3.0)
        lam, u, ylog = field_eigen(p, s, lam_hint)
        a_new = axis_response(ylog, s, beta, chi, ell, bc, a)
        residual = float(np.max(np.abs(a_new - a)))

        if residual < tolerance:
            a = a_new
            break

        if previous_residual is not None and residual > 1.05 * previous_residual:
            relaxation = max(0.15, 0.75 * relaxation)

        a = (1.0 - relaxation) * a + relaxation * a_new
        previous_residual = residual
        lam_hint = lam

    p = np.exp(-2.0 * beta * a / 3.0)
    lam, u, ylog = field_eigen(p, s, lam_hint)
    return Result(
        epsilon=2.0 * lam / 3.0,
        lam=lam,
        s=s,
        u=u,
        ylog=ylog,
        a=a,
        p=p,
        iterations=iteration + 1,
        residual=residual,
    )


def local_saturation_chi(beta: float) -> float:
    """Exact onset at the s=1 endpoint for ell=0, beta>0."""
    return math.exp(-4.0 * beta / 3.0) / (2.0 * beta)


def print_result(beta, chi, ell, bc, result):
    print(f"beta={beta:g} chi={chi:g} ell={ell:g} bc={bc}")
    print(f"epsilon_c={result.epsilon:.12f}")
    print(f"baseline_pi2_over_6={BASELINE_EPSILON:.12f}")
    print(f"threshold_shift={BASELINE_EPSILON-result.epsilon:.12f}")
    print(f"max_a={result.max_a:.12f}")
    print(f"saturation_fraction={result.saturation_fraction:.6f}")
    print(f"iterations={result.iterations} residual={result.residual:.3e}")
    if ell == 0.0 and beta > 0.0:
        print(f"local_endpoint_chi_sat={local_saturation_chi(beta):.12f}")
    if beta > 0.75 and ell == 0.0:
        print("warning=beta>3/4: local eliminated flux law can lose monotonicity before saturation")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--beta", type=float, default=0.5)
    parser.add_argument("--chi", type=float, default=0.5)
    parser.add_argument("--ell", type=float, default=0.1)
    parser.add_argument("--bc", choices=("neumann", "dirichlet"), default="neumann")
    parser.add_argument("--grid", type=int, default=321)
    args = parser.parse_args()

    result = solve_coupled(
        beta=args.beta,
        chi=args.chi,
        ell=args.ell,
        bc=args.bc,
        grid=args.grid,
    )
    print_result(args.beta, args.chi, args.ell, args.bc, result)


if __name__ == "__main__":
    main()
