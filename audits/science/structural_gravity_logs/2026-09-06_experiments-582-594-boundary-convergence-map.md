# DSD Gravity Research Log — Experiments 582–594

Date: 2026-09-06
Historical directory name `structural_gravity_logs` is retained for repository continuity. Current research name: DSD Gravity / Gravity in Dimensional-Structural Describability.

Status: reciprocal/common-action radial branch; grid convergence, fold/saturation classification, and local constitutive audit.

## Experiment 582 — Strong-branch fold grid convergence

Control parameters:

\[
(\beta_A,\chi_A,\ell_A)=(2,0.5,0.1).
\]

The unsaturated stationary branch was followed by pseudo-arclength continuation and the coupled Schur-complement zero was interpolated.

| radial grid N | fold epsilon | a_max at fold |
|---:|---:|---:|
| 41 | 0.52963563 | 0.62686 |
| 61 | 0.52933754 | 0.62777 |
| 81 | 0.52923284 | 0.62809 |
| 101 | 0.52918475 | 0.62824 |

The fold remains strictly pre-saturation on every grid tested.

### Verdict

The previously reported `epsilon_fold ~= 0.529338` at N=61 is not a one-grid artifact. The numerical value shifts downward with refinement, while the qualitative statement

\[
\boxed{a_{\max}^{\rm fold}<1}
\]

is stable.

---

## Experiment 583 — Middle-branch a=1 contact grid convergence

Continue the same unconstrained stationary branch past the fold until the middle branch reaches

\[
a_{\max}=1.
\]

| radial grid N | epsilon at a_max=1 contact |
|---:|---:|
| 41 | 0.50699700 |
| 61 | 0.50687974 |
| 81 | 0.50683849 |
| 101 | 0.50681921 |

### Verdict

The lower contact is also converging and remains well separated from the upper fold.

---

## Experiment 584 — Energy-exchange grid convergence

For the same parameters, solve the bounded low-alignment and high/saturated equilibria independently and compare the common-action energy.

Estimated energy-equality points:

| radial grid N | epsilon_eq |
|---:|---:|
| 41 | 0.51866516 |
| 61 | 0.51846452 |
| 81 | 0.51839827 |
| 101 | 0.51836659 |

At this point the two constrained stationary states exchange energetic preference.

### Verdict

The energy exchange remains between the lower middle-branch contact and the upper fold on every tested grid.

---

## Experiment 585 — h^2 extrapolation diagnostic

Because the finite-difference/trapezoidal discretization is nominally second order, fit the four-grid values to

\[
X_N=X_\infty+c h^2,
\qquad h=(N-1)^{-1}.
\]

The resulting diagnostic extrapolations are

\[
\boxed{\epsilon_{a=1}^{(h^2)}\approx0.50678555},
\]

\[
\boxed{\epsilon_{\rm eq}^{(h^2)}\approx0.51830871},
\]

\[
\boxed{\epsilon_{\rm fold}^{(h^2)}\approx0.52909879}.
\]

These are convergence diagnostics, not rigorous continuum error bounds.

The corresponding interval widths are approximately

\[
\epsilon_{\rm eq}-\epsilon_{a=1}\approx0.0115232,
\]

\[
\epsilon_{\rm fold}-\epsilon_{\rm eq}\approx0.0107901,
\]

and total coexistence width

\[
\boxed{\epsilon_{\rm fold}-\epsilon_{a=1}\approx0.0223132}.
\]

---

## Experiment 586 — Ordering is grid-stable

Across all tested grids,

\[
\boxed{
\epsilon_{a=1}
<
\epsilon_{\rm eq}
<
\epsilon_{\rm fold}.
}
\]

Interpretation inside this conditional static branch:

1. the unconstrained middle branch reaches the admissibility wall on the lower side;
2. the two bounded equilibria exchange energetic preference inside the coexistence interval;
3. the low-alignment branch terminates at the upper Schur-zero fold.

### Verdict

The first-order-like static branch-exchange interpretation survives grid refinement.

This remains a statement about the conditional common-action specialization, not a proof of a physical phase transition in nature.

---

## Experiment 587 — Fold-first / saturation-first control quantity

Define

\[
\boxed{\Delta_{FS}:=a_{\max}^{\rm fold}-1}.
\]

Then

- `Delta_FS < 0`: coupled Schur-zero/fold occurs before the axis admissibility bound is reached (`fold-first`);
- `Delta_FS > 0`: the unconstrained fold would lie outside the admissible axis domain, so physical continuation encounters `a=1` first (`saturation-first`);
- `Delta_FS = 0`: boundary between the two regimes.

This supplies a direct numerical classifier for parameter-space mapping.

---

## Experiment 588 — Finite-stiffness boundary at chi_A=0.5, ell_A=0.1

At N=41, continuation near the regime boundary gives

| beta_A | a_max at fold |
|---:|---:|
| 1.058 | 1.000503 |
| 1.059 | 0.999847 |
| 1.060 | 0.999193 |

Linear interpolation gives

\[
\boxed{\beta_{FS}^*(\chi_A=0.5,\ell_A=0.1)\approx1.0588}
\]

