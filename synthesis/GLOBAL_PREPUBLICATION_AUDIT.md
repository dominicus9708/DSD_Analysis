# DSD Analysis — Global Prepublication Audit

Audit date: 2026-08-26

Status: first-pass cross-domain corpus substantially complete; **not yet publication-frozen**.

This document audits the DSD Analysis corpus for later manuscript use. It does not re-score substantive results. It checks identifier integrity, source traceability, terminology, evidence accounting, branch reproducibility, stale status notes, and claim scope.

## 1. Corpus status

Completed or provisionally closed first-pass domain families currently recorded across project branches and Notion:

- Logic / philosophical logic: `LOGIC-001–010` plus `COH-001`.
- Law / institutions / decision formation: `LAW-001–014`.
- Linguistics / formal semantics: `LING-001–010`.
- Administration / organization / instruction structure: `ADMIN-001–003`.
- Mathematical structure / algebra: `MATH-001–005`.
- Computer science / types / program semantics: `CS-001–005`.
- Database / information structure: `DB-001–005`.
- Knowledge representation / ontology / classification: `K_R-001–005`.
- Philosophy / epistemology / thought-experiment audit: `PHIL-001–005`.

The philosophy validation records `BENCH-C01`, `BENCH-C02`, and `SYNTH-D01` remain calibration records, not additional domain cases.

## 2. Critical identifier finding

### 2.1 Historical `Global Case` numbers are not globally unique

Parallel branches independently allocated global-looking numbers. Confirmed collisions include:

- Law uses Global `012–025`, while the linguistics branch uses Global `014–023`.
- Administration uses Global `026–028` and computer science uses Global `029–033`, while the mathematics branch uses Global `028–032`.

Therefore historical `Global Case` numbers **must not be used as authoritative publication identifiers**.

### 2.2 Publication identifier policy

Authoritative identifiers are the domain-local IDs:

`LOGIC-*`, `COH-*`, `LAW-*`, `LING-*`, `ADMIN-*`, `MATH-*`, `CS-*`, `DB-*`, `K_R-*`, `PHIL-*`, `BENCH-*`, `SYNTH-*`.

Historical global numbers are retained only as legacy branch-local aliases. Do not rename historical directories solely to repair the old sequence, because that would damage reproducibility links and branch history.

If a paper later needs one numeric appendix index, generate a **new publication-only registry** from the domain-local IDs and preserve the legacy number as a separate alias column.

## 3. Canonical-branch finding

The repository default branch is not a publication snapshot. Substantive work is distributed over analysis and synthesis branches. In particular:

- `synthesis/philosophy-first-pass` contains the cumulative logic/law/administration/computer-science/database/knowledge-representation/philosophy corpus.
- `synthesis/linguistics-first-pass` contains the linguistics first-pass synthesis.
- `synthesis/math-028-032-first-pass-closure-audit` contains the mathematics first-pass synthesis.

The current audit branch is a coordination layer only. It does not pretend that linguistics and mathematics have already been content-merged into the cumulative branch.

Before a manuscript release, create one immutable publication snapshot (branch/tag/release) containing or unambiguously pinning all cited case files and exact commit hashes.

## 4. Source and citation audit

### 4.1 What is already strong

Many completed cases preserve source-side material separately from DSD interpretation, commonly through `SOURCE_NOTES.md`, `RESULT.md`, witness/countermodel files, and contradiction audits. This is the correct architecture for publication.

Law revalidation work is especially strong where it uses primary or official institutional sources and records jurisdiction-specific counterpressure instead of promoting one jurisdiction into a universal legal rule.

The logic corpus also demonstrates an appropriate boundary discipline: external formal results are stated first, followed by explicit non-identification clauses such as `LPF undefined != DSD undefined assignment`.

### 4.2 What remains before paper submission

A distributed source packet is not yet a manuscript bibliography. Before submission, build a master source table/BibTeX database containing for every externally cited claim:

- domain-local case ID;
- exact author/institution;
- exact title;
- publication/standard/case version and date;
- DOI or stable official URL;
- exact section/article/page when the claim depends on a narrow passage;
- access date for mutable web guidance;
- source class: primary, standard, official guidance, peer-reviewed secondary, textbook/reference, or project source;
- the exact claim supported by that source;
- whether the source is normative, descriptive, illustrative, or counterexample evidence.

No paper claim should rely only on the DSD internal registry when the claim concerns an external field.

### 4.3 Version-sensitive sources

The following families require version pinning in a manuscript:

- W3C Recommendations such as OWL 2 and PROV;
- software/security/database documentation and language/runtime specifications;
- election, court, administrative, and organizational guidance;
- legal instruments, model instructions, or case-law summaries where jurisdiction and effective version matter.

For stable standards, cite the dated Recommendation edition as well as the current landing page where useful.

## 5. Stale-status audit

Several pages were written as handoff notes and later became stale after downstream work completed. These should not be read as current tasks in a paper-preparation workflow.

Confirmed examples:

