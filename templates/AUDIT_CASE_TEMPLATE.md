# DSD Audit Case Template / DSD 감사 실행 템플릿

> Copy this file for each individual audit. Do not force an unknown field into a positive or negative conclusion. Use `undetermined` or `out of scope` when appropriate.
>
> 개별 감사마다 이 파일을 복사하여 사용합니다. 확인할 수 없는 항목을 억지로 긍정·부정으로 채우지 말고 `미정` 또는 `범위 밖`으로 기록합니다.

---

## 0. Identity / 식별

```text
AUDIT_ID:
TITLE:
DOMAIN:
DATE:
AUDITOR_OR_AGENT:
RELATED_SOURCE_OR_CASE:
AUDIT_VERSION:
DSD_INTERFACE_PROFILE_DATE:
```

## 1. DSD interface lock / DSD 인터페이스 잠금

Use only when DSD formal layers materially affect the case.

```text
FORMATION_LAYER: used / not used
PROPERTY_CORE: used / not used
STATIC_AGGREGATION_LAYER: used / not used
DYNAMICS_LAYER: used / not used
REALIZED_AXIS_SPECIALIZATION: supplied / not supplied
OTHER_SPECIALIZATION:
FORMATION_SOURCE_VERSION:
PROPERTY_SOURCE_VERSION:
STATIC_AGGREGATION_SOURCE_VERSION:
DYNAMICS_SOURCE_VERSION:
OTHER_SOURCE_VERSIONS:
```

## 2. Audit question / 감사 질문

```text
PRIMARY_QUESTION:
QUESTIONS_NOT_BEING_DECIDED:
```

## 3. Scope / 범위

```text
TARGET_SCOPE:
TIME_SCOPE:
DESCRIPTIVE_RESOLUTION:
INCLUDED_MATERIAL:
EXCLUDED_MATERIAL:
EXTERNAL_STANDARD:
ASSUMPTIONS:
```

## 4. Original source preservation / 원자료 보존

```text
SOURCE_CLAIM:
SOURCE_DEFINITION:
SOURCE_PROCEDURE:
SOURCE_DATA_OR_EVIDENCE:
SOURCE_VERSION:
SOURCE_DATE:
SOURCE_REFERENCE:
```

## 5. Evidence status / 감사 근거 상태

### Established within scope / 범위 내 확인

- 

### Undetermined or insufficient / 미정·불충분

- 

### Out of scope / 범위 밖

- 

## 6. DSD object-status ledger / DSD 객체 상태 장부

Do not merge this with audit evidence status.

```text
FORMATION_STATUS:
PROPERTY_STATUS:
DYNAMIC_STATUS:
STATUS_SIDECAR_REQUIRED:
STATUS_SIDECAR_SUPPLIED:
```

Useful property statuses when the general Property layer is used:

```text
UNDECLARED
PROFILE_UNAVAILABLE
INAPPLICABLE
PREREQUISITE_UNSATISFIED
APPLICABLE_BUT_UNDEFINED
DEFINED_ZERO
DEFINED_NONZERO_OR_OTHER_DEFINED_VALUE
```

## 7. Selection and exclusion / 선택·배제

### Available alternatives / 가능한 선택지

- 

### Selected / 실제 선택

- 

### Selection rule / 선택 기준

- 

### Excluded / 배제 항목

- 

### Exclusion reason / 배제 사유

- 

### Post-hoc change check / 사후 기준 변경 검사

```text
NONE / PRESENT / UNDETERMINED:
DETAILS:
```

## 8. Bridge and allocation audit / 브리지·배정 감사

Repeat this block for each material bridge.

```text
BRIDGE_NAME:
BRIDGE_SOURCE_LAYER:
BRIDGE_DOMAIN:
BRIDGE_CODOMAIN:
BRIDGE_ASSUMPTIONS:
BRIDGE_JUSTIFICATION:
IMPLICIT_BRIDGE_CHECK:
MULTI_INPUT_PROPERTY_ALLOCATION_REQUIRED:
ALLOCATION_RULE_SUPPLIED:
```

## 9. Proposition layers / 명제 층위

### Fact / 사실

- 

### Inference / 추론

- 

### Norm / 규범·기준

- 

### Decision / 판단·결정

- 

## 10. Transition audit / 전이 감사

