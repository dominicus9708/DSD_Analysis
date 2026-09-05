# Structural Gravity Research Log — Experiments 553–565

Date: 2026-09-05
Status: nonlinear numerical continuation and audit of the admissible radial axis/self-field threshold model

## Experiment 553 — Boundary-term correction to the perturbative threshold formula

The earlier perturbative discussion unnecessarily assumed `a(1)=0` in order to keep the Robin condition unchanged. That assumption is not needed.

For fixed positive

\[
p(s)=e^{-2\beta_Aa(s)/3},
\]

the critical radial eigenproblem is

\[
-\frac1{s^2}\frac{d}{ds}\left[s^2p(s)u_s\right]=\lambda u,
\]

with exterior matching

\[
\boxed{u(1)+p(1)u_s(1)=0.}
\]

Multiplying by `u s^2` and integrating gives the quadratic form

\[
\boxed{
\mathcal Q_p[u]
=\int_0^1s^2p(s)u_s^2\,ds+u(1)^2.
}
\]

The boundary term is independent of `p`. Therefore the first variation with respect to `p` is simply

\[
\delta\lambda_1
=
\frac{\int_0^1s^2\,\delta p\,u_{0,s}^2\,ds}
{\int_0^1s^2u_0^2\,ds},
\]

without requiring `a(1)=0`.

### Verdict

The previous local-restoration coefficient remains admissible under the general matching condition. The phrase `assume a(1)=0 so that the Robin boundary is unchanged` should be treated as an unnecessary restriction, not as a required premise.

---

## Experiment 554 — Numerical scheme for the constrained nonlinear eigenproblem

For a uniform sphere `d(s)=1`, the coupled endpoint equations are solved by alternating two well-defined subproblems:

1. fixed `a`: solve the first positive radial eigenpair of
   \[
   -s^{-2}(s^2pu_s)_s=\lambda u,
   \qquad
   u(1)+p(1)u_s(1)=0;
   \]
2. fixed `u`: solve the convex bound-constrained axis response
   \[
   -\ell_A^2L_2a+a
   =2\beta_A\chi_A(u_s/u)^2,
   \qquad
   0\le a\le1.
   \]

The primary control uses the variationally natural free axis boundary `a_s(1)=0`. A compact Dirichlet control `a(1)=0` is retained separately.

The numerical solver uses ODE shooting for the first radial eigenvalue and a bound-constrained convex minimization for the axis subproblem.

### Verdict

This is a reproducibility/control solver for the conditional specialization, not a proof of uniqueness of the full nonlinear branch.

---

## Experiment 555 — Baseline and grid-convergence check

With `beta_A=0`, the numerical solver recovers

\[
\epsilon_c=\pi^2/6
=1.644934066848\ldots
\]

to numerical precision.

For the representative nonlinear point

\[
(\beta_A,\chi_A,\ell_A)=(0.5,0.5,0.1)
\]

with the free axis boundary, the grid sequence gives

| grid points | epsilon_c | max a |
|---:|---:|---:|
| 101 | 1.60599819 | 0.49654 |
| 161 | 1.60600655 | 0.49630 |
| 241 | 1.60601251 | 0.49616 |
| 321 | 1.60601540 | 0.49611 |

### Verdict

The reported three-to-four significant-digit threshold shifts are stable under this grid refinement.

---

## Experiment 556 — Axis stiffness length suppresses the perturbative softening coefficient

Write the weak self-consistent threshold as

\[
\epsilon_c
=\frac{\pi^2}{6}
-C(\ell_A)\,\chi_A\beta_A^2+\cdots.
\]

For the free axis boundary, the linear axis-response calculation gives approximately

| ell_A | C(ell_A) |
|---:|---:|
| 0 | 0.259060728 |
| 0.1 | 0.23145 |
| 0.3 | 0.12743 |
| 0.5 | 0.06729 |
| 1.0 | 0.02095 |

Thus increasing the axis stiffness length strongly suppresses field-induced radial alignment and therefore suppresses the lowering of the spectral threshold.

### Verdict

\[
\boxed{\ell_A\uparrow\ \Rightarrow\ \text{weaker axis-feedback softening}}
\]
for this radial control family.

---

## Experiment 557 — Exact nonlinear thresholds in the weak/moderate branch

Representative free-boundary results are:

