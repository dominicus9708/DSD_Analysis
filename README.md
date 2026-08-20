# DSD Analysis

This repository records structured applications of **DSD Analysis (DSD 분석론)**.

DSD Analysis is not a numerical benchmark repository and does not treat cross-domain similarity as proof of the DSD axioms. Each case preserves the source discipline first, then tests which DSD distinctions are preserved, require extra encoding, fail to correspond, or reveal an actual contradiction.

## Repository organization

The repository now uses two independent classification axes.

### 1. Analysis purpose

See `campaigns/`.

- `campaigns/falsification/` — direct countermodel, contradiction, and integration stress tests
- `campaigns/coherence/` — consistency and compatibility with independent formal frameworks
- `campaigns/predefinition/` — tests of hidden assumptions, premature promotion, typing/signature exclusion, and describability prerequisites
- `campaigns/reinterpretation/` — structural decomposition and application to external problem domains

### 2. External domain

Existing case paths are preserved under `cases/` so that prior links and case history remain stable.

- `cases/logic/001_...` through `cases/logic/010_...` — completed mathematical/philosophical logic and direct axiom stress-test cases
- new cases continue in their domain path and are cross-indexed from the relevant campaign page

This avoids moving the same case between folders when one case is relevant to more than one analysis purpose.

## Common methodology

- `methodology/case_template.md` — base case template
- `methodology/analysis_taxonomy.md` — purpose classification rules
- `methodology/reproducibility_contract.md` — minimum evidence and rerun requirements

## DSD paper references

- `references/DSD_PAPERS.md` — current project paper titles, stable citation roles, and DOI registry notes

Each case must state exactly which DSD paper, section, definition, axiom, theorem, or closure clause it uses. A paper title alone is not sufficient for a completed case.

## Completed campaign

Cases 001–010 contain the first logic/falsification campaign. The aggregate record remains in:

- `synthesis/FALSIFICATION_CAMPAIGN_001_010.md`

Existing case directories and historical branches are intentionally preserved.

## Next prepared analysis

The next non-falsification workstream is **coherence / consistency comparison**.

Prepared case:

- Global case: `011`
- Purpose ID: `COH-001`
- Path: `cases/logic/011_formation_partiality_closure_coherence/`
- Primary target: the DSD Formation Axiom System
- Core question: whether its partiality, typed formation stages, primitive/closure separation, and structure-preserving comparison layers can be jointly interpreted without hidden contradiction in standard set-theoretic and typed formal settings.

The preparation separates source notes, analysis plan, reproducibility requirements, and result recording so the conclusion is not embedded in the setup.

## Reproducibility rule

A completed case should contain, as applicable:

1. `PLAN.md` — question and falsifiable/decidable criteria
2. `SOURCE_NOTES.md` — external and DSD source claims actually used
3. `RESULT.md` — derivation and judgment, including non-correspondence and boundaries
4. an explicit finite witness/countermodel file when a small construction is possible
5. `REPRODUCIBILITY.md` or `repro/` — exact inputs, commands/scripts when needed, and expected outputs

Missing, undefined, inapplicable, absent, and defined-zero states must not be collapsed for convenience in reproducibility code.

## Branch note

The repository's historical analysis branches are retained. This reclassification work is prepared on `reorg/analysis-taxonomy`, based on the cumulative `analysis/case-010-integrated-countermodel` state. The default `main` branch is not force-moved by this reorganization.