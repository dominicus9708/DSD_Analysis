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

Prepared next domain:

- `cases/philosophy_epistemology/` — starting with PHIL-001 / Global Case 044

See `cases/INDEX.md` for the global case map.

## Common methodology

- `methodology/case_template.md` — base case template
- `methodology/analysis_taxonomy.md` — purpose classification rules
- `methodology/reproducibility_contract.md` — minimum evidence and rerun requirements

A completed case must preserve non-correspondence and failed mappings rather than forcing every external concept into DSD terminology.

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

## Current prepared analysis

Next field: **Philosophy / Epistemology / Thought-Experiment Audit**.

Preparation branch: `analysis/philosophy-epistemology-preparation`.

Prepared case:

- Field ID: `PHIL-001`
- Global case: `044`
- Path: `cases/philosophy_epistemology/044_philosophical_zombie_premise_loading/`
- Topic: philosophical-zombie premise loading and admissibility audit
- Status: preparation only; no conclusion precommitted

The field begins by separating explicit setup, narrator information, internal observer access, derived consequences, hidden conclusion-equivalent assumptions, rival compatible structures, and bridge principles.

## Reproducibility rule

A completed case should contain, as applicable:

1. `PLAN.md` — question and falsifiable/decidable criteria
2. `SOURCE_NOTES.md` — external and DSD source claims actually used
3. `RESULT.md` — derivation and judgment, including non-correspondence and boundaries
4. an explicit witness/countermodel when a small construction is meaningful
5. `REPRODUCIBILITY.md` or `repro/` — exact inputs, scripts/commands, and expected outputs when computation is used

Missing, undefined, inapplicable, absent, and defined-zero states must not be collapsed for convenience.

## Branch policy

Historical analysis branches are retained. New field work branches from the cumulative prior-field state so that previous case records remain available without rewriting history. The default branch is not force-moved by field preparation work.
