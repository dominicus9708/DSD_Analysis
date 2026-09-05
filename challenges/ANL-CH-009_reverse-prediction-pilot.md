# ANL-CH-009 — Reverse-Prediction Challenge (Pilot)

Date: **2026-09-06**
Status: **REVERSE_PREDICTION_DISCIPLINE_PILOT_PASS_WITH_LIMITATIONS**

## 1. Purpose / 목적

Lock directional DSD predictions **before** revealing which structural perturbation templates will be instantiated.

This is a same-session **commit-before-reveal procedural pilot**, not an independent blind validation.

The prediction-only precommit was persisted first at commit:

```text
e40cdc74d873e56caca378921829e9913e69957c
```

The result sections below were added only after that commit existed.

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

The current source interface supports the distinctions used here: Formation separates absence, defined zero, admitted zero-bearing channels, and composite coincidence; Property separates applicability, prerequisite satisfaction, and partial definedness; Dynamics keeps the assigned value `v` inside inherited channel identity and uses explicit lineage across formation-level changes; realized-axis geometry is optional rather than universal.

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

After the precommit was persisted, SHA-256 was computed for the fixed string

```text
ANL-CH-009|2026-09-06|selection-v1
```

with result

```text
9ca70c75c81a608e2df1f9f116b7173b77b715903cec2b6ae75879c47a9efa8a
```

8-hex chunks, read left to right and reduced modulo 4, produced:

```text
9ca70c75 -> 1 -> P2
c81a608e -> 2 -> P3
2df1f9f1 -> 1 -> duplicate, skipped
16b7173b -> 3 -> P4
```

Therefore:

```text
SELECTED_VARIANTS: P2, P3, P4
UNSELECTED_VARIANT: P1
```

P1 remains `not_selected / not_scored` for this pilot.

## 6. Reveal R2 — Property prerequisite loss

Instantiate:

```text
property kind: release_ok
input: x
Ap_release = {x}
Sat_release,d = empty
Dom(Xi_release) = empty
```

The input remains applicable but fails the declared prerequisite.
The observed Property status is therefore `prerequisite_unsatisfied`, not `applicable_but_undefined`, `defined_zero`, or `defined_nonzero`.

```text
P2_PREDICTED_STATUS: prerequisite_unsatisfied
P2_OBSERVED_STATUS: prerequisite_unsatisfied
P2_PREDICTED_MINIMUM_LAYER_SET: Formation background + Property Core
P2_OBSERVED_MINIMUM_LAYER_SET: Formation background + Property Core
P2_RESULT: exact_match
```

## 7. Reveal R3 — Dynamic inherited-value identity change with lineage

Instantiate:

```text
t0: c0 = (p, a, lambda, 3, rho)
t1: c1 = (p, a, lambda, 4, rho)
formation transition: J_0,1 supplied
lineage: (c0,c1) in Lambda_0,1
```

Because the assigned value `v` is part of operational-channel identity:

```text
c0 != c1
```

Succession nevertheless exists through the explicitly supplied lineage edge.
Property and Static interfaces are unnecessary for this question.

```text
P3_PREDICTED_LITERAL_IDENTITY: changed
P3_OBSERVED_LITERAL_IDENTITY: changed
P3_PREDICTED_SUCCESSION: yes_through_supplied_lineage
P3_OBSERVED_SUCCESSION: yes_through_supplied_lineage
P3_PREDICTED_MINIMUM_LAYER_SET: Formation background + Dynamics
P3_OBSERVED_MINIMUM_LAYER_SET: Formation background + Dynamics
P3_RESULT: exact_match
```

## 8. Reveal R4 — Realized-axis specialization removal

Hold the general core fixed:

```text
Property Core:
  x applicable
  prerequisites satisfied
  Xi_phi(x) = 5
  status = defined_nonzero

Dynamics Core:
  supplied core state/lineage remains fixed

Realized-axis specialization before removal:
  l1 = span(e1)
  l2 = span(e2)
  arank_G = 2
  <e1,e2> = 0
```

Remove only `G`.

Result:

- the general Property value/status remains unchanged;
- the general Dynamics core remains unchanged;
- rank `2` and orthogonality become unavailable/not supplied;
- no fake `rank=0` or `false` replacement is introduced.

```text
P4_PREDICTED_CORE_CLAIMS: preserved
P4_OBSERVED_CORE_CLAIMS: preserved
P4_PREDICTED_AXIS_CLAIMS: withdrawn_as_unavailable
P4_OBSERVED_AXIS_CLAIMS: withdrawn_as_unavailable
P4_PREDICTED_AXIS_DEFAULT: none
P4_OBSERVED_AXIS_DEFAULT: none
P4_PREDICTED_RESULT_TYPE: exact_partition
P4_OBSERVED_RESULT_TYPE: exact_partition
P4_RESULT: exact_match
```

