# DSD Gravity Research Log — Experiments 566–581

Date: 2026-09-05
Status: common-action consistency correction, constrained static continuation, and pseudo-arclength branch audit

Historical repository path retains `structural_gravity_logs` for continuity. Current working name may be read as DSD Gravity / Gravity in Dimensional-Structural Describability.

## Experiment 566 — Common-action consistency audit

The previously studied admissible radial system combined

\[
-\frac1{s^2}\frac{d}{ds}\left[s^2p(a)u_s\right]=\frac{3\epsilon}{2}u,
\qquad
p(a)=e^{-2\beta_Aa/3},
\]

with the scale-invariant axis drive

\[
-\ell_A^2L_2a+a
=2\beta_A\chi_A\left(\frac{u_s}{u}\right)^2.
\]

This is a legitimate conditional mixed/nonreciprocal constitutive model if the field-sector metric dependence and the axis drive are supplied independently. However, it is **not** the Euler system of one reciprocal common action in which `a` is varied through the field metric `p(a)`.

Therefore a full symmetric Hessian cannot be claimed for that mixed branch without an additional reciprocal closure.

### Verdict

Experiments 553–565 remain valid for their stated scale-invariant axis-drive specialization, but their strong-coupling fold diagnostic must not be silently promoted to the reciprocal common-action branch.

---

## Experiment 567 — Reciprocal common-action energy

For a uniform sphere, introduce the dimensionless physical, exterior-normalized field `U` and the admissible radial axis amplitude `0<=a<=1`.

A reciprocal static energy yielding the field metric and axis backreaction together is

\[
\boxed{
\mathcal E[U,a]
=
\int_0^1
\left[
 s^2p(a)U_s^2
-\frac{3\epsilon}{2}s^2U^2
\right]ds
+[U(1)-1]^2
+\frac1{6\chi_A}
\int_0^1
\left[
 \ell_A^2(s^2a_s^2+6a^2)+s^2a^2
\right]ds.
}
\]

Here

\[
p(a)=e^{-2\beta_Aa/3}.
\]

The exterior term `[U(1)-1]^2` is the integrated harmonic exterior field energy and generates the matching condition automatically.

---

## Experiment 568 — Correct reciprocal Euler equations

Variation with respect to `U` gives

\[
\boxed{
-\frac1{s^2}\frac{d}{ds}
\left[s^2p(a)U_s\right]
=
\frac{3\epsilon}{2}U,
}
\]

with

\[
\boxed{U(1)+p(1)U_s(1)=1.}
\]

Variation with respect to the unconstrained interior of `a` gives

\[
\boxed{
-\ell_A^2L_2a+a
=
2\beta_A\chi_Ap(a)U_s^2.
}
\]

This differs from the earlier scale-invariant drive by the physical field normalization and by the metric factor `p(a)`.

---

## Experiment 569 — Why the normalization cancellation disappears

The exact `psi`-action contains the factor

\[
e^{-\psi}h_A^{ij}\partial_i\psi\partial_j\psi.
\]

Since

\[
U=e^{-\psi/2},
\qquad
\partial_i\psi=-2\partial_iU/U,
\]

one has

\[
\boxed{e^{-\psi}(\partial\psi)^2=4(\partial U)^2.}
\]

Thus in the reciprocal branch the axis drive is proportional to the physical normalized gradient `U_s^2`, not `(U_s/U)^2`.

### Consequence

The earlier statement that the diverging field normalization cancels out of the local axis drive applies only to the scale-invariant mixed branch. It does **not** apply to the reciprocal common-action branch.

---

## Experiment 570 — Saturation is forced near the reciprocal spectral endpoint

For positive `beta_A chi_A`, the finite-amplitude physical solution grows as the field support denominator approaches zero. At every fixed point with nonzero radial gradient, the common-action drive

\[
2\beta_A\chi_Ap(a)U_s^2
\]

therefore grows with the square of the physical normalization.

Because the admissible axis second moment requires

\[
0\le a\le1,
\]

the reciprocal branch generically reaches the upper axis bound before the unbounded unsaturated continuation can reach the original field endpoint.

---

## Experiment 571 — Fully saturated limiting axis profile

In the endpoint limit the field drive forces

\[
a(s)\to1
\]

for every fixed `s>0`, while center regularity retains the measure-zero condition `a(0)=0`.

The limiting radial coefficient is therefore

\[
\boxed{p_*=e^{-2\beta_A/3}}
\]

almost everywhere.

The shrinking regular center layer does not prevent this pointwise-a.e. limit because its weighted radial volume tends to zero.

---

## Experiment 572 — Exact analytic endpoint of the fully saturated branch

For constant `p_*`, the regular interior mode is

\[
U\propto\frac{\sin(ks)}{ks},
\qquad
k^2=\lambda/p_*.
\]

The critical homogeneous matching condition is

\[
u(1)+p_*u_s(1)=0,
\]

which reduces to

