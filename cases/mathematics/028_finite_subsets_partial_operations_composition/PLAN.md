# MATH-001 Analysis Plan

Global case: 028

Status: COMPLETED — first-pass adjudication closed.

## Research question

Determine the exact algebraic relation between finite DSD channel-family composition and standard structures on finite subsets, partial operations, additive codomains, and structure-preserving maps.

## Primary questions and disposition

1. What algebraic structure is naturally carried by `P_fin(C_L)` under union?
   - **Answered:** commutative idempotent monoid / join-semilattice with bottom.
2. Under what conditions does `Comp(F) = sum_{c in F} T(c)` preserve a union-like composition?
   - **Answered:** exactly on disjoint finite families in the general case.
3. Does overlap obstruct a homomorphism law through double counting?
   - **Answered:** yes; exact intersection correction obtained.
4. Which alternative source structure makes `Comp` a genuine homomorphism while retaining multiplicity?
   - **Answered:** free commutative monoid / finite multiset encoding, marked as additional encoding.
5. How should `F1 != F2` with `Comp(F1) = Comp(F2)` be classified?
   - **Answered:** aggregate-level information loss; source equality and strict equivalence do not follow.
6. How do Formation embeddings and strict equivalence compare with output equality?
   - **Answered for current scope:** they are structurally stronger; no collapse to aggregate equality is valid.

## H1–H4 final status

- H1: `Comp` is a monoid homomorphism from `(P_fin(C_L), union)` to `(W_L,+)`.
  - **Falsified except when `T_L` is identically zero.**
- H2: H1 fails in general but becomes valid on disjoint finite families.
  - **Confirmed exactly.**
- H3: a multiset/free-commutative-monoid encoding yields a stronger algebraic correspondence.
  - **Confirmed as additional encoding.**
- H4: equal aggregate output is strictly weaker than structural equality and strict descriptive equivalence.
  - **Confirmed; also already supported by DSD internal witnesses.**

## Required outputs

- standard-mathematics statement — complete,
- DSD statement — complete,
- explicit correspondence map — complete,
- preservation conditions — complete,
- smallest counterexample — complete,
- DSD-internal contradiction audit — complete,
- correspondence verdict — complete,
- reproducibility notes — complete.

## Final stop-rule assessment

No analogy was upgraded beyond its preserved algebraic laws. The final primary verdict is **partial correspondence**, with a separate **additional encoding** result for the free commutative monoid.
