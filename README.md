# DSD Analysis

This repository records structured applications of **DSD Analysis (DSD 분석론)**.

DSD Analysis is not a numerical benchmark repository and does not treat resemblance across fields as proof of the DSD axioms. Each domain preserves its own source concepts first, then records which DSD distinctions correspond directly, require additional encoding, fail to correspond, or expose a contradiction or scope boundary.

## Repository organization

The repository uses two independent classification axes.

### Analysis purpose

See `campaigns/`.

- `campaigns/falsification/` — direct countermodel, contradiction, and integration stress tests
- `campaigns/coherence/` — consistency and compatibility checks against independent formal structures
- `campaigns/predefinition/` — hidden assumptions, premature promotion, typing/signature exclusion, and predefinition audits
- `campaigns/reinterpretation/` — structural decomposition and disciplined application to external domains

### External domain

Case evidence remains under `cases/`.

- `cases/logic/` — Global Cases `001–011`; current recorded formal-logic and direct-axiom audit sequence complete through Case 011
- `cases/law/` — Global Cases `012–025`, domain IDs `LAW-001–014`; foundation sequence closed
- `cases/administration/` — Global Cases `026–027`, domain IDs `ADMIN-001–002`; active sequence
- `cases/mathematics/` — Global Cases `028–032`, domain IDs `MATH-001–005`; first-pass foundation closed
- `cases/linguistics/` — domain IDs `LING-001–010`; first-pass campaign complete and reconciled from the historical `synthesis/linguistics-first-pass` branch

Domains that exist only as Notion roadmaps are not represented by empty GitHub case folders. A GitHub domain folder is created when the first evidence-bearing case is recorded.

## Case numbering rule

`Global Case` is unique only in the reconciled cumulative index `cases/INDEX.md`.

A historical linguistics branch assigned the numeric prefixes `014–023` before the later legal sequence occupied those cumulative Global Case numbers. Those linguistics directory prefixes are preserved as historical paths and **must not be interpreted as current Global Case IDs**. Their stable identifiers are `LING-001–010`.

Future newly opened cases use the next available reconciled Global Case number. After the current cumulative sequence `001–032`, the next new Global Case is `033`.

## Domain status

### Logic

The first formal-logic/falsification campaign `001–010` is complete, and Global Case `011` adds the Formation partiality/typing/closure coherence audit. No additional logic case is scheduled merely to extend numbering. Reopen the domain when a new formal claim or specific vulnerability requires it.

See `cases/logic/README.md` and `synthesis/LOGIC_FORMAL_AUDIT_001_011.md`.

### Law

`LAW-001–014` is closed as the legal foundation sequence. Specialized legal applications, maintenance, and new counterexamples may be added without reopening the completed foundation by default.

See `cases/law/README.md` and the law-local synthesis files.

### Administration / organization

`ADMIN-001–002` are complete. The domain remains open; the next planned case is review, revision, reopening, and organizational error correction under changing information.

See `cases/administration/README.md`.

### Mathematics / algebra

`MATH-001–005` and their synthesis/closure audit are complete. No `MATH-006` is opened by default. The domain is reopened only when a new theorem, application, or review question crosses an identified mathematical boundary.

See `cases/mathematics/README.md`, `cases/mathematics/CLOSURE.md`, and `synthesis/MATHEMATICS_ALGEBRA_028_032.md`.

### Linguistics / formal semantics

`LING-001–010` is a completed first-pass campaign. Its evidence is retained under `cases/linguistics/`; its historical numeric directory prefixes are preserved for provenance while domain-local IDs are authoritative after reconciliation.

See `cases/linguistics/README.md` and `synthesis/LINGUISTICS_CAMPAIGN_014_023.md`.

## Synthesis index

See `synthesis/README.md` for completed synthesis and closure documents.

## Common methodology

- `methodology/case_template.md` — base case template
- `methodology/analysis_taxonomy.md` — purpose classification rules
- `methodology/reproducibility_contract.md` — minimum evidence and rerun requirements

A completed case should record the actual source claims used, the exact DSD interface invoked, the result, decisive witnesses/counterexamples where useful, and reproducibility information when computation is material.

Missing, undefined, inapplicable, absent, selected-zero, and defined-zero states must not be collapsed merely for implementation convenience.

## DSD paper references

- `references/DSD_PAPERS.md` — project paper titles, citation roles, and DOI registry notes

Each completed case should identify the DSD paper section, definition, axiom, theorem, or closure clause actually used. A paper title alone is not sufficient evidence.

## Branch policy

Historical analysis branches are retained as research provenance. Reorganization work does not force-move the default `main` branch. Reconciliations preserve old paths whenever practical and record numbering or scope changes explicitly rather than silently rewriting past evidence.
