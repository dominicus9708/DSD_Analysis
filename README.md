# DSD Analysis

This repository records structured applications of **DSD Analysis (DSD 분석론)**.

DSD Analysis is a logical/structural audit program. Cross-domain similarity is not treated as proof of the DSD axioms, and failed mappings are preserved rather than rewritten as successes.

## Domain sequence

Completed or provisionally closed first-pass domains:

- `cases/logic/` — Global 001–011
- `cases/law/` — Global 012–025
- `cases/administration/` — Global 026–028
- `cases/computer_science/` — Global 029–033
- `cases/database/` — Global 034–038
- `cases/knowledge_representation/` — Global 039–043

Current domain:

- `cases/philosophy_epistemology/` — Global 044 onward

See `cases/INDEX.md` for the global map.

## Four-mode validation protocol

The project keeps four validation modes separate.

1. **Mode A — Negative control / failure recording**: DSD must reject its own failed attacks.
2. **Mode B — Historical convergence**: DSD reaches an established external structure without novelty inflation.
3. **Mode C — Prospective/blind prediction**: predictions are sealed before dedicated reply literature is opened.
4. **Mode D — Synthetic controls**: hidden ground truth tests discrimination and false positives/false negatives.

Current calibration records:

- PHIL-001 supplies Mode-A failure records and Mode-B convergence.
- `BENCH-C01` Toxin Puzzle: partial-blind, mixed-positive prospective pilot.
- `BENCH-C02` Hume Missing Shade: first clean Mode-C record under the project retrieval protocol; positive with a preserved C3 miss and no C4 novelty lead.
- `SYNTH-D01`: first Mode-D baseline, `TP 5 / TN 3 / FP 0 / FN 0 / partial 0` on 8 hand-authored blinded controls. This is not treated as a general accuracy estimate.

Method files:

- `methodology/four_mode_validation_protocol.md`
- `methodology/prospective_blind_case_template.md`
- `methodology/synthetic_control_case_template.md`

## Philosophy / epistemology status

### PHIL-001 / Global 044 — Philosophical Zombie

Current campaign complete.

- naive premise-loading attack failed;
- simple modal-space attack was not novel;
- descriptor-completeness pressure converged with Stoljar/Russellian families;
- refinement-stability / uniform-completion survived only as a formal sharpening / under-justification pressure.

### Historical Chinese Room attempt

Retired from the active sequence because its central part/whole objection converged directly with Systems Reply / Virtual Mind.

Historical branch:

`analysis/phil-002-chinese-room-part-whole-audit`

### PHIL-002 / Global 045 — Human/AI Room

Path:

`cases/philosophy_epistemology/045_human_ai_trust_property_nonidentifiability/`

Core result:

`equal externally admitted trust-compatible behavior != identified hidden trust property`.

The case separates behavioral constitution, bearer/type gating, and unresolved assignment while preserving `inapplicable / unavailable / undefined / defined zero / defined nonzero`.

Current classification:

**new DSD-constructed rebuttal format and formal synthesis/sharpening of established neighboring ideas; historical novelty unproven.**

Reproduce:

```bash
python cases/philosophy_epistemology/045_human_ai_trust_property_nonidentifiability/repro/check_trust_attribution_trilemma.py
```

### PHIL-003 / Global 046 — Mary's Room

Path:

`cases/philosophy_epistemology/046_marys_room_epistemic_regime_audit/`

Branch:

`analysis/phil-003-marys-room-epistemic-regime-audit`

The audit grants, for the sake of argument, that post-release Mary may gain genuinely new propositional knowledge.

Application-level encoding:

- `F` — world-fact targets;
- `F_P` — physical fact targets;
- `K_0` — pre-release knowledge records;
- `K_1` — post-release knowledge records;
- `tau_0, tau_1` — knowledge-record-to-fact target maps.

Core non-implication:

`K_1 \ K_0 != empty`

**does not imply**

`tau_1(K_1) \ tau_0(K_0) != empty`.

A new epistemic/propositional record may target an already known physical fact under a newly available phenomenal concept, representation, or access mode.

The audit therefore separates:

1. fact completeness;
2. representation/access completeness;
3. ontological completeness.

Jackson's strong conclusion remains conditional on an independently defended bridge from new phenomenal propositional knowledge to a fact target outside the complete physical fact set.

Historical comparison:

**Mode B strong convergence with the New Knowledge / Old Fact and phenomenal-concept/new-representation families; DSD-specific formal sharpening; no historical novelty claim.**

Reproduce:

```bash
python cases/philosophy_epistemology/046_marys_room_epistemic_regime_audit/repro/check_record_target_nonimplication.py
```

Expected key result:

```text
new_records: ['k_phen']
new_targets: []
new_record_without_new_target: True
all_targets_physical: True
witness_passed: True
```

## Next stage

`PHIL-004 / Global 047 — Twin Earth`.

The planned audit separates a narrator-fixed external environmental difference from what an internal subject can identify, and tests whether semantic/externalist conclusions require an explicit bridge from external reference conditions to internally available descriptions.

Mode-D `SYNTH-D02` remains a later adversarial matched-pair follow-up rather than a prerequisite for PHIL-004.

## Reproducibility rule

A completed case should preserve, as applicable:

1. source reconstruction;
2. sealed prediction or explicit audit target;
3. result;
4. finite witness/countermodel when inferentially useful;
5. reproducibility instructions;
6. failed mappings and non-correspondence.

Missing, undefined, inapplicable, absent, and defined-zero states must not be collapsed for convenience.

## DSD paper references

See `references/DSD_PAPERS.md`.

Domain-specific applications require additional interpretation maps; philosophical concepts are not identified with DSD primitives merely by naming similarity.