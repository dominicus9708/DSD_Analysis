# Philosophy / Epistemology / Thought-Experiment Audit

Status: **PHIL-001–005 / Global 044–048 first-pass sequence complete; Mode-C and Mode-D validation baselines retained; synthesis audit next**.

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
- object-, role-, observer-, bearer-, status-, representation-, target-, semantic-signature-, equivalence-signature-, and time-slice-level attribution.

## Core audit rules

1. `assumption -> consequence` must not be silently promoted to a stronger modal, ontological, inverse-identification, or hidden-property claim without an explicit bridge.
2. `equality of a chosen descriptor != completeness or identity of the underlying structure`.
3. `local/refinement-wise witness existence != one uniform witness surviving all refinements`.
4. `property eligibility != property assignment`.
5. `undefined / unavailable / inapplicable != defined zero`.
6. equal reduced/output descriptions reconstruct hidden property records only under an explicit identification/injectivity condition.
7. a new epistemic/representational record does not by itself prove a new world-fact target.
8. completeness at one time slice does not by itself establish completeness over a later evolving interval.
9. an umbrella semantic label such as `meaning` or `content` must not collapse internal, surface, reference, environmental, historical, or community-dependent records before the property signature is fixed.
10. a claim of `indistinguishable experience` must specify which subject-accessible channels, monitoring cues, and time interval are included before equality is promoted to full experiential equivalence.

## Validation and convergence discipline

This field follows `methodology/four_mode_validation_protocol.md` and also preserves a narrow **precedent-convergence** category.

- **Mode A — Negative control / failure**: preserve attacks that fail.
- **Mode B — Historical convergence**: record independent convergence without novelty inflation.
- **Mode C — Prospective/blind**: seal predictions before dedicated reply literature.
- **Mode D — Synthetic controls**: use hidden ground truth, including clean/no-defect controls, and preserve false positives/false negatives.
- **Precedent convergence**: an established external argument is not primarily an adversarial target, but independently preserves a structural distinction also enforced by DSD.

Current validation records:

- PHIL-001 supplies negative-control/failure and historical-convergence records.
- BENCH-C01 Toxin Puzzle is a partial-blind mixed-positive pilot.
- BENCH-C02 Hume Missing Shade is the first clean Mode-C record under the project retrieval protocol.
- SYNTH-D01 is the first Mode-D baseline: `TP 5 / TN 3 / FP 0 / FN 0 / partial 0` on 8 hand-authored blinded controls. It is not treated as a general accuracy estimate.
- PHIL-004 Twin Earth is an explicit precedent-convergence case.
- PHIL-005 Generic BIV non-injectivity and Putnam's reference-shift component add a second, partial precedent-convergence record while preserving a separate physical-implementation audit.

See `PRECEDENT_CONVERGENCE.md` for the precedent-convergence criteria and evidence-accounting rule.

## PHIL-001 / Global 044 — Philosophical Zombie

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

Core result:

`equal externally admitted trust-compatible behavior != identified hidden trust property`.

The case separates behavioral constitution, bearer/type gating, and unresolved assignment while preserving `inapplicable / unavailable / undefined / defined zero / defined nonzero`.

Current classification:

**new DSD-constructed rebuttal format and formal synthesis/sharpening of established neighboring ideas; historical novelty unproven.**

Finite witness:

```bash
python cases/philosophy_epistemology/045_human_ai_trust_property_nonidentifiability/repro/check_trust_attribution_trilemma.py
```

## PHIL-003 / Global 046 — Mary's Room

Path:

`046_marys_room_epistemic_regime_audit/`

PHIL-003 preserves **two distinct arguments**.

### Argument 1 — epistemic-record novelty versus world-fact-target novelty

`K_1 \ K_0 != empty`

**does not imply**

`tau_1(K_1) \ tau_0(K_0) != empty`.

A new epistemic/propositional record may target an old physical fact under a newly available phenomenal concept, representation, or access mode.

Historical classification:

**Mode B strong historical convergence with the New Knowledge / Old Fact, phenomenal-concept, and new-representation families + DSD-specific formal sharpening; no historical novelty claim.**

Finite witness:

```bash
python cases/philosophy_epistemology/046_marys_room_epistemic_regime_audit/repro/check_record_target_nonimplication.py
```

### Argument 2 — temporal snapshot completeness versus diachronic completeness

Define:

`snapshot completeness: C_snap(t) iff F_P(t) subseteq T_M(t)`.

`diachronic completeness: C_dia(I) iff for every t in I, F_P(t) subseteq T_M(t)`.

Then one-time completeness does not itself guarantee later completeness in an evolving world:

`C_snap(t0) !=> C_snap(t1)`.

Current status:

**DSD-constructed dynamic extension; historical novelty not yet audited and not claimed.**

Finite witness:

```bash
python cases/philosophy_epistemology/046_marys_room_epistemic_regime_audit/repro/check_snapshot_completeness_nonpreservation.py
```

## PHIL-004 / Global 047 — Twin Earth

Path:

`047_twin_earth_reference_regime_audit/`

Branch:

`analysis/phil-004-twin-earth-reference-regime-audit`

### Primary classification — precedent convergence

