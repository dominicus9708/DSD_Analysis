#!/usr/bin/env python3
"""Boundary audit for the reciprocal/common-action DSD-gravity radial branch.

This script reuses the stationary/common-action solver stored beside it as
`2026-09-05_common_action_axis_continuation.py` and adds:

1. pseudo-arclength tracing of the unsaturated stationary branch;
2. the coupled Schur-zero (fold) location;
3. the post-fold a_max=1 contact of the unconstrained middle branch;
4. low/high bounded-energy exchange estimates;
5. the fold-first / saturation-first control `a_fold - 1`;
6. the exact local (ell=0) constitutive monotonicity audit.

It is a reproducibility/control calculation for a conditional specialization,
not a derivation of a universal gravity law.
"""

from __future__ import annotations

import argparse
import importlib.util
import math
from pathlib import Path

import numpy as np
from scipy.optimize import brentq


HERE = Path(__file__).resolve().parent
BASE = HERE / "2026-09-05_common_action_axis_continuation.py"
spec = importlib.util.spec_from_file_location("dsd_common_action", BASE)
ca = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(ca)


def stationary_from_bounded(epsilon, beta, chi, ell, grid, initial="low"):
    U, a, info = ca.solve_bounded(
        epsilon, beta, chi, ell, grid, initial=initial,
        tolerance=2.0e-7, max_iterations=500,
    )
    if U is None:
        raise RuntimeError(f"bounded seed failed: {info}")
    g = ca.make_grid(grid)
    x0 = np.concatenate([U, a[1:]])
    result = ca.newton_stationary(epsilon, x0, beta, chi, ell, g)
    if not result.success:
        raise RuntimeError(f"stationary Newton seed failed: {result.message}")
    return result.x, g


def trace_branch(beta, chi, ell, grid, e0, e1, ds, max_steps):
    x0, g = stationary_from_bounded(e0, beta, chi, ell, grid)
    x1, _ = stationary_from_bounded(e1, beta, chi, ell, grid)
    z0 = np.concatenate([x0, [e0]])
    z1 = np.concatenate([x1, [e1]])
    rows = []

    def record(z):
        x = z[:-1]
        epsilon = float(z[-1])
        _, H = ca.full_gradient_hessian(x, epsilon, beta, chi, ell, g, True)
        a = np.concatenate([[0.0], x[grid:]])
        return [epsilon, float(np.max(a)), ca.schur_minimum(H, grid)]

    rows.append(record(z0))
    rows.append(record(z1))
    for _ in range(max_steps):
        step = ca.pseudo_arclength_step(z0, z1, ds, beta, chi, ell, g)
        if not step.success:
            break
        z2 = step.x
        rows.append(record(z2))
        z0, z1 = z1, z2
        if rows[-1][1] > 1.05 and rows[-1][0] < rows[-2][0]:
            break
    return np.asarray(rows)


def linear_zero(x0, y0, x1, y1):
    t = -y0 / (y1 - y0)
    return x0 + t * (x1 - x0)


def branch_metrics(rows):
    fold_epsilon = None
    fold_a = None
    for i in range(len(rows) - 1):
        if rows[i, 2] * rows[i + 1, 2] <= 0.0:
            fold_epsilon = linear_zero(rows[i, 0], rows[i, 2], rows[i + 1, 0], rows[i + 1, 2])
            fold_a = linear_zero(rows[i, 1], rows[i, 2], rows[i + 1, 1], rows[i + 1, 2])
            break

    imax = int(np.argmax(rows[:, 0]))
    a_contact = None
    for i in range(imax, len(rows) - 1):
        y0 = rows[i, 1] - 1.0
        y1 = rows[i + 1, 1] - 1.0
        if y0 * y1 <= 0.0:
            a_contact = linear_zero(rows[i, 0], y0, rows[i + 1, 0], y1)
            break
    return fold_epsilon, fold_a, a_contact


def energy_difference(epsilon, beta, chi, ell, grid):
    Ul, al, il = ca.solve_bounded(
        epsilon, beta, chi, ell, grid, initial="low",
        tolerance=3.0e-7, max_iterations=500,
    )
    Uh, ah, ih = ca.solve_bounded(
        epsilon, beta, chi, ell, grid, initial="high",
        tolerance=3.0e-7, max_iterations=500,
    )
    if Ul is None or Uh is None:
        raise RuntimeError("bounded energy branch unavailable")
    return float(il["energy"] - ih["energy"]), float(np.max(al)), float(np.max(ah))


