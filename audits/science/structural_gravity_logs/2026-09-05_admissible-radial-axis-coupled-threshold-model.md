# Structural Gravity Research Log — Experiments 537–552

Date: 2026-09-05
Status: explicit admissible radial axis–progression coupled specialization

## Experiment 537 — Exact admissible radial second-moment parameterization

For a spherical branch let `n=x/r` and define the radial projector

\[
P_r=n\otimes n.
\]

Introduce one scalar alignment amplitude

\[
0\le a(r,t)\le1
\]

and set

\[
\boxed{
Q(a,n)=\frac{1-a}{3}I+aP_r
=\frac13I+a\left(P_r-\frac13I\right).
}
\]

Then automatically

\[
Q\succeq0,
\qquad
\operatorname{tr}Q=1.
\]

Its eigenvalues are

\[
q_r=\frac{1+2a}{3},
\qquad
q_t=\frac{1-a}{3}
\]

with the tangential eigenvalue repeated twice.

Interpretation:

- `a=0`: isotropic second moment;
- `a=1`: fully radial uniaxial second moment.

### Verdict

This parameterization removes the earlier problem that an unconstrained tensor wave equation could leave the realizable second-moment domain.

---

## Experiment 538 — Exact axis-metric eigenvalues

Define

\[
\mathcal A
=Q-\frac13I
=a\left(P_r-\frac13I\right),
\]

and retain the axis-informed metric candidate

\[
\boxed{h_A=e^{\beta_A\mathcal A}}.
\]

The metric eigenvalues in the radial/tangential orthonormal frame are

\[
\boxed{
h_r=e^{2\beta_Aa/3},
\qquad
h_t=e^{-\beta_Aa/3}
}
\]

with

\[
\det h_A=1.
\]

Hence

\[
\boxed{h_A^{rr}=e^{-2\beta_Aa/3}}.
\]

For finite `beta_A` and `0<=a<=1`, the spatial metric remains positive definite even at maximal radial alignment.

---

## Experiment 539 — Regularity at the spherical center

The unit radial direction `n=x/r` is undefined at `r=0`. The tensor

\[
\mathcal A_{ij}
=a(r)\left(\frac{x_ix_j}{r^2}-\frac13\delta_{ij}\right)
\]

therefore requires `a(r)->0` at the center.

A simple sufficient smoothness condition is

\[
\boxed{a(r)=O(r^2)\quad(r\to0)}.
\]

This makes the directional singularity removable at the tensor level.

### Verdict

The earlier smooth control `a(s)=s^2(1-s^2)` was not merely convenient; its quadratic center behavior is a natural sufficient regularity condition.

---

## Experiment 540 — Exact radial reduction of the tensor axis action

Start from the conditional tensor action density

\[
\mathcal L_A
=
\frac{\mu_A}{2}\|\partial_t\mathcal A\|^2
-\frac{\mathcal T_A}{2}\|\nabla\mathcal A\|^2
-\frac{\mathcal R_A}{2}\|\mathcal A\|^2
+\frac{\beta_A\mu_0c_*^2}{2}
\mathcal A^{ij}\partial_i\psi\partial_j\psi.
\]

For

\[
\mathcal A=a(r,t)S(n),
\qquad
S(n)=P_r-I/3,
\]

one has

\[
\|S\|^2=\frac23,
\]

\[
\|\partial_t\mathcal A\|^2
=\frac23a_t^2,
\]

\[
\|\nabla\mathcal A\|^2
=\frac23\left(a_r^2+\frac{6a^2}{r^2}\right),
\]

and for spherical `psi`,

\[
\mathcal A^{ij}\partial_i\psi\partial_j\psi
=\frac23a\psi_r^2.
\]

After variation, all common normalization factors cancel and the scalar amplitude equation is

\[
\boxed{
\mu_Aa_{tt}
-\mathcal T_A
\left(a_{rr}+\frac2r a_r-\frac6{r^2}a\right)
+\mathcal R_Aa
=
\frac{\beta_A\mu_0c_*^2}{2}\psi_r^2.
}
\]

### Verdict

The `1/2` source coefficient used in the earlier radial toy is **confirmed** by exact restriction of the tensor action; no normalization correction is required.

---

## Experiment 541 — Dimensionless static axis equation

Let

\[
s=r/R,
\qquad
\ell_A^2
:=\frac{\mathcal T_A}{\mathcal R_AR^2},
\qquad
\chi_A
:=\frac{\mu_0c_*^2}{\mathcal R_AR^2}.
\]

In a static spherical branch,

\[
\boxed{
-\ell_A^2
\left(
 a_{ss}+\frac2s a_s-\frac6{s^2}a
\right)
+a
=
\frac{\beta_A\chi_A}{2}\psi_s^2.
}
\]

Using `U=e^{-psi/2}` gives

\[
\psi_s=-2\frac{u_s}{u},
\]

so

\[
\boxed{
-\ell_A^2L_2a+a
=
2\beta_A\chi_A
\left(\frac{u_s}{u}\right)^2,
}
\]

where

\[
L_2a=a_{ss}+\frac2s a_s-\frac6{s^2}a.
\]

