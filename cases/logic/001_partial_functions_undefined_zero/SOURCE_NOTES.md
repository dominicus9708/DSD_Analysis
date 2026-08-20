# Case 001 — Source Notes

## Scope

These notes record the external partial-function literature before applying DSD terminology.

## Source 1 — Fitzgerald & Jones (2008)

John S. Fitzgerald and Cliff B. Jones, “The connection between two ways of reasoning about partial functions,” *Information Processing Letters* 107(3–4), 128–132 (2008), DOI: 10.1016/j.ipl.2008.02.005.

The publisher abstract states that undefined terms produced by partial functions and operators are common in program specifications and proof obligations. It compares two approaches:

1. classical first-order predicate calculus with a non-strict equality notion intended to insulate logical operators from undefined operands;
2. a Logic of Partial Functions (LPF) using strict/weak equality, where the law of excluded middle is not generally valid.

The paper's main comparison concerns translations between theorems in those approaches. Therefore the relevant external fact for Case 001 is not that LPF and DSD are the same, but that established formal reasoning treats failure of a partial term to denote a value as a genuine semantic/formal issue rather than automatically identifying it with an ordinary codomain value.

## Source 2 — Jones & Lovert (2010/2011)

Cliff B. Jones and Matthew J. Lovert, “Semantic Models for a Logic of Partial Functions,” Newcastle University Computing Science Technical Report CS-TR-1220 (2010); later published in *International Journal of Software and Informatics* 5(1–2), 55–76 (2011).

The Newcastle University abstract states that LPF is used for propositions containing terms that can fail to denote values. The work supplies structural-operational and denotational semantics, with relations used as an intuitive model of undefined terms.

This supports a source-side distinction between:

- a term that denotes a proper value, and
- a term that fails to denote a proper value.

It does not establish any DSD formation axiom, channel rule, or regime-global assignment principle.

## Source-side boundary for DSD comparison

The following identifications are **not** assumed:

- LPF undefined term = DSD undefined assignment;
- LPF truth-value behavior = DSD assignment-status structure;
- LPF semantics = DSD formation stages.

The comparison is restricted to one structural question: whether loss of definedness/domain information can be harmlessly replaced by an ordinary value such as zero without retaining extra status information.

## References

- Fitzgerald, J. S.; Jones, C. B. (2008). DOI: 10.1016/j.ipl.2008.02.005.
- Jones, C. B.; Lovert, M. J. (2010). Newcastle University Technical Report CS-TR-1220, “Semantic Models for a Logic of Partial Functions.”
