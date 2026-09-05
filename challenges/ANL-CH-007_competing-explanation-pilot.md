# ANL-CH-007 — Competing-Explanation Challenge (Pilot)

Date: **2026-09-06**
Status: **COMPETING_EXPLANATION_DISCIPLINE_PILOT_PASS_WITH_LIMITATIONS**

## 1. Purpose / 목적

Test whether DSD Analysis competes against the **strongest reasonable task-matched external baseline** rather than an intentionally weak strawman, and whether it can preserve a result in which DSD loses or ties.

This is a **self-generated pilot**, not an independent blind validation.

## 2. Source lock / 소스 잠금

```text
CHALLENGE_ID: ANL-CH-007
DATE: 2026-09-06
DSD_INTERFACE_PROFILE_DATE: 2026-09-05
SOURCE_VERSIONS:
  Formation Axiom System — supplied current manuscript
  Structural Reorganization Dynamics — supplied current manuscript
COMPETITION_MODE: strongest_reasonable_task_matched_baseline
```

The current Formation source distinguishes channel absence from admitted zero-bearing channels and permits distinct finite channel families to share one composite. The current Dynamics source separates literal identity, aggregate equality, and explicitly supplied cross-time lineage.

## 3. Precommitted criteria / 사전 판정 기준

1. **Same target** — DSD and competitor must answer the same questions from the same supplied data.
2. **Strong competitor** — the competitor may preserve all native structure reasonably required by the task; it is not frozen at an artificially lossy scalar-only baseline.
3. **No strawman** — beating only a weak baseline and then claiming DSD superiority is a failure.
4. **Target fit first** — compare correctness and preservation of essential task structure before discussing preference.
5. **Parsimony second** — if target fit is tied and neither side adds new discrimination or prediction, a method requiring less task-local machinery may be preferred for that case.
6. **No globalization** — a case-level result is not generalized into universal superiority or inferiority of DSD or the external method.

Vocabulary:

```text
COMPETITIVE_RESULT:
  dsd_preferred
  baseline_preferred
  tie
  indeterminate
```

## 4. Case C1 — Static support/zero distinction

Compare two states:

```text
State A:
  u = +1
  v = -1
  w = absent

State B:
  u = +1
  v = -1
  w = admitted and value/term = 0
```

Questions:

1. What is the total?
2. Is the third contribution `w` actually present in support?

### DSD explanation

```text
F_A = {c_u, c_v}
F_B = {c_u, c_v, c_w}
T(c_u)=+1
T(c_v)=-1
T(c_w)=0
Comp(F_A)=0
Comp(F_B)=0
```

DSD preserves the distinction between an absent third channel and an admitted zero-bearing channel despite identical aggregates.

### Weak external baseline

A scalar total alone maps both states to `0` and cannot answer Question 2.

Using only this baseline would be a strawman comparison.

### Strongest reasonable external baseline

Use an ordinary **tagged finite partial map plus ordinary sum**:

```text
A = {u: +1, v: -1}
B = {u: +1, v: -1, w: 0}
Total(A)=0
Total(B)=0
```

Key membership preserves absence versus present-zero, while ordinary summation answers the total.

Therefore the strong baseline and DSD are tied on target fit and essential-structure preservation. For this toy task alone, the tagged partial map requires less task-local machinery and DSD adds no further discrimination or prediction.

```text
CASE_RESULT: baseline_preferred
REASON: fit_tie_plus_task_local_parsimony
```

## 5. Case C2 — Cross-time identity versus succession

Supply two time-indexed records and one successor edge:

```text
t0: node a, payload 1
t1: node b, payload 2
successor relation: a -> b
```

Questions:

1. Are `a` and `b` literally the same object?
2. Does a successor relation exist?

### DSD explanation

DSD keeps formation-level identity distinct and records succession through a separate lineage relation:

```text
a != b
(a,b) in Lambda_{0,1}
```

### Strongest reasonable external baseline

Use an ordinary **directed state-transition graph**:

```text
vertices = {a,b}
payload(a)=1
payload(b)=2
edge = {(a,b)}
```

This baseline also separates literal node identity from successor relation completely.

Target fit is therefore tied, and there is no DSD-only prediction or distinction in this toy task.

```text
CASE_RESULT: baseline_preferred
REASON: fit_tie_plus_task_local_parsimony
```

## 6. Results / 결과

