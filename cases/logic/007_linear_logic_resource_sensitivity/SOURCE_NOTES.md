# Case 007 — Source Notes

## External source: Linear Logic
Jean-Yves Girard introduced Linear Logic in 1987. The original paper presents the new logic and its exponential modality `!` (“of course”). A central later primary-source formulation by Lincoln, Mitchell, Scedrov, and Shankar (1992) describes Linear Logic as giving an intrinsic accounting of resources by removing the unrestricted structural rules of contraction and weakening and using a modal storage operator to recover controlled reuse.

For this case, the relevant external fact is not that DSD should be a Linear Logic. It is only that a formalism can make repeated occurrence and discard/reuse structurally significant instead of treating them as harmless background operations.

Primary references:
- Jean-Yves Girard, “Linear Logic,” *Theoretical Computer Science* 50 (1987), 1–101, DOI 10.1016/0304-3975(87)90045-4.
- Patrick Lincoln, John Mitchell, Andre Scedrov, Natarajan Shankar, “Decision Problems for Propositional Linear Logic,” *Annals of Pure and Applied Logic* 56 (1992), 239–311, DOI 10.1016/0168-0072(92)90075-B.

## DSD Formation source
Closure Clause VI defines each admitted operational channel as a set-theoretic tuple

`c = (p,a,lambda,v,rho)`.

The assigned value is part of channel identity. Proposition 5.11 explicitly shows that distinct roles yield distinct channels even when the remaining coordinates agree.

Closure Clause VII fixes

`Dcomp_L = Pfin(C_L)`

and

`Comp_L(F) = sum_{c in F} T_L(c)`.

The paper explicitly states that a core channel family is an unordered set without repetition.

Therefore the current Formation core has two different notions that must not be conflated:

1. **distinct-tag multiplicity**: several distinct elements of `C_L`;
2. **same-tag occurrence multiplicity**: one element `c` used twice or more in one composite.

The first is representable; the second is not part of `Pfin(C_L)`.

## DSD Axis-Property source
The axis-property layer preserves operational channel tags. Proposition 2.11 states that distinct tagged channels may realize the same line and that channel multiplicity need not equal realized-axis rank.

This confirms that the word “multiplicity” in the current axis layer refers to cardinality of distinct inherited tags, not repeated occurrences of one identical tag.

The property layer can still use ordered finite tagged-axis tuples as typed inputs, so repeated argument positions belong to a different layer from Stage-VII channel composition.

## Static aggregation source
The static paper inherits `F in Pfin(C_L)` for Formation-compatible finite channel aggregation. Its property aggregate also uses a finite set of selected records. Section 8.4 explicitly says that reuse of the same underlying property record in semantically distinct output coordinates must be declared and is application-level bookkeeping.

This is important evidence that the downstream paper does not silently assume unrestricted duplication.

## Dynamic source
The dynamics paper fixes inherited channel identities and selected support during a regular epoch. Changes of support/channel set are transitions, not hidden smooth evolution. This again treats support identity explicitly rather than as a proof-context structural rule.