## 9. Reverse-prediction score / 역방향 예측 점수

| Variant | Precommitted directional result | Revealed result | Score |
|---|---|---|---|
| P2 | prerequisite-unsatisfied; Formation + Property | same | EXACT MATCH |
| P3 | identity changes; lineage succession; Formation + Dynamics | same | EXACT MATCH |
| P4 | core survives; axis claims unavailable; no zero default | same | EXACT MATCH |

```text
PREDICTION_CASES_SELECTED: 3
PREDICTION_CASES_SCORED: 3
PREDICTION_EXACT_MATCHES: 3
PREDICTION_PARTIAL_MATCHES: 0
PREDICTION_MISSES: 0
POST_REVEAL_PREDICTION_EDIT: none
POST_REVEAL_EXCEPTION_ADDED: none
REVERSE_PREDICTION_RESULT: exact_match_3_of_3
```

## 10. Challenge verdict / 도전 판정

All three selected variants matched the locked directional, status, and layer predictions.

The strongest checks were:

- prerequisite loss was not rewritten as ordinary undefinedness or Boolean false;
- inherited value change altered literal channel identity while succession remained lineage-based;
- realized-axis removal preserved general core data while withdrawing only specialization-dependent claims;
- no post-reveal prediction rewrite or exception was used.

Final classification:

```text
REVERSE-PREDICTION DISCIPLINE — PILOT PASS WITH LIMITATIONS
```

This does **not** establish empirical future prediction or independent predictive validity. The same session authored the perturbation templates, and the reveal consists of deterministic instantiations of those templates. What is directly tested here is commit-before-reveal rule consistency and resistance to post-hoc prediction editing.

## 11. Important refinement discovered / 발견된 정교화

Future challenge records should preserve:

```text
PREDICTION_LOCK_STATUS:
PREDICTION_LOCK_COMMIT:
PREDICTION_SELECTOR:
SELECTED_VARIANTS:
PREDICTION_CASES_SCORED:
PREDICTION_EXACT_MATCHES:
PREDICTION_PARTIAL_MATCHES:
PREDICTION_MISSES:
POST_REVEAL_PREDICTION_EDIT:
REVERSE_PREDICTION_RESULT: exact_match / partial_match / prediction_miss / indeterminate
```

For prediction challenges, a time-ordered precommit should be preferred over writing predictions and results together for the first time. The original precommit SHA should remain visible in the completed record.

## 12. Objectivity limits / 객관성 한계

- The same session authored P1-P4 perturbation templates.
- The SHA-256 selector constrains post-hoc variant choice but is not an independent case generator.
- The selected cases are manuscript-derived toy interface cases.
- No empirical outcome, unknown external data, or domain-expert holdout was used.

This is therefore **reverse-prediction procedure calibration**, not independent predictive validation.

## 13. Next strengthening step / 다음 강화 단계

1. Use a sealed case bank produced by an external person or independent generator.
2. Commit DSD structural predictions before the analyst can inspect outcomes.
3. Let a separate evaluator score exact, partial, miss, or indeterminate.
4. Preserve failed predictions together with their original precommit commits.
5. Proceed next to the **Minimal-Structure Challenge**.

## 14. Final record / 최종 기록

```text
ANALYSIS_RESULT: REVERSE_PREDICTION_DISCIPLINE_PILOT_PASS_WITH_LIMITATIONS
PREDICTION_LOCK_STATUS: locked_before_reveal
PREDICTION_LOCK_COMMIT: e40cdc74d873e56caca378921829e9913e69957c
PREDICTION_SELECTOR: sha256_chunk_mod4_unique3
SELECTOR_SHA256: 9ca70c75c81a608e2df1f9f116b7173b77b715903cec2b6ae75879c47a9efa8a
SELECTED_VARIANTS: P2,P3,P4
PREDICTION_CASES_SCORED: 3
PREDICTION_EXACT_MATCHES: 3
PREDICTION_PARTIAL_MATCHES: 0
PREDICTION_MISSES: 0
POST_REVEAL_PREDICTION_EDIT: none
POST_REVEAL_EXCEPTION_ADDED: none
REVERSE_PREDICTION_RESULT: exact_match_3_of_3
ANALYTICAL_GAIN: limited_procedural_calibration_gain
BLINDING_LEVEL: same-session commit-before-reveal / not independent blind
FAILURES_OR_LIMITS: same-session templates, deterministic selector not independent, toy interface cases, no empirical holdout
NEXT_STRENGTHENING_STEP: externally-sealed reverse-prediction benchmark
```
