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

PHIL-003 preserves **two distinct arguments**. The second is an extension of the analysis and does not replace the first.

#### Argument 1 — epistemic-record novelty versus world-fact-target novelty

The audit grants, for the sake of argument, that post-release Mary may gain genuinely new propositional knowledge.

Core non-implication:

`K_1 \ K_0 != empty`

**does not imply**

`tau_1(K_1) \ tau_0(K_0) != empty`.

A new epistemic/propositional record may target an already known physical fact under a newly available phenomenal concept, representation, or access mode.

Historical comparison:

**Mode B strong convergence with the New Knowledge / Old Fact and phenomenal-concept/new-representation families; DSD-specific formal sharpening; no historical novelty claim.**

Reproduce Argument 1:

```bash
python cases/philosophy_epistemology/046_marys_room_epistemic_regime_audit/repro/check_record_target_nonimplication.py
```

#### Argument 2 — temporal snapshot completeness versus diachronic completeness

Define snapshot completeness by:

`C_snap(t) iff F_P(t) subseteq T_M(t)`.

Define diachronic completeness on interval `I` by:

`C_dia(I) iff for every t in I, F_P(t) subseteq T_M(t)`.

The second core non-implication is:

`snapshot completeness at t0 !=> snapshot or diachronic completeness after t0`.

A finite dynamic witness allows Mary to be complete at `t0`, lose completeness at `t1` when a new remote physical fact appears but has not yet been incorporated, and regain completeness at `t2` after the update.

Argument 2 does not by itself refute Jackson's canonical Knowledge Argument. It is retained as a separate dynamic audit.

Current classification:

**DSD-constructed dynamic extension; historical novelty not yet audited and not claimed.**

Reproduce Argument 2:

```bash
python cases/philosophy_epistemology/046_marys_room_epistemic_regime_audit/repro/check_snapshot_completeness_nonpreservation.py
```

### PHIL-004 / Global 047 — Twin Earth

Path:

`cases/philosophy_epistemology/047_twin_earth_reference_regime_audit/`

Branch:

`analysis/phil-004-twin-earth-reference-regime-audit`

Putnam's core Twin Earth argument survives the first-pass DSD audit.

A naive attack of the form

`same narrow/internal state -> same broad reference`

fails when reference is explicitly modeled as an environment-sensitive relational property. Putnam's argument is designed precisely to deny that narrow psychological state alone determines natural-kind extension.

#### Semantic-Signature Fork

The DSD synthesis keeps three semantic-property branches separate.

1. **Narrow/internal signature** — internal/surface inputs only; Earth and Twin-Earth records may agree.
2. **Broad/externalist signature** — environment, causal history, and/or community inputs are constitutive; broad references may differ.
3. **Underspecified `meaning`** — equality or inequality is not yet a well-posed comparison until the property signature is fixed.

Thus:

`same narrow/internal semantic record`

can coexist with

`different broad reference/extension`

without contradiction, because the two values belong to different typed properties.

The subjects' inability to distinguish `H2O` and `XYZ` is not a counterexample to Putnam; it is an intentional feature of the thought experiment. DSD therefore records that proposed attack as a failure.

Putnam's 1975 argument first concerns linguistic reference/extension. Later externalist literature extends the Twin-Earth structure to propositional-attitude content, so PHIL-004 keeps a separate bridge between linguistic reference and broad mental content.

Historical comparison:

**Putnam core survives; Mode-A-style failed attack preserved; Mode-B strong convergence with narrow/broad-content and two-factor/two-dimensional response families; DSD Semantic-Signature Fork retained as typed formal sharpening; no historical novelty claim.**

Reproduce:

```bash
python cases/philosophy_epistemology/047_twin_earth_reference_regime_audit/repro/check_semantic_signature_fork.py
```

Expected key result:

```text
same_internal: True
same_surface: True
narrow_equal: True
broad_reference_equal: False
projection_noninjective_witness: True
witness_passed: True
```

## Next stage

`PHIL-005 / Global 048 — Brain in a Vat`.

The next audit will separate ordinary skeptical inverse reconstruction from Putnam-style semantic self-reference arguments and test what internally accessible experience actually licenses about external-world structure.

Mode-D `SYNTH-D02` remains a later adversarial matched-pair follow-up rather than a prerequisite for PHIL-005.

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