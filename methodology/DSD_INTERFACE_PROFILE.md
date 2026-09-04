# DSD Interface Profile / DSD 인터페이스 프로파일

Profile date: **2026-09-05**

This document fixes the DSD-specific interfaces used by **DSD Analysis** and the **DSD General Audit Framework**.
The general audit frame should remain comparatively stable; paper-specific changes are absorbed here first so that later analyses can state exactly which DSD layers, statuses, bridges, and transition rules were active.

이 문서는 DSD 분석론과 DSD 일반 감사체계가 사용하는 **DSD 전용 인터페이스 기준**을 고정합니다.
일반 감사의 공통 8축은 가능한 한 안정적으로 유지하고, 최신 논문에 따라 변할 수 있는 층위·상태·브리지·전이 규칙은 먼저 이 문서에서 갱신합니다.

## 1. Current reference set / 현재 기준 문서

- **Formation Axiom System — Dimensional-Structural Describability** — 2026-08-06
- **Property Axiom System in Dimensional-Structural Describability** — 2026-09-01
- **Channel-Indexed Static Aggregation in Dimensional-Structural Describability** — 2026-09-02
- **Structural Reorganization Dynamics in Dimensional-Structural Describability** — 2026-08-12

The date above is the interface-profile date, not a claim that all papers share the same revision date.
Every audit should record the exact source revision, DOI, commit, file, or archive reference actually used when available.

## 2. Layer model / 층위 모델

The current DSD analysis interface distinguishes the following layers.
They are **not** a mandatory serial package.

1. **Formation layer**
   - candidate structures and expressions
   - admission, restriction, realization, configuration describability
   - quantity-specific partial assignment
   - operational-channel formation
   - finite composition after the post-Stage-VI term data are supplied

2. **General Property layer**
   - parameterized by a fixed Stage-VI formation background
   - finite typed property profiles
   - applicability regions
   - contextual prerequisites
   - partial property assignments and status distinctions
   - does not modify formation assignments, roles, channels, or formation traces

3. **Static analytic layer**
   - analytic realization of admitted formation channels
   - finite formation-compatible aggregation
   - optional, separate aggregation of selected defined typed property data
   - the property aggregate is not identified with Formation Clause VII

4. **Dynamics layer**
   - component-resolved, time-indexed states
   - regular epochs over a fixed Stage-VI formation background
   - explicit lineage for formation-level identity changes
   - optional property, analytic, and geometric interfaces only when the chosen dynamic model uses them

5. **Optional specializations**
   - realized-axis geometry, lines, normals, rank, bilinear data, and related coordinates
   - these are specialization data, not universal coordinates of the general Property Axiom System

## 3. Interface lock / 인터페이스 잠금

Start each DSD analysis or audit with an explicit interface record whenever the DSD formal layers materially affect the result.

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

Do not infer that an unused layer is absent from DSD in general.
The field records only what the current case actually uses.

## 4. Evidence status and object status / 증거 상태와 객체 상태

Audit evidence status and DSD object status are different ledgers.
They must not be collapsed.

### 4.1 Audit evidence status

```text
ESTABLISHED_WITHIN_SCOPE
UNDETERMINED_OR_INSUFFICIENT
OUT_OF_SCOPE
```

### 4.2 Formation-side object status

At minimum, preserve distinctions relevant to the selected formation interface:

```text
UNDEFINED_ASSIGNMENT
DEFINED_ZERO
DEFINED_NONZERO_OR_OTHER_DEFINED_VALUE
CHANNEL_ABSENCE
ADMITTED_CHANNEL_WITH_ZERO_COMPONENT_TERM
```

An absent channel is not a zero-valued or zero-term channel.

### 4.3 Property-side object status

When the general Property layer is used, preserve as applicable:

```text
UNDECLARED
PROFILE_UNAVAILABLE
INAPPLICABLE
PREREQUISITE_UNSATISFIED
APPLICABLE_BUT_UNDEFINED
DEFINED_ZERO
DEFINED_NONZERO_OR_OTHER_DEFINED_VALUE
```