| Case | DSD target fit | Strong baseline target fit | Novel DSD discrimination | Competitive result |
|---|---|---|---|---|
| C1 | FULL | FULL | NONE beyond tagged-support baseline | BASELINE PREFERRED |
| C2 | FULL | FULL | NONE beyond transition-graph baseline | BASELINE PREFERRED |

```text
DSD_FULL_FIT: 2/2
STRONG_BASELINE_FULL_FIT: 2/2
STRAW_MAN_BASELINE_AVOIDED: yes
DSD_PREFERRED: 0/2
BASELINE_PREFERRED: 2/2
TIE: 0/2
ANALYTICAL_GAIN_OVER_STRONGEST_BASELINE: none
```

## 7. Challenge verdict / 도전 판정

The pass condition is **not that DSD wins**.
The pass condition is that the strongest reasonable competitor is allowed to remove an apparent DSD advantage and that the resulting loss or tie is recorded without rescue.

In C1, DSD beats a scalar-only baseline, but that advantage disappears once the competitor is upgraded to a tagged partial map. In C2, an ordinary state-transition graph already preserves identity versus succession.

For both toy cases, the external baseline is therefore preferred at the task level.

Final classification:

```text
COMPETING-EXPLANATION DISCIPLINE — PILOT PASS WITH LIMITATIONS
```

## 8. Important refinement discovered / 발견된 정교화

Future challenge records should preserve:

```text
COMPETING_EXPLANATIONS:
STRONGEST_REASONABLE_BASELINE:
TARGET_FIT_RESULT:
PARISMONY_RESULT:
NOVEL_DISCRIMINATION_RESULT:
STRAW_MAN_BASELINE_AVOIDED:
COMPETITIVE_RESULT: dsd_preferred / baseline_preferred / tie / indeterminate
```

`ANALYTICAL_GAIN` should, when possible, be evaluated relative to the **strongest reasonable baseline**, not merely relative to the weakest available comparator.

## 9. Interpretation limits / 해석상 주의

- `baseline_preferred` is a method preference for the tested toy task; it is not non-correspondence and does not show that DSD is false.
- A proposed DSD advantage in cross-domain reuse or shared vocabulary requires a separate cross-domain benchmark.
- External baselines must likewise pay for repeated ad hoc machinery if future tasks require it; that cost was not measured here.
- No claim about long-run framework complexity, empirical prediction, or computational complexity is made by this pilot.

## 10. Objectivity limits / 객관성 한계

- The same session designed the cases, strong baselines, and evaluation criteria.
- The baselines are toy formalisms rather than independently selected domain-standard methods.
- No empirical prediction, computational-complexity comparison, or cross-domain reuse benchmark was performed.
- This is therefore an internal calibration against DSD-first preference and strawman-baseline selection.

## 11. Next strengthening step / 다음 강화 단계

1. Lock real domain-standard external methods before DSD analysis begins.
2. Use separate blinded analysts for DSD and baseline analyses.
3. Pre-register target fit, assumptions, complexity, and new discrimination criteria.
4. Mix cases where the intended outcome is DSD-preferred, tied, baseline-preferred, or indeterminate.
5. Proceed next to the **Unseen-Problem Transfer Challenge**.

## 12. Final record / 최종 기록

```text
ANALYSIS_RESULT: COMPETING_EXPLANATION_DISCIPLINE_PILOT_PASS_WITH_LIMITATIONS
COMPETING_EXPLANATIONS: DSD_vs_task_matched_external_baselines
STRONGEST_REASONABLE_BASELINE: tagged_partial_map_and_directed_transition_graph
TARGET_FIT_RESULT: tie_2_of_2
PARISMONY_RESULT: baseline_preferred_2_of_2
NOVEL_DISCRIMINATION_RESULT: none_over_strongest_baseline
STRAW_MAN_BASELINE_AVOIDED: yes
COMPETITIVE_RESULT: baseline_preferred_2_of_2
ANALYTICAL_GAIN: none
CORRESPONDENCE_RESULT: direct_but_not_uniquely_advantageous
BASELINE_SUFFICIENCY: sufficient
BLINDING_LEVEL: self-generated pilot / not independent blind
FAILURES_OR_LIMITS: toy baselines, no independent analyst, no empirical prediction or cross-domain reuse comparison
NEXT_STRENGTHENING_STEP: blinded external-domain mixed-winner benchmark
```