| ell_A | beta_A | chi_A | exact epsilon_c | perturbative epsilon_c | max a |
|---:|---:|---:|---:|---:|---:|
| 0 | 0.10 | 1.0 | 1.64228718 | 1.64234346 | 0.2056 |
| 0 | 0.25 | 0.5 | 1.63624798 | 1.63683842 | 0.2739 |
| 0 | 0.50 | 0.5 | 1.59699657 | 1.61255148 | 0.9286 |
| 0 | 0.50 | 1.0 | 1.55195835 | 1.58016888 | 1.0000 |
| 0.1 | 0.25 | 0.5 | 1.63725709 | 1.63770120 | 0.1964 |
| 0.1 | 0.50 | 0.5 | 1.60601540 | 1.61600262 | 0.4961 |
| 0.1 | 0.50 | 1.0 | 1.55320228 | 1.58707117 | 1.0000 |
| 0.3 | 0.50 | 0.5 | 1.62667919 | 1.62900572 | 0.2104 |
| 0.3 | 0.50 | 1.0 | 1.60107417 | 1.61307737 | 0.4954 |

### Verdict

The nonlinear solution preserves the perturbative sign: radial axis response lowers the threshold. At moderate response, the exact softening is systematically stronger than the quadratic approximation.

---

## Experiment 558 — Perturbative validity range is controlled better by actual axis response than by beta_A alone

For the representative cases above, the perturbative estimate underestimates the exact threshold shift by roughly:

- about 2% when `max a ~= 0.21` in the `(beta,chi,ell)=(0.1,1,0)` case;
- about 6% when `max a ~= 0.20–0.27` for the `(0.25,0.5)` controls;
- about 13% for `ell=0.3, beta=0.5, chi=0.5`, where `max a ~=0.21`;
- about 25–37% once the response reaches `max a ~=0.5` or approaches saturation.

No universal sharp perturbative cutoff is claimed.

### Verdict

`max a` and the metric deformation `beta_A a` are better diagnostics of perturbative reliability than `beta_A` alone.

---

## Experiment 559 — Boundary/support choice is a genuine constitutive input

For the same bulk equations, compare the variational free boundary `a_s(1)=0` with the compact control `a(1)=0`.

Representative thresholds:

| ell_A | beta_A | chi_A | free epsilon_c | compact epsilon_c |
|---:|---:|---:|---:|---:|
| 0.1 | 0.25 | 0.5 | 1.63726 | 1.64081 |
| 0.1 | 0.50 | 0.5 | 1.60601 | 1.62639 |
| 0.1 | 0.50 | 1.0 | 1.55320 | 1.59909 |
| 0.3 | 0.25 | 0.5 | 1.64083 | 1.64379 |
| 0.3 | 0.50 | 0.5 | 1.62667 | 1.64021 |
| 0.3 | 0.50 | 1.0 | 1.60106 | 1.63506 |

The compact boundary suppresses radial alignment near the source edge and therefore reduces threshold softening.

### Verdict

\[
\boxed{\text{axis boundary/support law is not a disposable numerical detail.}}
\]
It is part of the constitutive specialization and must be declared in any physical model.

---

## Experiment 560 — Exact local-restoration saturation onset at the outer endpoint

For `ell_A=0`, the constrained axis equation is pointwise:

\[
\boxed{a=\min\{1,\,2\beta_A\chi_A y^2\}},
\qquad
y=u_s/u.
\]

At the spectral endpoint,

\[
y(1)=-\frac1{p(1)},
\qquad
p(1)=e^{-2\beta_Aa(1)/3}.
\]

The first endpoint saturation `a(1)=1` therefore satisfies exactly

\[
1=2\beta_A\chi_Ae^{4\beta_A/3},
\]

so

\[
\boxed{
\chi_{A,\rm sat}^{\rm endpoint}
=\frac{e^{-4\beta_A/3}}{2\beta_A}.
}
\]

For `beta_A=0.5`,

\[
\boxed{\chi_{A,\rm sat}=0.5134171190\ldots}
\]

Numerical continuation gives `max a ~=0.9286` at `chi_A=0.5` and reaches `a=1` at the predicted onset.

### Verdict

The admissibility bound produces a calculable nonlinear saturation point; saturation is not merely an after-the-fact clipping artifact.

---

## Experiment 561 — Eliminating a locally exposes a constitutive monotonicity/ellipticity audit

In the unsaturated `ell_A=0` branch,

\[
a=2\beta_A\chi_Ay^2,
\]

hence

\[
p(y)=\exp\left[-\frac43\beta_A^2\chi_Ay^2\right].
\]

