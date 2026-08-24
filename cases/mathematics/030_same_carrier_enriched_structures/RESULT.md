# Result

Status: COMPLETED — FIRST-PASS MATHEMATICS/ALGEBRA CASE.

Global case: 030
Domain case: MATH-003

## 1. Standard mathematical finding

An underlying carrier does not determine an enriched mathematical structure. The same set may carry nonisomorphic group operations, and the same vector space may carry nonisometric bilinear forms or other inequivalent extra structure.

However, a coarse invariant can be complete in a restricted signature. In particular, finite-dimensional vector spaces over a fixed field are classified up to linear isomorphism by dimension.

Therefore the correct standard principle is not `rank is always incomplete`, but:

> completeness of an invariant is relative to the signature of structure being classified.

## 2. DSD finding

The axis-property paper explicitly separates:

- inherited Stage-VI channel identity,
- bare realized line,
- tagged realized axis,
- realized-axis rank,
- typed property assignments,
- bilinear/normal/closure-associated data,
- optional representations,
- complete descriptor and strict equivalence.

Construction 11.11 gives two rank-three extensions over the same base, shared signature, and realized lines with equal bilinear and closure data but different unary property values. Proposition 12.1 therefore shows equal rank does not imply strict axis-property equivalence.

Proposition 12.2 similarly shows equal matrix size does not imply strict representation-inclusive property equivalence.

Tag-sensitive properties additionally show that equality of the bare line does not imply equality of the full tagged property record.

## 3. Correspondence verdict

**Primary classification: DIRECT CORRESPONDENCE, WITH A SIGNATURE-SCOPE BOUNDARY.**

The central DSD distinction is a standard enriched-structure distinction:

`same carrier / same coarse invariant != same full structure`.

The correspondence is direct because standard algebra, linear algebra with forms, and model-theoretic structure all make isomorphism relative to the full operations/relations/signature rather than the carrier alone.

The necessary boundary is that dimension/rank can be complete for a narrower signature, such as plain finite-dimensional vector spaces over a fixed field.

## 4. Minimal witnesses

### Same carrier, different algebra

A four-element carrier can support `C4` or `V4`; they are not group-isomorphic because element-order structure differs.

### Same vector carrier and dimension, different bilinear structure

`R^2` with `diag(1,1)` and `diag(1,-1)` has the same underlying vector space and dimension but different real bilinear-form inertia, hence the forms are not isometric.

### DSD same rank, different complete property structure

Axis Property Construction 11.11 fixes rank three and the realized lines but changes one unary property value; strict isomorphism fails.

## 5. H1–H6 disposition

- H1 — same carrier forces same structure: **falsified**.
- H2 — same realized-axis rank forces strict axis-property equivalence: **falsified**.
- H3 — same matrix size forces representation-inclusive strict equivalence: **falsified**.
- H4 — dimension/rank is never a complete invariant: **falsified as an overstatement**; it is complete for plain finite-dimensional vector spaces over a fixed field.
- H5 — equal bare line forces equal tagged-axis property values: **falsified for tag-sensitive properties**.
- H6 — a representation is identical with the abstract property system: **falsified / category error**.

## 6. DSD consequence

No contradiction with the Formation or Axis Property axiom systems was found.

The analysis sharpens the interpretation of `arank`:

- it is a valid complete invariant for the realized linear span only at the bare vector-space level;
- it is not a complete invariant for the enriched axis-property model once typed properties, tag sensitivity, bilinear data, closure data, or representations are part of the signature.

Likewise matrix size is metadata about a chosen representation index family, not a classifier of the full property structure.

## 7. Novelty assessment

This case does **not** establish a new algebraic phenomenon. The DSD distinction is substantially standard mathematics instantiated in the DSD layered vocabulary.

Its value for DSD Analysis is methodological and consistency-oriented:

1. the axis-property system uses the standard carrier-versus-structure distinction correctly;
2. its non-classification claims are valid at the enriched-signature level;
3. an over-broad reading of rank incompleteness is blocked by the plain-vector-space boundary;
4. the tag/line distinction has a precise standard role as retention of additional structure rather than a new algebraic principle.

## 8. Final case statement

MATH-003 closes as a **direct correspondence with a scope qualification**:

**The DSD distinction between realized-axis carrier/rank and the full typed axis-property structure is an ordinary enriched-structure distinction from standard mathematics. Equal carrier, rank, or matrix size need not imply strict property equivalence; but rank can be complete when the comparison signature is reduced to the bare finite-dimensional vector-space layer.**
