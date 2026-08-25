# Philosophy / Epistemology / Thought-Experiment Audit

Status: **PHIL-001 / Global 044 complete; PHIL-002 / Global 045 Human/AI Room complete; Mode-C and Mode-D validation baselines complete; PHIL-003 / Global 046 Mary's Room complete with two preserved arguments; PHIL-004 / Global 047 Twin Earth first pass complete; PHIL-005 next**.

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
- object-, role-, observer-, bearer-, status-, representation-, target-, semantic-signature-, and time-slice-level attribution.

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

PHIL-003 preserves **two distinct arguments**. The second does not replace the first.

### Argument 1 — epistemic-record novelty versus world-fact-target novelty

The audit grants that Mary may gain genuinely new propositional knowledge after release.

The key non-implication is:

`K_1 \ K_0 != empty`

**does not imply**

`tau_1(K_1) \ tau_0(K_0) != empty`.

A new epistemic/propositional record may target an old physical fact under a newly available phenomenal concept, representation, or access mode.

Argument 1 distinguishes:

1. fact completeness;
2. representation/access completeness;
3. ontological completeness.

Jackson's stronger conclusion survives this pressure if an independent fact-individuation bridge justifies:

`new phenomenal propositional record -> fact target outside the complete physical fact set`.

Historical classification:

**Mode B strong historical convergence with the New Knowledge / Old Fact, phenomenal-concept, and new-representation families + DSD-specific formal sharpening; no historical novelty claim.**

Finite witness:

```bash
python cases/philosophy_epistemology/046_marys_room_epistemic_regime_audit/repro/check_record_target_nonimplication.py
```

### Argument 2 — temporal snapshot completeness versus diachronic completeness

Let `F_P(t)` be the physical fact targets at time `t` and `T_M(t)` the targets Mary knows at time `t`.

Define:

`snapshot completeness: C_snap(t) iff F_P(t) subseteq T_M(t)`.

`diachronic completeness: C_dia(I) iff for every t in I, F_P(t) subseteq T_M(t)`.

The second non-implication is:

`C_snap(t0) !=> C_snap(t1)`

when the world-fact set can change after `t0` and no zero-delay global update bridge is supplied.

Argument 2 does not by itself refute Jackson's canonical Knowledge Argument. It is retained as a DSD dynamic extension, not as a replacement for Argument 1.

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

### Core source result

Putnam's Twin Earth argument survives the first-pass DSD audit.

A naive attack of the form

`same narrow/internal state -> same broad reference`

fails when linguistic reference is explicitly modeled as an environment-sensitive relational property. Putnam's argument is designed precisely to deny that narrow psychological state alone determines natural-kind extension.

### Semantic-Signature Fork

The DSD synthesis keeps three branches distinct.

1. **Narrow/internal signature** — internal/surface inputs only; Earth and Twin-Earth records may agree.
2. **Broad/externalist signature** — environment, causal history, and/or community inputs are constitutive; broad references may differ.
3. **Underspecified `meaning`** — equality or inequality is not yet a well-posed comparison until the semantic property signature is fixed.

Thus the following are jointly consistent:

`same narrow/internal semantic record`

and

`different broad reference/extension`.

The two claims concern different typed properties.

### Key failed attack

The subjects' inability to distinguish `H2O` and `XYZ` is not itself a counterexample to Putnam. The thought experiment intentionally makes the environmental microstructure cognitively unavailable in 1750 while letting broad reference differ.

This failed attack is preserved rather than rewritten as a success.

### Source-scope boundary

Putnam's 1975 argument first concerns linguistic reference/extension. Later externalist literature extends the Twin-Earth structure to propositional-attitude content.

PHIL-004 therefore requires a separate content-individuation bridge before treating the linguistic result as a proof about all mental content.

### Historical classification

The narrow/broad distinction and later two-factor/two-dimensional response families are already established in the literature.

Final classification:

**Putnam core survives; Mode-A-style failed attack preserved; Mode-B strong convergence with narrow/broad-content literature; DSD Semantic-Signature Fork retained as typed formal sharpening; no historical novelty claim.**

Finite witness:

```bash
python cases/philosophy_epistemology/047_twin_earth_reference_regime_audit/repro/check_semantic_signature_fork.py
```

## Planned next case

- `PHIL-005 / Global 048` — Brain in a Vat: test inverse reconstruction of external-world structure from internally accessible experience while distinguishing ordinary skeptical inference from Putnam-style semantic self-reference arguments.

Experience Machine and Gettier-family cases are opened only if a mechanism-overlap audit shows a genuinely distinct structural target.

## Source discipline

For each case:

- preserve source terminology before DSD mapping;
- distinguish original argument from textbook compression;
- preserve failed attacks and non-correspondence;
- do not identify philosophical concepts with DSD primitives by naming similarity;
- use application-level interpretation maps for external domains;
- attach dynamic claims to explicit time slices and supplied transition/propagation structure;
- specify semantic/property signatures before comparing values;
- for novelty-sensitive cases, preserve a strict pre-seal/post-search boundary.