| Step | Prior state or evidence / 이전 상태·근거 | Rule or reason / 전이 규칙·이유 | Next state or conclusion / 다음 상태·판단 | Status / 판정 |
|---|---|---|---|---|
| 1 |  |  |  |  |

Suggested status values:

```text
JUSTIFIED
CONDITIONALLY_JUSTIFIED
UNSUPPORTED
CONTRADICTED
UNDETERMINED
```

### DSD dynamic transition classification / DSD 동역학 전이 분류

```text
TRANSITION_CLASS:
SAME_REGULAR_EPOCH:
IDENTITY_PRESERVED:
LINEAGE_REQUIRED:
LINEAGE_SUPPLIED:
PRE_STATE:
POST_STATE:
```

Suggested classes:

```text
DOWNSTREAM_VALUE_EVOLUTION
PROPERTY_ASSIGNMENT_EVOLUTION
PROPERTY_STATUS_OR_DOMAIN_TRANSITION
OPTIONAL_GEOMETRIC_SPECIALIZATION_TRANSITION
CHANNEL_OR_FORMATION_LEVEL_TRANSITION
NOT_APPLICABLE
```

## 11. Alternative describabilities / 대안 기술가능성

```text
ALTERNATIVE_1:
COMPATIBILITY_BASIS:
EXCLUDED?:
EXCLUSION_BASIS:
ADDITIONAL_INFORMATION_NEEDED:
```

Add more alternatives as needed.

## 12. Aggregation, compression, and reconstruction / 집계·압축·복원

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

## 13. Witnesses, counterexamples, boundary cases / 증인·반례·경계 사례

```text
MINIMAL_POSITIVE_WITNESS:
MINIMAL_COUNTEREXAMPLE:
BOUNDARY_CASE:
AGGREGATE_COLLISION_WITNESS:
BRIDGE_FAILURE_WITNESS:
FINITE_EXHAUSTIVE_RANGE:
UNTESTED_REGION:
```

## 14. Contradiction audit / 모순 감사

```text
DEFINITION_CONTRADICTION:
INTERFACE_CONTRADICTION:
TRANSITION_CONTRADICTION:
STRUCTURAL_CONTRADICTION:
CLAIM_CONTRADICTION_OR_OVERREACH:
OMISSION:
```

## 15. Eight-axis summary / 8축 요약

| Axis | Audit result / 감사 결과 |
|---|---|
| D — Describability | |
| R — Resolution | |
| S — Selection | |
| E — Exclusion | |
| T — Transition | |
| C — Consistency | |
| N — Norm | |
| O — Outcome | |

## 16. Final verdict / 최종 판정

Choose the narrowest suitable verdict.

```text
CONFIRMED
CONDITIONALLY_CONFIRMED
PARTIALLY_CONFIRMED
UNDETERMINED
INSUFFICIENT_BASIS
EXCLUSION_ERROR
TRANSITION_ERROR
NORM_CONFLATION
CONTRADICTION
OVERCLAIM
```

```text
VERDICT:
VERDICT_BASIS:
MAXIMUM_SUPPORTED_CLAIM:
UNSUPPORTED_OR_UNRESOLVED_CLAIMS:
```

## 17. Reproducibility and traceability / 재현·추적

```text
REQUIRED_SOURCES:
REVIEW_OR_EXECUTION_ORDER:
REPOSITORY_AND_PATH:
COMMIT_SHA:
ENVIRONMENT:
DEPENDENCIES:
INPUTS:
RANDOM_SEED:
TOLERANCE:
BRIDGE_CONFIGURATION:
GENERATED_OUTPUTS:
RELATED_NOTION_PAGE:
```

Use only the fields relevant to the audit.

## 18. Follow-up / 후속 작업

- [ ] Obtain additional material / 추가 자료 확보
- [ ] Independent review / 독립 재검토
- [ ] Expand counterexample search / 반례 확대
- [ ] Compare with domain protocol / 분야별 프로토콜 대조
- [ ] Check interface migration need / 인터페이스 마이그레이션 필요성 확인
- [ ] Reflect in synthesis or paper preparation / 종합·논문화 반영
- [ ] Evaluate automation candidate checks / 자동화 가능한 검사 항목 분류

## 19. Revision and migration log / 개정·마이그레이션 기록

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
