# Case 003 — Institution Theory and Strict Formation Equivalence

## Status
Initial mathematical analysis in progress.

## Purpose
Test whether the DSD Formation Axiom System's strict base-fixed formation isomorphism behaves correctly under three increasingly weak comparison situations:

1. pure renaming with full structural preservation;
2. identical downstream composite with different formation structure;
3. satisfaction-preserving translation/reduct in Institution Theory that does not amount to structural isomorphism.

## DSD target
Primary target: Section 6 of the Formation Axiom System, especially Definition 6.10, Corollary 6.12, Remark 6.13, Theorem 6.14, and Proposition 6.22.

The case does not test the primitive formation axioms I–III or V directly. It tests the comparison/equivalence layer built over full formation models.

## External target
Joseph A. Goguen and Rod M. Burstall, *Institutions: Abstract Model Theory for Specification and Programming*, J. ACM 39(1), 95–146 (1992), DOI: 10.1145/147508.147524.

The relevant institutional principle is invariance of satisfaction under change of notation/signature translation. For a signature morphism `phi: Sigma -> Sigma'`, a `Sigma'`-model `M'`, and a `Sigma`-sentence `e`, the standard satisfaction condition has the form

`M' |=_{Sigma'} Sen(phi)(e)  iff  Mod(phi)(M') |=_{Sigma} e`.

This is not an isomorphism condition on the models.

## Three finite tests

### Test A — Renaming invariance
Construct two one-point DSD formation models with the same fixed base and identical structure up to bijective renaming of material, expression, configuration, quantity-kind, and role labels. Verify conditions (E1)–(E9).

Expected pass condition: strict equivalence must hold.

### Test B — Same composite, different formation
Compare a one-channel model with term `0` against a two-channel model with terms `1` and `-1` so both selected composites equal `0`.

Expected pass condition: strict equivalence must fail despite composite equality.

### Test C — Satisfaction preservation without isomorphism
Use a signature inclusion from `Sigma={P}` to `Sigma'={P,Q}` and a `Sigma'`-model whose reduct forgets `Q`. The sentence `exists x P(x)` remains satisfied under the satisfaction condition, even though the richer and poorer signatures/models are not structurally isomorphic.

Expected interpretation: DSD strict equivalence should not be required to identify this situation. Institution Theory and DSD are comparing different objects with different comparison goals.

## Falsification criteria
A defect in the tested DSD equivalence layer would be indicated if:

- a pure structure-preserving renaming fails strict equivalence for name-only reasons; or
- different formation/channel structures become strictly equivalent merely because their composites coincide; or
- the paper claims strict equivalence to cover arbitrary satisfaction-preserving translations across changing logical signatures without supplying the required signature/sentence/model translation machinery.

## Boundary criterion
If satisfaction-preserving translations are meaningful but fall outside strict formation isomorphism, record this as a scope boundary or possible future weaker translation layer, not as a contradiction.
