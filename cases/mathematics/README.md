# Mathematics / Algebra Domain

This domain records DSD Analysis cases whose source problems belong primarily to standard mathematical structures, algebra, structure-preserving maps, quotients, invariants, decomposition, and aggregation.

## Operating rule

The external mathematical structure is described first in its own terminology. DSD terminology is introduced only in a separate comparison layer. Similar names such as `composition`, `sum`, `union`, or `aggregation` do not establish identity of operations.

Each case must classify a proposed correspondence as one of:

- direct correspondence,
- partial correspondence,
- correspondence after explicit additional encoding,
- non-correspondence.

Counterexamples and failure boundaries are retained as results rather than removed from the analysis.

## Current sequence

### MATH-001 / Global Case 028 — finite subsets, partial operations, and DSD finite composition

Status: **first-pass analysis complete**.

Primary verdict: **partial correspondence**.

Established:

1. `(P_fin(C_L), union, emptyset)` is a commutative idempotent monoid / join-semilattice with bottom.
2. `Comp_L` is not a full union-monoid homomorphism except when `T_L` is identically zero.
3. `Comp_L` is exactly finitely additive on disjoint finite channel supports.
4. The exact overlap identity is
   `Comp(F)+Comp(G)=Comp(F union G)+Comp(F intersect G)`.
5. Free-commutative-monoid / multiset linearization is valid only as explicit additional encoding.
6. Equal composite output does not reconstruct source support or strict descriptive equivalence.
7. No contradiction with the DSD Formation Axiom System was found.

See `028_finite_subsets_partial_operations_composition/` for the proof, witnesses, audit, sources, reproducibility record, and verdict.

### Planned later sequence

- MATH-002: quotient structures, kernels, and aggregate information loss,
- MATH-003: same carrier with different algebraic or bilinear structures,
- MATH-004: invariants and incomplete classification,
- MATH-005: decomposition, composition, and reconstruction conditions.

## DSD source interfaces

Primary DSD sources for this domain are:

- Formation Axiom System: Stages VI–VII, finite composition, non-injective composition, forward maps, embeddings, strict equivalence.
- Axis-property system: separation of underlying carriers from additional properties and incomplete classification by rank or matrix size.
- Channel-Indexed Static Aggregation: finite aggregation, support-tagged data, aggregation kernels, and reconstruction limits.

Dynamics was not required for MATH-001. It remains out of scope unless a later mathematics case explicitly introduces temporal structure.
