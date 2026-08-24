# Finite Witnesses

Status: ADJUDICATED.

## Witness A — smallest full-union obstruction

Take one admitted channel `c` with

`T(c)=x`,

where `x != 0` in the vector space `W_L`.

Set

`F=G={c}`.

Then

`F union G={c}`,

so

`Comp(F union G)=x`.

But

`Comp(F)+Comp(G)=x+x=2x`.

Since `x != 0`, these are unequal.

Thus one channel is already sufficient to falsify the universal union-homomorphism claim in every nonzero-term regime.

### Minimality

No smaller nonempty witness exists because a failure requires at least one admitted channel. The empty-family case satisfies the identity trivially.

## Witness B — exact disjoint additivity

Take two distinct admitted channels `c1,c2` with arbitrary terms

`T(c1)=x`, `T(c2)=y`.

Let

- `F={c1}`,
- `G={c2}`.

Then `F intersect G=emptyset`, and

`Comp(F union G)=x+y=Comp(F)+Comp(G)`.

No condition on `x` or `y` is required.

## Witness C — DSD's own non-injective composition witness

Use the Formation Axiom System construction with three distinct admitted channels

`c1,c2,c3`

and

- `T(c1)=1`,
- `T(c2)=-1`,
- `T(c3)=0`.

Take

- `F1={c1,c2}`,
- `F2={c3}`.

Then

`Comp(F1)=0=Comp(F2)`

but

`F1 != F2`.

This is the primary witness that aggregate equality does not reconstruct channel support.

## Witness D — multiplicity boundary

Take one admitted channel `c` with `T(c)=x != 0`.

In core Stage VII, the finite support `{c}` contains `c` once and

`Comp({c})=x`.

In the free commutative monoid, the multiplicity element `2[c]` is distinct from `[c]` and maps to

`T_tilde(2[c])=2x`.

There is no Stage-VII finite set corresponding to two copies of the exact same channel. Thus the multiplicity model is a genuine extension of the source data type.

## Witness summary

| Witness | Purpose | Outcome |
|---|---|---|
| A | full union homomorphism | falsified by one nonzero channel |
| B | disjoint finite additivity | exact |
| C | aggregate reconstruction | fails; DSD-internal witness |
| D | multiset/free-monoid extension | exact only after additional encoding |
