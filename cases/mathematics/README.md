# Mathematics / Algebra Domain

This domain records DSD Analysis cases whose source problems belong primarily to standard mathematical structures, algebra, structure-preserving maps, quotients, invariants, decomposition, and aggregation.

## Operating rule

The external mathematical structure is described first in its own terminology. DSD terminology is introduced only in a separate comparison layer. Similar names such as `composition`, `sum`, `union`, `kernel`, `quotient`, `rank`, `matrix`, or `aggregation` do not establish identity of structures.

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
4. The exact overlap identity is `Comp(F)+Comp(G)=Comp(F union G)+Comp(F intersect G)`.
5. Free-commutative-monoid / multiset linearization is valid only as explicit additional encoding.
6. Equal composite output does not reconstruct source support or strict descriptive equivalence.
7. No contradiction with the DSD Formation Axiom System was found.

See `028_finite_subsets_partial_operations_composition/`.

### MATH-002 / Global Case 029 — quotients, kernels, and aggregate information loss

Status: **first-pass analysis complete**.
Primary verdict: **partial correspondence**.

Established:

1. For fixed finite support `F`, the DSD summation map `S_F:W_L^F->W_L` is an ordinary linear map and its kernel is a standard linear-algebra kernel.
2. The DSD fixed-support injectivity criterion `(A_F-A_F) intersect ker S_F={0}` is an exact standard reconstruction criterion.
3. The relation `F ~_Comp G iff Comp(F)=Comp(G)` is always an equivalence relation on finite supports.
4. This relation is not generally a congruence for union, so `P_fin(C_L)/~_Comp` is a quotient set but not generally a quotient join-semilattice.
5. A free-vector-space additive lift makes collisions exactly equivalent to differences lying in a linear kernel, but this is explicit additional encoding.
6. Naive global zero-padding is not faithful to DSD because it collapses channel absence into selected zero contribution.
7. No contradiction with the Formation, Axis-property, or Static Aggregation papers was found.

See `029_quotients_kernels_information_loss/`.

### MATH-003 / Global Case 030 — same carrier, rank, and matrix size versus enriched structure

Status: **first-pass analysis complete**.
Primary verdict: **direct correspondence with a signature-scope qualification**.

Established:

1. The same underlying carrier can support nonisomorphic algebraic structures.
2. The same vector carrier and dimension can support nonisometric symmetric bilinear forms.
3. DSD Construction 11.11 directly realizes the same standard pattern: same base, signature, realized lines, rank, bilinear data, and closure data but different typed unary property values, hence no strict axis-property isomorphism.
4. Equal matrix size does not classify representation-inclusive axis-property structure.
5. Equal bare realized line does not force equal tagged property values for tag-sensitive kinds.
6. Optional matrix/tensor/operator/quaternion representations remain encodings rather than the abstract property system itself.
7. Important boundary: finite-dimensional vector spaces over a fixed field are classified by dimension, so rank incompleteness is relative to the enriched axis-property signature, not universal.
8. No contradiction with the Formation or Axis Property axiom systems was found.

See `030_same_carrier_enriched_structures/`.

### Planned later sequence

- MATH-004: invariants and incomplete classification,
- MATH-005: decomposition, composition, and reconstruction conditions.

## DSD source interfaces

Primary DSD sources for this domain are:

- Formation Axiom System: Stages VI–VII, finite composition, non-injective composition, forward maps, embeddings, strict equivalence.
- Axis-property system: separation of underlying carriers from additional properties and incomplete classification by rank or matrix size.
- Channel-Indexed Static Aggregation: finite aggregation, support-tagged data, aggregation kernels, and reconstruction limits.

Dynamics remains outside the core mathematics sequence unless a later case explicitly introduces temporal structure.
