# DSD Source Notes

## Axis Property Axiom System

Primary section: Section 12, `Compression and Classification Obstructions`.

Relevant source facts:

- Theorem 10.7 makes strict Stage-VI-fixed, signature-fixed, representation-inclusive axis-property isomorphism an equivalence relation.
- Proposition 12.1: equal realized-axis rank need not imply strict property equivalence.
- Proposition 12.2: equal matrix size need not imply strict property equivalence.
- Definition 12.3 defines a displayed finite-coordinate scalar summary
  `Scal_{p,I}(D)=kappa(arank(D))+sum_{tau in I} omega_tau chi_tau(D)`.
- The `chi_tau` are introduced as indicator maps; Definition 12.3 does not state that they must be strict-isomorphism invariants.
- The paper explicitly says this summary is the displayed finite-coordinate compression, not an arbitrary set-theoretic scalar coding of the full descriptor.
- Proposition 12.4 is conditional: if two descriptors have equal rank and every selected indicator agrees, while one typed property value differs, then the scalar summaries collide although the full models are not strictly isomorphic.
- Corollary 12.5 therefore calls rank, matrix size, and the displayed summary incomplete classifiers on classes containing the relevant collisions.
- Section 12.1 says later scalar/functional aggregates should be treated as reduced representatives rather than complete classifiers unless a reconstruction theorem is supplied.

## Channel-Indexed Static Aggregation

- Theorem 11.4 gives exact fixed-support injectivity conditions.
- Corollary 11.5 states aggregate equality is not a general reconstruction theorem.
- Support-tagged records preserve distinctions erased by sums.

## Structural Reorganization Dynamics

- Section 16 defines reduced readouts after the component-resolved state is specified.
- A readout need not be a complete classifier.
- Proposition 16.1 and the later toy model provide same-readout/different-state collisions.

## Interpretation discipline

The axis-property paper proves incompleteness only for the displayed summary under its stated collision hypothesis. It does not prove that every finite summary, every scalar-valued map, or every possible encoding of a complete descriptor is necessarily incomplete.