Putnam's Twin Earth is **not primarily treated as an argument for DSD to attack**.

It independently preserves structural distinctions strongly aligned with DSD Formation, Axis-Property, observer/regime, and reconstruction disciplines.

The setup permits:

`I(O_E) = I(O_T)`

and

`U(O_E) = U(O_T)`

while

`E(O_E) != E(O_T)`.

If broad reference is defined by an environment-sensitive signature such as

`R_B = g(I, U, E, H, C)`,

then

`R_B(O_E) != R_B(O_T)`

is coherent.

The DSD `Semantic-Signature Fork` keeps narrow/internal, broad/externalist, and under-specified semantic properties separate. It is a typed formal restatement/sharpening of a precedent structure, not a new philosophical refutation.

Finite witness:

```bash
python cases/philosophy_epistemology/047_twin_earth_reference_regime_audit/repro/check_semantic_signature_fork.py
```

## PHIL-005 / Global 048 — Brain in a Vat

Path:

`048_brain_in_vat_reality_source_audit/`

Branch:

`analysis/phil-005-brain-in-vat-reality-source-audit`

PHIL-005 separates three questions that should not be collapsed.

### 1. Generic skeptical BIV — precedent convergence

Let `W_N` be an ordinary-world realization and `W_B` a BIV-world realization. If a declared subject-accessible projection satisfies

`A_Q(W_N, .) = A_Q(W_B, .)`

while

`W_N != W_B`,

then the projection is non-injective and the internal record does not uniquely reconstruct the full external world.

The generic BIV is therefore structurally aligned with DSD reduced/full reconstruction discipline rather than being a thought experiment DSD should reject merely because the full worlds differ.

This structural non-injectivity alone does not prove the stronger epistemological thesis that all external-world knowledge fails.

### 2. Physical implementation — Equivalence-Signature Audit

The phrase `exactly indistinguishable from ordinary experience` requires a declared comparison signature.

A serious subject-level signature may need to include sensory modalities, proprioception, vestibular/interoceptive information, motor/agency cues, temporal and memory continuity, and any empirically justified reality/source-monitoring discriminators.

Accordingly:

`equal selected electrical stimulation !=> complete subject-level indistinguishability`

without a constitutive bridge from interface variables to every declared discriminator over the relevant time interval.

Current neurotechnology can evoke artificial sensory percepts, but it does not establish complete BIV biological equivalence. This limits physical-realization claims without refuting a purely logical BIV that stipulates full equivalence directly.

### 3. Reality/source monitoring empirical comparison

The user's lived experience was used only to generate search hypotheses, not as medical evidence.

The literature supports a multi-cue framework in which internally generated and externally triggered experiences are distinguished through perceptual reality monitoring, source monitoring, self/other monitoring, and related metacognitive processes. Hallucination studies often find externalizing/source-attribution errors, while sleep/wake and hypnagogic research shows that environmental coupling and internal/external processing vary with state.

The project therefore preserves the distinction:

`external coupling / internal generation / source judgment`

without adopting the universal medical claim `reduced arousal -> hallucination`.

### 4. Putnam's always-envatted semantic BIV

Putnam's reference-shift component continues the PHIL-004 precedent-convergence family: the same surface string can have different semantic/reference conditions in ordinary-English and vat-English regimes because causal history differs.

However, moving from a sentence-level semantic result about `I am a BIV` to the object-level conclusion `I am not a BIV` requires a justified regime-sensitive disquotation/truth-condition bridge. Brueckner-style objections to this step are established literature.

Classification:

**generic BIV non-injectivity = precedent convergence; physical full-indistinguishability = constitutive implementation bridge / DSD formal sharpening; reality/source-monitoring = empirical comparison with cautious scope; Putnam reference shift = PHIL-004-family precedent convergence; strong anti-skeptical conclusion = Mode-B bridge/circularity issue; no historical novelty claim.**

Finite witness:

```bash
python cases/philosophy_epistemology/048_brain_in_vat_reality_source_audit/repro/check_biv_regime_noninjectivity.py
```

## Next stage — first-sequence synthesis audit

PHIL-001–005 now close the originally planned first-pass philosophy/thought-experiment sequence.

Before opening Experience Machine, Gettier-family, or other candidates, perform a synthesis audit that separately counts and interprets:

- negative-control / failed attacks;
- historical convergence;
- precedent convergence;
- DSD typed/formal sharpening;
- DSD-specific extension;
- prospective Mode-C evidence;
- synthetic Mode-D evidence.

Do **not** merge these into one success percentage.

## Source discipline

For each case:

- preserve source terminology before DSD mapping;
- distinguish original argument from textbook compression;
- preserve failed attacks and non-correspondence;
- do not identify philosophical concepts with DSD primitives by naming similarity;
- use application-level interpretation maps for external domains;
- attach dynamic claims to explicit time slices and supplied transition/propagation structure;
- specify semantic/property/equivalence signatures before comparing values;
- distinguish adversarial audits from precedent-convergence cases when the external argument already independently preserves the relevant DSD-like structural discipline;
- use autobiographical experience only as hypothesis-generation input unless independently supported;
- for novelty-sensitive cases, preserve a strict pre-seal/post-search boundary.