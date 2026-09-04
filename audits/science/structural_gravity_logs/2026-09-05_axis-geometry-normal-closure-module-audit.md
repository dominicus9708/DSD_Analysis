# Structural Gravity Research Log — Experiments 512–536

Date: 2026-09-05
Status: final DSD Analysis + DSD Audit of realized-axis geometry, normals, closure, and minimal structural-gravity axis module

## Experiment 512 — Independence is algebraic geometry, not a constitutive coefficient

Let realized lines be represented by nonzero vectors `n_a`, and let

\[
W_A=\operatorname{span}\{n_a\}.
\]

Linear independence is a statement about the span map itself. It does not require a bilinear form and does not determine inertia, stiffness, restoration, coupling, support, or propagation coefficients.

If a positive-definite reference bilinear form `b_0` is supplied, the Gram matrix

\[
G_{ab}=b_0(n_a,n_b)
\]

is positive definite exactly when the chosen representatives are independent.

However, for an indefinite or degenerate symmetric bilinear form, Gram nonsingularity instead tests nondegeneracy of the restricted form and is not generally equivalent to algebraic independence.

### Verdict

\[
\boxed{\text{axis independence}\neq\text{dynamic stiffness/support/force}}
\]

and `Gram determinant != 0` should be used as an independence test only under the stated positive-definite/nondegeneracy assumptions.

---

## Experiment 513 — Orthogonality is bilinear-form dependent

For two realized lines,

\[
\ell_a\perp_{b_0}\ell_b
\quad\Longleftrightarrow\quad
b_0(n_a,n_b)=0.
\]

The same line family can be orthogonal under one supplied symmetric bilinear form and nonorthogonal under another. Therefore orthogonality is not determined by line incidence alone.

### Verdict

`Axis orthogonality` belongs to the geometric prerequisite/representation layer relative to an explicitly supplied bilinear structure.

---

## Experiment 514 — Orthogonality does not imply isotropy

Let three mutually orthogonal unit axes have projectors `P_i` and weights `w_i > 0`, `sum_i w_i = 1`. Then

\[
Q=\sum_iw_iP_i.
\]

If `w_1=w_2=w_3=1/3`,

\[
Q=I/3,
\qquad
\mathcal A=Q-I/3=0.
\]

But if the weights are unequal,

\[
Q=\operatorname{diag}(w_1,w_2,w_3)
\]

in the orthogonal basis and is anisotropic.

### Verdict

\[
\boxed{\text{orthogonality}\not\Rightarrow\text{coarse isotropy}}
\]

without completeness and the appropriate weighting rule.

---

## Experiment 515 — Independence/rank does not determine support or characteristic speed

Keep one full-rank axis geometry fixed and choose two admissible constitutive bridges with different Hessians or kinetic/stiffness operators. One can be stable and the other unstable, or they can have different characteristic speeds.

Conversely, a lower-rank admitted axis sector can remain stable under a positive constitutive Hessian.

### Verdict

\[
\boxed{\text{axis rank/independence}\not\Rightarrow\text{support margin or propagation cone}}
\]

consistent with the existing DSD no-rank-only characteristic result.

---

## Experiment 516 — A normal is generally a subspace, not a unique vector

For an axis-generated subspace `S`, retain the old realized-axis definitions

\[
N^{\rm int}(S)=S^{\perp}\cap W_A,
\qquad
N^{\rm amb}(S)=S^{\perp}\cap E_{\rm amb}
\]

relative to the supplied bilinear structure.

A line in three dimensions has a two-dimensional orthogonal complement, so it does not possess a unique normal line. A unique normal line arises only when the relevant orthogonal complement is one-dimensional, for example for a nondegenerate codimension-one subspace.

### Verdict

The structural-gravity migration should preserve `normal subspace` as the primary notion. A normal vector or normal axis is an additional one-dimensional/oriented specialization.

---

## Experiment 517 — Pair-plane normal in a three-dimensional realized span

Let two independent axes span

\[
S_{12}=\operatorname{span}(\ell_1,\ell_2).
\]

