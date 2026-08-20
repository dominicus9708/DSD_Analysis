# Case 001 — Partial Functions: Undefinedness vs Zero Totalization

## Status
Completed initial mathematical analysis on 2026-08-20. See `SOURCE_NOTES.md`, `FINITE_WITNESS.md`, and `RESULT.md`.

## Why this is the first case
The DSD Analysis roadmap places mathematical/philosophical logic first. The first lightweight comparison recorded there is partial functions/partial terms, with the follow-up test explicitly asking what distinction is lost when undefined inputs are replaced by a default value or zero.

## Research question
Given a partial function or partial assignment, what structural information is lost if it is converted into a total function by assigning a default value—especially zero—to inputs outside the original domain?

The analysis compares three representations:

1. **Partial representation** — the domain is explicit and undefined inputs receive no value.
2. **Naive zero-totalized representation** — undefined inputs are assigned the same zero used by legitimate defined-zero inputs.
3. **Status-preserving totalized representation** — a total numerical representation is paired with an explicit domain/status mask.

## Minimal finite witness
Let

- input carrier `A = {u, z, n}`,
- value carrier `V = {0, 1}`,
- partial domain `Q = {z, n}`,
- `q(z) = 0`,
- `q(n) = 1`,
- `q(u)` undefined.

The naive zero-totalization is

- `q_bar(u) = 0`,
- `q_bar(z) = 0`,
- `q_bar(n) = 1`.

Therefore `u` and `z` collide numerically even though their domain statuses differ.

## DSD-side hypotheses tested
The current Formation Axiom System explicitly separates:

- undefined assignment,
- defined zero,
- defined nonzero values,
- channel absence,
- admitted channels with zero-valued assignments/terms.

The tested DSD-side result is not that totalization is forbidden, but that **naive totalization is not structure-faithful unless domain/status information is retained separately**.

## External comparison target
Primary literature for the initial comparison:

- John S. Fitzgerald and Cliff B. Jones, “The connection between two ways of reasoning about partial functions,” *Information Processing Letters* 107(3–4), 128–132 (2008), DOI: 10.1016/j.ipl.2008.02.005.
- Cliff B. Jones and Matthew J. Lovert, “Semantic Models for a Logic of Partial Functions,” Newcastle University CS-TR-1220 (2010), later published in *International Journal of Software and Informatics* 5(1–2), 55–76 (2011).

The DSD analysis preserves the distinction between those logical settings and DSD's formation-layer partial assignment.

## Questions answered
1. External partial-function logic treats failure to denote a proper value as a genuine formal/semantic issue.
2. Naive zero-totalization is globally non-injective on partial assignments when domain information is discarded.
3. The exact lost information is which zero-valued points were genuinely in the original domain.
4. A status/domain mask or disjoint bottom value restores injectivity.
5. In DSD, replacing the partial assignment by the naive totalized surrogate can create additional Stage-VI channels.
6. This supports the tested undefined-vs-zero distinction but does not prove Primitive Axiom V's regime-global assignment requirement or the entire Formation Axiom System.

## Artifacts
- `SOURCE_NOTES.md` — source claims and terminology, without DSD reinterpretation.
- `FINITE_WITNESS.md` — explicit finite construction, theorems, and channel-level lift.
- `RESULT.md` — final mapping judgment and Formation-Axiom-System verdict.

No Python script was added because the witness and proofs are finite and completely hand-checkable; a script would not add independent mathematical evidence at this stage.

## Case result

**Not falsified.** The tested Formation-Axiom-System claim is mathematically correct and admits a stronger non-injectivity/reconstruction formulation. No correction to the Formation paper is required from Case 001, although Proposition 5.4 could be strengthened in a later revision.
