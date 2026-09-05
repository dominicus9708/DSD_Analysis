# ANL-CH-005 — Layer-Restraint Challenge (Pilot)

Date: **2026-09-05**
Status: **LAYER_RESTRAINT_RECOGNIZED_PILOT_PASS_WITH_LIMITATIONS**

## 1. Purpose / 목적

Test whether DSD Analysis selects only the **minimum sufficient interface set** required by each case, instead of treating

```text
Formation -> Property -> Static -> Dynamics
```

as a mandatory serial chain for every problem.

This is a **self-generated pilot**, not an independent blind validation.

## 2. Source lock / 소스 잠금

```text
CHALLENGE_ID: ANL-CH-005
DATE: 2026-09-05
DSD_INTERFACE_PROFILE_DATE: 2026-09-05
SOURCE_VERSIONS:
  Formation Axiom System — supplied current manuscript
  Property Axiom System — 2026-09-01
  Channel-Indexed Static Aggregation — 2026-09-02
  Structural Reorganization Dynamics — supplied current manuscript
INTERFACE_SELECTION_MODE: casewise_minimal
REALIZED_AXIS_SPECIALIZATION: not supplied in all cases
```

The source manuscripts separate the layers as follows:

- Formation supplies Stage-VI admitted operational channels and relative Clause-VII finite composition.
- Property is a static typed applicability/prerequisite/partial-assignment layer over a fixed Stage-VI background.
- Static Aggregation is a separate analytic realization and aggregation interface.
- Dynamics introduces component-resolved time-indexed state, transition, and lineage, while Property, Static, and realized-axis data remain optional unless required by the chosen model.

## 3. Precommitted criteria / 사전 판정 기준

1. **Exact selection** — selected layers must equal the minimum sufficient layer set.
2. **No upward drag** — do not add Property, Static, Dynamics, or specialization merely because those layers exist.
3. **No prefix-chain assumption** — using Dynamics does not automatically require Property and Static first.
4. **No underfit** — do not force property status, analytic realization, or temporal lineage questions into Formation when their defining data live downstream.
5. **Declared-layer discipline** — record only layers actually used by the analysis.

Vocabulary:

```text
LAYER_SELECTION_RESULT:
  exact_match
  over_specified
  under_specified
  indeterminate
```

## 4. Case L1 — Formation only

Take three candidate channels, with `c1` and `c3` admitted at Stage VI and `c2` absent.

```text
T(c1) = 4
c2 = absent; T(c2) is not defined by the core
T(c3) = 0; c3 is admitted
F = {c1, c3}
Comp(F) = 4
```

The case only asks which channels contribute and what the finite composition is.
The admitted zero-bearing `c3` must remain distinct from absent `c2`.

```text
MINIMUM_SUFFICIENT_LAYER_SET: {Formation}
SELECTED_LAYER_SET: {Formation}
LAYER_SELECTION_RESULT: exact_match
```

Property, analytic realization, and time evolution are unnecessary.

## 5. Case L2 — Property Core required

Fix the Stage-VI formation background and declare one property kind `varpi` over four typed inputs.

```text
Ap_varpi = {x1, x2, x4}
Sat_varpi,d = {x1, x3, x4}
Dom(Xi_varpi) = {x1}
Xi_varpi(x1) = 7
```

The resulting distinctions are:

```text
x1: applicable + prerequisite-satisfied + defined nonzero
x2: applicable but prerequisite-unsatisfied
x3: inapplicable
x4: applicable + prerequisite-satisfied but undefined
```

Formation does not determine these property-specific applicability, prerequisite, and assignment-status coordinates.

```text
MINIMUM_SUFFICIENT_LAYER_SET: {Formation background, Property Core}
SELECTED_LAYER_SET: {Formation background, Property Core}
LAYER_SELECTION_RESULT: exact_match
```

Static Aggregation and Dynamics are unnecessary.

## 6. Case L3 — Static Aggregation required

Two channels are already admitted. The task is to derive their component terms from supplied analytic realization data.
Use scalar Banach space `W = R`, a two-point counting-measure space, and normalized weights.

```text
c1:
  zeta = (2, 6)
  w = (1/2, 1/2)
  T^R(c1) = 2*(1/2) + 6*(1/2) = 4

c2:
  zeta = (1, 3)
  w = (1/2, 1/2)
  T^R(c2) = 1*(1/2) + 3*(1/2) = 2

Comp^R({c1,c2}) = 6
```