If the realized span is three-dimensional and the bilinear restriction is nondegenerate, then

\[
\dim N^{\rm int}(S_{12})=1.
\]

This yields an **unoriented normal line**. A signed normal vector requires further orientation data (for example an oriented volume form or oriented axis tags); the line projectors alone do not fix the sign.

---

## Experiment 518 — Higher-dimensional normal ambiguity

For codimension greater than one,

\[
\dim N^{\rm int}(S)>1
\]

in the ordinary nondegenerate case. Therefore an `axis normal` cannot be generalized to arbitrary rank as one preferred direction without an additional selection rule.

### Verdict

Any later N-dimensional structural-gravity specialization must keep the normal as a subspace until a separate directional selector is justified.

---

## Experiment 519 — Reference geometry must be separated from derived axis geometry

The current structural-gravity candidate

\[
h_A=\exp(\beta_A\mathcal A)
\]

uses projectors/second moments to construct a downstream axis-informed spatial metric. If the same `h_A` is silently used upstream to define the orthogonality, normal spaces, and normalized projectors from which `\mathcal A` is constructed, the definition becomes implicit/circular.

A clean baseline is therefore:

1. supply a reference bilinear structure `b_0` in the realized-axis specialization;
2. define lines, projectors, Gram data, orthogonality, normals, and `Q` relative to `b_0`;
3. derive `\mathcal A` and then `h_A` downstream.

If physical orthogonality is intended to be self-consistent with `h_A`, this must instead be posed as an explicit fixed-point/implicit constitutive problem rather than hidden in the notation.

### Verdict

\[
\boxed{b_0\text{ (reference geometry)}\neq h_A\text{ (derived axis metric)}}
\]

in the minimal noncircular branch.

---

## Experiment 520 — Closure is not one scalar property

Retain the old three-way distinction:

1. formal obligation–witness closure `ClStat`;
2. cyclic triadic closure `CycProf`;
3. nondegeneracy `NonDeg`.

The old realized-axis system already proves that these statuses can differ.

### Verdict

A structural-gravity implementation must not collapse them into one Boolean `axis closure` variable unless an additional theorem shows equivalence on the chosen model class.

---

## Experiment 521 — Exact meaning of cyclic triadic closure

For an ordered independent triad `(ell_1,ell_2,ell_3)`, with pair spans `S_12,S_23,S_31`, the retained geometric specialization uses

\[
N^{\rm int}(S_{12})=\ell_3,
\quad
N^{\rm int}(S_{23})=\ell_1,
\quad
N^{\rm int}(S_{31})=\ell_2.
\]

This is a geometric relation relative to the supplied bilinear structure. A single inclusion such as `ell_3 subset N_int(S_12)` is not sufficient; the old R^4 witness demonstrates the failure.

---

## Experiment 522 — Closure can imply rank three only conditionally

If an axis-generated two-dimensional subspace `S` is nondegenerate and

\[
\dim N^{\rm int}(S)=1,
\]

then the orthogonal direct-sum dimension formula gives

\[
\boxed{\dim W_A=2+1=3}.
\]

This is a conditional linear-algebraic statement. It does not establish that physical space has dimension three and does not make cyclic closure a universal dimensional-selection law.

---

## Experiment 523 — Closure does not imply dynamic support

Fix exactly the same closure-satisfied realized-axis geometry and static closure records. Supply two structural-gravity constitutive bridges:

\[
B_1\mapsto H_A\succ0,
\qquad
B_2\mapsto H_A\text{ indefinite}.
\]

The closure profile is identical while the support margin differs in sign.

### Verdict

\[
\boxed{\text{closure satisfaction}\not\Rightarrow\text{stability/support}}
\]

---

## Experiment 524 — Dynamic support does not imply closure

Conversely, one may choose a positive-definite axis Hessian on a geometry that does not satisfy a declared cyclic or formal closure requirement.

### Verdict

\[
\boxed{\text{support}\not\Rightarrow\text{closure}}
\]

so the two notions are independent layers.

---

## Experiment 525 — Closure cannot provide an absolute normalization

