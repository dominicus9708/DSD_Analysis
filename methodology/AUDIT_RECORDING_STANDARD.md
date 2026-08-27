# DSD Audit Recording Standard

## 1. Purpose

This document defines how an audit should be recorded so that the result can be reviewed later without relying on memory or conversational context.

The recording standard is intentionally stricter than an informal analysis note.
It should preserve both the path that led to the verdict and the paths that were rejected.

## 2. Record identity

Every audit should have a stable identifier.

Recommended format:

```text
DSD-AUDIT-YYYYMMDD-DOMAIN-NNN
```

Example:

```text
DSD-AUDIT-20260827-MATH-001
```

Record at minimum:

- Audit ID
- Title
- Domain
- Date
- Auditor / execution agent
- Related source, document, repository, case, or dataset
- Version or revision when applicable

## 3. Scope lock

Before evaluating the result, record:

- target object
- audit question
- included material
- excluded material
- time range
- descriptive resolution
- external standard or rule used
- assumptions

If scope changes during the audit, record the change explicitly rather than silently editing the original scope.

## 4. Source preservation

Preserve original claims before rewriting them in DSD terms.

Recommended fields:

```text
SOURCE_CLAIM
SOURCE_DEFINITION
SOURCE_PROCEDURE
SOURCE_DATA
SOURCE_VERSION
SOURCE_DATE
```

When the source is external, include a stable citation, URL, commit, DOI, case identifier, or archive reference where possible.

## 5. Descriptive-status ledger

Separate information into:

```text
ESTABLISHED_WITHIN_SCOPE
UNDETERMINED_OR_INSUFFICIENT
OUT_OF_SCOPE
```

Do not move an item from one category to another without recording the reason.

## 6. Selection and exclusion ledger

For every material selection, record:

```text
AVAILABLE_OPTIONS
SELECTED_OPTION
SELECTION_RULE
EXCLUDED_OPTIONS
EXCLUSION_REASONS
POST_HOC_CHANGE_CHECK
```

An exclusion may be legitimate, but it must remain visible to later reviewers.

## 7. Transition ledger

Use one row per material transition.

| Step | Prior state / evidence | Rule or reason | Next state / conclusion | Status |
|---|---|---|---|---|
| 1 |  |  |  |  |

Recommended statuses:

- justified
- conditionally justified
- unsupported
- contradicted
- undetermined

## 8. Proposition-layer ledger

Separate propositions by role:

| ID | Statement | Layer | Source / basis |
|---|---|---|---|
| P1 |  | Fact / Inference / Norm / Decision |  |

A proposition may be reused in later steps, but its original layer should remain unchanged unless the change is explicitly justified.

## 9. Alternative-possibility ledger

Record alternative describable structures, causes, interpretations, hypotheses, or paths that remain compatible with the observed result.

For each alternative, record:

- description
- evidence for compatibility
- evidence against
- whether excluded
- exclusion rule
- additional information required for exclusion

## 10. Witness and counterexample record

When applicable, record:

- minimal positive witness
- minimal counterexample
- boundary case
- finite exhaustive search range
- known untested region

A finite computational check must be labeled as finite unless a separate argument establishes a general result.

## 11. Contradiction audit

Check at least four levels:

1. **Definition contradiction** — incompatible definitions or scope commitments.
2. **Transition contradiction** — actual transition conflicts with the declared rule.
3. **Structural contradiction** — locally valid components combine into an invalid or incompatible global structure.
4. **Claim contradiction / overreach** — the evidence is compatible with the process, but the stated conclusion exceeds what it establishes.

Also record omission when a required step or source is missing without necessarily creating a contradiction.

## 12. Eight-axis summary

Every completed audit should summarize:

| Axis | Summary |
|---|---|
| D — Describability | |
| R — Resolution | |
| S — Selection | |
| E — Exclusion | |
| T — Transition | |
| C — Consistency | |
| N — Norm | |
| O — Outcome | |

## 13. Verdict discipline

The verdict must include:

```text
VERDICT
VERDICT_BASIS
MAXIMUM_SUPPORTED_CLAIM
UNSUPPORTED_OR_UNRESOLVED_CLAIMS
```

Use the verdict vocabulary defined in `GENERAL_AUDIT_FRAMEWORK.md`.

Do not compress multiple independent failures into a generic `FAIL` if the failure type can be identified more precisely.

## 14. Reproducibility and traceability

For computational or procedural audits, record where applicable:

- code repository and path
- commit SHA
- environment
- dependencies
- input files
- random seed
- numerical tolerance
- execution order
- generated outputs

For non-computational audits, record:

- source set
- source dates
- quoted or cited passages
- classification rules
- decision rules
- unresolved material

The goal is not always exact computational reproduction; it is **independent reconstruction of the audit path**.

## 15. Change log

When an audit is revised, append a change record rather than overwriting the history of the conclusion.

Recommended form:

```text
REVISION_DATE:
CHANGED_SCOPE:
NEW_SOURCE:
CHANGED_VERDICT:
REASON:
```

This is especially important when new evidence changes an earlier reasonable conclusion.
