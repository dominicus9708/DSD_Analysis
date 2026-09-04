# Structural Gravity Audit — Axis Stiffness, Tension, Support, and Inertia Bridges

Date: 2026-09-04
Status: DSD Analysis + DSD Audit continuation

## Source constraint

The current Structural Reorganization Dynamics layer explicitly allows stiffness-like, restoration-like, inertia-like, and coupling-like operator roles only through a supplied constitutive dynamic bridge. Property names do not canonically determine coefficients or operators. Static property aggregation likewise preserves typed multi-input records and does not supply universal physical semantics.

Accordingly, the constructions below are structural-gravity specializations and audits, not retroactive definitions of the predecessor property labels.

---

## Experiment 417 — Minimal deformation carrier for axis stiffness

Let `q` denote an admissible local axis-deformation coordinate. Depending on the chosen realized-axis specialization, `q` may be a small anisotropy tensor, a projector-coordinate chart, a local orientation variable, or another typed deformation coordinate.

A stiffness bridge cannot be defined from a stiffness label alone. At minimum it must supply:

1. a deformation carrier `Q_A`;
2. an equilibrium/reference state `q_*`;
3. a constitutive response map `Sigma_A(q, grad q, ...)` or an energy functional `E_A[q]`;
4. a tangent operator on admissible perturbations.

If an energy representation is used,

\[
\Sigma_A = \frac{\delta E_A}{\delta q},
\qquad
\mathsf K_A = D\Sigma_A[q_*] = D^2E_A[q_*].
\]

### Verdict

`axis stiffness` is most naturally mapped to a tangent response operator, not to a static stress value.

---

## Experiment 418 — Zero-order restoration and gradient stiffness are analytically distinct

A minimal quadratic axis energy near `q_*` is

\[
E_A[q_*+\delta q]
=
E_*+
\frac12\langle\delta q,\mathsf R_A\delta q\rangle
+
\frac12\int (\nabla_r\delta q):\mathsf K_A^{rs}:(\nabla_s\delta q)\,dV
+\cdots .
\]

The corresponding linearized operator is schematically

\[
\mathcal L_A\delta q
=
\mathsf R_A\delta q
-
\nabla_r\bigl(\mathsf K_A^{rs}\nabla_s\delta q\bigr).
\]

Thus:

- `restoration` is naturally a zero-order tendency toward a target manifold/state;
- `stiffness` is naturally a response to spatial or configurational deformation gradients.

They may coexist but are not the same operator.

### Fourier witness

For a homogeneous scalar specialization,

\[
\lambda_A(k)=R_A + K_A |k|^2.
\]

The uniform mode `k=0` sees restoration but not gradient stiffness. Shorter wavelengths probe stiffness more strongly.

### Verdict

\[
\boxed{\text{restoration}\neq\text{stiffness}}
\]

except under an explicitly reduced single-mode model where only their sum is observable.

---

## Experiment 419 — Finite-domain non-identifiability of restoration versus stiffness

On a bounded domain with Laplacian eigenvalues `lambda_n`, a scalar axis mode obeys

\[
\omega_n^2
=
\frac{R_A + K_A\lambda_n}{\mu_A}.
\]

One static threshold or one single-mode frequency constrains only the combination

\[
R_A+K_A\lambda_n.
\]

Therefore a single measurement cannot identify `R_A` and `K_A` separately.

Different spatial modes, different domain scales, or an independently known restoration target/operator are required.

### DSD audit verdict

Inferring `axis restoration` and `axis stiffness` separately from one combined stability observable is an inverse-problem overclaim.

---

## Experiment 420 — Tension is a state; stiffness is a tangent derivative

Let `e` be a scalar axis strain-like coordinate and consider

\[
W(e)=\tau_0 e + \frac12 K_A e^2.
\]

Then

\[
\tau(e)=\frac{dW}{de}=\tau_0+K_Ae,
\qquad
\frac{d\tau}{de}=K_A.
\]

At `e=0`, the current tension-like state is `tau_0`, while stiffness is `K_A`.

Two systems can therefore have:

- the same `tau_0` but different `K_A`;
- the same `K_A` but different `tau_0`.

### Verdict

\[
\boxed{\text{axis tension state}\neq\text{axis stiffness}}
\]

and the earlier toy coefficient multiplying `|grad A|^2` should be interpreted more cautiously as a gradient stiffness modulus, not automatically as axis tension.

---

## Experiment 421 — Prestress can affect stability without becoming stiffness

A nonzero tension/prestress may contribute a geometric tangent term after linearization of the geometry. Schematically,

\[
\mathsf K_{\rm tangent}
=
\mathsf K_{\rm material}
+
\mathsf K_{\rm geometric}(\tau_0).
\]

Hence tension may change a stability threshold, but only through an explicit geometry-to-tangent bridge.

This does not justify identifying `tau_0` with `K_A`.

### Verdict

Tension and stiffness may be dynamically coupled while remaining logically and dimensionally distinct roles.

---

## Experiment 422 — Minimal tension bridge

A structurally clean tension bridge should output at least a stress-like state on a declared deformation carrier:

\[
B_{\rm tens}:D_{\rm tens}\to \Sigma_A.
\]

If the model also uses stiffness, a second derivative/tangent bridge is required:

\[
B_{\rm stiff}:D_{\rm stiff}\to \mathsf K_A.
\]