\[
\boxed{
(1-p_*)\sin k+p_*k\cos k=0.
}
\]

Let the first root in `(pi/2,pi)` be `k_*`. Then

\[
\boxed{
\epsilon_{*,\rm sat}
=\frac23p_*k_*^2.
}
\]

This is an exact endpoint formula inside the fully saturated radial common-action specialization.

---

## Experiment 573 — Saturated endpoint values

Representative values are

| beta_A | p_* | k_* | epsilon_sat |
|---:|---:|---:|---:|
| 0.1 | 0.9355069850 | 1.6134968749 | 1.6236485635 |
| 0.5 | 0.7165313106 | 1.7884900996 | 1.5279776241 |
| 0.75 | 0.6065306597 | 1.8998433259 | 1.4594763943 |
| 1.0 | 0.5134171190 | 2.0111686765 | 1.3844461855 |
| 2.0 | 0.2635971381 | 2.4264296185 | 1.0346294329 |

These are not universal DSD constants; they are consequences of the chosen reciprocal radial specialization.

---

## Experiment 574 — Role separation of beta_A versus chi_A and ell_A at the saturated endpoint

Once the endpoint limit has saturated `a=1` almost everywhere, the limiting coefficient `p_*` depends only on `beta_A`.

Therefore, within this endpoint branch,

\[
\boxed{
\chi_A,\ell_A
\text{ control the approach to saturation, while }
\beta_A
\text{ controls the limiting saturated geometry.}
}
\]

This does **not** mean `chi_A` and `ell_A` are dynamically irrelevant; they control when and how the bound becomes active.

---

## Experiment 575 — The beta_A=3/4 local flux fold is branch-specific

For the common action, at fixed `U` the `a`-dependent field term is proportional to

\[
e^{-c a}(\Delta U)^2,
\]

whose second derivative with respect to `a` is positive. Adding the positive restoration/stiffness functional leaves the fixed-`U` axis subproblem convex.

Therefore the earlier local eliminated-flux fold at

\[
\beta_A=3/4
\]

is **not** a universal feature of the reciprocal common-action model. It remains a valid warning for the earlier scale-invariant locally eliminated branch only.

---

## Experiment 576 — Representative reciprocal stable branch for beta_A=0.5

Control parameters:

\[
(\beta_A,\chi_A,\ell_A)=(0.5,0.5,0.1),
\]

finite-difference grid `N=61`.

Representative bound-constrained minima:

| epsilon | max U | max a | frozen-field minimum eigenvalue |
|---:|---:|---:|---:|
| 0.90 | 2.6246646 | 0.4956461 | 2.7782e-3 |
| 0.95 | 2.9161174 | 0.7138309 | 2.6780e-3 |
| 1.00 | 3.3466846 | 1.0000000 | 2.5015e-3 |
| 1.20 | 5.8517044 | 1.0000000 | 1.7048e-3 |
| 1.50 | 73.9937678 | 1.0000000 | 1.6480e-4 |
| 1.52 | 261.0565367 | 1.0000000 | 4.7300e-5 |

The axis bound activates between `epsilon=0.95` and `1.00`, well before the saturated field endpoint `1.5279776241`.

---

## Experiment 577 — Saturation-first control at moderate coupling

Following the unconstrained reciprocal stationary branch for the same `(0.5,0.5,0.1)` control gives

- at `epsilon=0.980`: `a_max ~= 0.945932`, Schur minimum `~=3.57e-3`;
- at `epsilon=0.985`: `a_max ~= 1.002198`, Schur minimum `~=3.32e-3`.

Linear interpolation places the first `a_max=1` contact near

\[
\boxed{\epsilon_{\rm sat,onset}\approx0.9848}
\]

on the `N=61` control grid, while the coupled Schur complement is still positive.

### Verdict

For this moderate-coupling control, **admissibility saturation occurs before any unsaturated coupled Hessian zero mode**.

---

## Experiment 578 — Strong-coupling direct Newton branch for beta_A=2

For

\[
(\beta_A,\chi_A,\ell_A)=(2.0,0.5,0.1)
\]

and `N=61`, direct Newton continuation of the unsaturated stationary equations gives

| epsilon | max a | max U | Schur minimum |
|---:|---:|---:|---:|
| 0.520 | 0.44771 | 1.69352 | 3.9699e-3 |
| 0.526 | 0.51523 | 1.72931 | 2.7193e-3 |
| 0.528 | 0.55477 | 1.74818 | 1.8447e-3 |
| 0.529 | 0.59030 | 1.76400 | 9.8181e-4 |

Ordinary parameter continuation fails near `epsilon ~=0.53`, motivating pseudo-arclength continuation rather than interpreting the failure as a physical endpoint.

---

## Experiment 579 — Pseudo-arclength resolves the strong-coupling fold

Pseudo-arclength continuation across the same stationary branch gives the turning sequence

