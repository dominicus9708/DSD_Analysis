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
VERSION:
```

## 1. Audit question / 감사 질문

```text
PRIMARY_QUESTION:
QUESTIONS_NOT_BEING_DECIDED:
```

## 2. Scope / 범위

```text
TARGET_SCOPE:
TIME_SCOPE:
DESCRIPTIVE_RESOLUTION:
INCLUDED_MATERIAL:
EXCLUDED_MATERIAL:
EXTERNAL_STANDARD:
ASSUMPTIONS:
```

## 3. Original source preservation / 원자료 보존

```text
SOURCE_CLAIM:
SOURCE_DEFINITION:
SOURCE_PROCEDURE:
SOURCE_DATA_OR_EVIDENCE:
SOURCE_VERSION:
SOURCE_DATE:
SOURCE_REFERENCE:
```

## 4. Descriptive status / 기술 상태

### Established within scope / 범위 내 확인

- 

### Undetermined or insufficient / 미정·불충분

- 

### Out of scope / 범위 밖

- 

## 5. Selection and exclusion / 선택·배제

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

## 6. Proposition layers / 명제 층위

### Fact / 사실

- 

### Inference / 추론

- 

### Norm / 규범·기준

- 

### Decision / 판단·결정

- 

## 7. Transition audit / 전이 감사

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

## 8. Alternative describabilities / 대안 기술가능성

```text
ALTERNATIVE_1:
COMPATIBILITY_BASIS:
EXCLUDED?:
EXCLUSION_BASIS:
ADDITIONAL_INFORMATION_NEEDED:
```

Add more alternatives as needed.

## 9. Witnesses, counterexamples, boundary cases / 증인·반례·경계 사례

```text
MINIMAL_POSITIVE_WITNESS:
MINIMAL_COUNTEREXAMPLE:
BOUNDARY_CASE:
FINITE_EXHAUSTIVE_RANGE:
UNTESTED_REGION:
```

## 10. Contradiction audit / 모순 감사

```text
DEFINITION_CONTRADICTION:
TRANSITION_CONTRADICTION:
STRUCTURAL_CONTRADICTION:
CLAIM_CONTRADICTION_OR_OVERREACH:
OMISSION:
```

## 11. Eight-axis summary / 8축 요약

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

## 12. Final verdict / 최종 판정

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

## 13. Reproducibility and traceability / 재현·추적

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
GENERATED_OUTPUTS:
RELATED_NOTION_PAGE:
```

Use only the fields relevant to the audit.

## 14. Follow-up / 후속 작업

- [ ] Obtain additional material / 추가 자료 확보
- [ ] Independent review / 독립 재검토
- [ ] Expand counterexample search / 반례 확대
- [ ] Compare with domain protocol / 분야별 프로토콜 대조
- [ ] Reflect in synthesis or paper preparation / 종합·논문화 반영

## 15. Revision log / 개정 기록

```text
REVISION_DATE:
CHANGED_SCOPE:
NEW_SOURCE:
CHANGED_VERDICT:
REASON:
```