The same predecessor property record may contribute to both only if an application-specific constitutive law explicitly supplies that relation.

---

## Experiment 423 — Support should not be used circularly

If `axis support` is defined as `the system is stable`, and then stability is proved because `support is present`, the argument is circular.

Therefore the predecessor support-like property record and the structural-gravity stability diagnostic must remain distinct.

Write

\[
z_{\rm sup}\in P_{\rm sup}
\]

for a typed support-like property record, and separately define a derived support margin from the actual coupled Hessian/operator.

---

## Experiment 424 — Derived axis-support margin

For a self-adjoint linearized coupled operator `H`, define

\[
\boxed{
m_{\rm sup}
:=
\inf_{\|v\|=1}\langle v,\mathcal H v\rangle
}
\]

when the variational setting is valid.

Then:

- `m_sup > 0`: linearly supported/stable against the admitted perturbation class;
- `m_sup = 0`: marginal support limit / zero mode;
- `m_sup < 0`: unstable direction exists.

This makes `support limit` a derived diagnostic rather than an unexplained force scale.

### Connection to the present structural-gravity collapse audit

The previously found coupled zero-mode threshold is exactly a case of

\[
\boxed{m_{\rm sup}=0}.
\]

Thus the older intuition of a finite `axis-support limit` can be retained in a sharpened form without assuming a primitive maximum-support constant.

---

## Experiment 425 — Two-mode support witness

For

\[
\mathcal H
=
\begin{pmatrix}
k_U & g\\
g & k_A
\end{pmatrix},
\]

positive support requires

\[
k_U>0,\qquad k_A>0,\qquad k_Uk_A-g^2>0.
\]

Hence a positive axis restoration/stiffness sector `k_A>0` does not by itself guarantee support. Strong coupling can make the full system unstable.

### Verdict

\[
\boxed{\text{axis support}\neq\text{restoration alone}}
\]

and support is naturally a property of the coupled admissible perturbation problem.

---

## Experiment 426 — If a predecessor support property is retained, three bridge roles remain possible

A typed predecessor support record may enter structural gravity in at least three non-equivalent ways:

1. **admissibility bridge** — changes the allowed perturbation/domain set;
2. **operator bridge** — changes `R_A`, `K_A`, boundary conditions, or coupling coefficients;
3. **diagnostic association** — is empirically/structurally correlated with the derived margin `m_sup`.

These possibilities must not be silently identified.

---

## Experiment 427 — Axis inertia is kinetic, not static support

For an admissible axis deformation coordinate `q`, a kinetic term has the form

\[
T_A
=
\frac12\langle \dot q,\mathsf M_A\dot q\rangle,
\qquad
\mathsf M_A\succ0
\]

in a stable inertial specialization.

The linearized equation is

\[
\mathsf M_A\ddot q + \mathcal H_A q = 0.
\]

The static equilibrium and zero-mode threshold are determined by `H_A`, not by an overall positive rescaling of `M_A`.

### Scaling witness

\[
\mathsf M_A\to \lambda\mathsf M_A,
\qquad \lambda>0
\]

leaves the static support boundary unchanged but rescales characteristic times as

\[
t\to \sqrt{\lambda}\,t.
\]

### Verdict

Axis inertia is naturally a reorganization-timescale/kinetic operator, not a static support coefficient and not automatically physical matter mass.

---

## Experiment 428 — Dynamic frequency separates inertia from stiffness/restoration

For a homogeneous mode,

\[
\omega^2(k)
=
\frac{R_A+K_A|k|^2}{M_A}.
\]

Consequently:

- static threshold data constrain the numerator;
- time/frequency data are required to identify the inertial denominator;
- multiple `k` values are required to separate restoration from stiffness.

This provides a concrete identification protocol for future structural-gravity toy models.

---

## Experiment 429 — Minimal bridge map after the audits

The current minimum non-circular specialization can be written schematically as

\[
B_A:
D_A
\to
(\mathsf M_A,\mathsf R_A,\mathsf K_A,\Sigma_A,\mathcal A_*,\mathcal C_A),
\]

where each output has a distinct role:

- `M_A`: kinetic inertia;
- `R_A`: zero-order restoration;
- `K_A`: deformation/gradient stiffness;
- `Sigma_A`: present stress/tension-like state;
- `A_*`: restoration target;
- `C_A`: coupling operator.

No equality among these outputs follows from the predecessor labels alone.

---

## Experiment 430 — Consolidated migration result

The former axis-property vocabulary survives the migration, but its structural-gravity interpretation is now sharpened:

\[
\boxed{
\begin{aligned}
\text{axis tension}&\to \text{stress/prestress state candidate},\\
\text{axis stiffness}&\to \text{tangent deformation operator},\\
\text{axis restoration}&\to \text{target-directed zero-order operator},\\
\text{axis inertia}&\to \text{kinetic/reorganization operator},\\
\text{axis support}&\to \text{preferably a coupled stability/admissibility diagnostic or explicit bridge input}.
\end{aligned}}
\]

This classification is compatible with the rewritten DSD hierarchy and with the current structural-gravity calculations without retrofitting either side to the other.

## Next audit target

1. separate axis crossing from axis coupling at operator level;
2. determine when geometric crossing/angle data can enter a coupling tensor without predefining interaction;
3. audit whether `axis support` should remain as a named predecessor property in the eventual structural-gravity paper or whether only the derived `support margin` should appear in the physical specialization.
