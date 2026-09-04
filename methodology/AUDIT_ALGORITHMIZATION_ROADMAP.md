# DSD Audit Algorithmization Roadmap / DSD 감사 알고리즘화 로드맵

Status: **planning document**
Baseline date: **2026-09-05**

This document describes how the current manual DSD Analysis and General Audit records may later be converted into a reproducible software-assisted audit pipeline.
It does **not** claim that domain validity can be reduced to one universal algorithm.

이 문서는 현재의 수동 DSD 분석·감사 기록을 장차 재현 가능한 소프트웨어 보조 감사 파이프라인으로 옮기기 위한 계획입니다.
수학적 참, 과학적 경험 검증, 법적 판단, 정책적 규범 등을 하나의 보편 알고리즘으로 대체한다는 뜻이 아닙니다.

## 1. Design principle / 설계 원칙

Keep three layers separate:

```text
A. mechanically checkable record integrity
B. semi-automatic DSD structural audit
C. external-domain judgment
```

A future program may enforce A strongly and assist B, while C remains governed by the external field's own standards unless a domain-specific formal checker is separately supplied.

## 2. Stable input schema / 안정 입력 스키마

The executable design should be built from the fields already required by:

- `DSD_INTERFACE_PROFILE.md`
- `GENERAL_AUDIT_FRAMEWORK.md`
- `AUDIT_RECORDING_STANDARD.md`
- `templates/AUDIT_CASE_TEMPLATE.md`

Minimum machine-readable groups:

```text
record_identity
interface_lock
scope_lock
source_preservation
evidence_status
object_status
selection_exclusion
bridge_declarations
transition_ledger
lineage_records
alternatives
aggregation_reconstruction
witness_counterexample
contradiction_audit
verdict
reproducibility
revision_migration
```

## 3. Phase 0 — manual structure stabilization / 수동 구조 안정화

Goal: confirm that repeated real audits can be recorded without ad-hoc field invention.

Tasks:

1. Use the updated template across mathematics, science, software/algorithm, and at least one non-technical domain.
2. Record which fields are repeatedly unused, ambiguous, or missing.
3. Keep case-specific research results out of the general methodology unless the same need recurs independently.
4. Preserve failed mappings and cases where DSD adds no useful distinction.
5. Version every interface migration.

Exit condition: the common record schema remains stable across several heterogeneous audits.

## 4. Phase 1 — static schema validator / 정적 스키마 검사기

Potential deterministic checks:

- required identifiers are present;
- exact source/version locks are present when a DSD layer is used;
- layer declarations are syntactically valid;
- evidence status and object status are stored separately;
- `CHANNEL_ABSENCE` is not automatically serialized as defined zero;
- property undefined statuses are not zero-padded without an explicit status sidecar declaration;
- a bridge-dependent claim has a bridge declaration;
- a formation-level transition marked as identity-preserving has an explicit justification or is flagged;
- a reconstruction claim from reduced data has an injectivity/reconstruction field;
- a revision does not silently erase the previous verdict record.

Output should be validation messages, not a truth verdict.

## 5. Phase 2 — DSD structural rule engine / DSD 구조 규칙 엔진

Potential rule families:

### Status rules

Detect forbidden or unsupported collapses such as:

```text
undefined -> zero
absent channel -> zero-valued channel
inapplicable -> defined false/zero
profile unavailable -> inapplicable
```

unless the audit explicitly declares a coarsening map and preserves the side information required by the claim.

### Bridge rules

Flag cases where:

- a multi-input property is allocated to one channel without a declared selector;
- a property label is used as a dynamic coefficient without a constitutive bridge;
- an optional representation is treated as the property core itself.

### Aggregation rules

Flag unsupported implications of the form:

```text
same aggregate -> same support
same summary -> strict structural equivalence
same scalar readout -> same component state
```

unless the record supplies an applicable injectivity or reconstruction basis.

### Transition rules

Flag cases where a Stage-VI channel identity coordinate changes while the record still claims literal unchanged channel identity without lineage or transition treatment.

## 6. Phase 3 — domain adapters / 분야별 어댑터

Each domain adapter should add its own validators without changing the common DSD core.

Examples:

- Mathematics: theorem statement lock, proof-step graph, finite-computation boundary, counterexample search metadata.
- Science: observation/model separation, uncertainty, dataset provenance, constitutive assumptions, reproducibility metadata.
- Software: executable environment, tests, branch/state traces, deterministic or seeded reproduction.
- Law/institutions: source-time information state, authority, burden/standard, norm/evidence separation.

A domain adapter may return a domain-specific status, but the common DSD audit verdict remains separately recorded.

## 7. Phase 4 — reproducible execution pipeline / 재현 실행 파이프라인

Planned high-level flow:

```text
SOURCE LOCK
  -> INTERFACE LOCK
  -> TYPE/STATUS VALIDATION
  -> SELECTION/EXCLUSION CHECK
  -> BRIDGE CHECK
  -> TRANSITION/LINEAGE CHECK
  -> ALTERNATIVE/WITNESS CHECK
  -> AGGREGATION/RECONSTRUCTION CHECK
  -> CONTRADICTION CHECK
  -> MAXIMUM-SUPPORTED-CLAIM CHECK
  -> DOMAIN VERDICT + DSD AUDIT VERDICT
```

The program should preserve an audit trace for every generated warning or verdict component.

## 8. What should not be automated by default / 기본 자동화 금지 영역

Do not let the common engine decide by itself:

- whether an unproved mathematical statement is true;
- whether an empirical constitutive model is physically correct;
- whether a legal norm is authoritative or correctly interpreted;
- whether a policy value judgment is normatively preferable;
- whether one historical interpretation is uniquely correct when the sources do not establish uniqueness.

These require domain evidence, a specialized checker, or human/expert judgment.

## 9. Test strategy / 시험 전략

Use both positive and negative fixtures.

Required fixture types:

```text
valid minimal audit
missing interface lock
undefined-zero conflation
absent-channel zero extension
undeclared-property misuse
missing multi-input selector
missing dynamic constitutive bridge
aggregate collision
unsupported reconstruction
formation-level identity change without lineage
finite computation overclaimed as proof
post-hoc exclusion
```

The test suite should include cases where the correct result is `UNDETERMINED` or `NOT_APPLICABLE`, not only pass/fail outcomes.

## 10. Implementation gate / 구현 시작 조건

Do not begin a full rule engine merely because the schema exists.
Implementation should begin after manual audits show that:

1. the interface profile is stable enough;
2. repeated fields have consistent meanings;
3. at least several domains can use the same core fields;
4. common mechanical checks can be separated from domain judgment;
5. legacy audit migration rules are documented.

Until then, use the repository as the authoritative structured specification and continue accumulating real audit cases.
