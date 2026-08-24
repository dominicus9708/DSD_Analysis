# Result

Status: COMPLETED — FIRST-PASS MATHEMATICS/ALGEBRA CASE.

Global case: 032
Domain case: MATH-005

## 1. Standard mathematical finding

Unique additive decomposition is controlled by injectivity of the canonical sum map. For subspaces `U_c`, the map

`Sigma((u_c))=sum_c u_c`

is injective exactly when the corresponding sum is direct.

For the different problem of selecting fixed additive terms, distinct finite subset sums are controlled by the absence of nontrivial signed `{-1,0,1}` relations. In additive combinatorics this is the dissociated-set condition.

These are related but distinct reconstruction problems.

## 2. DSD forward-uniqueness finding

Formation Clause VII and the Static Aggregation realization uniquely determine the **forward** composite operator after Stage VI and the term map have been supplied:

`Comp_L(F)=sum_{c in F}T_L(c)`.

This uniqueness does not imply that `Comp_L` is injective. Hence it does not imply unique inverse recovery of the channel family or component record.

## 3. Fixed-support variable-component finding

For fixed `F`, the DSD static paper defines

`S_F:W_L^F->W_L`,

`S_F(y)=sum_c y_c`.

When `W_L != {0}` and `|F|>=2`, the full-product map has a nontrivial kernel, so arbitrary component decomposition is not unique.

The exact DSD theorem is more general than a direct-sum assumption:

`S_F|A_F` is injective iff `(A_F-A_F) intersect ker S_F={0}`.

If an application additionally constrains each coordinate to a channel-specific subspace `U_c`, then the usual direct-sum condition is exactly the special case that makes the sum map injective on the full product `product U_c`.

Thus direct-sum structure is a valid standard specialization, not a DSD axiom and not a necessary condition for every restricted admissible record class.

## 4. Exact Stage-VII support-reconstruction criterion

Fix a finite candidate channel family `C_0`. The support map

`Phi_T(F)=sum_{c in F}T_L(c)`

is injective exactly when there is no nonzero channel-indexed coefficient family

`epsilon_c in {-1,0,1}`

such that

`sum_c epsilon_c T_L(c)=0`.

When the term map is injective, this is exactly dissociativity of the finite term image.

Therefore Stage-VII support reconstruction needs only distinct subset sums. Full linear independence or a direct-sum decomposition of the ambient term space is sufficient but stronger than necessary.

## 5. Minimal boundary witnesses

- In `R`, `S(x,y)=x+y` is noninjective: `1=1+0=0+1`.
- In `R^2`, axis subspaces `span(e_1)` and `span(e_2)` give unique direct-sum decomposition.
- Terms `1` and `2` in `R` are linearly dependent but have distinct subset sums `0,1,2,3`.
- Terms `1,2,3` have the signed relation `1+2-3=0`, producing `{a,b}` versus `{c}` collision.
- A zero term gives `Comp(emptyset)=Comp({c})`, so absence and selected zero cannot be reconstructed from the aggregate.

## 6. Support-tag boundary

Numeric coordinate recovery is not automatically DSD support recovery. If a selected channel may contribute zero, then an absent channel and a selected-zero channel have the same numeric coordinate.

Therefore faithful varying-support reconstruction requires at least one of:

- explicit support retention, as in the DSD support-tagged carrier;
- a separate presence marker;
- a declared nonzero-selection rule together with sufficient numeric uniqueness conditions.

The current static paper chooses explicit support retention.

## 7. Combined typed-record finding

The static paper's combined channel/property map has kernel

`ker S_F direct-sum ker P_G`

and uses the same exact difference-set criterion for injectivity on admissible combined records. This is an ordinary product of two standard linear reconstruction problems.

## 8. H1–H7 disposition

- H1 — unique Clause-VII completion implies unique inverse reconstruction: **falsified**.
- H2 — arbitrary fixed-support component decomposition is unique: **falsified when at least two unrestricted coordinates are present**.
- H3 — direct-sum independence gives unique variable-component decomposition: **confirmed**.
- H4 — direct sum / linear independence is necessary for Stage-VII finite-support recovery: **falsified**.
- H5 — absence of nontrivial signed `{-1,0,1}` relations exactly characterizes fixed-term support recovery: **confirmed**.
- H6 — numeric uniqueness alone reconstructs support when selected zero is allowed: **falsified**.
- H7 — the DSD static reconstruction theorem matches standard injectivity theory: **confirmed**.

## 9. Correspondence verdict

**Primary classification: DIRECT CORRESPONDENCE, WITH FORWARD/INVERSE AND SUPPORT-TAG BOUNDARIES.**

The DSD fixed-support kernel theorem is standard injectivity/reconstruction theory. Direct sums provide the standard unique-decomposition specialization. Stage-VII finite support recovery corresponds more precisely to distinct subset sums / dissociativity, while support tagging retains the additional DSD distinction between absence and selected zero.

## 10. DSD consequence

No contradiction with the current Formation, Axis Property, or Static Aggregation papers was found.

The strongest sharpening is:

> `unique Stage-VII closure`, `unique additive decomposition`, and `unique channel-support reconstruction` are different mathematical statements and must not be used interchangeably.

## 11. Final case statement

MATH-005 closes as a **direct correspondence with reconstruction-layer qualifications**:

**DSD finite aggregation follows standard additive reconstruction theory: direct-sum independence characterizes unique variable-component decomposition on full subspace products, the existing difference-set/kernel theorem exactly characterizes restricted fixed-support reconstruction, and Stage-VII recovery of a finite selected channel support is governed by distinct subset sums rather than by linear independence. Explicit support tags remain necessary whenever channel absence must stay distinct from selected zero contribution.**
