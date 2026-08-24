# Result

Status: COMPLETED — FIRST-PASS MATHEMATICS/ALGEBRA CASE.

Global case: 029
Domain case: MATH-002

## 1. Standard mathematical finding

For a linear map `T:V->W`, the kernel is a subspace and the quotient `V/ker T` is naturally isomorphic to `im T`. More generally, an equivalence relation on an algebra defines a quotient algebra only when it is compatible with the operations, i.e. when it is a congruence.

## 2. DSD fixed-support finding

For each fixed finite channel support `F`, the static aggregation layer defines

`S_F:W_L^F->W_L`,

`S_F(y_F)=sum_{c in F} y_c`.

This is an ordinary linear map. Therefore:

- `ker S_F` is a standard linear kernel;
- `W_L^F/ker S_F ~= im S_F`;
- if `F` is nonempty, `S_F` is surjective and `W_L^F/ker S_F ~= W_L`;
- the DSD criterion `(A_F-A_F) intersect ker S_F={0}` is exactly the condition that the aggregation restriction be injective on the admissible record class `A_F`.

This part is a **direct correspondence** with standard linear algebra.

## 3. DSD varying-support finding

Define on Stage-VII finite channel families

`F ~_Comp G iff Comp(F)=Comp(G)`.

This relation is always an equivalence relation, so the quotient set

`P_fin(C_L)/~_Comp`

exists and is in canonical bijection with `im Comp` as a set.

However, it is not generally a congruence for union. The minimal witness uses `T(a)=T(b)=1`:

- `{a} ~_Comp {b}`,
- but after union with `{a}`, the aggregates become `1` and `2`.

Hence the operation

`[F] join [G] := [F union G]`

is not well-defined on aggregate-equality classes in general.

Therefore the aggregate-equality quotient of finite supports is **not generally a quotient semilattice**.

## 4. Exact additive lift

Let `K^(C_L)` be the free vector space on the admitted channels and define

`L_T(a)=sum_c a(c)T_L(c)`.

Then `L_T` is linear and

`K^(C_L)/ker L_T ~= im L_T`.

For finite supports `F,G`,

`Comp(F)=Comp(G)`

iff

`1_F-1_G in ker L_T`.

This gives an exact standard kernel/quotient account of finite-support collisions, but only after **explicit additional encoding** because the free vector space contains signed and repeated coefficients not present in the original Stage-VII finite-set carrier.

## 5. Support-retention obstruction

The DSD static paper retains records in a disjoint union of support-tagged spaces specifically so that

- channel absent,
- channel selected with zero contribution

remain distinct.

A naive global zero-padded vector representation identifies those states. Therefore one cannot replace the support-tagged carrier by an ordinary global value vector without losing a DSD distinction.

This is not a new algebraic theorem; it is a typing/representation constraint on which standard quotient construction is faithful to the DSD source semantics.

## 6. Correspondence verdict

**Primary classification: PARTIAL CORRESPONDENCE.**

### Direct correspondence

- fixed-support summation kernel;
- quotient by the fixed-support linear kernel;
- injectivity/reconstruction criterion via the kernel;
- equal aggregate as a fiber equivalence relation.

### Non-correspondence

- aggregate-equality classes of finite supports do not generally form a quotient semilattice under union.

### Additional encoding correspondence

- free vector-space or free additive lift gives an exact quotient-by-kernel theorem for support collisions.

### Representation boundary

- naive zero-padding is not faithful because it collapses absence into selected zero.

## 7. H1–H5 disposition

- H1 — fixed-support kernel criterion is standard linear algebra: **confirmed**.
- H2 — aggregate equality on finite supports is an equivalence relation: **confirmed**.
- H3 — aggregate equality is a union congruence: **falsified**.
- H4 — explicit additive lift restores exact kernel quotient: **confirmed as additional encoding**.
- H5 — naive zero-padding preserves DSD support semantics: **falsified**.

## 8. DSD consequence

No contradiction with the Formation, Axis-property, or Static Aggregation papers was found. The current DSD sources already distinguish fixed-support kernel analysis from varying-support reconstruction and already reject aggregate equality as a complete classifier.

The new analytical sharpening is the precise algebraic reason: across varying finite supports, aggregate equality is only a fiber equivalence relation and fails the congruence condition required for a quotient algebra under ordinary union.

## 9. Cross-domain significance

MATH-002 strengthens a recurring DSD Analysis pattern in a fully formal setting:

`same reduced result` does not automatically license `same source structure` or `quotient structure under the source operation`.

The important addition is that the failure is now located exactly at the congruence condition rather than stated only as generic information loss.

## 10. Final case statement

MATH-002 closes as a **boundary-confirming partial correspondence**:

**DSD fixed-support aggregation uses ordinary linear kernel and quotient theory exactly; across varying Stage-VII supports, equal aggregate values define a quotient set but not generally a quotient semilattice, unless an additional additive encoding is introduced.**