- The four-mode validation protocol still contained an instruction to open `PHIL-003`, although `PHIL-001–005` are now complete.
- The database synthesis handed off to `K_R-001`, although `K_R-001–005` are now complete.
- The knowledge-representation synthesis handed off to philosophy, although `PHIL-001–005` are now complete.

These are workflow-history issues, not substantive contradictions. Notion should mark them as historical handoffs or replace them with the current state.

## 6. Terminology and prose policy for a later manuscript

### 6.1 Preferred scope language

Prefer:

- `within the audited cases`;
- `no direct contradiction was found under the declared interpretation map`;
- `structural convergence`;
- `partial correspondence`;
- `requires an additional bridge`;
- `historical convergence`;
- `prospective record under the project protocol`;
- `small synthetic-control baseline`.

Avoid unqualified forms such as:

- `DSD is validated`;
- `DSD proved the field`;
- `universal law`;
- `100% accuracy` from `SYNTH-D01`;
- `new philosophical refutation` before novelty and priority review;
- `independent evidence` merely because two examples appear in different paragraphs.

### 6.2 Stable distinctions

The following distinctions survived multiple domains and are suitable as synthesis-level mechanisms, provided each is linked to its actual source families rather than counted by raw case total:

1. missing / unavailable / undefined / defined-zero / defined-nonzero are not automatically one state;
2. candidate / admitted / realized / assigned / effective are not automatically one state;
3. role, authority, relation, and effect require source-defined bridges;
4. later repair, inference, or effect does not rewrite the earlier state;
5. same reduced output does not automatically identify the source structure, support, provenance, or full descriptor;
6. constitutive dependence and inverse reconstruction are different questions;
7. snapshot equality does not automatically imply diachronic preservation;
8. stronger conclusions require an explicit bridge premise or interpretation rule.

These are cross-domain recurrence candidates, not a proof-by-analogy theorem.

## 7. Evidence-accounting policy

Raw case count is not an evidence count.

Group evidence by genuinely independent external formal families or mechanisms. Repeated examples inside one standard, jurisdiction, philosophical family, or shared formal mechanism should normally be clustered. Preserve negative controls, misses, and failed mappings in the same registry as positive correspondences.

Mode A, B, C, D, and precedent convergence answer different questions and must remain separate. They must not be added into a single validation percentage.

## 8. Domain-by-domain publication risk summary

| Domain | First-pass status | Main manuscript risk |
|---|---|---|
| Logic | closed | exact bibliography and theorem/source mapping must be centralized |
| Law | closed | jurisdiction-specific rules must not be universalized; cite primary/official sources precisely |
| Linguistics | closed on separate synthesis branch | branch integration and exact primary/secondary literature mapping |
| Administration | provisionally closed | organizational manuals are examples, not one universal theory |
| Mathematics | closed on separate synthesis branch | legacy global-ID collision; distinguish standard mathematics from DSD-specific claims |
| Computer science | provisionally closed | pin language/runtime/security documentation versions and distinguish implementation from semantics |
| Database | closed | distinguish SQL/DBMS conventions from DSD states; mark completed KR handoff as historical |
| Knowledge representation | closed | cite exact OWL 2 / RDF / PROV Recommendation sections; preserve open-world/identity/provenance boundaries |
| Philosophy | closed | novelty/priority restraint, exact primary works, Mode separation, no generalization from small controls |

## 9. Manuscript architecture recommended by this audit

A paper should not simply narrate every case in chronological order. A more defensible structure is:

1. DSD Analysis scope and non-claims;
2. corpus construction and case-registration rules;
3. source-first comparison protocol and interpretation maps;
4. failure/negative-control policy;
5. cross-domain mechanisms grouped by structural distinction;
6. representative cases from independent source families;
7. prospective and synthetic-control records as separate calibration sections;
8. non-correspondence and application-boundary results;
9. limitations and threats to validity;
10. appendix containing the authoritative domain-local case registry and source matrix.

This structure makes failed mappings and non-independence visible rather than hiding them behind a positive case count.

## 10. Publication readiness checklist

A manuscript should be considered publication-frozen only after all of the following are complete:

- authoritative domain-local case registry frozen;
- historical Global-ID collision documented and excluded from manuscript identifiers;
- one integrated or commit-pinned repository snapshot created;
- master bibliography/source matrix completed;
- all dynamic/official web sources versioned or access-dated;
- stale workflow handoffs removed or marked historical;
- Korean/English terminology and hyphenation normalized;
- every synthesis claim traced to representative independent source families;
- every novelty statement given a dedicated prior-art search or softened appropriately;
- every prospective/synthetic result reports raw outcomes and protocol limitations;
- final grammar, notation, DOI, section-number, and cross-reference pass completed;
- reproducibility instructions tested from the frozen snapshot.

## 11. Current audit verdict

The first-pass DSD Analysis corpus is **structurally usable for manuscript preparation but not yet publication-frozen**.

No corpus-wide substantive contradiction was identified in this audit from the current synthesis records. The most serious confirmed problems are documentary: non-unique historical Global IDs, branch fragmentation, incomplete centralized bibliography, and stale workflow handoffs. Those issues can materially damage traceability or create misleading claims if ignored, but they do not by themselves invalidate the individual analyses.