def energy_exchange(beta, chi, ell, grid, elo, ehi):
    def f(e):
        return energy_difference(e, beta, chi, ell, grid)[0]
    root = brentq(f, elo, ehi, xtol=2.0e-7)
    diff, alo, ahi = energy_difference(root, beta, chi, ell, grid)
    return root, diff, alo, ahi


def fold_saturation_boundary(beta, chi, ell, grid, e0, e1, ds, max_steps):
    rows = trace_branch(beta, chi, ell, grid, e0, e1, ds, max_steps)
    fold_eps, fold_a, _ = branch_metrics(rows)
    if fold_eps is None:
        raise RuntimeError("no Schur-zero found in continuation window")
    return fold_a - 1.0, fold_eps, fold_a


def local_common_action_a_fold(beta):
    """Axis amplitude at local flux-monotonicity loss for ell=0."""
    return 3.0 / (2.0 * beta)


def print_local_audit(beta, chi):
    # z=(2 beta/3)a=W((4 beta^2 chi/3) U_s^2)
    a_fold = local_common_action_a_fold(beta)
    print(f"local_beta={beta:.12g}")
    print(f"local_a_fold={a_fold:.12g}")
    print("local_fold_first=" + str(a_fold < 1.0).lower())
    print("exact_local_fold_saturation_boundary_beta=1.5")
    if beta > 0.0 and chi > 0.0:
        us2_fold = 3.0 * math.e / (4.0 * beta * beta * chi)
        print(f"local_Us2_fold={us2_fold:.12g}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=("branch", "energy", "beta-boundary", "local"), default="branch")
    p.add_argument("--beta", type=float, default=2.0)
    p.add_argument("--chi", type=float, default=0.5)
    p.add_argument("--ell", type=float, default=0.1)
    p.add_argument("--grid", type=int, default=61)
    p.add_argument("--e0", type=float, default=0.45)
    p.add_argument("--e1", type=float, default=0.49)
    p.add_argument("--ds", type=float, default=0.02)
    p.add_argument("--max-steps", type=int, default=260)
    p.add_argument("--energy-lo", type=float, default=0.515)
    p.add_argument("--energy-hi", type=float, default=0.521)
    p.add_argument("--beta-lo", type=float, default=1.05)
    p.add_argument("--beta-hi", type=float, default=1.07)
    args = p.parse_args()

    if args.mode == "local":
        print_local_audit(args.beta, args.chi)
        return

    if args.mode == "branch":
        rows = trace_branch(args.beta, args.chi, args.ell, args.grid, args.e0, args.e1, args.ds, args.max_steps)
        fold_eps, fold_a, a_contact = branch_metrics(rows)
        print(f"grid={args.grid}")
        print(f"fold_epsilon={fold_eps}")
        print(f"fold_a_max={fold_a}")
        print(f"middle_branch_a1_contact_epsilon={a_contact}")
        return

    if args.mode == "energy":
        e, diff, alo, ahi = energy_exchange(args.beta, args.chi, args.ell, args.grid, args.energy_lo, args.energy_hi)
        print(f"energy_exchange_epsilon={e:.12f}")
        print(f"energy_difference={diff:.6e}")
        print(f"low_a_max={alo:.12f}")
        print(f"high_a_max={ahi:.12f}")
        return

    def control(beta):
        value, _, _ = fold_saturation_boundary(beta, args.chi, args.ell, args.grid, args.e0, args.e1, args.ds, args.max_steps)
        print(f"beta={beta:.9f} a_fold_minus_1={value:.9e}")
        return value

    beta_star = brentq(control, args.beta_lo, args.beta_hi, xtol=2.0e-5)
    value, fold_eps, fold_a = fold_saturation_boundary(beta_star, args.chi, args.ell, args.grid, args.e0, args.e1, args.ds, args.max_steps)
    print(f"beta_star={beta_star:.9f}")
    print(f"fold_epsilon={fold_eps:.9f}")
    print(f"fold_a_max={fold_a:.9f}")
    print(f"classification_control={value:.3e}")


if __name__ == "__main__":
    main()