Formation can compose a **supplied** term map, but the task here explicitly requires deriving that term from measure/field/weight realization data. Therefore the analytic Static layer is required.

```text
MINIMUM_SUFFICIENT_LAYER_SET: {Formation background, Static Aggregation}
SELECTED_LAYER_SET: {Formation background, Static Aggregation}
LAYER_SELECTION_RESULT: exact_match
```

No Property model or Dynamics is required.

## 7. Case L4 — Dynamics required without Property or Static

At two times, take

```text
t0: c0 = (p, a, lambda, 1, rho)
t1: c1 = (p, a, lambda, 2, rho)
Lambda_{0,1} = {(c0,c1)}
```

The assigned value `v` is part of Formation channel identity, so `c0 != c1`.
Formation can establish that they are distinct inherited objects, but it does not by itself determine **temporal succession**.
The supplied cross-time lineage relation is therefore a Dynamics-layer datum.

```text
MINIMUM_SUFFICIENT_LAYER_SET: {Formation background, Dynamics}
SELECTED_LAYER_SET: {Formation background, Dynamics}
LAYER_SELECTION_RESULT: exact_match
```

Adding Property, Static Aggregation, or realized-axis geometry merely because Dynamics is used would be over-specification.

## 8. Results / 결과

| Case | Minimum sufficient layers | Selected layers | Result |
|---|---|---|---|
| L1 | Formation | Formation | EXACT MATCH |
| L2 | Formation + Property | Formation + Property | EXACT MATCH |
| L3 | Formation + Static | Formation + Static | EXACT MATCH |
| L4 | Formation + Dynamics | Formation + Dynamics | EXACT MATCH |

```text
EXACT_SELECTION: 4/4
OVER_SPECIFICATION: 0/4
UNDER_SPECIFICATION: 0/4
```

## 9. Challenge verdict / 도전 판정

All four cases selected the minimum sufficient layer set exactly.
The strongest restraint checks were:

- L3 did **not** insert Property as a compulsory intermediate layer before Static analytic realization.
- L4 did **not** turn the optional downstream interfaces into a mandatory prefix chain before Dynamics.

Final classification:

```text
LAYER RESTRAINT RECOGNIZED — PILOT PASS WITH LIMITATIONS
```

## 10. Important refinement discovered / 발견된 정교화

Future challenge records should preserve:

```text
MINIMUM_SUFFICIENT_LAYER_SET:
SELECTED_LAYER_SET:
LAYER_SELECTION_RESULT: exact_match / over_specified / under_specified / indeterminate
UNNECESSARY_LAYER_INTRODUCED:
MISSING_REQUIRED_LAYER:
```

The current DSD architecture is more accurately treated as a **fixed Formation background with selectively activated downstream branches**, not as one compulsory serial ladder.

## 11. Objectivity limits / 객관성 한계

- The same session designed the cases and selected their minimum sufficient layers.
- The cases were intentionally derived from explicit interface boundaries in the current manuscripts.
- No independent layer selector or external-domain blind benchmark was used.
- This is an internal calibration against interface overuse, not strong independent validation.

## 12. Next strengthening step / 다음 강화 단계

1. Present external cases without layer labels.
2. Keep the minimum-layer answer key with a separate evaluator.
3. Ask the analyst to select only the necessary combination among Formation, Property, Static, and Dynamics.
4. Score over-specification and under-specification separately.
5. Test realized-axis and other optional specializations separately in the next **Specialization-Removal Challenge**.

## 13. Final record / 최종 기록

```text
ANALYSIS_RESULT: LAYER_RESTRAINT_RECOGNIZED_PILOT_PASS_WITH_LIMITATIONS
MINIMUM_SUFFICIENT_LAYER_SET: casewise
SELECTED_LAYER_SET: casewise_exact
LAYER_SELECTION_RESULT: exact_match_4_of_4
UNNECESSARY_LAYER_INTRODUCED: none
MISSING_REQUIRED_LAYER: none
CORRESPONDENCE_RESULT: not_primary
BASELINE_SUFFICIENCY: not_primary
ANALYTICAL_GAIN: not_primary
BLINDING_LEVEL: self-generated pilot / not independent blind
FAILURES_OR_LIMITS: manuscript-derived toy cases, no independent layer selector, no external-domain cases
NEXT_STRENGTHENING_STEP: blinded external mixed-layer benchmark
```
