# Case 001 — Partial Functions: Undefinedness vs Zero Totalization

## Status
Preparation.

## Why this is the first case
The DSD Analysis roadmap places mathematical/philosophical logic first. The first lightweight comparison recorded there is partial functions/partial terms, with the follow-up test explicitly asking what distinction is lost when undefined inputs are replaced by a default value or zero.

## Research question
Given a partial function or partial assignment, what structural information is lost if it is converted into a total function by assigning a default value—especially zero—to inputs outside the original domain?

The analysis will compare three representations:

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

## DSD-side hypotheses to test
The current Formation Axiom System explicitly separates:

- undefined assignment,
- defined zero,
- defined nonzero values,
- channel absence,
- admitted channels with zero-valued assignments/terms.

The expected DSD-side result is not that totalization is forbidden, but that **naive totalization is not structure-faithful unless domain/status information is retained separately**.

## External comparison target
Primary literature for the initial comparison:

- John S. Fitzgerald and Cliff B. Jones, “The connection between two ways of reasoning about partial functions,” *Information Processing Letters* 107(3–4), 128–132 (2008), DOI: 10.1016/j.ipl.2008.02.005.

The paper treats undefined terms arising from partial functions as a genuine formal issue and compares reasoning in classical first-order predicate calculus with a Logic of Partial Functions. The DSD analysis must preserve the distinction between that logical setting and DSD's formation-layer partial assignment.

## Mapping questions
1. Is the external undefined term a value, lack of denotation, or domain failure in the chosen formalism?
2. Which DSD distinction is genuinely analogous, and which is only superficially similar?
3. Does replacing undefinedness by zero create a many-to-one representation?
4. Can the original structure be reconstructed from the zero-totalized output alone?
5. Does adding a status/domain mask restore reconstruction?
6. Does downstream channel formation make the loss more consequential than at the assignment layer alone?

## Planned artifacts
- `SOURCE_NOTES.md` — source claims and terminology, without DSD reinterpretation.
- `FINITE_WITNESS.md` — explicit finite construction and comparison table.
- `RESULT.md` — final mapping judgment and boundary conditions.
- optional `verify_case_001.py` only if a script adds reproducibility beyond the hand-checkable witness.

## Success criterion
A successful analysis must produce a source-faithful distinction table and an explicit finite witness showing whether naive totalization preserves or destroys the relevant information. It must also state where the LPF comparison stops and must not claim that LPF proves the DSD axioms.

## Failure criterion
The case is not counted as a supporting cross-domain node if the apparent correspondence depends only on shared terminology, or if the relevant distinction is already fully preserved by an external representation with no meaningful DSD-side structural comparison.
