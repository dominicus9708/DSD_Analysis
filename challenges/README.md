# DSD Analysis Objectivity & Consistency Challenges / DSD 분석론 객관성·일관성 도전

This directory records adversarial and repeatability-oriented challenges for **DSD Analysis**.

이 디렉터리는 **DSD 분석론의 객관성·일관성**을 높이기 위한 도전 시험을 순차적으로 기록합니다.
성공 사례뿐 아니라 실패, 비대응, 무효용, 미결정 결과도 동일하게 보존합니다.

## Purpose / 목적

- Test whether structurally irrelevant changes such as names, presentation order, or evaluative framing change the analysis.
- Test whether structurally identical cases receive the same structural analysis.
- Test whether a materially different formation/property/dynamic structure is actually distinguished.
- Test whether declared symmetry transformations produce the corresponding transformed result rather than directional bias.
- Test whether DSD can explicitly recognize cases where an external baseline is already sufficient and DSD adds no analytical gain.
- Test whether an essential external structure is genuinely preserved before granting `direct` or `partial` correspondence.
- Keep explicit encoding, bridge insertion, and added-layer rescue distinct from direct correspondence.
- Test whether the minimum sufficient DSD layer set is selected without automatic upward drag or a compulsory serial-chain assumption.
- Permit `no analytical gain`, `negative analytical gain`, `non-correspondence`, and `undetermined` as normal outcomes.
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
CORRESPONDENCE_RESULT:
ESSENTIAL_STRUCTURE:
ESSENTIAL_STRUCTURE_PRESERVED:
ENCODED_EXTENSION_RESULT:
BASELINE_SUFFICIENCY:
INVARIANCE_RESULT:
EQUIVARIANCE_RESULT:
DISCRIMINATION_RESULT:
ANALYTICAL_GAIN:
MINIMUM_SUFFICIENT_LAYER_SET:
SELECTED_LAYER_SET:
LAYER_SELECTION_RESULT:
UNNECESSARY_LAYER_INTRODUCED:
MISSING_REQUIRED_LAYER:
FAILURES_OR_LIMITS:
NEXT_STRENGTHENING_STEP:
```

`INVARIANCE_RESULT` and `EQUIVARIANCE_RESULT` are distinct.
Invariance requires a result to remain unchanged under a nonessential relabeling.
Equivariance requires a result to transform consistently when the tested structure itself is transformed by an explicit symmetry map.

`CORRESPONDENCE_RESULT`, `BASELINE_SUFFICIENCY`, and `ANALYTICAL_GAIN` are also distinct.
A direct DSD correspondence can coexist with a fully sufficient external baseline and `ANALYTICAL_GAIN: none`.
Representability is not counted as usefulness by itself.

`ESSENTIAL_STRUCTURE_PRESERVED` prevents surface alignment from being promoted into a meaningful correspondence claim.
A `partial` result should preserve some structure that is genuinely relevant to the external target's defining distinction.
`ENCODED_EXTENSION_RESULT` records whether a mapping requires explicit position, relation, bridge, or added-layer data; such an extension is not retroactively classified as `direct`.

`MINIMUM_SUFFICIENT_LAYER_SET` and `SELECTED_LAYER_SET` are recorded separately.
`LAYER_SELECTION_RESULT` uses `exact_match / over_specified / under_specified / indeterminate`.
The current DSD interface must not be treated as a compulsory serial ladder when the source manuscripts define Property, Static, realized-axis, and other downstream interfaces as optional or selectively activated.

Recommended analytical-gain vocabulary:

```text
substantial
limited
none
negative
```

## Interpretation rule / 해석 규칙

A `PASS` means only that the stated challenge criterion was met.
It is not evidence that DSD as a whole is true.
A null challenge can pass precisely because DSD correctly recognizes that it is unnecessary for the tested case.
A non-correspondence challenge can pass precisely because the selected interface correctly refuses to claim preservation of an essential structure.
A layer-restraint challenge can pass only when required layers are not omitted and unnecessary layers are not introduced.
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
- [`ANL-CH-002_symmetric-case-pilot.md`](ANL-CH-002_symmetric-case-pilot.md) — sign/orientation symmetry and composition-equivariance pilot.
- [`ANL-CH-003_dsd-null-no-gain-pilot.md`](ANL-CH-003_dsd-null-no-gain-pilot.md) — direct correspondence with a sufficient external baseline and correctly recognized zero analytical gain.
- [`ANL-CH-004_forced-non-correspondence-pilot.md`](ANL-CH-004_forced-non-correspondence-pilot.md) — ordered-sequence obstruction showing that essential-structure loss must be recorded as non-correspondence rather than rescued post hoc.
- [`ANL-CH-005_layer-restraint-pilot.md`](ANL-CH-005_layer-restraint-pilot.md) — casewise minimum-layer selection across Formation, Property, Static, and Dynamics without unnecessary serial-chain expansion.
