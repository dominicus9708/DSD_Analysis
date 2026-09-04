# ANL-CH-002 — Symmetric-Case Challenge (Pilot)

Date: **2026-09-05**
Status: **PILOT_PASS_WITH_LIMITATIONS**

## 1. Purpose / 목적

Test whether DSD Analysis treats sign, orientation, and evaluative direction symmetrically rather than implicitly privileging `+` over `-` or one semantic wrapper over its mirror.

This is a **self-generated pilot**, not an independent blind validation.

## 2. Interface lock / 인터페이스 잠금

```text
CHALLENGE_ID: ANL-CH-002
DATE: 2026-09-05
DSD_INTERFACE_PROFILE_DATE: 2026-09-05
FORMATION_LAYER: used
PROPERTY_CORE: not used
STATIC_AGGREGATION_LAYER: not used
DYNAMICS_LAYER: not used
REALIZED_AXIS_SPECIALIZATION: not supplied
OTHER_SPECIALIZATION: none
```

Only Formation support and finite composition are used.
No Property or Dynamics machinery is introduced merely to explain sign symmetry.

## 3. Symmetry map and precommitted criteria / 대칭 변환과 사전 판정 기준

Define the sign-reversal map

```text
S(x) = -x
```

Precommitted criteria:

1. **Support symmetry** — E and F must retain the same admission pattern and support cardinality.
2. **Composition equivariance** — after sign reversal, `S(Comp(E)) = Comp(S(E))` must hold. Literal output equality is not required; the output must transform consistently with the input symmetry.
3. **No privileged sign** — `+1` must not be treated as more formed, more normal, or procedurally prior merely because it is positive.
4. **Status preservation** — sign reversal must not change admitted/absent or defined/undefined status distinctions.
5. **Scope** — the challenge tests structural orientation symmetry only, not whether any real-world affirmative or negative position is morally or practically preferable.

## 4. Case E — forward orientation / 정방향

All three operational inputs are formally admitted.

```text
T(e1) = +1
T(e2) = +1
T(e3) = -1
```

### DSD analysis

```text
admitted support = {e1, e2, e3}
Comp(E) = +1
```

All three channels have the same admission status independently of the signs of their supplied terms.

## 5. Case F — complete sign reversal / 완전 부호반전

Preserve E's admission structure and reverse every supplied term through `S`.

```text
T(f1) = -1
T(f2) = -1
T(f3) = +1
```

### DSD analysis

```text
admitted support = {f1, f2, f3}
Comp(F) = -1
```

Under the bijection `ei -> fi`, the formation-admission structure is preserved while term orientation is reversed.

### E/F symmetry check

```text
S(Comp(E)) = S(+1) = -1 = Comp(F)
```

E and F are therefore not cases that should have the same literal output.
They test whether composition transforms **equivariantly** under the declared symmetry.

## 6. Auxiliary cases G/H — zero fixed point / 0의 고정점

### G

```text
T(g1) = +1
T(g2) = 0
T(g3) = -1
all three channels admitted
Comp(G) = 0
```

### H

Apply sign reversal:

```text
T(h1) = -1
T(h2) = 0
T(h3) = +1
all three channels admitted
Comp(H) = 0
```

Because `S(0)=0`, zero is a fixed point of the sign-reversal symmetry.
The zero in this auxiliary pair is an **admitted zero-bearing term**, not channel absence.

## 7. Results / 결과

| Item | Result | Interpretation |
|---|---|---|
| Support symmetry | PASS (pilot) | E/F preserve admission pattern and support cardinality |
| Composition equivariance | PASS (pilot) | sign reversal of inputs induces the corresponding sign reversal of composition |
| No privileged sign | PASS | `+1` and `-1` receive no different ontological or procedural status merely from sign |
| Zero/absence discipline | PASS | admitted zero in G/H is not collapsed into absence |
| Layer restraint | PASS | Formation alone is sufficient |
| Analytical gain | LIMITED | the symmetry is clear, but the core arithmetic is already immediate from ordinary addition |

## 8. Important refinement discovered / 발견된 정교화

ANL-CH-001's **invariance** and ANL-CH-002's **symmetry** are not the same criterion.

- **001 invariance:** under nonessential relabeling, the result itself should remain unchanged.
- **002 equivariance:** when a meaningful orientation is transformed, the result should transform correspondingly.

Future challenge records should therefore preserve a separate field:

```text
EQUIVARIANCE_RESULT:
```

rather than forcing every symmetry test into `INVARIANCE_RESULT`.

## 9. Objectivity limits / 객관성 한계

This result is not strong validation because:

- the same session generated and analyzed the cases;
- additive finite composition makes the symmetry outcome highly predictable;
- there is no external-domain baseline or independent analyst;
- the challenge is primarily a sanity check against directional or sign bias in the analysis procedure.

Final classification:

```text
ANALYSIS_RESULT: PILOT_PASS_WITH_LIMITATIONS
INVARIANCE_RESULT: not_applicable_as_primary_metric
EQUIVARIANCE_RESULT: PASS
DISCRIMINATION_RESULT: not_primary
ANALYTICAL_GAIN: limited
BLINDING_LEVEL: self-generated pilot / not independent blind
FAILURES_OR_LIMITS: algebraically transparent toy case, no independent analyst, no external baseline
NEXT_STRENGTHENING_STEP: independently blinded value-reversed matched pairs
```

## 10. Next strengthening step / 다음 강화 단계

1. Pre-register matched pairs from an external domain whose evaluative meanings are reversed.
2. Hide names and directional labels before analysis.
3. Keep the analyst unaware that two cases form a mirror pair.
4. Compare correspondence class and analytical gain as well as the structural verdict.
