# Source Notes

Status: COMPLETED FOR MATH-001.

## DSD primary sources

### Formation Axiom System

The core composition operator uses finite sets of admitted channels. The paper explicitly states that each composable family is a finite set and that Stage VII contains the supplied term space `W_L`, component-term map `T_L`, finite composition domain, and composite operator.

The relevant Stage-VII rule is:

`D_comp_L = P_fin(C_L)`

and

`Comp_L(F) = sum_{c in F} T_L(c)`.

The paper also proves:

- channel absence is not zero contribution,
- non-injective composition is permitted,
- distinct finite channel families can have equal composite output,
- composite-level coincidence does not imply strict equivalence,
- forward maps, embeddings, and strict equivalence preserve different amounts of structure.

Primary source file in the project: `DSD_Formation_Axiom_System_EN.pdf`.

### Channel-Indexed Static Aggregation

The static aggregation paper restates the core finite domain exactly as `P_fin(C_L)` and realizes

`Comp^R_L(F) = sum_{c in F} T^R_L(c)`.

It treats countable composition only as a separate analytic extension and explicitly preserves support-tagged information because aggregate equality does not reconstruct channel support.

Primary source file in the project: `DSD_Channel_Indexed_Static_Aggregation_EN.pdf`.

### Axis-property system

Not required for the proof of the principal MATH-001 theorem. It remains relevant only to the wider roadmap distinction between an underlying carrier and additional structure, and to later invariant/classification cases.

## External mathematics sources

### Encyclopedia of Mathematics — Semi-lattice

A semilattice is a commutative idempotent semigroup. The entry also states that the free join-semilattice on a set `X` is the set of all finite subsets of `X` ordered by inclusion.

https://encyclopediaofmath.org/wiki/Semi-lattice

### Encyclopedia of Mathematics — Monoid

A monoid is a semigroup with identity. For a commutative monoid the operation is often written additively with identity zero.

https://encyclopediaofmath.org/wiki/Monoid

### Encyclopedia of Mathematics — Additive set function

A finitely additive set function satisfies

`mu(union_i E_i) = sum_i mu(E_i)`

for finite pairwise disjoint families in its domain.

https://encyclopediaofmath.org/wiki/Additive_set_function

### Encyclopedia of Mathematics — Ring of sets

A ring of sets contains the empty set and is closed under finite union and set difference. Since finite unions and differences of finite subsets remain finite, `P_fin(C_L)` is a ring of sets.

https://encyclopediaofmath.org/wiki/Ring_of_sets

### nLab — Free commutative monoid

The free commutative monoid on a set `S` is represented by finitely supported functions `S -> N`, equivalently formal finite natural-number combinations / finite multisets. This source retains multiplicity and therefore differs from ordinary finite subsets.

https://ncatlab.org/nlab/show/free+commutative+monoid

## Source-derived comparison constraints

1. The DSD core source object is an ordinary finite set, not a multiset.
2. Standard union on finite subsets is idempotent.
3. Ordinary vector addition is cancellative and generally non-idempotent.
4. Standard finite additivity requires disjointness, which is exactly the condition that eliminates overlap double counting.
5. A multiplicity-preserving free-commutative-monoid model is a mathematically valid extension but is not identical to core Stage VII.

## Citation discipline result

All final MATH-001 verdicts can be reconstructed from the cited standard definitions plus the exact DSD finite-composition rule. No empirical or physical claim is used.
