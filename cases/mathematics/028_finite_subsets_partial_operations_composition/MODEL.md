# Formal Comparison Model

Status: scaffold; equations below define the objects to test, not a final verdict.

## DSD side

Let `C_L` be the admitted operational-channel set and let

`D_comp = P_fin(C_L)`.

For supplied term data `T_L : C_L -> W_L`, finite composition is

`Comp_L(F) = sum_{c in F} T_L(c)`.

The source family is an unordered finite set without repetition.

## Standard algebra side candidates

### Candidate A — finite-subset union structure

Source object:

`(P_fin(C_L), union, emptyset)`.

Properties to verify independently:

- closure,
- associativity,
- commutativity,
- identity,
- idempotence.

Candidate preservation equation:

`Comp_L(F union G) ?= Comp_L(F) + Comp_L(G)`.

The overlap case `F intersect G != emptyset` is an explicit attack case.

### Candidate B — disjoint finite-family composition

Restrict the binary operation to pairs with

`F intersect G = emptyset`.

Test whether the same preservation equation holds on this partial domain.

### Candidate C — explicit multiplicity encoding

If direct finite-set comparison is insufficient, test a multiset or free-commutative-monoid source in which multiplicity is retained explicitly.

This is not a direct correspondence to Formation Stage VII and must be marked `additional encoding`.

## Comparison-strength ladder

Record separately:

1. equality of one aggregate value,
2. preservation of one operation,
3. injective structure-preserving map,
4. full structural equivalence / isomorphism.

Do not infer a higher level from a lower one.
