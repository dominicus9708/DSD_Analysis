# DSD Analysis

This repository records structured applications of **DSD Analysis (DSD 분석론)**.

DSD Analysis is not a numerical benchmark repository and does not treat cross-domain similarity as proof of the DSD axioms. Each case preserves the source discipline first, then tests which DSD distinctions are preserved, require extra encoding, fail to correspond, or reveal an actual contradiction.

## Repository organization

The repository uses two independent classification axes.

### 1. Analysis purpose

See `campaigns/`.

- `campaigns/falsification/` — direct countermodel, contradiction, and integration stress tests
- `campaigns/coherence/` — consistency and compatibility with independent formal frameworks
- `campaigns/predefinition/` — hidden-assumption, premature-promotion, typing/signature, and describability-prerequisite audits
- `campaigns/reinterpretation/` — structural decomposition and application to external problem domains

### 2. External domain

Historical case paths are preserved under `cases/`.

Current completed or provisionally closed first-pass domains include:

- `cases/logic/` — Global Cases 001–011
- `cases/law/` — Global Cases 012–025
- `cases/administration/` — Global Cases 026–028
- `cases/computer_science/` — Global Cases 029–033
- `cases/database/` — Global Cases 034–038
- `cases/knowledge_representation/` — Global Cases 039–043

Current active domain:

- `cases/philosophy_epistemology/` — PHIL-001 / Global 044 current campaign completed; PHIL-002 / Global 045 replaced with the Human/AI Room trust-property case

See `cases/INDEX.md` for the global case map.

### 3. Validation benchmarks

- `benchmarks/prospective/` — Mode-C prospective/blind prediction benchmarks
- `benchmarks/prospective/C01_toxin_puzzle/` — BENCH-C01, partial-blind pilot
- `benchmarks/prospective/C02_hume_missing_shade/` — BENCH-C02, first clean Mode-C record under the project retrieval protocol

## Common methodology

- `methodology/case_template.md` — base case template
- `methodology/analysis_taxonomy.md` — purpose classification rules
- `methodology/reproducibility_contract.md` — minimum evidence and rerun requirements
- `methodology/four_mode_validation_protocol.md` — four-mode validation protocol
- `methodology/prospective_blind_case_template.md` — prospective/blind prediction-seal template
- `methodology/synthetic_control_case_template.md` — blinded synthetic-control template

A completed case must preserve non-correspondence and failed mappings rather than forcing every external concept into DSD terminology.

## Four-mode validation protocol

Validation campaigns distinguish four modes rather than counting every favorable-looking result together.

1. **Negative-control / failure recording** — DSD must be able to reject its own initially plausible attack or mapping.
2. **Historical convergence / independent rediscovery** — DSD reaches a structure already established in an external literature and records the overlap without claiming novelty.
3. **Prospective / blind prediction** — DSD predictions are timestamped before dedicated objection/reply literature is opened.
4. **Synthetic / controlled cases** — hidden ground-truth mechanisms and clean controls are used to expose both correct detection and false positives/false negatives.

The intended cumulative claim is methodological, not metaphysical:

`DSD distinctions repeatedly function as useful analytical operators under controlled and externally calibrated tests`.

No combination of these validation modes by itself proves the Formation Axiom System or Axis-Property Axiom System true as a description of fundamental reality.

## DSD paper references

- `references/DSD_PAPERS.md` — current project paper titles, stable citation roles, and DOI registry notes

Each completed case should state the exact DSD paper section, definition, axiom, theorem, or closure clause actually used.

## Completed synthesis points

- `synthesis/FALSIFICATION_CAMPAIGN_001_010.md`
- `cases/computer_science/CS_001_005_FIRST_PASS_SYNTHESIS.md`
- `cases/database/SYNTHESIS.md`
- `cases/knowledge_representation/SYNTHESIS.md`

## Current philosophy / epistemology work

### PHIL-001 / Global 044

Current campaign completed.

Retained pattern:

1. naive premise-loading attack rejected;
2. simple modal-space counterattack rejected as a new refutation;
3. descriptor-completeness squeeze survives but converges with Stoljar/Russellian literature;
4. refinement-stability / uniform-completion formalization partially survives as an under-justification pressure, not as a wholesale refutation or clean blind novelty result.

### Retired PHIL-002 attempt — Chinese Room

The Chinese Room case is **retired from the active case sequence** because its central part/whole objection converged directly with the classic Systems Reply and later Virtual Mind family.

Its historical branch is preserved:

`analysis/phil-002-chinese-room-part-whole-audit`

The Chinese Room files are removed from the new active branch and are not counted as the current Global 045 result.

### PHIL-002 / Global 045 — Human/AI Room

Active case:

`cases/philosophy_epistemology/045_human_ai_trust_property_nonidentifiability/`

