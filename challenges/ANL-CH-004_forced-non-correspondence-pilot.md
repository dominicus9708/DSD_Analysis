# ANL-CH-004 — Forced Non-Correspondence Challenge (Pilot)

Date: **2026-09-05**
Status: **NON_CORRESPONDENCE_RECOGNIZED_PILOT_PASS_WITH_LIMITATIONS**

## 1. Purpose / 목적

Test whether DSD Analysis can explicitly return **non-correspondence** when the selected DSD interface fails to preserve the target's essential structure, instead of rescuing the mapping through post-hoc encoding and retroactively calling it `direct` or `partial`.

This is a **self-generated pilot**, not an independent blind validation.

## 2. Interface lock / 인터페이스 잠금

```text
CHALLENGE_ID: ANL-CH-004
DATE: 2026-09-05
DSD_INTERFACE_PROFILE_DATE: 2026-09-05
FORMATION_LAYER: used
PROPERTY_CORE: not used
STATIC_AGGREGATION_LAYER: not used
DYNAMICS_LAYER: not used
REALIZED_AXIS_SPECIALIZATION: not supplied
OTHER_SPECIALIZATION: none
```

The challenge uses only direct Formation Clause-VII finite composition.
Under the current Formation interface, a core channel family is an unordered finite set without repetition and its composite is the vector sum of supplied component terms.

## 3. External target and essential structure / 외부 대상과 핵심 구조

Target: ordered length-2 sequences over symbols `A` and `B`, evaluated by native concatenation.

```text
Case J: (A, B) -> AB
Case K: (B, A) -> BA
```

In the native system:

```text
AB != BA
```

Therefore **order** is the essential structure that any meaningful correspondence must preserve.

## 4. Precommitted directness constraints / 직접 대응의 사전 제약

A mapping counts as `direct` only if:

1. the same native component maps to the same DSD channel/term independent of sequence position or surrounding context: `A -> c_A`, `B -> c_B`;
2. position is not silently inserted into configuration, role, assigned value, or term-space basis;
3. no ordered Property profile, selector, bridge, or downstream representation is added;
4. incidental preservation of the symbol set is not sufficient for `partial` if the essential order structure is lost.

## 5. Formation-only direct mapping attempt / Formation-only 직접 대응 시도

Under the componentwise direct map, both cases yield the same finite admitted family:

```text
F_J = {c_A, c_B}
F_K = {c_A, c_B}
```

Clause-VII composition gives:

```text
Comp(F_J) = T(c_A) + T(c_B)
Comp(F_K) = T(c_B) + T(c_A)
          = T(c_A) + T(c_B)
```

Hence:

```text
Comp(F_J) = Comp(F_K)
```

while the native target requires `AB != BA`.

The direct Formation-only map therefore fails to preserve the essential structure.

## 6. Why this is not recorded as partial correspondence / 왜 partial이 아닌가

The two cases do share the same unordered symbol support `{A,B}`.
However, the target problem is **ordered concatenation**, and order is exactly what distinguishes the cases.

Preserving only the incidental carrier elements while losing the target's defining relation does not count as meaningful partial correspondence in this challenge.

Therefore:

```text
CORRESPONDENCE_RESULT: non_correspondence
ESSENTIAL_STRUCTURE_PRESERVED: no
```

## 7. Available escapes and their status / 가능한 우회와 그 지위

This result does **not** claim that DSD as a whole cannot represent order.
Order can be supplied by additional structure, for example:

- encode `A@1`, `B@2` into channel identity or a position-indexed term representation;
- use the General Property layer with an ordered typed input profile such as `(first, second)`;
- use a separate downstream representation or bridge that preserves sequence position.

These are legitimate extensions, but they add structure that is absent from the locked Formation-only componentwise direct map.
They are therefore recorded as **encoded extensions**, not retroactively reclassified as direct correspondence.

## 8. Results / 결과

| Item | Result | Interpretation |
|---|---|---|
| Essential structure | ORDER | sequence order distinguishes J/K |
| Essential structure preserved | NO | unordered finite family plus vector sum identifies J/K |
| Direct correspondence | NON-CORRESPONDENCE | Formation-only componentwise mapping cannot preserve order |
| Partial correspondence | REJECTED | support similarity does not preserve the target's essential relation |
| Encoded extension | POSSIBLE | explicit position encoding or ordered Property data can represent order |
| Baseline sufficiency | SUFFICIENT | native sequence/concatenation formalism already represents the task |
| Analytical gain | NONE | DSD adds no target-level problem-solving value here |

## 9. Challenge verdict / 도전 판정

The pass condition is not "find some DSD encoding."
It is to **refuse a correspondence claim when the locked interface does not preserve the essential target structure**.

If position had been inserted after seeing the failure and the resulting enriched mapping were then labeled as the original `direct correspondence`, the challenge would have failed.

Final classification:

```text
NON-CORRESPONDENCE RECOGNIZED — PILOT PASS WITH LIMITATIONS
```

## 10. Important refinement discovered / 발견된 정교화

Future challenge records should preserve:

```text
ESSENTIAL_STRUCTURE:
ESSENTIAL_STRUCTURE_PRESERVED: yes / partial / no
ENCODED_EXTENSION_RESULT: not_needed / possible / required / unavailable
```

`partial correspondence` should be used only when some **essential target structure** is genuinely preserved, not merely because a few surface elements can be aligned.

## 11. Objectivity limits / 객관성 한계

- The same session designed and analyzed the case.
- The obstruction is intentionally sharp: unordered finite-sum composition versus ordered concatenation.
- There is no independent analyst or pre-registration.
- The non-correspondence result is scoped to the precommitted componentwise Formation-only direct interface; it is not a claim of universal DSD inexpressibility.

## 12. Next strengthening step / 다음 강화 단계

1. Collect real external-domain cases whose native structures conflict with a selected DSD interface.
2. Pre-register `direct / partial / encoded / non-correspondence` criteria before case disclosure.
3. Build a mixed benchmark containing cases from all four correspondence classes.
4. Blind the analyst to the intended class.

## 13. Final record / 최종 기록

```text
ANALYSIS_RESULT: NON_CORRESPONDENCE_RECOGNIZED_PILOT_PASS_WITH_LIMITATIONS
CORRESPONDENCE_RESULT: non_correspondence
ESSENTIAL_STRUCTURE: ordered_sequence
ESSENTIAL_STRUCTURE_PRESERVED: no
ENCODED_EXTENSION_RESULT: possible_but_not_counted_as_direct
BASELINE_SUFFICIENCY: sufficient
ANALYTICAL_GAIN: none
INVARIANCE_RESULT: not_primary
EQUIVARIANCE_RESULT: not_primary
DISCRIMINATION_RESULT: fail_for_direct_formation_mapping_as_expected
BLINDING_LEVEL: self-generated pilot / not independent blind
FAILURES_OR_LIMITS: intentionally sharp toy obstruction, componentwise-directness scope, no independent analyst
NEXT_STRENGTHENING_STEP: blinded mixed benchmark of direct/partial/encoded/non-correspondence cases
```