---

## Experiment 542 — Exact coupled transformed field equation

The self-field transform remains exact in the static axis metric:

\[
\Delta_{h_A}U+\frac{\rho}{2\mu_0}U=0.
\]

Because `det h_A=1`, the spherical radial equation is

\[
\boxed{
-\frac1{s^2}\frac{d}{ds}
\left[
 s^2e^{-2\beta_Aa/3}u_s
\right]
=
\frac{3\epsilon}{2}d(s)u,
}
\]

with

\[
\epsilon=\frac{M}{4\pi\mu_0R}.
\]

Thus the radial axis sector enters the self-field spectral problem through the positive coefficient

\[
\boxed{p_A(s)=e^{-2\beta_Aa(s)/3}}.
\]

---

## Experiment 543 — General exterior matching and critical denominator

Assume the axis metric is Euclidean outside the bounded source. Let the interior shape be `u(s)` and the exterior normalized solution be

\[
U_{\rm out}=1+\frac{c}{s}.
\]

Continuity of `U` and radial flux at `s=1` gives

\[
A\bigl[u(1)+p_A(1)u_s(1)\bigr]=1.
\]

Hence the generalized normalization denominator is

\[
\boxed{
D_A(\epsilon)
=u(1)+p_A(1)u_s(1).
}
\]

The static positive normalized branch reaches its spectral endpoint when

\[
\boxed{D_A=0}.
\]

If the axis anisotropy vanishes smoothly at the source boundary,

\[
a(1)=0
\quad\Rightarrow\quad
p_A(1)=1,
\]

this reduces to the familiar Robin condition

\[
\boxed{u_s(1)+u(1)=0}.
\]

---

## Experiment 544 — Baseline consistency limits

The explicit coupled model passes three immediate reduction checks.

### No axis coupling

If

\[
\beta_A=0,
\]

then the regular restored solution is `a=0`, `p_A=1`, and the original self-field spectral problem is recovered.

### Infinite restoration

If `R_A -> infinity` with the other dimensional coefficients fixed, then

\[
\chi_A\to0,
\qquad
\ell_A\to0,
\]

and field-driven anisotropy is suppressed.

### Isotropic axis state

If `a=0`,

\[
h_A=I
\]

independently of the value of `beta_A`.

For a uniform sphere, these limits recover

\[
\epsilon_c=\pi^2/6.
\]

---

## Experiment 545 — Self-consistent axis feedback starts at second order in `beta_A`

For an initially isotropic axis sector, expand

\[
a=\beta_Aa_1+O(\beta_A^2).
\]

The leading response satisfies

\[
\boxed{
(-\ell_A^2L_2+1)a_1
=2\chi_A\left(\frac{u_{0,s}}{u_0}\right)^2.
}
\]

Then

\[
p_A
=e^{-2\beta_Aa/3}
=1-\frac23\beta_A^2a_1+O(\beta_A^3).
\]

Therefore the **self-consistent** metric feedback begins at

\[
\boxed{O(\beta_A^2)}.
\]

This reconciles two earlier results:

- externally prescribed radial anisotropy can shift the threshold at `O(beta_A)`;
- field-induced anisotropy starting from isotropy shifts it first at `O(beta_A^2)`.

---

## Experiment 546 — Sign-definite leading threshold shift for a positivity-preserving axis response

Assume `a(1)=0` so the Robin boundary term is unchanged, and let `u_0` be the positive uncoupled critical mode. The first nonzero variation of the critical eigenvalue is

\[
\boxed{
\delta\lambda_c^{(2)}
=-\frac23\beta_A^2
\frac{
\int_0^1a_1(s)s^2u_{0,s}^2\,ds
}{
\int_0^1d(s)s^2u_0^2\,ds
}.
}
\]

Because

\[
\epsilon_c=\frac23\lambda_c,
\]

one obtains

\[
\boxed{
\delta\epsilon_c^{(2)}
=-\frac49\beta_A^2
\frac{
\int_0^1a_1(s)s^2u_{0,s}^2\,ds
}{
\int_0^1d(s)s^2u_0^2\,ds
}.
}
\]

If the axis response operator is positivity-preserving so that the positive field-gradient drive gives

\[
a_1(s)\ge0,
\]

then

\[
\boxed{\delta\epsilon_c^{(2)}\le0}.
\]

Thus the earlier Schur-complement `relaxable axis softens the coupled threshold` result is recovered directly inside the explicit admissible radial model.

---

## Experiment 547 — Uniform-sphere local-restoration coefficient reproduces the earlier result

Take the local-restoration limit

\[
\ell_A=0.
\]

Then

\[
a_1
=2\chi_A\left(\frac{u_{0,s}}{u_0}\right)^2.
\]

For the uniform-sphere critical mode

\[
u_0(s)=\frac{\sin(\pi s/2)}{(\pi/2)s},
\]

the threshold-shift formula gives

\[
\boxed{
\epsilon_c
=
\frac{\pi^2}{6}
-0.2590607279738906\,\chi_A\beta_A^2
+O(\beta_A^3).
}
\]

This independently reproduces the coefficient `0.259060728` obtained earlier from the local-restoration toy calculation.