Topic:

**Human/AI Room: Trust-Property Non-Identifiability and Trust Attribution Trilemma**.

Core assumption:

`O_E(H) = O_E(A)`.

Core non-implication:

`equal externally admitted trust-compatible behavior != identified hidden trust property`.

The active rebuttal separates three routes:

1. **behavioral constitution** — trust is defined by the observed behavioral construct;
2. **bearer/type gating** — a theory restricts the property domain through explicit prerequisites;
3. **unresolved assignment** — trust is not behaviorally constitutive and no identification bridge is available, so the correct status can remain undefined.

The case also preserves:

`inapplicable / unavailable input / undefined / defined zero / defined nonzero`.

A human/AI substrate label does not by itself license the pair `trust(H)=1`, `trust(A)=0`, and equal output does not by itself license equal hidden trust values.

Finite witness command:

```bash
python cases/philosophy_epistemology/045_human_ai_trust_property_nonidentifiability/repro/check_trust_attribution_trilemma.py
```

### PHIL-002 novelty status

The formulation was sealed before the dedicated search for its exact construction.

Prior literature already contains strong neighboring material, so the current claim remains conservative:

**new DSD-constructed rebuttal format and formal synthesis/sharpening of established neighboring ideas; historical novelty unproven.**

## BENCH-C01 — Toxin Puzzle prospective pilot

Branch:

`benchmark/c01-toxin-puzzle-prospective`

Prediction seal:

`ad682b7354555de6ad004154e9846e4e1ec31cc7`

Blind integrity: **partial**.

Outcome:

- **C1:** correct localization of the bridge between present intention formation and anticipated future reasons/action conditions;
- **C2:** stage decomposition and persistence/revision distinctions matched established literature;
- **C3:** missed normative vs motivating/explanatory reasons and Mele's Ted counterexample;
- **C4:** none;
- new solution: no.

Overall: **mixed-positive prospective pilot**.

## BENCH-C02 — Hume's Missing Shade of Blue

Branch:

`benchmark/c02-hume-missing-shade-prospective`

Prediction seal:

`0a47759cd395a5d7ebd6c265d11a180d917e27c4`

Blind integrity: **clean under the project retrieval protocol**.

Before dedicated response literature was opened, DSD predicted that the mature fault lines would include:

1. direct corresponding impression versus relational/neighbor-supported formation;
2. gap localization versus possession of the exact qualitative idea;
3. the ordered gradation as substantive information;
4. simple content versus non-derived formation history;
5. a restricted exception versus wholesale collapse of the broader empirical principle.

Post-seal literature contained close or direct versions of all five structures:

- SEP mental mixing;
- Fogelin resemblance/color-space gap analysis;
- Cummins recognitional-capacity interpretation;
- Garrett natural-resemblance approach;
- Kelahan theoretical-posits interpretation;
- Finch empirical test;
- Earp's broader methodological survival argument.

Validation outcome:

- Prediction 1: **C1**;
- Prediction 2: **C1/C2**;
- Prediction 3: **C1**;
- Prediction 4: **C1/C2**;
- Prediction 5: **C1**;
- major miss: **C3** — the pre-seal model did not explicitly separate resemblance and causal theses within Hume's first principle;
- **C4:** none;
- new philosophical solution: no.

Overall classification:

**positive clean prospective validation**.

BENCH-C02 is the project's first clean Mode-C validation record under the explicit retrieval protocol. This is evidence for pre-literature structural localization, not historical novelty and not proof of the DSD axioms.

See:

- `benchmarks/prospective/C02_hume_missing_shade/PREDICTION.md`
- `benchmarks/prospective/C02_hume_missing_shade/SOURCE_NOTES.md`
- `benchmarks/prospective/C02_hume_missing_shade/RESULT.md`
- `benchmarks/prospective/C02_hume_missing_shade/REPRODUCIBILITY.md`

## Next-stage sequence

1. Build the first **Mode-D synthetic control set**, including premise-loading, part/whole, status/descriptor, valid-bridge, and clean/no-defect controls.
2. Preserve raw TP/TN/FP/FN/partial outcomes without merging Mode-D into the Mode-C evidence count.
3. After Synthetic Control Set 01 is closed, open PHIL-003 under the expanded protocol.

## Reproducibility rule

A completed case should contain, as applicable:

1. `PLAN.md`
2. `SOURCE_NOTES.md`
3. `RESULT.md`
4. an explicit witness/countermodel when it adds inferential value
5. `REPRODUCIBILITY.md` or `repro/`

Missing, undefined, inapplicable, absent, and defined-zero states must not be collapsed for convenience.

## Branch policy

Historical analysis branches are retained. New field work branches from the cumulative prior-field state so that previous case records remain available without rewriting history. The default branch is not force-moved by field analysis work.