The radial constitutive flux is proportional to

\[
q(y)=p(y)y.
\]

Its differential response is

\[
\boxed{
\frac{dq}{dy}
=p(y)\left[1-\frac83\beta_A^2\chi_Ay^2\right].
}
\]

Thus the locally eliminated quasilinear field equation loses monotonicity when

\[
y^2=\frac{3}{8\beta_A^2\chi_A}.
\]

The axis saturation gradient is

\[
y_{\rm sat}^2=\frac1{2\beta_A\chi_A}.
\]

Their ratio is

\[
\boxed{
\frac{y_{\rm fold}^2}{y_{\rm sat}^2}
=\frac{3}{4\beta_A}.
}
\]

Therefore:

- `beta_A < 3/4`: saturation is reached before this local flux fold;
- `beta_A = 3/4`: the two coincide;
- `beta_A > 3/4`: the reduced unsaturated flux law can lose monotonicity before saturation.

### Verdict

\[
\boxed{\beta_A=3/4}
\]
is a **conditional local constitutive monotonicity boundary** of the `ell_A=0` eliminated model. It is not a universal DSD constant and not a black-hole threshold.

---

## Experiment 562 — Strong-coupling continuation warning

Numerical fixed-point continuation becomes branch-sensitive in the strong local-response regime, especially when the constitutive monotonicity condition from Experiment 561 is approached or violated.

This is not sufficient evidence for a physical discontinuity by itself: the alternating solver is not a global uniqueness theorem, and the full two-field `(u,a)` formulation can remain the appropriate object even when the locally eliminated `q(y)` law folds.

### Verdict

Strong-coupling results beyond the monotone branch must be treated as **continuation-dependent / unresolved** until the coupled variational Hessian or a direct boundary-value continuation method is used.

---

## Experiment 563 — Nonperturbative geometric bound remains respected

Because

\[
0\le a\le1,
\qquad
p=e^{-2\beta_Aa/3},
\]

one has

\[
e^{-2\beta_A/3}\le p\le1.
\]

For the same Robin quadratic form this implies the previously derived comparison bound

\[
\boxed{
\epsilon_c[a]
\ge e^{-2\beta_A/3}\epsilon_c^{(0)}
}
\]
for the radial control family.

All converged numerical cases reported here respect this lower bound.

### Verdict

Axis saturation bounds the amount by which this metric channel alone can lower the spectral endpoint.

---

## Experiment 564 — Numerical interpretation of the first nonlinear axis feedback

The combined results now separate three regimes:

1. **weak response**: quadratic softening is accurate;
2. **nonlinear unsaturated response**: exact softening becomes stronger than the quadratic estimate but `a<1`;
3. **saturated response**: part of the source reaches `a=1`, after which the admissible geometry limits further local axis alignment.

A fourth warning regime exists for the locally eliminated `ell_A=0`, `beta_A>3/4` branch where flux monotonicity can fail before saturation.

---

## Experiment 565 — Reproducibility script

Added

`audits/science/structural_gravity_logs/2026-09-05_radial_axis_threshold_solver.py`

to reproduce the controlled nonlinear endpoint calculation.

Example command from the repository root:

```bash
python audits/science/structural_gravity_logs/2026-09-05_radial_axis_threshold_solver.py --beta 0.5 --chi 0.5 --ell 0.1 --bc neumann --grid 321
```

The script reports `epsilon_c`, the baseline `pi^2/6`, threshold shift, maximum axis alignment, saturation fraction, and iteration residual.

## Consolidated verdict

The admissible radial axis/self-field model survives its first nonlinear numerical audit in the weak and moderate response regimes:

\[
\boxed{
\text{field-driven radial axis response}
\Rightarrow
\text{lower static spectral endpoint}
}
\]
within the stated conditional specialization.

However, the numerical audit also adds two important qualifications:

- the axis boundary/support law materially changes the threshold and must be specified;
- the locally eliminated zero-stiffness branch has a constitutive monotonicity boundary at `beta_A=3/4`, so strong-coupling continuation cannot be inferred by naive extrapolation.

## Next audit target

1. replace alternating fixed-point continuation by direct pseudo-arclength or coupled Newton continuation near strong response;
2. compute the full coupled static Hessian and identify whether the first branch loss is a spectral zero mode, a constitutive fold, or admissibility saturation;
3. then add `mu_A` and evolve the time-dependent two-field system across the static boundary to distinguish adiabatic tracking, overshoot, and finite-time instability.