at this grid resolution.

This is a numerical boundary of the chosen reciprocal spherical specialization, not a universal DSD constant.

---

## Experiment 589 — Susceptibility slice of the fold/saturation boundary

At fixed

\[
\ell_A=0.1,
\]

N=41 control calculations give approximately

| chi_A | beta_FS^* |
|---:|---:|
| 0.25 | 0.889 |
| 0.50 | 1.059 |
| 1.00 | 1.208 |

### Verdict

For this slice, increasing axis susceptibility moves the fold-first boundary to larger `beta_A`.

This trend is empirical for the present finite-stiffness radial model; it is not promoted to a general theorem.

---

## Experiment 590 — Stiffness-length slice of the fold/saturation boundary

At fixed

\[
\chi_A=0.5,
\]

N=41 controls give approximately

| ell_A | beta_FS^* |
|---:|---:|
| 0.05 | 1.159 |
| 0.10 | 1.059 |
| 0.20 | 0.934 |
| 0.30 | 0.838 |

Thus, in this finite-stiffness slice,

\[
\boxed{\ell_A\uparrow\quad\Rightarrow\quad\beta_{FS}^*\downarrow}
\]

numerically.

The zero-stiffness limit is treated separately below because the algebraic axis elimination changes the structure of the problem and showed slow grid drift in the global fold classifier.

---

## Experiment 591 — Exact local elimination for the reciprocal ell_A=0 branch

For `ell_A=0` and before saturation, the common-action axis equation is

\[
\boxed{
a=2\beta_A\chi_A e^{-2\beta_Aa/3}U_s^2.
}
\]

Define

\[
z:=\frac{2\beta_Aa}{3}.
\]

Then

\[
\boxed{
z e^z
=\frac{4\beta_A^2\chi_A}{3}U_s^2,
}
\]

so

\[
\boxed{
a
=\frac{3}{2\beta_A}
W\!\left(\frac{4\beta_A^2\chi_A}{3}U_s^2\right).
}
\]

This is an exact algebraic elimination on the unsaturated local reciprocal branch.

---

## Experiment 592 — Exact local flux-monotonicity condition

The radial constitutive flux is

\[
q(v)=p(v)v,
\qquad
v=U_s,
\qquad
p=e^{-z}.
\]

Using

\[
z e^z=c v^2,
\qquad c=\frac{4\beta_A^2\chi_A}{3},
\]

one obtains

\[
\frac{dz}{dv}
=\frac{2z}{v(1+z)}.
\]

Therefore

\[
\boxed{
\frac{dq}{dv}
=e^{-z}\frac{1-z}{1+z}.
}
\]

The local eliminated flux loses monotonicity at

\[
\boxed{z=1}.
\]

Equivalently,

\[
\boxed{
a_{\rm fold}^{\rm local}=\frac{3}{2\beta_A}},
\]

and

\[
\boxed{
U_{s,\rm fold}^2
=\frac{3e}{4\beta_A^2\chi_A}.
}
\]

---

## Experiment 593 — Exact local saturation-versus-constitutive-fold boundary

The physical axis admissibility wall is

\[
a=1.
\]

The local constitutive fold lies inside the admissible interval iff

\[
\frac{3}{2\beta_A}<1.
\]

Thus

\[
\boxed{
\beta_A=\frac32
}
\]

is the exact **local constitutive** saturation/fold boundary of the reciprocal `ell_A=0` branch:

- `beta_A < 3/2`: local saturation occurs before local flux-monotonicity loss;
- `beta_A = 3/2`: they coincide;
- `beta_A > 3/2`: local flux fold is reached at `a<1`.

This differs from the earlier value

\[
\beta_A=\frac34
\]

found for the **scale-invariant mixed branch**. The two constants belong to different constitutive specializations and must not be merged.

Also, this local `3/2` criterion is not automatically identical to the **global spherical Schur-zero boundary**; the latter is a full boundary-value stability problem.

---

## Experiment 594 — Current regime map and next target

The reciprocal common-action branch now has three distinct notions that must remain separate:

1. local constitutive monotonicity loss;
2. global coupled Schur-zero/fold;
3. axis admissibility saturation.

For finite `ell_A`, the first axis response is nonlocal and the fold/saturation classification is genuinely a multi-parameter numerical surface in

\[
(\beta_A,\chi_A,\ell_A).
\]

The first slices show that this surface is not determined by `beta_A` alone.

### Consolidated verdict

The strong-case coexistence interval survives radial-grid refinement, and the fold-first/saturation-first distinction can now be tracked by a well-defined control quantity. The local zero-stiffness reciprocal branch additionally admits an exact Lambert-W reduction and an exact constitutive monotonicity boundary at `beta_A=3/2`.

### Next audit target

1. compute a denser `(beta_A, chi_A, ell_A)` fold/saturation surface with N=61 controls;
2. distinguish global Schur-zero from local constitutive monotonicity loss near `ell_A -> 0`;
3. compute the smallest full constrained Hessian eigenmode on both low and high branches;
4. only after the static classification is stable, add positive axis inertia `mu_A` and damping and test dynamic hysteresis, overshoot, and delayed crossing.
