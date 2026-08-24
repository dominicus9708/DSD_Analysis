# Result

Status: COMPLETED — FIRST-PASS MATHEMATICS/ALGEBRA CASE.

Global case: 028
Domain case: MATH-001

## 1. Standard mathematical finding

The finite subsets of a set `C` form a commutative idempotent monoid under union, equivalently a join-semilattice with bottom. The idempotence law is

`F union F = F`.

A finitely additive set function, by contrast, is required to preserve unions only for pairwise disjoint domain sets.

The free commutative monoid on `C` retains arbitrary finite multiplicity and therefore differs from the ordinary finite-subset carrier.

## 2. DSD finding

Formation Stage VII uses

`D_comp_L = P_fin(C_L)`

and

`Comp_L(F)=sum_{c in F}T_L(c)`.

The core source object is an ordinary finite set of admitted operational channels without repetition of the exact same channel.

For arbitrary finite `F,G`,

`Comp_L(F)+Comp_L(G)=Comp_L(F union G)+Comp_L(F intersect G)`.

Hence direct preservation of ordinary union would require the intersection contribution to vanish universally.

## 3. Correspondence verdict

**Primary classification: PARTIAL CORRESPONDENCE.**

Directly preserved structure:

- finite support,
- empty support maps to additive zero,
- finite additivity on disjoint supports,
- exact finite decomposition into channel terms.

Not directly preserved:

- the full idempotent union operation as ordinary vector addition.

Additional encoding:

- replacing finite sets by the free commutative monoid / finite multisets produces a genuine additive monoid homomorphism but adds multiplicity not present in core Stage VII.

## 4. Counterexample boundary

The smallest nontrivial failure witness uses one admitted channel `c` with `T(c)!=0` and

`F=G={c}`.

Then

`Comp(F union G)=T(c)`

while

`Comp(F)+Comp(G)=2T(c)`.

Therefore a full union-monoid homomorphism exists only when `T(c)=0` for every admitted channel.

## 5. DSD consequence

### Support for an existing DSD distinction

The result supports the existing separation between:

- channel support and aggregate output,
- finite source structure and downstream numerical combination,
- aggregate equality and strict structural equivalence.

### Newly sharpened restriction

The strongest direct standard-algebra description of core Stage VII is:

> `Comp_L` is a finitely additive `W_L`-valued set function on the ring of finite admitted-channel supports.

It is **not** generally a homomorphism from the join-semilattice `(P_fin(C_L), union)` to the additive vector space.

### Genuine contradiction with DSD

None found.

### Material contribution

The case removes an over-strong possible interpretation and gives an exact algebraic boundary. It also identifies a clean optional multiplicity extension without retroactively changing the DSD core.

## 6. H1–H4 disposition

- H1 — full union-monoid homomorphism: **falsified except trivial zero map**.
- H2 — disjoint finite additivity: **confirmed exactly**.
- H3 — free-commutative-monoid / multiset linearization: **confirmed as additional encoding**.
- H4 — equal aggregate is weaker than source equality / strict equivalence: **confirmed; already supported by DSD internal witnesses**.

## 7. Cross-domain synthesis note

This first mathematics/algebra case repeats a structural pattern already seen elsewhere in DSD Analysis: a downstream result does not license reverse reconstruction of the full source structure. In this domain the statement is not analogical but algebraically explicit, because the aggregation map is provably non-injective and the union/addition operations have different algebraic laws.

Cross-domain recurrence remains supporting structure, not proof by analogy.

## 8. Final case statement

MATH-001 closes positively as a **boundary-confirming partial correspondence**:

**DSD Stage-VII finite composition is naturally characterized as finite additivity over disjoint finite channel supports; treating it as an ordinary union-monoid homomorphism is incorrect except in the zero-term regime.**
