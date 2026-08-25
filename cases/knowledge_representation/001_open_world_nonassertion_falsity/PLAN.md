# K_R-001 / Global Case 039 — Open-World Non-Assertion versus Falsity

Status: **first-pass analysis completed**.

## Primary question

In an open-world knowledge-representation formalism, is the absence of an assertion equivalent to the assertion being false?

## Why this is the first case

This case is deliberately chosen so that the field does not merely repeat SQL NULL behavior from the database campaign. The target is a logical inference rule of a knowledge-representation formalism, not a storage-cell convention.

## Primary external sources

1. W3C OWL 2 Direct Semantics (Second Edition).
2. W3C OWL 2 Primer (Second Edition).
3. W3C OWL 2 Structural Specification and Functional-Style Syntax for explicit negative assertions.

## Pressure tests executed

### Test A — non-assertion versus falsity

Construct two admissible interpretations of the same underconstrained ontology: one with `P(a,b)` true and one with `P(a,b)` false. Since OWL entailment requires truth in every model, neither polarity is entailed from non-assertion alone.

### Test B — explicit negative information

Add a `NegativeObjectPropertyAssertion(P a b)`. The Direct Semantics requires `(a,b)` not to belong to the extension of `P`, so the explicit negative assertion has stronger semantic content than silence.

### Test C — class membership versus property value

Assert `C(a)` without a property axiom that constrains `P`. The class assertion does not by itself select a concrete `P(a,b)` truth value; models differing only on `P(a,b)` remain possible.

### Test D — closed-world contrast

A rule of the form `not asserted P(a,b) => false P(a,b)` can be imposed by a closed-world/completeness layer, but that is an additional semantic assumption rather than OWL 2 Direct Semantics.

## DSD comparison target

The comparison is limited to the structural pattern:

`not established / not assigned != explicitly false or defined zero`.

The Formation Axiom System distinguishes undefined assignment from defined zero and rejects zero-padding as assignment-faithful. The axis-property system likewise distinguishes undefined application from defined zero.

## Required non-identity statement

Open-world non-entailment is **not** DSD undefined assignment.

The former is a model-theoretic property of knowledge-base entailment across admissible interpretations; the latter is a status in the DSD partial-assignment/formation architecture.

## Deliverables

- `RESULT.md`
- `SOURCE_NOTES.md`
- `REPRODUCIBILITY.md`
- `repro/check_open_world_models.py`
- `repro/expected_output.txt`
- Notion case page updated under `지식표현·온톨로지·분류`
- roadmap updated to `K_R-001 / Global Case 039` completed