### Verdict

The old coefficient survives the exact second-moment admissibility parameterization and exact tensor-to-radial reduction.

---

## Experiment 548 — Exact admissibility requires a constrained axis equation

The unconstrained Euler–Lagrange equation does not by itself guarantee

\[
0\le a\le1.
\]

A faithful model should therefore treat the static axis problem as a constrained variational problem. Schematically,

\[
-\ell_A^2L_2a+a-f_A
-\lambda_-+\lambda_+=0,
\]

where

\[
f_A=2\beta_A\chi_A(u_s/u)^2,
\]

with KKT conditions

\[
\lambda_-\ge0,
\quad
\lambda_+\ge0,
\quad
\lambda_-a=0,
\quad
\lambda_+(a-1)=0.
\]

This supplies an exact saturation mechanism at the realizable second-moment boundary.

### Verdict

The previous bound `0<=a<=1` should be enforced as an admissibility constraint, not merely checked after solving an unconstrained tensor equation.

---

## Experiment 549 — Critical normalization divergence does not blow up the axis drive

Write the physical interior solution as

\[
U=A(\epsilon)u(s).
\]

Then

\[
\psi_s
=-2\partial_s\ln U
=-2\frac{u_s}{u}.
\]

The normalization factor `A(epsilon)` cancels exactly.

Therefore, as the self-field spectral denominator approaches zero and `A -> infinity`, the local field-gradient drive of the axis equation does **not** diverge merely because of that normalization.

### Verdict

The axis feedback can move the spectral endpoint, but the self-field response-mass divergence does not automatically produce a divergent local axis torque/drive.

---

## Experiment 550 — Dynamic parameter compression

Define the axis restoration time

\[
\boxed{\tau_A^2=\mu_A/\mathcal R_A}
\]

and the free axis characteristic speed in the simple isotropic principal specialization

\[
\boxed{c_A^2=\mathcal T_A/\mu_A}.
\]

Then

\[
\boxed{
\ell_A^2
=\frac{\mathcal T_A}{\mathcal R_AR^2}
=\frac{c_A^2\tau_A^2}{R^2}.
}
\]

Thus the static shape-response length is the distance an axis reorganization mode travels in one restoration time, measured relative to the source radius.

The second dimensionless response parameter remains

\[
\boxed{\chi_A=\frac{\mu_0c_*^2}{\mathcal R_AR^2}}.
\]

`c_info` may constrain `c_A`, but does not determine `tau_A`, `R_A`, or the common absolute constitutive scale.

---

## Experiment 551 — Minimal equations for the first explicit coupled axis/self-field witness

The present audit supports the following minimal static system for a bounded spherical source:

\[
\boxed{
-\frac1{s^2}\frac{d}{ds}
\left[s^2e^{-2\beta_Aa/3}u_s\right]
=\frac{3\epsilon}{2}d(s)u,
}
\]

\[
\boxed{
-\ell_A^2L_2a+a
=2\beta_A\chi_A\left(\frac{u_s}{u}\right)^2,
\qquad
0\le a\le1,
}
\]

with center regularity and an explicitly chosen boundary/support condition for `a`, plus the exterior critical matching condition

\[
\boxed{
u(1)+p_A(1)u_s(1)=0
}
\]

at the static spectral endpoint.

This system uses only:

- the progression/self-field sector `(u, epsilon, mu_0)`;
- radial second-moment geometry `a`;
- axis metric coupling `beta_A`;
- restoration/stiffness response `(chi_A, ell_A)`.

Axis tension, explicit crossing data, general closure data, and full pair-coupling networks are **not required** for this first spherical witness.

---

## Experiment 552 — Paper-design consequence

The migration audit now yields a concrete scope rule for a first structural-gravity paper/model:

### Main equations need only

1. realized-axis second-moment geometry and admissibility;
2. the minimal restoration/stiffness/inertia roles actually used by the axis field;
3. the progression-field coupling;
4. the spectral/support diagnostics.

### Keep optional or later unless used

- axis tension/prestress;
- explicit crossing geometry;
- pair-coupling graph;
- cyclic/formal closure;
- higher-order normal/closure profiles.

These concepts remain valid specialization material, but carrying every old axis-property name into the first physical model would add undeclared constitutive assumptions without improving the present calculation.

## Consolidated verdict

The explicit admissible radial model closes an important gap in the earlier toy calculations:

\[
\boxed{
Q\succeq0,\ \operatorname{tr}Q=1
\quad\text{is now built into the field variable itself.}
}
\]

The model reproduces the previous weak axis-softening coefficient, preserves the exact nonlinear self-field transform, and makes the static coupled threshold a well-defined constrained nonlinear eigenvalue problem.

## Next audit target

1. solve the constrained nonlinear eigenvalue problem numerically for a uniform sphere over `(beta_A, chi_A, ell_A)`;
2. compare the exact nonlinear threshold with the perturbative formula and the nonperturbative geometric bound;
3. identify whether axis saturation `a=1` is reached before the coupled spectral endpoint;
4. then add the inertial time-dependent axis equation and test finite-time threshold crossing versus adiabatic tracking.
