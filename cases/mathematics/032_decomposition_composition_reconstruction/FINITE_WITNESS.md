# Finite Witnesses

## Witness A — nonunique arbitrary fixed-support decomposition

Let `W=R`, `F={a,b}`.

The sum map is

`S_F(x,y)=x+y`.

Then

`1 = 1+0 = 0+1`.

Thus the same aggregate has two different component records. Equivalently `(1,-1)` is a nonzero kernel vector.

## Witness B — direct-sum recovery

Let `W=R^2`,

`U_a=span(e_1)`, `U_b=span(e_2)`.

Every `(x,y)` has the unique decomposition

`(x,y)=(x,0)+(0,y)`.

The canonical sum map `U_a x U_b -> W` is injective.

## Witness C — Stage-VII support recovery without linear independence

Let two channel terms in `R` be

`T(a)=1`, `T(b)=2`.

Subset sums are

- `emptyset -> 0`,
- `{a} -> 1`,
- `{b} -> 2`,
- `{a,b} -> 3`.

Hence support is uniquely recoverable although `{1,2}` is linearly dependent over `R`.

This shows direct-sum/linear-independence assumptions are stronger than necessary for fixed-term finite-support recovery.

## Witness D — support collision by signed relation

Let

`T(a)=1`, `T(b)=2`, `T(c)=3`.

Then

`T(a)+T(b)-T(c)=0`,

so

`Comp({a,b})=3=Comp({c})`.

The nontrivial signed `{-1,0,1}` relation exactly produces a support collision.

## Witness E — selected zero versus absence

Let `T(z)=0`.

Then

`Comp(emptyset)=0=Comp({z})`.

The aggregate cannot determine whether `z` was absent or selected with zero contribution. Support tagging preserves this distinction.
