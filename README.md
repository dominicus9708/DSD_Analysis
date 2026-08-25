# DSD Analysis

This repository records structured applications of **DSD Analysis (DSD 분석론)**.

DSD Analysis is a logical/structural audit program. Cross-domain similarity is not treated as proof of the DSD axioms, and failed mappings are preserved rather than rewritten as successes. Some external arguments are also retained as **precedent-convergence cases** when they independently preserve a structural discipline that DSD later formalizes in a broader setting.

## Domain sequence

Completed or provisionally closed first-pass domains:

- `cases/logic/` — Global 001–011
- `cases/law/` — Global 012–025
- `cases/administration/` — Global 026–028
- `cases/computer_science/` — Global 029–033
- `cases/database/` — Global 034–038
- `cases/knowledge_representation/` — Global 039–043
- `cases/philosophy_epistemology/` — PHIL-001–005 / Global 044–048 first-pass sequence complete

See `cases/INDEX.md` for the global map.

## Validation and convergence protocol

The project keeps four validation modes separate.

1. **Mode A — Negative control / failure recording**: DSD must reject its own failed attacks.
2. **Mode B — Historical convergence**: DSD reaches an established external structure without novelty inflation.
3. **Mode C — Prospective/blind prediction**: predictions are sealed before dedicated reply literature is opened.
4. **Mode D — Synthetic controls**: hidden ground truth tests discrimination and false positives/false negatives.

A separate narrow **precedent-convergence** label is used when an established external argument is not primarily an adversarial target, but independently preserves a structural distinction also enforced by DSD.

Current calibration records:

- PHIL-001 supplies Mode-A failure records and Mode-B convergence.
- `BENCH-C01` Toxin Puzzle: partial-blind, mixed-positive prospective pilot.
- `BENCH-C02` Hume Missing Shade: first clean Mode-C record under the project retrieval protocol; positive with a preserved C3 miss and no C4 novelty lead.
- `SYNTH-D01`: first Mode-D baseline, `TP 5 / TN 3 / FP 0 / FN 0 / partial 0` on 8 hand-authored blinded controls. This is not treated as a general accuracy estimate.
- PHIL-004 Twin Earth is an explicit precedent-convergence case.
- PHIL-005 Generic BIV non-injectivity and Putnam's reference-shift component provide a second partial precedent-convergence record, while the physical implementation layer remains a separate constitutive-bridge audit.

Method files:

- `methodology/four_mode_validation_protocol.md`
- `methodology/prospective_blind_case_template.md`
- `methodology/synthetic_control_case_template.md`
- `cases/philosophy_epistemology/PRECEDENT_CONVERGENCE.md`

## Philosophy / epistemology status

### PHIL-001 / Global 044 — Philosophical Zombie

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

Current classification:

**new DSD-constructed rebuttal format and formal synthesis/sharpening of established neighboring ideas; historical novelty unproven.**

Reproduce:

```bash
python cases/philosophy_epistemology/045_human_ai_trust_property_nonidentifiability/repro/check_trust_attribution_trilemma.py
```

### PHIL-003 / Global 046 — Mary's Room

Path:

`cases/philosophy_epistemology/046_marys_room_epistemic_regime_audit/`

PHIL-003 preserves two arguments.

#### Argument 1 — epistemic-record novelty versus world-fact-target novelty

`K_1 \ K_0 != empty`

**does not imply**

`tau_1(K_1) \ tau_0(K_0) != empty`.

Historical comparison:

**Mode B strong convergence with New Knowledge / Old Fact and phenomenal-concept/new-representation families; DSD-specific formal sharpening; no historical novelty claim.**

#### Argument 2 — temporal snapshot completeness versus diachronic completeness

`snapshot completeness at t0 !=> snapshot or diachronic completeness after t0`.

Current classification:

**DSD-constructed dynamic extension; historical novelty not yet audited and not claimed.**

Reproduce:

```bash
python cases/philosophy_epistemology/046_marys_room_epistemic_regime_audit/repro/check_record_target_nonimplication.py
python cases/philosophy_epistemology/046_marys_room_epistemic_regime_audit/repro/check_snapshot_completeness_nonpreservation.py
```

### PHIL-004 / Global 047 — Twin Earth

Path:

`cases/philosophy_epistemology/047_twin_earth_reference_regime_audit/`

Primary classification:

**precedent convergence**.

