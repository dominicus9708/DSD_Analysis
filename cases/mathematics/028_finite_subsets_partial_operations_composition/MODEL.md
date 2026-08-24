# Formal Comparison Model

Status: ADJUDICATED.

## DSD side

Let `C_L` be the admitted operational-channel set determined at Stage VI. Stage VII supplies a vector space `W_L`, a component-term map

`T_L : C_L -> W_L`,

and the finite composition domain

`D_comp_L = P_fin(C_L)`.

For every finite channel family `F`,

`Comp_L(F) = sum_{c in F} T_L(c)`.

The source family is an unordered finite set without repetition.

## Standard algebra side A — finite-subset union

The carrier

`P_fin(C_L)`

with union and empty set satisfies:

- closure under union,
- associativity,
- commutativity,
- identity `emptyset`,
- idempotence `F union F = F`.

Thus it is a commutative idempotent monoid and, equivalently, a join-semilattice with bottom.

### Exact comparison identity

For arbitrary finite `F,G`:

`Comp_L(F) + Comp_L(G) = Comp_L(F union G) + Comp_L(F intersect G)`.

Hence

`Comp_L(F union G) = Comp_L(F) + Comp_L(G) - Comp_L(F intersect G)`.

The intersection term is the complete overlap correction.

### Full-homomorphism criterion

Suppose `Comp_L` preserved ordinary union for every pair:

`Comp_L(F union G) = Comp_L(F) + Comp_L(G)`.

Set `F=G={c}`. Idempotence gives

`T_L(c)=2T_L(c)`,

so `T_L(c)=0` in the vector space `W_L`. Since `c` is arbitrary, the entire term map must vanish.

Therefore:

`Comp_L : (P_fin(C_L), union, emptyset) -> (W_L,+,0)`

is a monoid homomorphism **if and only if** `T_L` is identically zero.

This makes direct union-monoid homomorphism a trivial special case, not the general algebraic type of DSD Stage VII.

## Standard algebra side B — disjoint union / finite additivity

Define the partial composition

`F sqcup G = F union G`

only when

`F intersect G = emptyset`.

Then exactly:

`Comp_L(F sqcup G) = Comp_L(F)+Comp_L(G)`.

Since `P_fin(C_L)` is closed under finite union and set difference, it is a ring of sets. `Comp_L` is therefore a finitely additive `W_L`-valued set function on this ring.

This is the strongest direct standard characterization established in MATH-001 without altering the Stage-VII source object.

## Standard algebra side C — multiplicity-preserving extension

Let `N^(C_L)` be the free commutative monoid on `C_L`, represented by finitely supported multiplicity functions `m : C_L -> N`.

Define

`T_tilde(m)=sum_c m(c) T_L(c)`.

Then

`T_tilde(m+n)=T_tilde(m)+T_tilde(n)`,

so `T_tilde` is a genuine monoid homomorphism.

Every finite set `F` embeds as its 0/1 indicator `1_F`, and

`T_tilde(1_F)=Comp_L(F)`.

However, for overlapping `F,G`,

`1_(F union G) != 1_F + 1_G`.

Thus multiplicity gives a useful exact linearization, but it is **additional encoding** and not the original Stage-VII finite-set convention.

## Comparison-strength ladder after audit

1. aggregate equality — weakest; may collapse distinct supports,
2. disjoint finite-additivity — directly satisfied by Stage VII,
3. full union-monoid homomorphism — only in the zero-term regime,
4. multiplicity-preserving monoid homomorphism — available after explicit free-commutative-monoid extension,
5. formation embedding / strict equivalence — stronger typed structural comparison and not reducible to aggregate equality.

## Primary verdict

**Partial correspondence.**

DSD Stage-VII finite composition corresponds directly to finite additivity on disjoint finite channel families, but not to a homomorphism from the full join-semilattice of finite supports into ordinary vector addition except trivially.
