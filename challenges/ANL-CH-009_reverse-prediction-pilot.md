# ANL-CH-009 — Reverse-Prediction Challenge (Pilot)

Date: **2026-09-06**
Status: **PRECOMMIT_LOCKED_AWAITING_REVEAL**

## 1. Purpose / 목적

Lock directional DSD predictions **before** revealing which structural perturbation templates will be instantiated.

This is a same-session **commit-before-reveal procedural pilot**, not an independent blind validation.

## 2. Source lock / 소스 잠금

```text
CHALLENGE_ID: ANL-CH-009
DATE: 2026-09-06
DSD_INTERFACE_PROFILE_DATE: 2026-09-05
SOURCE_VERSIONS:
  Formation Axiom System — current supplied manuscript
  Property Axiom System — 2026-09-01
  Channel-Indexed Static Aggregation — 2026-09-02
  Structural Reorganization Dynamics — current supplied manuscript
PREDICTION_LOCK_STATUS: locked_before_reveal
```

## 3. Precommitted criteria / 사전 판정 기준

1. **Directional prediction** — state the direction of the DSD result for each structural perturbation before reveal.
2. **Exact-status prediction** — do not collapse `absent`, `defined zero`, `prerequisite-unsatisfied`, and `unsupported/unavailable`.
3. **Layer prediction** — predeclare the minimum DSD layer set for each perturbation.
4. **No rescue** — a mismatch after reveal is recorded as `prediction_miss`; the original prediction is not rewritten.
5. **No inflated success** — same-session template hits count only as internal rule-consistency calibration.

## 4. Locked prediction dictionary / 잠긴 예측 사전

### P1 — Formation zero-support addition

Condition: add one **admitted zero-bearing channel** to a state whose two existing admitted channels already sum to zero.

```text
PREDICTED_AGGREGATE_CHANGE: none
PREDICTED_SUPPORT_CHANGE: yes
PREDICTED_STRUCTURAL_STATE_EQUALITY: different
PREDICTED_STATUS: previous absence != new admitted zero-bearing channel
PREDICTED_MINIMUM_LAYER_SET: Formation
```

### P2 — Property prerequisite loss

Condition: the property input remains applicable, but one declared prerequisite changes from satisfied to unsatisfied and no defined assignment is supplied for that input.

```text
PREDICTED_PROPERTY_STATUS: prerequisite_unsatisfied
PREDICTED_NOT_STATUS: applicable_but_undefined, defined_zero, defined_nonzero
PREDICTED_MINIMUM_LAYER_SET: Formation background + Property Core
```

### P3 — Dynamic inherited-value identity change with lineage

Condition: the assigned value `v`, which is part of operational-channel identity, changes across time; a formation transition and an explicit lineage edge are supplied.

```text
PREDICTED_LITERAL_IDENTITY: changed
PREDICTED_SUCCESSION: yes, only through supplied lineage
PREDICTED_MINIMUM_LAYER_SET: Formation background + Dynamics
PREDICTED_PROPERTY_OR_STATIC_REQUIREMENT: none
```

### P4 — Realized-axis specialization removal

Condition: hold the general Property/Dynamics core fixed and remove only the realized-axis specialization.

```text
PREDICTED_CORE_CLAIMS: preserved
PREDICTED_AXIS_CLAIMS: withdrawn_as_unavailable
PREDICTED_AXIS_DEFAULT: no rank=0 / false substitution
PREDICTED_RESULT_TYPE: exact_partition if no core contamination occurs
```

## 5. Reveal selector / 공개 선택 절차

After this precommit is persisted, compute SHA-256 of the fixed string

```text
ANL-CH-009|2026-09-06|selection-v1
```

Read 8-hex chunks from left to right, convert each chunk to an integer, and take `mod 4`.
Map `0,1,2,3` to `P1,P2,P3,P4`. Skip duplicates until **three distinct variants** have been selected.

Only after selection are the chosen templates numerically instantiated. Their structural conditions and the scoring criteria above remain locked.

## 6. Current record / 현재 기록

```text
ANALYSIS_RESULT: PRECOMMIT_LOCKED_AWAITING_REVEAL
PREDICTION_RESULT: not_yet_scored
POST_REVEAL_PREDICTION_EDIT: prohibited
```