Putnam's Twin Earth is not primarily treated as a target that DSD needs to defeat. It is an established predecessor whose source-level structure independently aligns with DSD typed-property, observer/regime, and reconstruction disciplines.

The DSD `Semantic-Signature Fork` keeps narrow/internal, broad/externalist, and under-specified semantic properties separate. It is a typed formal restatement/sharpening of a precedent structure, not a new philosophical refutation.

Reproduce:

```bash
python cases/philosophy_epistemology/047_twin_earth_reference_regime_audit/repro/check_semantic_signature_fork.py
```

### PHIL-005 / Global 048 — Brain in a Vat

Path:

`cases/philosophy_epistemology/048_brain_in_vat_reality_source_audit/`

Branch:

`analysis/phil-005-brain-in-vat-reality-source-audit`

PHIL-005 separates generic skeptical reconstruction, physical implementation, reality/source monitoring, and Putnam's semantic anti-skeptical argument.

#### Generic skeptical BIV — precedent convergence

The skeptical setup deliberately allows

`A_Q(W_N, .) = A_Q(W_B, .)`

while

`W_N != W_B`.

The accessible projection is therefore non-injective. This is structurally aligned with DSD reduced/full reconstruction discipline. The stronger claim that external-world knowledge therefore fails requires an additional epistemology.

#### Physical BIV — Equivalence-Signature Audit

`exactly indistinguishable` is not a well-posed physical comparison until the subject-accessible equivalence signature and time interval are declared.

A serious signature may include ordinary sensory modalities, proprioceptive, vestibular and interoceptive information, agency/efference cues, memory/temporal continuity, and empirically justified reality/source-monitoring discriminators.

Thus:

`equal selected electrical stimulation !=> complete subject-level indistinguishability`

without a constitutive bridge.

Current neurotechnology does not establish complete BIV biological equivalence. A logical thought experiment may still stipulate full equality directly.

#### Reality/source monitoring

Autobiographical experience was used only to generate search hypotheses, not as medical evidence.

The research comparison supports a multi-cue distinction among externally driven sensory evidence, internally generated activity, and source/reality-monitoring judgment. Hallucination studies often report externalizing/source-attribution errors, while sleep/wake transition research shows state-dependent changes in environmental coupling. No universal `reduced arousal -> hallucination` rule is adopted.

#### Putnam's always-envatted semantic BIV

The reference-shift component continues the PHIL-004 precedent-convergence family: the same surface sentence may have different semantic/reference conditions in ordinary-English and vat-English regimes because causal history differs.

However, moving from sentence-level semantic non-truth to the object-level conclusion `I am not a BIV` requires a justified regime-sensitive disquotation/truth-condition bridge. This matches established Brueckner-style circularity objections and is recorded as Mode-B convergence rather than novelty.

Reproduce:

```bash
python cases/philosophy_epistemology/048_brain_in_vat_reality_source_audit/repro/check_biv_regime_noninjectivity.py
```

Expected key result:

```text
worlds_different: True
weak_indistinguishable: True
weak_projection_noninjective: True
strong_indistinguishable: False
added_discriminator_breaks_equivalence: True
same_surface: True
different_reference_regime: True
witness_passed: True
```

## Next stage

The originally planned PHIL-001–005 first-pass philosophy sequence is closed.

Next: **philosophy first-sequence synthesis audit**.

The synthesis will separately classify negative controls, historical convergence, precedent convergence, DSD typed/formal sharpening, DSD-specific extensions, prospective Mode-C records, and synthetic Mode-D records. These categories must not be merged into one success rate.

Mode-D `SYNTH-D02` remains a later adversarial matched-pair follow-up rather than a prerequisite for the synthesis.

## Reproducibility rule

A completed case should preserve, as applicable:

1. source reconstruction;
2. sealed prediction or explicit audit target;
3. result;
4. finite witness/countermodel when inferentially useful;
5. reproducibility instructions;
6. failed mappings and non-correspondence;
7. precedent-convergence status when the external argument itself independently preserves the relevant DSD-like structural discipline;
8. explicit separation of empirical/biological implementation claims from purely stipulated logical equivalence.

Missing, undefined, inapplicable, absent, and defined-zero states must not be collapsed for convenience.

## DSD paper references

See `references/DSD_PAPERS.md`.

Domain-specific applications require additional interpretation maps; philosophical or medical concepts are not identified with DSD primitives merely by naming similarity.