- `epsilon=0.529326755`, `a_max=0.620800`, Schur `=+1.8799e-4`;
- `epsilon=0.529337673`, `a_max=0.626487`, Schur `=+3.4764e-5`;
- `epsilon=0.529338048`, `a_max=0.627627`, Schur `=+3.8334e-6`;
- next arclength step: `epsilon=0.529337822`, `a_max=0.628769`, Schur `=-2.7192e-5`.

Linear interpolation of the Schur zero gives approximately

\[
\boxed{
\epsilon_{\rm fold}\approx0.52933802
}
\]

for this `N=61` control.

The parameter `epsilon` reaches a local maximum at the same point to numerical resolution.

### Verdict

This is a genuine **pre-saturation coupled zero mode / stationary fold witness** in the reciprocal common-action specialization.

---

## Experiment 580 — Unstable middle branch and admissibility contact

Continuing past the fold along the unstable stationary branch makes `epsilon` decrease while `a_max` increases.

Representative continuation points include

| branch point | epsilon | max a | Schur minimum |
|---:|---:|---:|---:|
| after fold | 0.52727 | 0.72749 | -2.94e-3 |
| later | 0.52012 | 0.85132 | -7.19e-3 |
| later | 0.51328 | 0.93389 | -1.03e-2 |
| near bound | 0.50749 | 0.99399 | -1.27e-2 |
| unconstrained crossing | 0.50660 | 1.00273 | -1.30e-2 |

Thus the unstable middle branch reaches the axis admissibility boundary near

\[
\boxed{
\epsilon\approx0.5066
}
\]

on this grid.

---

## Experiment 581 — Bistability and first-order-like equilibrium exchange

Bound-constrained minimization with different initial conditions finds two locally stable equilibria in part of the strong-coupling interval.

For `(beta_A,chi_A,ell_A)=(2,0.5,0.1)`, `N=61`:

### epsilon=0.510

- low-a branch: `a_max=0.38088`, `U_max=1.65276`, `E=-0.373341885`;
- saturated branch: `a_max=1`, `U_max=1.95043`, `E=-0.370091951`.

The low-a branch has lower energy.

### epsilon=0.520

- low-a branch: `a_max=0.44769`, `U_max=1.69352`, `E=-0.384849616`;
- saturated branch: `a_max=1`, `U_max=2.09290`, `E=-0.385511311`.

The saturated branch has lower energy.

Refining the energy difference gives the equilibrium preference exchange near

\[
\boxed{
\epsilon_{\rm eq}\approx0.51847
}
\]

for this finite-grid control. Near that point the two states differ substantially:

- low branch `a_max ~=0.435` and `U_max ~=1.686`;
- high branch `a_max=1` and `U_max ~=2.074`.

### Interpretation

The strong reciprocal toy therefore exhibits a **first-order-like static branch exchange with metastability/hysteresis structure**:

\[
\boxed{
\epsilon_{\rm lower}\sim0.5066
<
\epsilon_{\rm eq}\sim0.51847
<
\epsilon_{\rm upper}\sim0.529338.
}
\]

These numbers are grid- and specialization-dependent controls, not universal physical constants or a black-hole prediction.

## Consolidated verdict

The calculation splits the previous axis/self-field work into two legitimately different conditional branches:

1. **scale-invariant mixed branch** — axis drive proportional to `(U_s/U)^2`; previous Experiments 553–565 belong here;
2. **reciprocal common-action branch** — axis drive proportional to `p(a) U_s^2`; this branch admits a symmetric static Hessian and shows both saturation-first and fold-first regimes depending on coupling strength.

The common-action branch gives a substantially sharper nonlinear picture:

\[
\boxed{
\text{weak/moderate coupling}
\to
\text{saturation first}
}
\]

but

\[
\boxed{
\text{strong coupling}
\to
\text{coupled fold/zero mode}
\to
\text{metastable branch exchange}
\to
\text{axis-bound contact}.
}
\]

No claim of horizon formation, finite-time collapse, or universal coupling is made.

## Reproducibility

Added:

`audits/science/structural_gravity_logs/2026-09-05_common_action_axis_continuation.py`

Example from repository root:

```bash
python audits/science/structural_gravity_logs/2026-09-05_common_action_axis_continuation.py --beta 0.5 --chi 0.5 --ell 0.1 --epsilon 0.9 --grid 61
```

Exact saturated endpoint only:

```bash
python audits/science/structural_gravity_logs/2026-09-05_common_action_axis_continuation.py --beta 2.0 --saturated-endpoint
```

## Next audit target

1. repeat the fold and energy-exchange calculation at multiple grids to estimate continuum convergence;
2. map the boundary in `(beta_A,chi_A,ell_A)` between saturation-first and fold-first regimes;
3. add positive axis inertia `mu_A` and damping as separate constitutive controls;
4. dynamically ramp `epsilon` through the metastable interval to distinguish adiabatic switching, overshoot, hysteresis, and genuine finite-time instability.