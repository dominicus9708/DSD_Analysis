# LAW-004 Reproducibility Record

## Execution date

2026-08-23 KST.

## External source verification

Verify the following operative sources before rerunning the legal comparison:

1. Criminal Procedure Act, effective 2026-07-01: Articles 294, 307, 308, 308-2, 310-2 and related provisions.
2. Civil Procedure Act operative evidence provisions: Articles 202, 288-292.
3. Supreme Court 2024Da222212, judgment 2026-04-30, official case bulletin published 2026-05-11.

Exact URLs are recorded in `SOURCE_NOTES.md`.

## DSD source verification

Use the current project manuscripts:

- Formation Axiom System — Sections 2.3, 3, 4-5, 6.5.
- Channel-Indexed Static Aggregation — Sections 2.3-2.4, 5.2, 11.

Do not replace these with memory-only summaries when revising the case.

## Deterministic state checks

The first-pass analysis succeeds only if all following distinctions can be represented simultaneously:

1. `exists != offered`.
2. `offered != investigated/usable`.
3. `usable != sufficiently probative`.
4. `sufficiently probative evidence state != automatic final finding without the governing legal standard`.
5. `inadmissible != nonexistent`.
6. `unlawfully collected != universally inadmissible across every source regime`.
7. `legal probative weight != DSD analytic weight` unless an additional bridge is supplied.

## Finite witnesses

Rerun the five constructions in `FINITE_WITNESS.md` and confirm that no witness requires collapsing a not-reached status into zero, absence, admissible, inadmissible, proved, or disproved.

## No code requirement

This case is a finite logical/legal state audit. No numerical script is required for the first-pass result. Adding code solely to turn qualitative legal categories into numbers would introduce unsupported structure.

If a future formal evidence-scoring model is added, place its code under a separate application subdirectory and record its explicit legal-analytic bridge and assumptions.

## Expected result

Expected first-pass classification:

- Formation: compatible after typed application encoding; no direct contradiction found.
- Static Aggregation: not required; numerical-weight identity rejected.
- Axis-Property: not required.
- Dynamics: not required for the static first pass.

Any later source-law amendment or binding decision that changes the relevant rules requires reopening the source lock rather than silently updating the conclusion.
