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

- `cases/philosophy_epistemology/` — PHIL-001 / Global Case 044 current campaign completed; PHIL-002 / Global 045 first pass completed

See `cases/INDEX.md` for the global case map.

## Common methodology

- `methodology/case_template.md` — base case template
- `methodology/analysis_taxonomy.md` — purpose classification rules
- `methodology/reproducibility_contract.md` — minimum evidence and rerun requirements
- `methodology/four_mode_validation_protocol.md` — four-mode validation protocol
- `methodology/prospective_blind_case_template.md` — prospective/blind prediction-seal template
- `methodology/synthetic_control_case_template.md` — blinded synthetic-control template

A completed case must preserve non-correspondence and failed mappings rather than forcing every external concept into DSD terminology.

## Four-mode validation protocol

Future validation campaigns distinguish four result modes instead of counting all favorable-looking cases together.

1. **Negative-control / failure recording** — DSD must be able to reject its own initially plausible attack or mapping.
2. **Historical convergence / independent rediscovery** — DSD independently reaches a structure already established in an external literature, then records the overlap without claiming novelty.
3. **Prospective / blind prediction** — the DSD prediction is timestamped before dedicated objection/reply literature is opened, then compared after unblinding.
4. **Synthetic / controlled cases** — hidden ground-truth mechanisms and clean controls are used to measure false positives and false negatives as well as successful detection.

These modes answer different questions and must not be merged into a single success count.

The intended cumulative claim is methodological, not metaphysical:

`DSD distinctions repeatedly function as useful analytical operators under controlled and externally calibrated tests`.

No combination of these validation modes by itself proves the Formation Axiom System or Axis-Property Axiom System true as a description of fundamental reality.

## DSD paper references

- `references/DSD_PAPERS.md` — current project paper titles, stable citation roles, and DOI registry notes

Each completed case should state the exact DSD paper section, definition, axiom, theorem, or closure clause actually used. A paper title alone is not sufficient.

## Completed synthesis points

- `synthesis/FALSIFICATION_CAMPAIGN_001_010.md` — first logic/falsification campaign
- `cases/computer_science/CS_001_005_FIRST_PASS_SYNTHESIS.md` — computer-science first pass
- `cases/database/SYNTHESIS.md` — database/information-structure first pass
- `cases/knowledge_representation/SYNTHESIS.md` — knowledge-representation first pass

The knowledge-representation sequence K_R-001–005 is conservatively grouped into two external formal families:

1. OWL 2 semantic family;
2. RDF Dataset + W3C PROV provenance family.

The second family reinforces, rather than double-counts, the broader support/provenance-retention pattern already observed in database analysis and DSD static aggregation.

## Current philosophy / epistemology work

Current active branch: `analysis/phil-002-chinese-room-part-whole-audit`.

### PHIL-001 / Global 044

Current campaign completed.

Retained pattern:

1. naive premise-loading attack rejected;
2. simple modal-space counterattack rejected as a new refutation;
3. descriptor-completeness squeeze survives but converges with Stoljar/Russellian literature;
4. refinement-stability / uniform-completion formalization partially survives as an under-justification pressure, not as a wholesale refutation or clean blind novelty result.

### PHIL-002 / Global 045

First-pass historical-convergence audit completed.

Source-level result:

- `not U(operator)` does not entail `not U(system)`;
- this is the classic Systems Reply already present in the 1980 debate;
- Searle’s internalization response does not by itself identify the host person with every system-level or realized cognitive bearer;
- later Virtual Mind variants make that bearer distinction explicit;
- DSD therefore converges strongly with the Systems/Virtual-Mind family rather than producing a novel objection;
- Searle’s stronger syntax/semantics and biological-naturalist claims remain separate and are not refuted by this part/whole audit.

PHIL-002 intentionally contains no Python witness because a toy computation would not add evidential value to a bearer-attribution argument.

## Next-stage sequence

1. Select the first **clean prospective/blind benchmark** whose dedicated objection/reply literature has not yet been reviewed. Seal its `PREDICTION.md` using `methodology/prospective_blind_case_template.md` before unblinding.
2. Prepare the first **synthetic control set** in parallel using `methodology/synthetic_control_case_template.md`, including at least one clean/no-defect control and preserving false positives/false negatives.
3. Only after those two validation tracks are prepared should PHIL-003 be opened under the expanded protocol.

## Reproducibility rule

A completed case should contain, as applicable:

1. `PLAN.md` — question and falsifiable/decidable criteria
2. `SOURCE_NOTES.md` — external and DSD source claims actually used
3. `RESULT.md` — derivation and judgment, including non-correspondence and boundaries
4. an explicit witness/countermodel when a small construction is meaningful
5. `REPRODUCIBILITY.md` or `repro/` — exact inputs, scripts/commands, and expected outputs when computation is used

Missing, undefined, inapplicable, absent, and defined-zero states must not be collapsed for convenience.

## Branch policy

Historical analysis branches are retained. New field work branches from the cumulative prior-field state so that previous case records remain available without rewriting history. The default branch is not force-moved by field analysis work.