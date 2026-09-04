# Structural Gravity Audit — Minimal Axis-Property Bridges and Separation Countermodels

Date: 2026-09-04
Method: DSD Analysis / General Audit / Mode-D matched controls
Status: follow-up to axis-property migration audit

## 1. Minimal operator carrier

Let H_A be the chosen axis-reorganization state space of a structural-gravity specialization. A constitutive bridge may output

- M_A : H_A -> H_A* — axis-reorganization inertia/kinetic operator,
- K_A^{ij} — spatial stiffness operator/tensor,
- R_A : H_A -> H_A* — restoration/relaxation operator,
- C_A — coupling operator between the axis sector and other structural-gravity sectors,
- Omega_A — reorientation generator or generator-producing map,
- diagnostic maps derived only after these operators and the state are fixed.

Possible well-posedness conditions such as symmetry, positivity, coercivity, locality, covariance, or boundedness belong to the specialization and are not supplied by property names alone.

## 2. Tension is not stiffness

Suppose a one-mode axis deformation coordinate q has stress/tension state

sigma(q) = sigma_0 + k q + O(q^2).

At q=0 two models may have the same tension

sigma_1(0) = sigma_2(0) = sigma_0

but different stiffness

k_1 != k_2.

Conversely sigma_0 = 0 can coexist with k > 0.

Therefore

axis tension != axis stiffness

without an explicit constitutive derivative or bridge.

Recommended layering:

- tension: static stress/balance property P/R,
- stiffness: constitutive operator O,
- optional bridge: B_tauK : tension/deformation records -> K_A.

## 3. Crossing is not coupling

Matched control A:

Two realized lines intersect or are non-orthogonal, but C_A = 0.

Matched control B:

Two nonintersecting or spatially separated axis-associated components communicate through a mediator field, so C_A != 0.

Hence geometric crossing/incidence is neither necessary nor sufficient for dynamical coupling.

Recommended layering:

- crossing: G/R,
- coupling: R -> O through B_cpl.

## 4. Support is not restoration

Let a local stability/support margin be defined after linearization by

m_sup = lambda_min(L_eff),

where schematically

L_eff = K_A + R_A - C_A L_other^{-1} C_A*.

Two systems can have the same restoration R_A but different coupling C_A, producing different m_sup. Likewise a system may have nonzero restoration while the total effective operator is unstable.

Therefore support is naturally a derived admissibility/stability diagnostic unless an independent static support property is explicitly supplied.

Recommended layering:

- support-state: optional P,
- support/stability margin: D,
- restoration: P -> O.

## 5. Reorientation is not rank transition

A rigid rotation

P_i(t) = R(t) P_i(0) R(t)^T

can change realized-axis directions while preserving rank and all projector ranks.

Conversely line dependencies can change realized-axis rank without requiring a change in a selected static property value.

Therefore

reorientation != rank transition.

Recommended layering:

- reorientation: E,
- rank: G diagnostic,
- rank transition: E only when the realized-axis span actually changes.

## 6. Axis inertia is not matter mass

An axis-orientation field can have kinetic term

(1/2) <dot A, M_A dot A>

with M_A changed while the matter density rho and total matter mass M remain fixed.

Therefore the coefficient controlling resistance to axis reorganization is not identified with matter mass and is also distinct from the universal progression-sector normalization mu_0.

Recommended layering:

- axis-inertia property: P,
- M_A or mu_A: O supplied by B_inertia,
- matter mass: separate source sector.

## 7. Restoration is not support capacity

A restoration operator can drive A toward a target A_*:

F_rest = -R_A(A-A_*).

This says how the state is driven back locally. It does not by itself specify how much forcing the full coupled system can withstand before a stability threshold is crossed.

Support/capacity can depend on R_A, K_A, C_A, geometry, boundary conditions, and the progression-field state simultaneously.

Therefore restoration and support capacity must remain separate.

## 8. Coupling property is not coupling coefficient

Let p_cpl be one fixed typed coupling property record. Two admissible constitutive bridges can assign

B_1(p_cpl) = C_A,
B_2(p_cpl) = 2 C_A.

The static property data are identical while the coupled stability threshold changes.

Thus the property record does not determine the coefficient without an additional law.

## 9. Minimal bridge package

Use separate typed maps rather than one semantic identity:

B_inertia : D_inertia -> Op_inertia,
B_stiff   : D_stiff   -> Op_stiff,
B_rest    : D_rest    -> Op_rest,
B_cpl     : D_cpl     -> Op_cpl,
B_reor    : D_reor    -> Generator_A.

Each domain retains the full typed profile inherited from the Property Axiom System and realized-axis specialization. If two bridges reuse one property record, that reuse is explicit bookkeeping rather than automatic duplication of the property.

## 10. DSD General Audit verdicts

D — The sources support the separation of property data, realized-axis geometry, and dynamic operators.

R — The classifications are made at property/geometric/dynamic/operator resolution rather than at name-only resolution.

S — Retain old axis-specific vocabulary as candidate specialization material.

E — Exclude direct semantic identities that have explicit countermodels.

T — Require an explicit bridge for every transition from property/geometry to physical operator.

C — No contradiction was found between the rewritten papers and the migration plan once the layers are separated.

N — No external normative rule is introduced; physical well-posedness criteria remain specialization-specific.

O — Migration survives as a typed specialization workflow; several naive pairwise identifications are rejected.

## 11. Final migration matrix

- tension -> P/R -> optional stress/stiffness bridge,
- crossing -> G/R -> geometric input only unless coupled explicitly,
- coupling -> R -> C_A,
- support -> P and/or D -> stability/capacity diagnostic,
- reorganization -> E -> Omega_A or another declared evolution law,
- stiffness -> P -> K_A,
- inertia -> P -> M_A,
- restoration -> P -> R_A.

The arrows denote candidate constitutive use, not axiomatic identity.

## Next target

Formalize one bridge at a time, beginning with axis restoration because it has the cleanest current operator role. Audit its typed domain, positivity/coercivity conditions, locality, target state, and countermodels before moving to stiffness, inertia, and coupling.
