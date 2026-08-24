# MATH-001 Proof Record

Global case: 028

## 1. External algebraic structure

Let `C` be any set and let `P_fin(C)` be its finite subsets.

Under ordinary union:

- `F union G` is finite,
- union is associative,
- union is commutative,
- `emptyset` is an identity,
- `F union F = F`.

Hence `(P_fin(C), union, emptyset)` is a commutative idempotent monoid; equivalently, it is a join-semilattice with bottom.

## 2. DSD finite composition

For the Formation Stage-VII data, let

- `C_L` be the admitted operational-channel set,
- `W_L` be the supplied term space,
- `T_L : C_L -> W_L` be the supplied component-term map,
- `Comp_L(F) = sum_{c in F} T_L(c)` for `F in P_fin(C_L)`.

The source family is an ordinary finite set, so repeated occurrence of the same channel is not part of the core Stage-VII data type.

## 3. Exact overlap identity

For arbitrary finite `F, G subseteq C_L`, partition into three disjoint pieces:

- `F \ G`,
- `G \ F`,
- `F intersect G`.

Then

`Comp_L(F) + Comp_L(G)`

counts each channel in `F intersect G` twice, while

`Comp_L(F union G)`

counts it once. Therefore, in the additive group underlying the vector space `W_L`,

`Comp_L(F) + Comp_L(G) = Comp_L(F union G) + Comp_L(F intersect G)`.

Equivalently,

`Comp_L(F union G) = Comp_L(F) + Comp_L(G) - Comp_L(F intersect G)`.

This identity is the exact algebraic boundary between ordinary union and additive channel composition.

## 4. H1 — full union-monoid homomorphism

Hypothesis H1 claims

`Comp_L(F union G) = Comp_L(F) + Comp_L(G)`

for all finite `F, G`.

Set `F = G = {c}`. Since union is idempotent,

`F union F = F`.

If H1 held, then

`T_L(c) = Comp_L({c}) = Comp_L({c}) + Comp_L({c}) = 2 T_L(c)`.

Because `W_L` is a vector space, cancellation gives

`T_L(c) = 0`.

Since `c` was arbitrary, H1 can hold on the whole finite-subset union monoid only when `T_L` is identically zero. Conversely, if `T_L` is identically zero, H1 trivially holds.

### H1 verdict

**Falsified in every nontrivial Stage-VII term model.**

Exact condition:

`Comp_L : (P_fin(C_L), union) -> (W_L, +)`

is a monoid homomorphism if and only if `T_L(c)=0` for every admitted channel `c`.

This is not a contradiction in DSD because the Formation Axiom System never asserts that `Comp_L` is a union-monoid homomorphism.

## 5. H2 — disjoint finite additivity

Suppose `F intersect G = emptyset`. The overlap identity reduces to

`Comp_L(F union G) = Comp_L(F) + Comp_L(G)`.

More generally, for pairwise disjoint finite families `F_1, ..., F_n`,

`Comp_L(union_i F_i) = sum_i Comp_L(F_i)`.

Therefore `Comp_L` is exactly a finitely additive `W_L`-valued set function on the ring of finite subsets `P_fin(C_L)`.

Equivalently, define a partial operation

`F sqcup G := F union G`

only when `F intersect G = emptyset`.

Then `Comp_L` preserves this partial disjoint composition exactly:

`Comp_L(F sqcup G) = Comp_L(F) + Comp_L(G)`.

### H2 verdict

**Survives audit as a direct correspondence.**

The strongest standard description supported without changing the Stage-VII source object is finite additivity on disjoint finite channel families, not ordinary union-monoid homomorphism.

## 6. H3 — multiplicity-preserving extension

Let `N^(C_L)` denote the free commutative monoid on `C_L`, represented by finitely supported multiplicity functions

`m : C_L -> N`.

Define

`T_tilde(m) = sum_{c in C_L} m(c) T_L(c)`.

The sum is finite because `m` has finite support. Then

`T_tilde(m+n) = T_tilde(m) + T_tilde(n)`

and `T_tilde(0)=0`, so `T_tilde` is a genuine commutative-monoid homomorphism.

Embed a finite subset `F` as its indicator multiplicity `1_F`. Then

`T_tilde(1_F) = Comp_L(F)`.

However,

`1_{F union G}` is not generally equal to `1_F + 1_G` when `F intersect G` is nonempty.

Thus the free-commutative-monoid construction gives an exact additive linearization only by introducing multiplicity that is absent from the original Stage-VII finite-set convention.

### H3 verdict

**Correspondence after explicit additional encoding.**

It is mathematically natural but must not be attributed to the original DSD core.

## 7. H4 — aggregate equality versus structural equality

The Formation Axiom System itself permits distinct finite channel families with equal composite output. Its finite witness uses three distinct channels `c1, c2, c3` with terms

- `T(c1)=1`,
- `T(c2)=-1`,
- `T(c3)=0`,

so that

`Comp({c1,c2}) = 0 = Comp({c3})`

while

`{c1,c2} != {c3}`.

Therefore aggregate equality does not imply equality of channel support. The same Formation paper separately proves that composite-level coincidence can occur below strict descriptive equivalence.

### H4 verdict

**Survives audit as an already DSD-internal theorem and is independently natural from the algebraic viewpoint.**

## 8. Main case theorem

For every DSD Stage-VII formation model with finite composition

`Comp_L(F)=sum_{c in F}T_L(c)`:

1. `(P_fin(C_L), union, emptyset)` is a commutative idempotent monoid / join-semilattice with bottom.
2. `Comp_L` is a homomorphism from that union monoid to `(W_L,+)` if and only if `T_L` is the zero map.
3. For disjoint finite families, `Comp_L` is exactly finitely additive.
4. Passing to the free commutative monoid on `C_L` yields a genuine multiplicity-preserving homomorphic extension, but this is additional encoding beyond core Stage VII.
5. Equality of composite outputs is weaker than equality of finite channel families and weaker than strict descriptive equivalence.

## 9. DSD consequence

No DSD axiom or theorem is contradicted.

The analysis sharpens the mathematical characterization of Stage VII:

**core DSD finite composition behaves as a finitely additive set function on finite channel supports, not as a homomorphism from the join-semilattice of finite supports into ordinary vector addition, except in the trivial zero-term regime.**

This is a scope clarification and external structural characterization, not a new axiom.
