# KR-001 / Global Case 039 — Open-World Non-Assertion versus Falsity

Status: **prepared, analysis not yet executed**.

## Primary question

In an open-world knowledge-representation formalism, is the absence of an assertion equivalent to the assertion being false?

## Why this is the first case

This case is deliberately chosen so that the new field does not merely repeat SQL NULL behavior from the database campaign. The target is a logical inference rule of a knowledge-representation formalism, not a storage-cell convention.

## External source targets

Prefer primary/authoritative material:

1. W3C OWL 2 Direct Semantics.
2. W3C OWL 2 Primer or Structural Specification when a worked example is needed.
3. RDF 1.1 Semantics only when a distinction specifically depends on RDF entailment rather than OWL semantics.

Do not treat tutorials/blogs as primary evidence when the W3C specification already settles the point.

## Pressure tests

### Test A — non-assertion versus falsity

Construct a knowledge base in which `P(a)` is not asserted and test whether `not P(a)` follows.

### Test B — explicit negative information

Compare non-assertion with an explicit negative property assertion or another formal negative statement where the chosen formalism supports one.

### Test C — class membership versus property value

If `a` is asserted to be a member of class `C`, test whether this alone yields a concrete value for property `P` without an axiom that entails one.

### Test D — closed-world countermodel

Contrast the open-world result with a deliberately closed-world rule or validation layer. Record the difference as a semantic boundary, not as a contradiction.

## DSD comparison targets

Formation/axis-property comparison should ask only whether the following structural pattern recurs:

`not established / not assigned != explicitly false or defined zero`.

Potential DSD comparison layers:

- undefined partial assignment versus defined zero/value;
- property kind declaration versus application-domain membership;
- candidate/configuration presence versus actually formed operational object.

## Required non-identity statement

Open-world non-entailment is **not** DSD undefined assignment.

The former is a model-theoretic property of knowledge-base entailment across admissible interpretations; the latter is a status in the DSD partial-assignment/formation architecture.

## Falsification direction

The DSD-supportive reading should fail or weaken if the selected formalism licenses the inference:

`not asserted P(a) => false P(a)`

without any additional closed-world/completeness assumption.

If such an inference only appears after adding a closed-world rule, validation constraint, completeness statement, or local closure axiom, record that extra assumption explicitly.

## Expected deliverables when executed

- `RESULT.md`
- `SOURCE_NOTES.md`
- `REPRODUCIBILITY.md` if a finite reasoner/witness is useful
- optional reproducibility script or ontology fixture
- Notion child page under `지식표현·온톨로지·분류`
- roadmap status update to KR-001 / Global Case 039