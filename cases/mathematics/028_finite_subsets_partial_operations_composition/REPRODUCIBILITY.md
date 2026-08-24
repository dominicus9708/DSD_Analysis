# Reproducibility Protocol

Status: COMPLETED FOR THE FINITE HAND-CHECKABLE CORE.

## Goal

Make every MATH-001 verdict reconstructible from explicit finite objects and preservation equations.

## Manual reconstruction A — universal union-homomorphism failure

Input:

- carrier `C={c}`,
- vector term space `W=R`,
- `T(c)=1`,
- `F=G={c}`.

Compute:

- `F union G={c}`,
- `Comp(F union G)=1`,
- `Comp(F)+Comp(G)=1+1=2`.

Conclusion:

`Comp(F union G) != Comp(F)+Comp(G)`.

This is the smallest nontrivial witness.

## Manual reconstruction B — disjoint finite additivity

Input:

- carrier `C={c1,c2}`,
- arbitrary `T(c1)=x`, `T(c2)=y`,
- `F={c1}`, `G={c2}`.

Compute:

- `F intersect G=emptyset`,
- `Comp(F union G)=x+y`,
- `Comp(F)+Comp(G)=x+y`.

Conclusion:

disjoint finite additivity holds identically.

## Manual reconstruction C — overlap identity

For any finite `F,G`, split them into the pairwise disjoint families

- `F\G`,
- `G\F`,
- `F intersect G`.

Direct finite-sum expansion yields

`Comp(F)+Comp(G)=Comp(F union G)+Comp(F intersect G)`.

No numerical enumeration is required.

## Manual reconstruction D — non-injective DSD witness

Input from the Formation paper:

- distinct channels `c1,c2,c3`,
- `T(c1)=1`, `T(c2)=-1`, `T(c3)=0`,
- `F1={c1,c2}`, `F2={c3}`.

Compute:

- `Comp(F1)=0`,
- `Comp(F2)=0`,
- `F1 != F2`.

Conclusion:

aggregate equality does not reconstruct source support.

## Manual reconstruction E — multiplicity extension

Use the free commutative monoid on `C`, represented by finitely supported functions `m:C->N`.

Define

`T_tilde(m)=sum_c m(c)T(c)`.

Then expand directly:

`T_tilde(m+n)=sum_c (m(c)+n(c))T(c)=T_tilde(m)+T_tilde(n)`.

For a finite set `F`, its indicator `1_F` satisfies

`T_tilde(1_F)=Comp(F)`.

For overlapping supports, `1_(F union G)` differs from `1_F+1_G`, marking the additional-encoding boundary.

## Code decision

No Python program is needed for MATH-001. The decisive counterexample has one channel, and every positive identity follows by direct finite-sum decomposition. Adding code would reduce transparency rather than improve reproducibility.

## Completion criterion

Satisfied. Another reader can reconstruct every equality, inequality, and correspondence verdict from the explicit finite data without hidden assumptions about repetition, ordering, undefinedness, or zero padding.
