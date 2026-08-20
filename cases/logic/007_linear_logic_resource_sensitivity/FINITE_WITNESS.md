# Case 007 — Finite Witnesses

## Witness A — distinct-tag multiplicity is preserved
Take two distinct admitted channels

`c1 != c2`

with term space `W = R` and

`T(c1)=T(c2)=1`.

Then

`Comp({c1}) = 1`,

while

`Comp({c1,c2}) = 2`.

Therefore DSD finite composition does not collapse two distinct channel tags merely because their realized term is equal.

This is compatible with Formation Proposition 5.11 and Axis-Property Proposition 2.11: multiplicity of distinct operational tags is retained even when roles, lines, or term values partially coincide.

## Witness B — same-tag occurrence multiplicity is not representable by `Pfin`
Take one admitted channel `c` with

`T(c)=1`.

Consider an external finite-multiset semantics with multiplicity function `m:C -> N` of finite support. Let

- `m1(c)=1`,
- `m2(c)=2`.

Their multiset sums would be

`MComp(m1)=1`,

`MComp(m2)=2`.

But both have the same underlying support set

`supp(m1)=supp(m2)={c}`.

Any Formation core composite factors only through the set support `F in Pfin(C_L)`, so it receives the same input `{c}` in both cases.

Hence no function

`Comp:Pfin(C_L)->R`

can simultaneously reproduce both occurrence-sensitive values while keeping the same channel identity and term map.

### Result
The current core intentionally cannot distinguish

`one occurrence of c`

from

`two occurrences of the identical operational tag c`

inside one Stage-VII family.

This is not an inconsistency because Closure Clause VII explicitly declares the input type to be an unordered set without repetition.

## Witness C — deletion is not semantically free
With the same `c` and `T(c)=1`,

`Comp({c})=1 != 0=Comp(emptyset)`.

Thus choosing a smaller finite support can change the composite. DSD does not contain a general semantic rule saying that an admitted channel may be discarded without consequence.

There can be special cases where deletion leaves the aggregate unchanged—for example `T(c)=0`, or cancellation among several terms—but the full descriptor still retains support identity, so aggregate equality does not identify the structures.

## Witness D — set-idempotence is a data-type effect, not contraction
Because families are sets,

`{c} union {c} = {c}`.

Therefore writing the same set element twice does not create a second channel occurrence. This is ordinary set extensionality, not a Linear-Logic contraction theorem and not a proof rule inside DSD.

If an application needs two distinguishable uses, it must add distinguishing data or move to an explicitly multiplicity-sensitive downstream structure.

## Witness E — repeated typed input is a separate axis-property issue
The axis-property system admits ordered tuples of tagged-axis inputs for binary/higher-order profiles and block declarations. A typed input such as `(t,t)` can therefore be meaningful as a repeated argument position when the profile permits it.

This does not create two Formation channels. It only shows that repeated argument occurrence in an extension-level property record is a distinct concept from Stage-VII repeated channel occurrence.

## Candidate extensions if occurrence multiplicity is later required
Three non-equivalent choices exist:

1. refine operational identity with an explicit occurrence/event coordinate;
2. replace `Pfin(C_L)` by a finite-multiset domain in a separate extension;
3. encode only a numerical count/weight downstream, accepting loss of occurrence provenance.

None is forced by the current Formation core.
