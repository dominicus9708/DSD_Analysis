# Structural Gravity Research Log — Experiments 417–431

Date: 2026-09-05
Status: DSD Analysis + DSD Audit of axis crossing / axis coupling migration

## Experiment 417 — Split `axis crossing` into geometric descriptors

A bare realized axis represented only by a one-dimensional subspace or projector does not by itself encode a physical crossing event in space.

For localized axes, separate at least:

- incidence/contact indicator \(\iota_{ab}\): whether the localized carriers intersect or contact;
- unoriented angular descriptor
  \[
  s_{ab}=\operatorname{tr}(P_aP_b)=\cos^2\theta_{ab};
  \]
- optional oriented descriptor \(\eta_{ab}=n_a\cdot n_b\) only when an orientation/tag is explicitly admitted;
- location/support data of the crossing region.

A linear subspace crossing at the origin is not yet a physical localized interaction point.

### Verdict

`Axis crossing` is not a single primitive scalar. It is primarily a geometric/relational descriptor bundle.

---

## Experiment 418 — Crossing graph and coupling graph are distinct

Define the geometric crossing graph

\[
G_\times=(V,E_\times),
\qquad
(a,b)\in E_\times\iff\iota_{ab}=1,
\]

and the dynamic coupling graph

\[
G_C=(V,E_C),
\qquad
(a,b)\in E_C\iff \mathsf C_{ab}\neq0.
\]

No current DSD layer implies

\[
G_\times=G_C.
\]

A locality specialization may impose relations such as \(G_C\subseteq G_\times\) or a neighborhood graph, but that is an additional constitutive rule.

### Verdict

\[
\boxed{\text{crossing}\neq\text{coupling}}
\]

---

## Experiment 419 — Crossing without coupling countermodel

Keep the same localized crossing geometry, angle, axis tags, and static property profile. Choose

\[
\mathsf C_{ab}=0.
\]

The axes geometrically cross but there is no dynamic exchange or response transfer.

### Verdict

\[
\boxed{\text{crossing}\not\Rightarrow\text{coupling}}
\]

---

## Experiment 420 — Coupling without crossing countermodel

Take two spatially separated axis carriers and couple both to a mediator/progression field \(\psi\). Eliminating the mediator can generate an effective nonlocal coupling

\[
\mathsf C_{ab}^{\rm eff}\neq0
\]

while \(\iota_{ab}=0\).

### Verdict

\[
\boxed{\text{coupling}\not\Rightarrow\text{crossing}}
\]

---

## Experiment 421 — What angle information is available for an unoriented axis?

For projector axes \(P_a=n_an_a^{\mathsf T}\), reversal \(n_a\mapsto-n_a\) changes nothing. Therefore the elementary rotationally invariant pair descriptor is

\[
\boxed{s_{ab}=\operatorname{tr}(P_aP_b)=\cos^2\theta_{ab}}.
\]

It cannot distinguish \(\theta\) from \(\pi-\theta\), nor incoming from outgoing direction.

Hence any `entry-angle` effect that depends on signed orientation requires an additional oriented axis/tag and cannot be recovered from the line projector alone.

### Verdict

- unoriented crossing angle: representable by projector data;
- directed entry/exit angle: **requires extra orientation data**.

---

## Experiment 422 — Geometry does not select a unique coupling law

Even after \(s_{ab}\) is supplied, many rotationally invariant constitutive laws remain possible, for example

\[
\mathsf C_{ab}=\kappa F(s_{ab})\mathsf C_0
\]

with

\[
F(s)=s,
\qquad
F(s)=1-s,
\qquad
F(s)=s(1-s),
\qquad
F(s)=1.
\]

All are compatible with the same basic axis reversal and rotation invariances, but predict different angle dependence.

### Verdict

\[
\boxed{\text{crossing angle geometry}\not\Rightarrow\text{unique coupling law}}
\]

---

## Experiment 423 — Angle can modulate coupling but cannot generate its absolute scale

If \(F(s)\) is dimensionless, then the dimensional coupling magnitude must come from an independent coefficient \(\kappa\) or another dimensional source property.

Thus

\[
\boxed{\text{angle/incidence can modulate a supplied coupling scale, not create it}}
\]

and crossing geometry cannot by itself recover the universal structural-gravity normalization \(\mu_0[M/L]\).

---

## Experiment 424 — Minimal pair-interaction bridge

A clean conservative specialization is to supply a pair potential

\[
E_{ab}=V_{ab}(s_{ab}),
\qquad
s_{ab}=\operatorname{tr}(P_aP_b).
\]

This is not implied by the crossing descriptor itself. The structural-gravity bridge is

\[
B_{\rm pair}:
(\iota_{ab},s_{ab},z_a,z_b,\ldots)
\mapsto
V_{ab}
\quad\text{or}\quad
\mathsf C_{ab}.
\]

For direct-local coupling one may additionally impose

\[
V_{ab}=0\quad\text{when}\quad\iota_{ab}=0,
\]

but mediated coupling need not satisfy that condition.

---

## Experiment 425 — Pair coupling generates a projector-commutator reorientation direction

Under an admissible infinitesimal axis rotation

\[
\delta P_a=[\Omega_a,P_a],
\qquad
\Omega_a^{\mathsf T}=-\Omega_a,
\]

one has

\[
\delta s_{ab}
=\operatorname{tr}\!\left(\Omega_a[P_a,P_b]\right).
\]

Therefore

\[
\delta E_{ab}
=V_{ab}'(s_{ab})
\operatorname{tr}\!\left(\Omega_a[P_a,P_b]\right).
\]

A gradient-flow-type reorientation consequently has the structural form

