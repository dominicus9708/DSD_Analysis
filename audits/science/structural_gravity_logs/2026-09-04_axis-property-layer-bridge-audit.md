# Structural Gravity Audit — Axis-Property Layer Classification and Minimal Bridge Contract

Date: 2026-09-04
Method: DSD Analysis + DSD General Audit + Mode-A/Mode-D controls
Status: migration follow-up

## 1. Audit question

After the rewritten Formation Axiom System, general Property Axiom System, Channel-Indexed Static Aggregation, and Structural Reorganization Dynamics, classify the axis-specific material preserved from the former realized-axis property system into the correct logical layers before importing it into structural gravity.

The audit explicitly forbids retrofitting old property names to the current structural-gravity equations.

## 2. Source constraints

The current Property Axiom System keeps realized-axis machinery as a downstream geometric specialization rather than part of the universal property core. The dynamics layer treats realized-axis geometry as optional and requires an explicit constitutive dynamic bridge before typed properties can become inertia, restoration, stiffness, coupling, transport, or propagation operators. The static aggregation layer preserves full typed profiles and does not allocate multi-input properties to one channel without an explicit selector.

Therefore the migration cannot be a literal transfer of old labels into physical coefficients.

## 3. Six-layer classification

Use the following layer tags.

- G — geometric datum: realized line, rank, angle, normal, bilinear/closure data.
- P — static typed property: a property record defined at one static slice.
- R — relational/higher-order property: property data whose input profile contains multiple axes/tags/configurations.
- E — dynamic event/law: line motion, reorientation, rank transition, support-signature transition.
- O — constitutive operator/coefficient: inertia, stiffness, restoration, coupling, transport, propagation operator.
- D — derived diagnostic: support margin, stability index, residual, threshold distance, postprocessed observable.

The allowed dependency pattern is

G/P/R -> explicit constitutive bridge -> O/E -> D.

No old property label is allowed to collapse P or R directly into O.

## 4. Per-property classification

### Axis tension

Primary layer: P or R.
Possible downstream role: O.

Preserve it as a stress/balance-type or tension-like property record. It may inform a spatial stiffness operator, but `tension = stiffness coefficient` is not a definition. Equilibrium relations do not fix an absolute magnitude.

Verdict: RETAIN; BRIDGE REQUIRED.

### Axis crossing

Primary layer: G or R.
Possible downstream role: input to O.

Crossing, incidence, angle, or non-orthogonality are geometric/relational facts. They do not imply dynamical coupling by themselves.

Verdict: RETAIN AS GEOMETRIC/RELATIONAL INPUT.

### Axis coupling

Primary layer: R.
Possible downstream role: O.

A coupling property can inform a coupling operator C_A or dimensionless sensitivity beta_A, but the operator/value is not determined by the label.

Verdict: RETAIN; CONSTITUTIVE BRIDGE REQUIRED.

### Axis support

Primary layer: P or D.
Possible downstream role: E/constraint.

Separate a static support-state property from a derived stability/capacity diagnostic. Current audits do not support treating support as an absolute force scale or as the origin of the universal progression normalization.

Verdict: RETAIN; ROLE PARTLY OPEN.

### Axis reorganization

Primary layer: E.
Possible downstream role: O supplies the rate/generator.

Treat reorganization mainly as realized-axis geometric evolution or transition, not as a static scalar property. A projector-commutator flow is one possible downstream law, not the definition of reorganization.

Verdict: MOVE TO DYNAMIC EVENT/LAW LAYER.

### Axis stiffness

Primary layer: P.
Possible downstream role: O.

Natural current role witness: spatial stiffness operator of the axis-reorganization sector, denoted K_A or T_A in current toy models.

Verdict: RETAIN; STRONG OPERATOR-ROLE CANDIDATE.

### Axis inertia

Primary layer: P.
Possible downstream role: O.

Natural current role witness: kinetic/inertial operator of axis reorganization, denoted M_A or mu_A in current toy models. Keep distinct from physical matter mass and from the universal progression-sector normalization mu_0.

Verdict: RETAIN; STRONG OPERATOR-ROLE CANDIDATE.

### Axis restoration

Primary layer: P.
Possible downstream role: O.

Natural current role witness: restoration/relaxation operator R_A controlling axis-anisotropy susceptibility.

Verdict: RETAIN; STRONG OPERATOR-ROLE CANDIDATE.

## 5. Minimal constitutive bridge

For a structural-gravity specialization use a typed map

B_ax,dyn,t : D_ax(t) -> O_ax(t),

where D_ax(t) preserves the complete typed realized-axis geometry and selected axis-property records, and O_ax(t) is an application-declared carrier such as

{M_A, K_A, R_A, C_A, Omega_A, ...}.

This bridge is additional data. It is not fixed by the property names.

## 6. Mandatory regression checks

A1. Preserve complete typed profiles; do not unary-assign a binary/higher-order record without an explicit selector.

A2. Preserve undeclared / inapplicable / prerequisite-unsatisfied / undefined / defined-zero distinctions.

A3. Keep geometry and property independent unless a law connects them: fixed rank may coexist with property change, and fixed property may coexist with rank change.

A4. Allow bridge non-uniqueness unless uniqueness is proved.

A5. Respect representation invariance: a line-invariant property must be invariant under n -> -n; orientation-sensitive data must declare that sensitivity.

A6. Every regular dynamic slice must reduce to a valid static property slice and valid realized-axis specialization.

A7. Equal aggregate readouts do not reconstruct full property support/profile without an injectivity theorem.

A8. No property label alone may be promoted to force, mass, energy, propagation speed, or absolute normalization.

## 7. DSD Analysis Mode-A negative control

Reject the tempting direct identities

axis inertia == mu_A,
axis stiffness == T_A,
axis restoration == R_A

as universal definitions.

The current dynamics explicitly permits multiple admissible constitutive bridges over the same static typed data. Therefore the direct-identification hypothesis fails, while the migration plan itself survives.

## 8. DSD Analysis Mode-D synthetic controls

D1. Same realized-axis geometry, different property value: any rule reconstructing property solely from geometry must fail.

D2. Same property value, different realized-axis rank: any rule reconstructing rank solely from one property must fail.

D3. Same complete static property data, two admissible bridges: different dynamics must remain possible unless an extra uniqueness law is supplied.

D4. Same aggregate output, different property support/profile: automatic reconstruction from aggregate must fail.

These controls should remain as regression tests for any future structural-gravity axis module.

## 9. Acceptance protocol for future migration

Before an axis-specific item enters a structural-gravity equation, record:

1. item name;
2. typed input profile;
3. applicability/prerequisite/status;
4. logical layer G/P/R/E/O/D;
5. constitutive bridge domain/codomain;
6. operator/event interpretation;
7. locality/covariance/positivity/invariance conditions;
8. minimal countermodel;
9. observable or diagnostic consequence.

Items with no bridge are preserved candidates. Items with a supplied but non-unique bridge are conditional operator-role candidates. Stronger physical status requires an independent derivation or empirical constraint.

## 10. Final verdict

The axis-property migration plan remains valid and is made cleaner by the rewritten papers. The correct operation is not `copy old axis properties into structural gravity`, but

realized-axis specialization -> typed axis-property candidate -> layer audit -> explicit constitutive bridge -> structural-gravity operator/event/diagnostic.

Current structural-gravity calculations are useful role witnesses and countermodels, not retroactive definitions of the earlier axis-property labels.
