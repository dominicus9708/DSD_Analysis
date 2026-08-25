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

- `cases/philosophy_epistemology/` — PHIL-001 / Global Case 044 current campaign completed; PHIL-002 / Global 045 next

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

## Current philosophy / epistemology work

Current branch: `analysis/phil-001-refinement-stability-attack`.

Completed current campaign:

- Field ID: `PHIL-001`
- Global case: `044`
- Path: `cases/philosophy_epistemology/044_philosophical_zombie_premise_loading/`
- Topic: philosophical-zombie premise loading, modal bridge, physical-descriptor completeness, and refinement-stable uniform completion
- Result: no wholesale refutation; multiple attacks were falsified or narrowed, with a surviving under-justification pressure on ideal positive conceivability

PHIL-001 has four retained stages.

1. **Naive premise-loading attack — rejected.** Chalmers's mature argument does not merely define a zombie and infer possibility. It explicitly distinguishes prima facie/ideal, positive/negative, and primary/secondary conceivability and defends a restricted modal bridge.
2. **Simple modal-space counterattack — rejected as new refutation.** Chalmers already anticipates a positively conceivable situation with no corresponding possible world under the strong-necessity problem.
3. **Descriptor-completeness squeeze — survives but converges with prior literature.** A structural/dispositional `P` may be too weak for full physical identity; a fuller intrinsic/categorical `P` requires renewed support for ideal conceivability. This is conservatively grouped with Stoljar/Russellian lines.
4. **Refinement-stability / uniform-completion attack — partially survives.** The attack was committed before a dedicated search for its exact formulation. It separates
   `forall finite refinements F exists a zombie-like z_F`
   from
   `exists one z that survives every refinement F`.
   The former does not entail the latter. Thus repeated local detail-fillability does not by itself establish one globally complete physical duplicate. Chalmers's ideal positive conceivability is naturally intended to demand the stronger global reading, so this is a challenge to the evidential support for the premise rather than a contradiction in the mature theory.

Close prior literature on complete physical specification and positive conceivability prevents any current historical-novelty claim. The refinement result is classified as a **DSD-specific formal sharpening/recasting** pending broader literature review.

Reproducibility scripts:

```bash
python cases/philosophy_epistemology/044_philosophical_zombie_premise_loading/repro/check_modal_space_separation.py
python cases/philosophy_epistemology/044_philosophical_zombie_premise_loading/repro/check_refinement_stability.py
python cases/philosophy_epistemology/044_philosophical_zombie_premise_loading/repro/check_uniform_completion.py
```

Next case:

- `PHIL-002 / Global 045` — Chinese Room part/system understanding attribution and Systems Reply audit

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
