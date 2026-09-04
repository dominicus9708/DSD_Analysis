# ANL-CH-001 — Blind + Twin Challenge (Pilot)

Date: **2026-09-05**
Status: **PILOT_PASS_WITH_LIMITATIONS**

## 1. Purpose / 목적

Test two properties of DSD Analysis:

1. **Invariance** — structurally identical cases should remain analytically identical under nonessential relabeling or wrapper changes.
2. **Discrimination** — a materially different formation structure should be distinguished even when the surface wording is similar.

This is a **self-generated pilot**, not an independent blind validation.
The same session designed and analyzed the cases.

## 2. Interface lock / 인터페이스 잠금

```text
CHALLENGE_ID: ANL-CH-001
DATE: 2026-09-05
DSD_INTERFACE_PROFILE_DATE: 2026-09-05
FORMATION_LAYER: used
PROPERTY_CORE: not used
STATIC_AGGREGATION_LAYER: not used
DYNAMICS_LAYER: not used
REALIZED_AXIS_SPECIALIZATION: not supplied
OTHER_SPECIALIZATION: none
```

The pilot intentionally uses only the Formation layer.
This also acts as a small **layer-restraint check**: no Property or Dynamics machinery is introduced when it is unnecessary.

## 3. Precommitted criteria / 사전 판정 기준

1. **Invariance criterion** — A and B must have the same admitted-channel pattern and same finite composition when they differ only by nonessential relabeling.
2. **Discrimination criterion** — C and D must differ when the third input is formally admitted in C but not in D.
3. **Status criterion** — an informal or non-admitted expression must not be converted into a defined-zero channel or a zero-valued admitted channel.
4. **Scope criterion** — the challenge evaluates procedural structure only; it does not decide the moral, political, or policy value of the content wrapper.

## 4. Case A — wrapper 1

- Actors: `A1`, `A2`, `A3`.
- `A1` submits `+1` through the recognized formal path.
- `A2` submits `-1` through the recognized formal path.
- `A3` expresses `-1` informally but makes no recognized formal submission.
- Only formal submissions become operational inputs.
- Supplied post-Stage-VI term data: `T(c1)=+1`, `T(c2)=-1`.

### DSD analysis

```text
admitted support = {c1, c2}
A3 informal expression ≠ admitted -1 channel
A3 informal expression ≠ zero channel
Comp({c1,c2}) = 0
```

## 5. Case B — wrapper 2

Names and surface vocabulary are changed to `B1`, `B2`, `B3`, `retain/remove`, but the formal structure is preserved.

- `B1`: formal `+1`
- `B2`: formal `-1`
- `B3`: informal `-1` expression only
- Same admission rule and term structure as A.

### DSD analysis

```text
admitted support = {d1, d2}
B3 informal expression is not promoted to an admitted channel
Comp({d1,d2}) = 0
```

### A/B comparison

Under the relabeling `c1 -> d1`, `c2 -> d2`, with all relevant structure preserved, A and B have the same formation pattern at the selected resolution.

**Result:** nonessential relabeling did not change the analysis.

## 6. Case C — formal third input

Same base structure as A, except `A3` formally submits `-1` through the recognized path before the cutoff.

Supplied term data: `T(c3)=-1`.

### DSD analysis

```text
admitted support = {c1, c2, c3}
Comp({c1,c2,c3}) = -1
```

## 7. Case D — informal third expression

The surface summary can still say that `A3 expressed opposition`, but the actual record contains only an informal expression and no recognized formal submission.

### DSD analysis

```text
admitted support = {c1, c2}
Comp({c1,c2}) = 0
```

### C/D comparison

C and D are surface-similar but differ in **formation admission**.
They must therefore not be treated as the same structural case.

## 8. Results / 결과

| Item | Result | Interpretation |
|---|---|---|
| Invariance | PASS (pilot) | A/B remained analytically invariant under nonessential relabeling |
| Discrimination | PASS (pilot) | C/D formal-admission difference changed support and composition |
| Status discipline | PASS | non-admitted expression was not collapsed into zero |
| Layer restraint | PASS | Formation alone was sufficient |
| Analytical gain | LIMITED | the structural distinction is clear, but the toy rule is also expressible directly by ordinary formal-submission rules |

## 9. Objectivity limits / 객관성 한계

This result is **not** counted as strong blind validation because:

- the same analyst/session generated and analyzed the cases;
- the cases were intentionally constructed around Formation admission/absence distinctions;
- no independent external baseline or independent analyst was used;
- the sample is tiny and purely toy-level.

Therefore the final classification is:

```text
ANALYSIS_RESULT: PILOT_PASS_WITH_LIMITATIONS
INVARIANCE_RESULT: PASS
DISCRIMINATION_RESULT: PASS
ANALYTICAL_GAIN: limited
BLINDING_LEVEL: self-generated pilot / not independent blind
FAILURES_OR_LIMITS: no independent generator, no independent analyst, no external baseline, toy cases
NEXT_STRENGTHENING_STEP: independent blinded case generation and precommitted analysis
```

## 10. Next strengthening step / 다음 강화 단계

1. Separate case generation from analysis.
2. Freeze the interface and verdict rules before the analyst sees the cases.
3. Hide case names, evaluative framing, and expected labels.
4. Generate both isomorphic permutations and one-feature structural perturbations automatically.
5. Compare DSD output with an external-domain baseline rather than only with itself.