\[
\boxed{
\Omega_a
\propto
-\sum_bV_{ab}'(s_{ab})[P_a,P_b]
}
\]

up to the constitutive mobility/inertia choice.

This matches the previously identified admissible projector-commutator form: geometry determines the allowed reorientation direction once a pair potential is supplied, but not its rate.

---

## Experiment 426 — Alignment versus orthogonalization is a constitutive sign choice

For a simple pair energy

\[
V(s)=\kappa s,
\]

- \(\kappa>0\): lower energy favors \(s\to0\), i.e. orthogonalization;
- \(\kappa<0\): lower energy favors \(s\to1\), i.e. alignment.

Thus the same crossing geometry can support opposite reorganization tendencies depending on the constitutive coupling.

### Verdict

`Axis coupling` does not have a universal sign or preferred angle without an additional law.

---

## Experiment 427 — Relative coupling does not provide absolute restoration

For small axis deformation coordinates \(q_a\), take

\[
E_C
=\frac12\sum_{a<b}\kappa_{ab}\|q_a-q_b\|^2.
\]

The Hessian is a coupling-graph Laplacian \(L_C\). For a connected graph,

\[
L_C\mathbf 1=0.
\]

Hence positive pair coupling can suppress relative deformation while leaving a common rigid mode free.

### Verdict

\[
\boxed{\text{coupling coherence}\neq\text{absolute restoration/support}}
\]

A restoration term, boundary anchoring, or coupling to another field is required to remove the common zero mode.

---

## Experiment 428 — Coupling and support remain different layers

For two stable axis sectors with stiffness operators \(K_a,K_b\) and conservative coupling \(C\), the block Hessian is

\[
\mathcal H=
\begin{pmatrix}
K_a&C\\
C^*&K_b
\end{pmatrix}.
\]

Even if \(K_a>0\) and \(K_b>0\), full support/stability requires the Schur-complement condition

\[
\boxed{
K_b-C^*K_a^{-1}C>0
}
\]

(or its symmetric equivalent).

Thus coupling may stiffen some relative modes yet destabilize a coupled mode if its sign/structure is unfavorable.

---

## Experiment 429 — Conservative reciprocity is an extra condition

If coupling descends from a real quadratic energy, the off-diagonal blocks satisfy

\[
\boxed{C_{ba}=C_{ab}^*}.
\]

A dissipative, driven, or nonreciprocal specialization need not satisfy this.

Therefore the old label `axis coupling` does not by itself imply reciprocity.

---

## Experiment 430 — Pairwise coupling can control the structural-gravity anisotropy tensor

For equal weights,

\[
Q=\frac1N\sum_aP_a,
\qquad
\mathcal A=Q-\frac13I.
\]

For three orthonormal axes,

\[
P_1+P_2+P_3=I
\Rightarrow
Q=\frac13I
\Rightarrow
\boxed{\mathcal A=0}.
\]

For three fully aligned axes,

\[
P_1=P_2=P_3=P
\Rightarrow
Q=P
\Rightarrow
\boxed{\mathcal A=P-\frac13I},
\]

whose eigenvalues are

\[
\left(\frac23,-\frac13,-\frac13\right).
\]

This saturates the uniaxial second-moment anisotropy bound.

### Structural-gravity consequence

- an orthogonalization-favoring coupling can suppress \(\mathcal A\) and return the axis metric toward isotropy;
- an alignment-favoring coupling can increase \(\mathcal A\) toward its admissible uniaxial limit.

Thus old `axis coupling` can influence structural gravity indirectly by controlling the axis distribution that enters

\[
h_A=e^{\beta_A\mathcal A}.
\]

---

## Experiment 431 — Connection to the collapse-threshold branch

In the radial-alignment branch,

\[
\mathcal A=a(r)\left(n\otimes n-\frac13I\right),
\qquad
0\le a\le1.
\]

An alignment-promoting pair coupling can raise \(a\), which reduces

\[
h_A^{rr}=e^{-2\beta_Aa/3}
\]

for \(\beta_A>0\) and can therefore lower the s-wave spectral critical threshold found previously.

An orthogonalization/isotropization coupling acts in the opposite direction and can restore the threshold toward the isotropic baseline.

This is a conditional downstream consequence, not a definition of `axis coupling`.

---

# Consolidated DSD Analysis / DSD Audit verdict

The migrated concepts should be separated as follows:

1. **axis crossing** -> localized incidence/support geometry + unoriented/signed angle descriptors;
2. **axis coupling** -> constitutive operator or pair potential supplied after the geometry is known;
3. **axis reorganization** -> event/evolution generated by the supplied coupling and inertia/mobility;
4. **axis support** -> derived stability/admissibility of the full coupled operator.

The strongest surviving chain is

\[
\boxed{
\text{crossing geometry}
\to
\text{constitutive coupling bridge}
\to
\text{projector reorganization}
\to
Q,\mathcal A
\to
h_A
\to
\text{structural-gravity corrections/stability}
}
\]

with every arrow requiring an explicit bridge or already defined geometric map.

## Main negative controls

- crossing without coupling: survives;
- coupling without crossing: survives via mediator;
- same angle with different coupling laws: survives;
- coupling without absolute restoration: survives through graph-Laplacian zero mode;
- crossing geometry deriving the absolute gravity normalization: rejected.

## Next audit target

Audit `axis reorganization` itself as an event/law rather than a property:

- distinguish kinematic reorientation from dynamically driven reorganization;
- distinguish rigid common rotation from relative reorganization that changes \(Q\);
- determine the minimal law required for rank-preserving projector flow;
- then audit when reorganization can become rank transition, support loss, or the earlier `stasis` candidate.
