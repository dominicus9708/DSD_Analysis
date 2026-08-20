# DSD Analysis

This repository records structured applications of **DSD Analysis (DSD 분석론)**.

DSD Analysis is not a numerical benchmark repository and does not treat cross-domain similarity as proof of the DSD axioms. Each case preserves the source discipline first, then tests which DSD distinctions are preserved, require extra encoding, fail to correspond, or reveal an actual contradiction.

## Repository organization

The repository uses two independent classification axes.

### 1. Analysis purpose

See `campaigns/`.

- `campaigns/falsification/` — direct countermodel, contradiction, and integration stress tests
- `campaigns/coherence/` — consistency and compatibility with independent formal frameworks
- `campaigns/predefinition/` — tests of hidden assumptions, premature promotion, typing/signature exclusion, and describability prerequisites
- `campaigns/reinterpretation/` — structural decomposition and application to external problem domains

### 2. External domain

Case paths are preserved under `cases/` so historical links remain stable.

- `cases/logic/` — logic, formal-framework comparison, and direct axiom stress tests
- `cases/law/` — legal / institutional decision-structure analyses
- `cases/linguistics/` — linguistics, formal semantics, pragmatics, speech acts, and adjacent institutional-language analyses
- `cases/INDEX.md` — global case number, topic, and purpose cross-index

This avoids moving or duplicating the same evidence when one case contributes to more than one campaign purpose.

## First-pass linguistics domain

`LING-001`–`LING-010` correspond to Global Cases `014`–`023`.

The first-pass domain campaign is closed as a structural reinterpretation campaign. Its aggregate record is:

- `synthesis/LINGUISTICS_CAMPAIGN_014_023.md`

The campaign preserves source-theory distinctions first and records where Formation, Axis-Property, Static Aggregation, or no stronger DSD layer is actually needed. It does not claim a DSD theory of linguistics.

New linguistic cases should be added only when they introduce a genuinely new structural node, meaningful counterpressure, a real applied case, or an empirical/computational benchmark; routine variants of already-recorded phenomena should not be counted as independent evidence.

## Common methodology

- `methodology/case_template.md` — base case template
- `methodology/analysis_taxonomy.md` — purpose classification rules
- `methodology/reproducibility_contract.md` — minimum evidence and rerun requirements

## DSD paper references

- `references/DSD_PAPERS.md` — current project paper titles, stable citation roles, and DOI registry notes

Each case must state exactly which DSD paper, section, definition, axiom, theorem, or closure clause it uses. A paper title alone is not sufficient for a completed case.

## Campaign syntheses

See `synthesis/README.md`.

Current synthesis records include:

- `synthesis/FALSIFICATION_CAMPAIGN_001_010.md` — first logic / falsification-oriented stress-test campaign
- `synthesis/LINGUISTICS_CAMPAIGN_014_023.md` — first-pass linguistics / formal-semantics campaign

Synthesis files summarize patterns and boundaries; they do not replace case-level evidence.

## Reproducibility rule

A completed case should contain, as applicable:

1. `PLAN.md` — question and falsifiable/decidable criteria
2. `SOURCE_NOTES.md` — external and DSD source claims actually used
3. `RESULT.md` — derivation and judgment, including non-correspondence and boundaries
4. an explicit finite witness/countermodel file when a small construction is possible
5. `REPRODUCIBILITY.md` or `repro/` — exact inputs, commands/scripts when needed, and expected outputs

Missing, unknown, unavailable, undefined, inapplicable, absent, defined-zero, graded, and unresolved-candidate states must not be collapsed merely for implementation convenience. A source theory may identify some of these, but that identification must be explicit and source-supported.

## Branch policy

Historical analysis branches are retained. Domain synthesis is prepared on dedicated synthesis branches; the default `main` branch is not force-moved by synthesis work.