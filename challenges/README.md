# DSD Analysis Objectivity & Consistency Challenges / DSD 분석론 객관성·일관성 도전

This directory records adversarial and repeatability-oriented challenges for **DSD Analysis**.

이 디렉터리는 **DSD 분석론의 객관성·일관성**을 높이기 위한 도전 시험을 순차적으로 기록합니다.
성공 사례뿐 아니라 실패, 비대응, 무효용, 미결정 결과도 동일하게 보존합니다.

## Purpose / 목적

- Test whether structurally irrelevant changes such as names, presentation order, or evaluative framing change the analysis.
- Test whether structurally identical cases receive the same structural analysis.
- Test whether a materially different formation/property/dynamic structure is actually distinguished.
- Permit `no analytical gain`, `non-correspondence`, and `undetermined` as normal outcomes.
- Reduce post-hoc favorable reinterpretation by precommitting interface and verdict criteria before reading the result.

## Common fields / 공통 기록 항목

```text
CHALLENGE_ID:
DATE:
DSD_INTERFACE_PROFILE_DATE:
PRECOMMITTED_CRITERIA:
CASE_GENERATION:
BLINDING_LEVEL:
ANALYSIS_RESULT:
INVARIANCE_RESULT:
DISCRIMINATION_RESULT:
ANALYTICAL_GAIN:
FAILURES_OR_LIMITS:
NEXT_STRENGTHENING_STEP:
```

## Interpretation rule / 해석 규칙

A `PASS` means only that the stated challenge criterion was met.
It is not evidence that DSD as a whole is true.
A `FAIL` is preserved as a revision or scope-limitation signal.
A case designed and analyzed by the same person or same model session is **not** counted as an independent blind validation.

## Planned sequence / 진행 순서

1. Blind + Twin Challenge
2. Symmetric-case challenge
3. DSD-null / no-gain cases
4. Forced non-correspondence challenge
5. Layer-restraint challenge
6. Specialization-removal challenge
7. Competing-explanation challenge
8. Unseen-problem transfer challenge
9. Reverse-prediction challenge
10. Minimal-structure challenge

## Current records / 현재 기록

- [`ANL-CH-001_blind-twin-pilot.md`](ANL-CH-001_blind-twin-pilot.md) — first pilot invariance/discrimination challenge.
