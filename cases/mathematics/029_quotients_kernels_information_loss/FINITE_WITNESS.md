# Finite Witnesses

## Witness A — aggregate-equality is not a union congruence

Take two distinct admitted channels `a,b` with

`T(a)=1`, `T(b)=1` in `W_L=R`.

Let

- `F={a}`,
- `G={b}`.

Then

`Comp(F)=1=Comp(G)`,

so `F ~_Comp G`.

Now choose `H={a}`. Then

`F union H = {a}`,

while

`G union H = {a,b}`.

Therefore

`Comp(F union H)=1`,

but

`Comp(G union H)=2`.

Hence

`F union H not~_Comp G union H`.

So `~_Comp` is not a congruence for ordinary union in general. The quotient set by aggregate equality therefore does not inherit a well-defined union operation from `P_fin(C_L)`.

## Witness B — fixed-support kernel

Fix `F={a,b}` and `W_L=R`. Let

`x=(1,-1)`, `y=(0,0)` in `R^F`.

Then

`S_F(x)=0=S_F(y)`

and

`x-y=(1,-1) in ker S_F`.

This is the minimal standard linear-kernel collision already represented by the DSD static aggregation theorem.

## Witness C — exact linear lift of a support collision

With the same channels and terms `T(a)=T(b)=1`, let `e_a,e_b` be the basis vectors of the free vector space `R^(C_L)`.

Then

`L_T(e_a-e_b)=1-1=0`.

Thus `e_a-e_b in ker L_T`, exactly encoding the collision

`Comp({a})=Comp({b})`.

The lift makes kernel language exact, but `e_a-e_b` is not itself a finite channel set.

## Witness D — zero-padding loses DSD support semantics

Compare the support-tagged records

- `({a}, (0))`,
- `(emptyset, ())`.

DSD distinguishes them: the first contains an admitted selected channel with zero contribution; the second contains no channel.

A naive global value vector with absent entries padded by zero sends both to the same all-zero vector. Hence zero-padding is not a faithful encoding of the DSD support-tagged record carrier.