Keep all axis lines, bilinear geometry, and closure statuses fixed while rescaling the dynamic operator block

\[
(M_A,K_A,R_A,C_A)\mapsto
\lambda(M_A,K_A,R_A,C_A),
\qquad\lambda>0.
\]

The geometric closure data remain unchanged while dynamic energies/susceptibilities change, and characteristic ratios may remain unchanged under common principal rescaling.

### Verdict

Closure cannot determine `mu_0`, `mu_A`, or another universal absolute constitutive scale.

---

## Experiment 526 — Closure as an admissible-domain constraint

A productive structural-gravity use of closure is to define an admissible configuration subset

\[
\mathcal M_{\rm cl}
\subseteq
\mathcal M_{\rm axis}.
\]

If the closure condition is locally represented by

\[
\Phi(q)=0,
\]

then a dynamics that preserves closure must satisfy the tangency condition

\[
\boxed{D\Phi(q)\dot q=0}.
\]

A second-order constrained realization may introduce Lagrange multipliers or a projection onto the tangent bundle of `M_cl`.

Alternatively, the model may explicitly permit a `closure-transition event` and leave `M_cl`.

### Verdict

Closure is naturally an admissibility/constraint structure. A restoring force toward closure requires an additional constitutive energy or penalty coefficient and is not supplied by closure status itself.

---

## Experiment 527 — Penalty enforcement is an extra law, not closure itself

For example,

\[
E_{\rm cl}=\frac{\kappa_{\rm cl}}2\|\Phi(q)\|^2
\]

would generate a force toward the closure manifold, but `kappa_cl` is a new constitutive coefficient.

Hence

\[
\boxed{\text{closure constraint}\neq\text{closure-restoring stiffness}.}
\]

---

## Experiment 528 — Cyclic closure does not by itself imply isotropy

Even when a cyclic triad becomes pairwise orthogonal under the chosen nondegenerate positive reference geometry, the second moment

\[
Q=\sum_iw_iP_i
\]

still depends on the weights. Unequal weights give `A != 0` even for an orthogonal triad.

### Verdict

\[
\boxed{\text{cyclic/orthogonal triad}\not\Rightarrow\mathcal A=0}
\]

without the equal-weight/completeness specialization.

---

## Experiment 529 — Nondegeneracy is not dynamic positivity

The old nondegeneracy condition checks whether selected subspaces have zero radical,

\[
\operatorname{Rad}(S)=S\cap S^\perp=\{0\}.
\]

This ensures clean bilinear decompositions where declared, but it does not imply

\[
M_A\succ0,
\quad
K_A\succeq0,
\quad
H_A\succ0.
\]

### Verdict

\[
\boxed{\text{bilinear nondegeneracy}\neq\text{kinetic/stiffness/support positivity}.}
\]

---

## Experiment 530 — Minimal realized-axis geometric block

The migration audit now supports the following **geometry-only** block:

\[
\boxed{
\mathcal G_A
=
\{\ell_a/P_a,\ b_0,\ W_A,\operatorname{arank},\ G_{ab},
N^{\rm int/amb},\ \mathcal C_{\rm cl}\}
}
\]

where `C_cl` denotes the separately typed closure/nondegeneracy profiles.

No physical inertia, force, support coefficient, or gravity normalization is placed in this block.

---

## Experiment 531 — Minimal static property block

Retain the old typed property records as a separate block

\[
\boxed{
\mathcal P_A
=
\{z_{\rm tension},z_{\rm stiffness},z_{\rm restoration},
 z_{\rm inertia},z_{\rm coupling},z_{\rm support},\ldots\}
}
\]

with their original unary/binary/higher/mixed typed profiles and status distinctions.

The records are not yet physical coefficients.

---

## Experiment 532 — Minimal constitutive operator block

An explicit structural-gravity bridge

\[
\boxed{
B_A:(\mathcal G_A,\mathcal P_A)
\longrightarrow
\mathcal O_A
}
\]

supplies, when admitted,