Do not zero-pad an undefined state without retaining side information when the distinction matters to the claim.

## 5. Bridge discipline / 브리지 규율

No cross-layer mathematical role is inferred from names alone.
Record every bridge that materially affects the result.

### 5.1 Property-to-channel association

A multi-input property datum has no canonical unary formation-channel owner.
If selected property data inform one channel realization, record the explicit selector or allocation rule.

### 5.2 Static property bridge

If selected typed property records are sent to an analytic output carrier, record the bridge, its domain, codomain, and assumptions.

### 5.3 Constitutive dynamic bridge

If property data are used as transport, relaxation, stiffness, inertia-like, coupling, propagation, or other dynamic operator data, record the separate constitutive dynamic bridge.
A property label alone does not determine a dynamic coefficient.

Recommended audit fields:

```text
BRIDGE_NAME:
BRIDGE_SOURCE_LAYER:
BRIDGE_DOMAIN:
BRIDGE_CODOMAIN:
BRIDGE_ASSUMPTIONS:
BRIDGE_JUSTIFICATION:
IMPLICIT_BRIDGE_CHECK:
```

## 6. Aggregation and reconstruction discipline / 집계·복원 규율

Aggregate equality does not automatically imply support, decomposition, or structural equality.
When a reduced aggregate or summary is used, audit:

```text
OUTPUT_EQUALITY_CHECK:
SUPPORT_EQUALITY_CHECK:
DECOMPOSITION_RETENTION_CHECK:
INJECTIVITY_ESTABLISHED:
COLLISION_WITNESS:
KERNEL_OR_INFORMATION_LOSS_CHECK:
RECONSTRUCTION_CLAIM:
```

A reconstruction claim requires a theorem or explicit condition appropriate to the selected admissible data class.

## 7. Dynamic transition and lineage discipline / 동역학 전이·lineage 규율

When dynamics is used, distinguish at least:

```text
DOWNSTREAM_VALUE_EVOLUTION
PROPERTY_ASSIGNMENT_EVOLUTION
PROPERTY_STATUS_OR_DOMAIN_TRANSITION
OPTIONAL_GEOMETRIC_SPECIALIZATION_TRANSITION
CHANNEL_OR_FORMATION_LEVEL_TRANSITION
```

A change to a coordinate belonging to Stage-VI channel identity is not written as a time-varying value of one unchanged inherited channel.
When the model treats a post-transition component as a successor of a pre-transition component, record the required lineage relation.

Recommended fields:

```text
TRANSITION_CLASS:
SAME_REGULAR_EPOCH:
IDENTITY_PRESERVED:
LINEAGE_REQUIRED:
LINEAGE_SUPPLIED:
PRE_STATE:
POST_STATE:
```

## 8. Migration rule / 마이그레이션 규칙

When a predecessor DSD paper changes:

1. Do not rewrite the stable eight-axis audit core first.
2. Compare the new paper with this interface profile.
3. Identify whether layer boundaries, status distinctions, bridge obligations, aggregation rules, or transition rules changed.
4. Update this profile and the execution template only where necessary.
5. Preserve older audit records under the interface version used at the time.
6. If an old audit is re-evaluated, append a migration or revision record rather than silently replacing its historical verdict.

Recommended migration fields:

```text
METHODOLOGY_VERSION:
DSD_INTERFACE_PROFILE_DATE:
MIGRATION_STATUS:
LEGACY_TERMINOLOGY:
MIGRATION_NOTES:
```

## 9. Relationship to future automation / 향후 자동화와의 관계

This profile is intentionally structured so that later software can validate mechanical conditions without pretending to decide every domain judgment.
Potentially automatable checks include missing version locks, type/status conflation, missing required bridge declarations, zero-padding without status sidecars, unsupported reconstruction from non-injective summaries, and missing lineage records for formation-level transitions.

Domain validity remains primary: mathematical proof, empirical scientific validation, legal judgment, software correctness, and other field-specific standards are not replaced by the DSD audit layer.
