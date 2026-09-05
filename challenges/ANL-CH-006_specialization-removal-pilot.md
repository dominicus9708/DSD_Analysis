# ANL-CH-006 — Specialization-Removal Challenge (Pilot)

Date: **2026-09-05**
Status: **SPECIALIZATION_REMOVAL_DISCIPLINE_PILOT_PASS_WITH_LIMITATIONS**

## 1. Purpose / 목적

Test whether DSD Analysis removes only conclusions that actually depend on an optional specialization while preserving conclusions supported by predecessor/core interfaces.

The challenge also tests that removal of an optional interface is **not** converted into a numerical default such as rank `0`, a zero vector, or an empty geometric object.

This is a **self-generated pilot**, not an independent blind validation.

## 2. Source lock / 소스 잠금

```text
CHALLENGE_ID: ANL-CH-006
DATE: 2026-09-05
DSD_INTERFACE_PROFILE_DATE: 2026-09-05
SOURCE_VERSIONS:
  Property Axiom System — 2026-09-01
  Channel-Indexed Static Aggregation — 2026-09-02
  Structural Reorganization Dynamics — supplied current manuscript
SPECIALIZATION_UNDER_TEST: realized-axis specialization
REMOVAL_OPERATOR: delete G while preserving independently supplied predecessor/core data
```

The current source interface states that realized-axis lines, rank, bilinear forms, orthogonality, normals, and related geometric data are specialization-level coordinates rather than universal Property coordinates. General Dynamics likewise allows a model without a realized-axis specialization, and no realized-axis rank is assigned when the specialization is absent. Static Aggregation does not require realized-axis data for its definition.

## 3. Precommitted criteria / 사전 판정 기준

1. **Core survival** — conclusions supported independently by Formation, general Property, or general Dynamics must survive specialization removal unchanged.
2. **Specialization withdrawal** — conclusions using axis lines, rank, orthogonality, normals, or other specialization data must be withdrawn after removal.
3. **No default substitution** — absence of the specialization must not be replaced by rank `0`, a zero vector, or another fake default.
4. **No feedback** — removing realized-axis data alone must not alter general property status or formation data unless an explicit law connects them.
5. **No leakage** — removed geometric information must not be silently reused under a different core/property label.

Vocabulary:

```text
SPECIALIZATION_REMOVAL_RESULT:
  exact_partition
  over_retained
  over_deleted
  indeterminate
```

## 4. Case S1 — Static Property Core + optional realized-axis geometry

Fix a Stage-VI formation background and one general property kind `varpi` with typed input `x`:

```text
Ap_varpi = {x}
Sat_varpi,d = {x}
Dom(Xi_varpi) = {x}
Xi_varpi(x) = 7
```

Therefore `x` is applicable, prerequisite-satisfied, and defined nonzero.

Add a separate realized-axis specialization `G`:

```text
l1 = span(e1)
l2 = span(e2)
comparison carrier = R^2
arank_G = 2
<e1,e2> = 0
```

Pre-removal claims:

```text
CORE CLAIM C1: x is applicable + prerequisite-satisfied + defined nonzero with value 7
SPECIALIZATION CLAIM S1: realized-axis rank = 2
SPECIALIZATION CLAIM S2: supplied realized lines are orthogonal
```

### Remove realized-axis specialization

Delete only `G`.

Result:

- `C1` survives unchanged.
- `S1` and `S2` become unavailable/unsupported in the stripped model.
- No `arank = 0` default is introduced.
- Property value `7` and its status are not changed.

```text
CASE_RESULT: exact_partition
```

## 5. Case S2 — Property Dynamics + optional realized-axis geometry

Use a fixed applicable and prerequisite-satisfied property domain and explicitly supply the time-indexed assignment

```text
Xi_t,varpi(x) = 1 + t,  t in [0,1]
```

so that

```text
t=0: Xi_0,varpi(x) = 1
t=1: Xi_1,varpi(x) = 2
status: defined nonzero throughout
```

Separately supply a realized-axis specialization `G_t` whose two realized lines remain `span(e1)` and `span(e2)` with rank `2` throughout the interval.

Pre-removal claims:

```text
CORE/DYNAMIC CLAIM C2: property value evolves from 1 to 2 under the supplied law
CORE/DYNAMIC CLAIM C3: defined-nonzero status is preserved on [0,1]
SPECIALIZATION CLAIM S3: realized-axis rank is 2 on [0,1]
```

### Remove realized-axis specialization

