# Philosophy / Epistemology / Thought-Experiment Audit

Status: **PHIL-001 / Global 044 complete; PHIL-002 / Global 045 Human/AI Room complete; Mode-C and Mode-D validation baselines complete; PHIL-003 / Global 046 Mary's Room first pass complete; PHIL-004 next**.

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
- object-, role-, observer-, bearer-, status-, representation-, and target-level attribution.

## Core audit rules

1. `assumption -> consequence` must not be silently promoted to a stronger modal, ontological, inverse-identification, or hidden-property claim without an explicit bridge.
2. `equality of a chosen descriptor != completeness or identity of the underlying structure`.
3. `local/refinement-wise witness existence != one uniform witness surviving all refinements`.
4. `property eligibility != property assignment`.
5. `undefined / unavailable / inapplicable != defined zero`.
6. equal reduced/output descriptions reconstruct hidden property records only under an explicit identification/injectivity condition.
7. a new epistemic/representational record does not by itself prove a new world-fact target.

## Four-mode validation discipline

This field follows `methodology/four_mode_validation_protocol.md`.

- **Mode A — Negative control / failure**: preserve attacks that fail.
- **Mode B — Historical convergence**: record independent convergence without novelty inflation.
- **Mode C — Prospective/blind**: seal predictions before dedicated reply literature.
- **Mode D — Synthetic controls**: use hidden ground truth, including clean/no-defect controls, and preserve false positives/false negatives.

Current validation records:

- PHIL-001 supplies negative-control/failure and historical-convergence records.
- BENCH-C01 Toxin Puzzle is a partial-blind mixed-positive pilot.
- BENCH-C02 Hume Missing Shade is the first clean Mode-C record under the project retrieval protocol.
- SYNTH-D01 is the first Mode-D baseline: `TP 5 / TN 3 / FP 0 / FN 0 / partial 0` on 8 hand-authored blinded controls. It is not treated as a general accuracy estimate.

## PHIL-001 / Global 044

**Philosophical Zombie: Premise Loading, Modal Bridge, Descriptor Completeness, and Refinement-Stable Completion Audit**

Retained results:

1. naive premise-loading attack failed against Chalmers's mature formulation;
2. simple modal-space counterattack was not a new refutation because strong-necessity worries are already explicit;
3. descriptor-completeness pressure converged with Stoljar/Russellian lines;
4. refinement-stability / uniform-completion formalization partially survived as an under-justification pressure but not as a wholesale refutation or clean blind novelty result.

## Retired historical Chinese Room attempt

The former PHIL-002 Chinese Room case is retired from the active sequence because its central part/whole objection converged directly with the Systems Reply / Virtual Mind family.

Historical branch:

`analysis/phil-002-chinese-room-part-whole-audit`

It remains only as an audit trail.

## PHIL-002 / Global 045 — Human/AI Room

Path:

`045_human_ai_trust_property_nonidentifiability/`

Core setup:

`O_E(H) = O_E(A)`.

Core result:

`equal externally admitted trust-compatible behavior != identified hidden trust property`.

The case separates:

1. behavioral constitution;
2. bearer/type gating;
3. unresolved assignment.

It preserves `inapplicable / unavailable / undefined / defined zero / defined nonzero` and requires an identification/reconstruction bridge before output equality is treated as a hidden-property identifier.

Current classification:

**new DSD-constructed rebuttal format and formal synthesis/sharpening of established neighboring ideas; historical novelty unproven.**

Finite witness:

```bash
python cases/philosophy_epistemology/045_human_ai_trust_property_nonidentifiability/repro/check_trust_attribution_trilemma.py
```

## PHIL-003 / Global 046 — Mary's Room

Path:

`046_marys_room_epistemic_regime_audit/`

Branch:

`analysis/phil-003-marys-room-epistemic-regime-audit`

### Source target

The audit reconstructs Jackson's 1982/1986 Knowledge Argument, using the stronger 1986 clarification that the relevant new knowledge concerns the already existing experiences of others rather than merely Mary's newly changed post-release state.

The analysis does **not** rely on an ability-only reply. It grants, for the sake of the audit, that Mary may gain genuinely new propositional knowledge.

### Core application-level encoding

Let:

- `F` = world-fact targets;
- `F_P` = physical fact targets;
- `K_0` = pre-release knowledge records;
- `K_1` = post-release knowledge records;
- `tau_0, tau_1` = target maps from knowledge records to world facts.

The key non-implication is:

`K_1 \ K_0 != empty`

**does not imply**

`tau_1(K_1) \ tau_0(K_0) != empty`.

A new epistemic/propositional record may target an old physical fact under a newly available phenomenal concept, representation, or access mode.

### Completeness separation

PHIL-003 distinguishes:

1. **fact completeness** — every physical fact target is known;
2. **representation/access completeness** — every admissible way of representing/accessing those facts is available;
3. **ontological completeness** — every fact is physical.

A failure of representation/access completeness does not by itself establish failure of ontological completeness.

### Surviving Jackson branch

Jackson's stronger conclusion survives this DSD pressure if an independent fact-individuation bridge justifies:

`new phenomenal propositional record -> fact target outside the complete physical fact set`.

DSD does not decide the correct metaphysics of fact or proposition individuation.

### Literature classification

The result converges strongly with the established **New Knowledge / Old Fact**, phenomenal-concept, and new-representation/mode-of-presentation families.

Therefore:

**Mode B strong historical convergence + DSD-specific formal sharpening; no historical novelty claim.**

Finite witness:

```bash
python cases/philosophy_epistemology/046_marys_room_epistemic_regime_audit/repro/check_record_target_nonimplication.py
```

## Planned next cases

- `PHIL-004 / Global 047` — Twin Earth: separate a narrator-fixed environmental difference from an internal subject's ability to identify that difference.
- `PHIL-005 / Global 048` — Brain in a Vat: test inverse reconstruction of external-world structure from internally accessible experience.

Experience Machine and Gettier-family cases are opened only if a mechanism-overlap audit shows a genuinely distinct structural target.

## Source discipline

For each case:

- preserve source terminology before DSD mapping;
- distinguish original argument from textbook compression;
- preserve failed attacks and non-correspondence;
- do not identify philosophical concepts with DSD primitives by naming similarity;
- use application-level interpretation maps for external domains;
- for novelty-sensitive cases, preserve a strict pre-seal/post-search boundary.