# DSD Audit Recording Standard

## 1. Purpose

This document defines how an audit should be recorded so that the result can be reviewed later without relying on memory or conversational context.

The recording standard is intentionally stricter than an informal analysis note.
It should preserve both the path that led to the verdict and the paths that were rejected.
It also records the DSD interface version used by the audit so that later paper revisions are not silently projected backward.

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
- Audit version or revision
- DSD interface profile date
- Exact DSD predecessor-source revisions used when relevant

## 3. DSD interface lock

Before a DSD-dependent audit is evaluated, record the layer selection from `DSD_INTERFACE_PROFILE.md`.

```text
DSD_INTERFACE_PROFILE_DATE:
FORMATION_LAYER: used / not used
PROPERTY_CORE: used / not used
STATIC_AGGREGATION_LAYER: used / not used
DYNAMICS_LAYER: used / not used
REALIZED_AXIS_SPECIALIZATION: supplied / not supplied
OTHER_SPECIALIZATION:
SOURCE_VERSIONS:
```

If the audit does not use the DSD formal layers, record that explicitly rather than fabricating empty structures.

## 4. Scope lock

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

## 5. Source preservation

Preserve original claims before rewriting them in DSD terms.

Recommended fields:

```text
SOURCE_CLAIM
SOURCE_DEFINITION
SOURCE_PROCEDURE
SOURCE_DATA
SOURCE_VERSION
SOURCE_DATE
SOURCE_REFERENCE
```

When the source is external, include a stable citation, URL, commit, DOI, case identifier, or archive reference where possible.

## 6. Evidence-status ledger

Separate audit evidence into:

```text
ESTABLISHED_WITHIN_SCOPE
UNDETERMINED_OR_INSUFFICIENT
OUT_OF_SCOPE
```

Do not move an item from one category to another without recording the reason.

This ledger describes the audit evidence, not the internal status of a DSD object.

## 7. DSD object-status ledger

When a DSD formal layer is used, record the object status separately.

### Formation examples

```text
UNDEFINED_ASSIGNMENT
DEFINED_ZERO
DEFINED_NONZERO_OR_OTHER_DEFINED_VALUE
CHANNEL_ABSENCE
ADMITTED_CHANNEL_WITH_ZERO_COMPONENT_TERM
```

### Property examples

```text
UNDECLARED
PROFILE_UNAVAILABLE
INAPPLICABLE
PREREQUISITE_UNSATISFIED
APPLICABLE_BUT_UNDEFINED
DEFINED_ZERO
DEFINED_NONZERO_OR_OTHER_DEFINED_VALUE
```

### Dynamic examples

```text
DOWNSTREAM_VALUE_EVOLUTION
PROPERTY_ASSIGNMENT_EVOLUTION
PROPERTY_STATUS_OR_DOMAIN_TRANSITION
OPTIONAL_GEOMETRIC_SPECIALIZATION_TRANSITION
CHANNEL_OR_FORMATION_LEVEL_TRANSITION
```

Do not replace undefined or absent object statuses with numerical zero unless the representation also preserves the status information required by the claim.

## 8. Selection and exclusion ledger

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

## 9. Bridge and allocation ledger

When one DSD layer is mapped into another, record the bridge explicitly.

```text
BRIDGE_NAME:
BRIDGE_SOURCE_LAYER:
BRIDGE_DOMAIN:
BRIDGE_CODOMAIN:
BRIDGE_ASSUMPTIONS:
BRIDGE_JUSTIFICATION:
IMPLICIT_BRIDGE_CHECK:
```

Typical cases include:

- multi-input property data allocated to one formation channel;
- typed property records mapped to a static analytic carrier;
- property data mapped to dynamic coefficients or operators;
- represented or specialized coordinates treated as core data.

A bridge may be domain-specific and valid without being universal.
The audit should record its scope rather than promote it into a DSD axiom.

## 10. Transition ledger

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

When the DSD dynamics interface is used, also record:

```text
TRANSITION_CLASS:
SAME_REGULAR_EPOCH:
IDENTITY_PRESERVED:
LINEAGE_REQUIRED:
LINEAGE_SUPPLIED:
PRE_STATE:
POST_STATE:
```

A formation-level identity change must not be recorded as ordinary value evolution of one unchanged channel.

## 11. Proposition-layer ledger

Separate propositions by role:

| ID | Statement | Layer | Source / basis |
|---|---|---|---|
| P1 |  | Fact / Inference / Norm / Decision |  |

A proposition may be reused in later steps, but its original layer should remain unchanged unless the change is explicitly justified.

## 12. Alternative-possibility ledger

Record alternative describable structures, causes, interpretations, hypotheses, or paths that remain compatible with the observed result.

For each alternative, record:

- description
- evidence for compatibility
- evidence against
- whether excluded
- exclusion rule
- additional information required for exclusion

## 13. Aggregation, compression, and reconstruction ledger

If a reduced aggregate, summary, scalarization, or other compressed readout is used, record:

```text
REDUCED_READOUT_USED:
OUTPUT_EQUALITY_CHECK:
SUPPORT_EQUALITY_CHECK:
DECOMPOSITION_RETENTION_CHECK:
NEGATIVE_STATUS_RETENTION_CHECK:
INJECTIVITY_ESTABLISHED:
COLLISION_WITNESS:
KERNEL_OR_INFORMATION_LOSS_CHECK:
RECONSTRUCTION_CLAIM:
RECONSTRUCTION_BASIS:
```

Do not infer equal support or structural equality from equal aggregate outputs without an appropriate injectivity or reconstruction result.

## 14. Witness and counterexample record

When applicable, record:

- minimal positive witness
- minimal counterexample
- boundary case
- finite exhaustive search range
- known untested region
- aggregate collision witness when relevant
- bridge-failure witness when relevant

A finite computational check must be labeled as finite unless a separate argument establishes a general result.

## 15. Contradiction audit

Check at least five levels:

1. **Definition contradiction** — incompatible definitions or scope commitments.
2. **Interface contradiction** — a later DSD layer or optional specialization is used as if it were mandatory or already supplied.
3. **Transition contradiction** — actual transition conflicts with the declared rule or identity discipline.
4. **Structural contradiction** — locally valid components combine into an invalid or incompatible global structure.
5. **Claim contradiction / overreach** — the evidence is compatible with the process, but the stated conclusion exceeds what it establishes.

Also record omission when a required source, bridge, status sidecar, lineage relation, injectivity basis, or proof step is missing without necessarily creating a contradiction.

## 16. Eight-axis summary

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

## 17. Verdict discipline

The verdict must include:

```text
VERDICT
VERDICT_BASIS
MAXIMUM_SUPPORTED_CLAIM
UNSUPPORTED_OR_UNRESOLVED_CLAIMS
```

Use the verdict vocabulary defined in `GENERAL_AUDIT_FRAMEWORK.md`.

Do not compress multiple independent failures into a generic `FAIL` if the failure type can be identified more precisely.

## 18. Reproducibility and traceability

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
- interface-profile date
- predecessor paper/file revision
- bridge configuration

For non-computational audits, record:

- source set
- source dates
- quoted or cited passages
- classification rules
- interface layers used
- decision rules
- unresolved material

The goal is not always exact computational reproduction; it is **independent reconstruction of the audit path**.

## 19. Change and migration log

When an audit is revised, append a change record rather than overwriting the history of the conclusion.

Recommended form:

```text
REVISION_DATE:
CHANGED_SCOPE:
NEW_SOURCE:
CHANGED_VERDICT:
REASON:
METHODOLOGY_VERSION:
DSD_INTERFACE_PROFILE_DATE:
MIGRATION_STATUS:
LEGACY_TERMINOLOGY:
MIGRATION_NOTES:
```

This is especially important when a new DSD paper changes the interface under which an older audit was originally reasonable.