Delete only `G_t`.

Result:

- `C2` and `C3` survive unchanged.
- `S3` becomes unavailable after removal.
- The model remains a general property-dynamical model without a realized-axis rank.
- Missing realized-axis data are omitted rather than zero-filled.
- No property-status change is inferred from removal of rank data.

```text
CASE_RESULT: exact_partition
```

## 6. Results / 결과

| Case | Independent claims | Specialization-dependent claims | After removal | Result |
|---|---|---|---|---|
| S1 | property status/value `7` | rank `2`, orthogonality | core survives; geometry withdrawn | EXACT PARTITION |
| S2 | property evolution `1 -> 2`, defined status | rank `2` through time | dynamic core survives; rank withdrawn | EXACT PARTITION |

```text
CORE_CLAIMS_EXPECTED_TO_SURVIVE: 3
CORE_CLAIMS_SURVIVED: 3
SPECIALIZATION_CLAIMS_EXPECTED_TO_WITHDRAW: 3
SPECIALIZATION_CLAIMS_WITHDRAWN: 3
OVER_RETAINED: 0
OVER_DELETED: 0
DEFAULT_SUBSTITUTION_INTRODUCED: no
```

## 7. Challenge verdict / 도전 판정

Both cases partitioned claims correctly.

The analysis did not delete general Property/Dynamics conclusions merely because realized-axis geometry was removed, and it did not retain rank or orthogonality as though they were universal core coordinates.

Final classification:

```text
SPECIALIZATION REMOVAL DISCIPLINE — PILOT PASS WITH LIMITATIONS
```

## 8. Important refinement discovered / 발견된 정교화

Future challenge records should preserve:

```text
SPECIALIZATION_UNDER_TEST:
SPECIALIZATION_DEPENDENT_CLAIMS:
SPECIALIZATION_INDEPENDENT_CLAIMS:
POST_REMOVAL_WITHDRAWN_CLAIMS:
POST_REMOVAL_SURVIVING_CLAIMS:
SPECIALIZATION_REMOVAL_RESULT: exact_partition / over_retained / over_deleted / indeterminate
DEFAULT_SUBSTITUTION_INTRODUCED:
```

A key distinction is:

```text
claim becomes unsupported after specialization removal
!=
claim becomes false
```

If realized-axis data are no longer supplied, rank is not automatically `0`; it is unavailable/not supplied in the stripped model.

## 9. Objectivity limits / 객관성 한계

- The same session designed the cases and the expected claim partition.
- The source manuscripts explicitly mark realized-axis geometry as optional, so the expected result is comparatively transparent.
- No independent analyst or hidden specialization label was used.
- Only realized-axis removal was tested in this pilot.

This is therefore an internal calibration against specialization leakage and over-deletion, not independent validation of DSD as a whole.

## 10. Next strengthening step / 다음 강화 단계

1. Prepare external cases with the specialization identity hidden.
2. Keep a separate evaluator answer key for core versus specialization-dependent claims.
3. Remove the specialization and ask a blinded analyst to classify surviving and withdrawn claims.
4. Extend the same test to optional application bridges, local-scaling readouts, and other non-core specializations.
5. Proceed next to the **Competing-Explanation Challenge**, where DSD and non-DSD explanations are compared under the same precommitted criteria.

## 11. Final record / 최종 기록

```text
ANALYSIS_RESULT: SPECIALIZATION_REMOVAL_DISCIPLINE_PILOT_PASS_WITH_LIMITATIONS
SPECIALIZATION_UNDER_TEST: realized_axis
SPECIALIZATION_INDEPENDENT_CLAIMS: 3
SPECIALIZATION_DEPENDENT_CLAIMS: 3
POST_REMOVAL_SURVIVING_CLAIMS: 3_of_3
POST_REMOVAL_WITHDRAWN_CLAIMS: 3_of_3
SPECIALIZATION_REMOVAL_RESULT: exact_partition
DEFAULT_SUBSTITUTION_INTRODUCED: no
UNNECESSARY_LAYER_INTRODUCED: none
MISSING_REQUIRED_LAYER: none
CORRESPONDENCE_RESULT: not_primary
ANALYTICAL_GAIN: limited_calibration_gain
BLINDING_LEVEL: self-generated pilot / not independent blind
FAILURES_OR_LIMITS: manuscript-explicit optionality, toy cases, no independent analyst, only realized-axis tested
NEXT_STRENGTHENING_STEP: blinded mixed-specialization removal benchmark
```
