# Reproducibility Protocol

## Goal

Make every MATH-001 verdict reconstructible from explicit finite objects and preservation equations.

## Procedure

1. Fix a finite admitted-channel carrier `C`.
2. Fix a term codomain `W` with the algebraic structure actually required by the test.
3. Give the term map `T : C -> W` explicitly.
4. List every finite family `F`, `G`, `F1`, `F2` used by the argument.
5. Evaluate `Comp` directly as a finite sum.
6. Evaluate the candidate source operation independently.
7. Compare the two sides of the proposed preservation equation.
8. Record whether the case uses ordinary finite sets, disjoint pairs, multisets, or another encoding.
9. Repeat with the smallest counterexample found by the contradiction audit.
10. Separate DSD-internal conclusions from standard-algebra conclusions.

## Optional code

No Python program is required merely to verify one- or two-channel finite witnesses. If enumeration grows large enough that code materially improves auditability, add a deterministic script only after the mathematical witness is specified by hand.

Any future code must report its exact input carrier, term map, generated family set, and output table; computation must not substitute for the proof of the preservation condition.

## Completion criterion

The case is reproducible when another reader can reconstruct every claimed equality or inequality from the stated finite data without relying on an unstated convention about repetition, ordering, undefinedness, or zero padding.
