# Philosophy / Epistemology / Thought-Experiment Audit

Status: **PHIL-001 / Global 044 current campaign completed; PHIL-002 / Global 045 replaced with Human/AI Room trust-property case; first clean blind benchmark + synthetic controls next**.

Field-case identifier: **PHIL-###**.

## Field objective

Audit philosophical and epistemological arguments without presupposing that their traditional conclusion is correct or incorrect.

Keep separate:

- explicit initial conditions;
- narrator/experimenter information;
- information accessible to internal subjects;
- derived consequences;
- hidden conclusion-equivalent assumptions;
- alternative structures compatible with the same observation;
- object-, role-, observer-, bearer-, status-, and description-level attribution.

## Core audit rules

1. `assumption -> consequence` must not be silently promoted to a stronger modal, ontological, inverse-identification, or hidden-property claim without an explicit bridge.
2. `equality of a chosen descriptor != completeness or identity of the underlying structure`.
3. `local/refinement-wise witness existence != one uniform witness surviving all refinements`.
4. `property eligibility != property assignment`.
5. `undefined / unavailable / inapplicable != defined zero`.
6. equal reduced/output descriptions reconstruct hidden property records only under an explicit identification/injectivity condition.

## Four-mode validation discipline

This field follows `methodology/four_mode_validation_protocol.md`.

- **Mode A — Negative control / failure**: preserve attacks that fail.
- **Mode B — Historical convergence**: record independent convergence without novelty inflation.
- **Mode C — Prospective/blind**: seal predictions before dedicated reply literature.
- **Mode D — Synthetic controls**: use hidden ground truth, including clean/no-defect controls, and preserve false positives/false negatives.

## PHIL-001 / Global Case 044 — completed for current campaign

**Philosophical Zombie: Premise Loading, Modal Bridge, Descriptor Completeness, and Refinement-Stable Completion Audit**

Retained results:

1. naive premise-loading attack failed against Chalmers's mature formulation;
2. simple modal-space counterattack was not a new refutation because strong-necessity worries are already explicit;
3. descriptor-completeness pressure converged with Stoljar/Russellian lines;
4. refinement-stability / uniform-completion formalization partially survived as an under-justification pressure but not as a wholesale refutation or clean blind novelty result.

## Retired historical PHIL-002 attempt — Chinese Room

The former active PHIL-002 Chinese Room case has been **retired from the active case sequence**.

Reason:

- its central part/whole objection converged directly with the classic Systems Reply and later Virtual Mind family;
- it therefore added historical calibration but not a sufficiently distinct active PHIL-002 mechanism.

The historical branch `analysis/phil-002-chinese-room-part-whole-audit` is preserved for auditability. The Chinese Room files are removed from the new active branch and are not counted as the current Global 045 evidence node.

## PHIL-002 / Global Case 045 — active replacement

**Human/AI Room: Trust-Property Non-Identifiability and Trust Attribution Trilemma**

Path:

`045_human_ai_trust_property_nonidentifiability/`

Current branch:

`analysis/phil-002-human-ai-trust-nonidentifiability`

### Setup

Human room `H` and AI room `A` are opaque to external observer `E` except through a fixed interaction regime.

Assume:

`O_E(H) = O_E(A)`.

The target property `T` is an externally interpreted property labeled `trust`; DSD does not define psychological or machine trust.

### Core rebuttal

Equal trust-compatible output does not by itself identify a unique hidden trust property or mechanism:

`O_E(H)=O_E(A) -/-> T_E(H)=T_E(A)`.

The reverse asymmetric shortcut is also blocked:

`human/AI bearer labels -/-> T_E(H)=1 and T_E(A)=0`.

### Trust Attribution Trilemma

Any strong trust attribution must disclose which route is being used.

1. **Behavioral constitution** — trust is defined by the admitted behavioral descriptor. Equal behavior then gives equal behavioral trust by definition, but not a deeper hidden-state identity.
2. **Bearer/type gating** — a theory restricts trust to bearers satisfying human-specific, normative, affective, conscious, biological, or other prerequisites. The asymmetry then comes from the property domain, not the equal behavior. Inapplicable/unavailable status is not automatically numerical zero.
3. **Unresolved assignment** — trust is non-behavioral and no identification/measurement bridge is supplied. The correct status may remain undefined rather than false/zero.

General rule:

`fix property signature + bearer domain + observation regime + identification map before assigning a hidden property value`.

### Finite witness

Run from repository root:

```bash
python cases/philosophy_epistemology/045_human_ai_trust_property_nonidentifiability/repro/check_trust_attribution_trilemma.py
```

The witness gives one external observation vector compatible with multiple human/AI mechanisms and with distinct trust records: defined `1`, defined `0`, and `undefined`.

### Literature comparison

Dedicated precedent search was performed only after `PREDICTION.md` was sealed.

Established prior families include:

- cognitive/attitudinal trust versus trusting behavior;
- trust versus trustworthiness;
- behavioral indicators versus latent/internal constructs;
- AI anthropomorphism and mental-state attribution;
- disputes about whether artificial agents are eligible bearers of genuine trust;
- behavioral AI-as-trustor experiments that use weaker wording such as `behavior consistent with trust`.

The exact combined DSD trilemma was not located in the retrieved sources, but that absence is not proof of historical novelty.

Current classification:

**new DSD-constructed rebuttal format and formal synthesis/sharpening of established neighboring ideas; historical novelty unproven.**

See:

- `045_human_ai_trust_property_nonidentifiability/PREDICTION.md`
- `045_human_ai_trust_property_nonidentifiability/PLAN.md`
- `045_human_ai_trust_property_nonidentifiability/SOURCE_NOTES.md`
- `045_human_ai_trust_property_nonidentifiability/RESULT.md`
- `045_human_ai_trust_property_nonidentifiability/REPRODUCIBILITY.md`
- `045_human_ai_trust_property_nonidentifiability/repro/check_trust_attribution_trilemma.py`

## First clean prospective/blind benchmark — next

Before PHIL-003, select a philosophical argument or thought experiment whose dedicated objection/reply literature has not yet been reviewed in this project.

Required sequence:

1. retrieve only the original/authoritative formulation and neutral definitions;
2. declare withheld literature;
3. seal `PREDICTION.md`;
4. unblind only after the prediction is committed;
5. classify matches, misses, refinements, and unresolved novelty leads.

## First synthetic-control set — in parallel

Prepare at least:

- one premise-loading defect;
- one part/whole defect;
- one descriptor/status defect;
- one explicit valid-bridge case;
- one clean/no-defect control.

Preserve raw TP/TN/FP/FN counts.

## Later planned cases

- `PHIL-003 / Global 046` — Mary's Room
- `PHIL-004 / Global 047` — Twin Earth
- `PHIL-005 / Global 048` — Brain in a Vat

## Source discipline

For each case:

- preserve source terminology before DSD mapping;
- distinguish original argument from textbook compression;
- preserve failed attacks and non-correspondence;
- do not identify philosophical concepts with DSD primitives by naming similarity;
- for novelty-sensitive cases, preserve a strict pre-seal/post-search boundary.
