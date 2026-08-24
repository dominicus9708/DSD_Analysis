# Result

Status: COMPLETED — FIRST-PASS MATHEMATICS/ALGEBRA CASE.

Global case: 031
Domain case: MATH-004

## 1. Standard mathematical finding

For a class `X` with equivalence relation `~`, an invariant `I:X->Y` is constant on equivalence classes. It is complete when

`I(x)=I(y) iff x~y`.

Equivalently, the induced map `X/~ -> Y` is injective.

Thus a collision between inequivalent objects is exactly the obstruction to completeness.

## 2. Standard finite witness

The matrices

`A=[[0,0],[0,0]]`,

`B=[[0,1],[0,0]]`

have the same characteristic polynomial `lambda^2`, trace, determinant, and eigenvalue multiset, but they are not similar because their ranks differ. Hence familiar similarity invariants can be incomplete.

By contrast, Jordan block data form a complete similarity classifier when Jordan normal form is available. Therefore reduced invariants may be incomplete, but incompleteness is not forced merely by finite-dimensional or scalar representation.

## 3. DSD rank and matrix-size finding

Under strict axis-property isomorphism, realized spans are transported by linear isomorphism, so realized-axis rank is an invariant.

Construction 11.11 and Proposition 12.1 give equal-rank nonisomorphic models, so rank is not complete for the full axis-property signature.

Proposition 12.2 similarly shows matrix size is not a complete classifier of representation-inclusive axis-property structure.

This directly matches standard invariant theory.

## 4. Displayed finite-coordinate scalar summary

Definition 12.3 defines

`Scal(D)=kappa(arank(D))+sum_tau omega_tau chi_tau(D)`

using arbitrary indicator maps `chi_tau`.

Therefore the displayed scalar summary is **not automatically an invariant** under strict axis-property isomorphism. It becomes an invariant if the selected indicators are separately required to be invariant.

This is not a defect in the source paper: the paper calls the construction a scalar summary/compression, not an invariant.

## 5. Collision obstruction

Proposition 12.4 assumes equal rank and equal selected indicator values while a typed property value differs. It concludes that the displayed scalar summaries agree although strict axis-property isomorphism fails.

Hence:

- as written, the proposition is a valid incomplete-classifier/readout collision theorem;
- if all selected indicators are additionally strict-isomorphism invariants, the same witness proves that the scalar invariant is incomplete.

## 6. Overstatement boundary

The DSD source does **not** prove:

`every scalar-valued map is incomplete`,

or

`every finite-coordinate compression loses structure`.

The paper explicitly restricts Definition 12.3 to the displayed finite-coordinate compression and says it is not an arbitrary set-theoretic scalar coding of the full descriptor.

A complete invariant may be finite or even scalar-valued whenever it separates the relevant equivalence classes. Completeness is a property of the map relative to the equivalence relation, not of the codomain label `scalar` alone.

## 7. Downstream corroboration

The Static Aggregation paper independently requires injectivity/reconstruction conditions before aggregate equality reconstructs records, and the Dynamics paper says a reduced readout need not be a complete classifier and supplies collision examples.

These statements are consistent with the same standard classification principle.

## 8. H1–H7 disposition

- H1 — realized-axis rank is invariant under strict axis-property isomorphism: **confirmed**.
- H2 — rank is complete for the full axis-property signature: **falsified**.
- H3 — matrix size is complete for representation-inclusive structure: **falsified**.
- H4 — Definition 12.3's scalar summary is automatically an invariant: **falsified without an invariance condition on the indicators**.
- H5 — invariant indicators make the weighted scalar summary invariant: **confirmed**.
- H6 — a Proposition-12.4 collision makes such an invariant summary incomplete: **confirmed**.
- H7 — every scalar or finite summary is intrinsically incomplete: **falsified as an overstatement**.

## 9. Correspondence verdict

**Primary classification: DIRECT CORRESPONDENCE, WITH AN INVARIANT/READOUT TERMINOLOGY BOUNDARY.**

The DSD compression/classification obstruction is an ordinary incomplete-invariant / non-separating-readout phenomenon from standard classification theory. The source papers preserve the necessary scope by stating explicit collisions and reconstruction conditions rather than claiming universal impossibility of complete compression.

## 10. DSD consequence

No contradiction with the Formation, Axis Property, Static Aggregation, or Dynamics papers was found.

The main sharpening for future use is:

> A DSD descriptor/readout should be called an invariant only after invariance under the declared strict equivalence has been established; it should be called complete only after a reconstruction or separation theorem proves the converse.

## 11. Final case statement

MATH-004 closes as a **direct correspondence with terminology and scope qualification**:

**DSD rank, matrix-size, finite-coordinate-summary, aggregate, and readout collisions instantiate the standard distinction between invariants and complete invariants. Their incompleteness follows from explicit failure to separate strict-equivalence classes, not from scalarity or finite compression by itself.**