\[
\mathcal O_A
=
\{M_A,K_A,R_A,C_A,\Sigma_A,\mathcal A_*,
\Gamma_A,\text{field/source couplings}\}.
\]

Interpretation:

- `M_A`: tangent kinetic/inertial operator;
- `K_A`: tangent/spatial stiffness operator;
- `R_A`: restoration operator;
- `C_A`: coupling block;
- `Sigma_A`: prestress/tension-like state;
- `A_*`: restoration target;
- `Gamma_A`: optional dissipation/mobility data.

Every numerical map remains model-specific unless separately derived.

---

## Experiment 533 — Minimal dynamic event block

The operator block acts on a component-resolved axis state. For projector axes a safe kinematic layer is

\[
\dot P_a=[\Omega_a,P_a].
\]

The event vocabulary is kept separate:

- line reorientation;
- relational change;
- collective rank transition;
- closure transition;
- property-status/domain transition;
- support-loss event.

No one of these is identified with another by name.

---

## Experiment 534 — Minimal derived structural-gravity readout block

From the component-resolved state one may derive

\[
Q=\sum_aw_aP_a,
\qquad
\mathcal A=Q-I/3,
\qquad
h_A=e^{\beta_A\mathcal A},
\]

plus diagnostics such as

\[
m_{\rm sup}=\lambda_{\min}(H_{\rm full}),
\qquad
c_{A,\rm char},
\]

collective rank, closure status, and stasis/critical-slowing indicators.

These are reduced/derived readouts and need not reconstruct the full typed component state.

---

## Experiment 535 — Minimal axis-module architecture

The structural-gravity axis specialization can now be organized as

\[
\boxed{
\mathfrak M_A^{\rm SG}
=
(\mathcal G_A,\mathcal P_A,B_A,\mathcal O_A,
\mathcal S_A,\mathcal D_A)
}
\]

where

1. `G_A` — realized-axis geometry and closure prerequisites;
2. `P_A` — typed static property records;
3. `B_A` — explicit constitutive bridge;
4. `O_A` — dynamic coefficients/operators/forms;
5. `S_A` — component-resolved dynamic state and event laws;
6. `D_A` — derived coarse geometry and stability/propagation diagnostics.

The progression-field coupling (`psi`, `mu_0`, source/probe bridge) remains an adjacent structural-gravity sector and is **not** absorbed into the axis-property module.

---

## Experiment 536 — Final migration verdict

The original plan to move the old realized-axis property material into structural gravity survives, but its completed meaning is now:

\[
\boxed{
\text{preserve axis specialization}
\to
\text{preserve typed candidate properties}
\to
\text{classify each layer}
\to
\text{supply/audit constitutive bridges}
\to
\text{derive structural-gravity dynamics and diagnostics}
}
\]

The audit rejects the following retroactive identifications:

- independence/rank = support;
- orthogonality = isotropy;
- normal = unique vector in all ranks;
- cyclic closure = physical dimension selection;
- closure = stability;
- closure = restoring force;
- nondegeneracy = dynamic positivity;
- axis geometry = absolute gravity normalization.

The strongest surviving positive roles are:

- independence/orthogonality/normals/closure constrain the **admissible geometry**;
- tension/prestress, stiffness, restoration, inertia, and coupling become **operator roles only through `B_A`**;
- reorganization/rank/closure/support loss are **distinct dynamic events or diagnostics**;
- `Q -> A -> h_A` is a downstream coarse geometric bridge, not a complete axis-state representation;
- `mu_0` remains a separate progression-sector normalization and is not recovered by the axis module.

## Next audit target

With the migration layer now closed at the role/architecture level, the next structural-gravity step should return to physical calculation rather than continue renaming old properties:

1. choose the **minimal** axis module needed by the current progression-field coupled model;
2. remove unused old property roles from the first structural-gravity paper rather than carrying the full vocabulary into the main equations;
3. test one explicit constrained projector/axis-field model against the previously derived self-field spectral threshold and coupled-instability results;
4. only after that decide which migrated axis properties deserve named definitions in the paper body and which should remain optional appendix/specialization material.
