# DSD Analysis — Master Source Audit

Audit date: 2026-08-26

Purpose: publication-preparation source discipline. This file does not replace case-level `SOURCE_NOTES.md` files. It specifies what must be extracted from them before a manuscript bibliography is frozen.

## Source hierarchy

Use the strongest available source for the exact claim.

1. original paper, monograph, treaty/statute, judgment, normative standard, or official rule;
2. official guidance or institutional documentation where the operational rule is the object of study;
3. peer-reviewed secondary literature for interpretation/history/comparison;
4. scholarly reference works or textbooks for stable background facts;
5. project sources only for DSD definitions, theorems, protocol states, and reproducibility records.

A DSD paper or project note is never sufficient evidence for a claim about an external discipline merely because the external structure is being mapped to DSD.

## Required bibliography fields

For every manuscript-level external citation record:

- `case_id`
- `source_key`
- `source_class`
- `authors_or_institution`
- `title`
- `container_or_instrument`
- `edition_or_version`
- `date`
- `pages_or_section_or_article`
- `doi`
- `stable_official_url`
- `access_date` when mutable
- `claim_supported`
- `normative_status`
- `notes_on_scope`

## Verified representative metadata in this audit

### Logic / partial functions

`LOGIC-001`

- John S. Fitzgerald and Cliff B. Jones, “The connection between two ways of reasoning about partial functions,” *Information Processing Letters* 107(3–4), 128–132 (2008), DOI `10.1016/j.ipl.2008.02.005`.
- Cliff B. Jones and Matthew J. Lovert, “Semantic Models for a Logic of Partial Functions,” Newcastle University Computing Science Technical Report `CS-TR-1220` (2010), later journal publication recorded by the case notes.

The case boundary remains essential: LPF undefined terms are external formal-semantic objects; they are not identified with DSD undefined assignments.

### Logic / Institution Theory

- Joseph A. Goguen and Rod M. Burstall, “Institutions: Abstract Model Theory for Specification and Programming,” *Journal of the ACM* 39(1), 95–146 (1992), DOI `10.1145/147508.147524`.

Use this for institution-level signature/model/satisfaction structure, not as evidence that DSD strict formation isomorphism is identical to institution morphisms or satisfaction-preserving translation.

### Knowledge representation / OWL 2

Use the dated W3C Recommendation rather than an undated tutorial page as the normative target:

- Boris Motik, Peter F. Patel-Schneider, Bernardo Cuenca Grau (eds.), *OWL 2 Web Ontology Language: Direct Semantics (Second Edition)*, W3C Recommendation, 11 December 2012.
- Related structural claims should cite the corresponding *OWL 2 Web Ontology Language: Structural Specification and Functional-Style Syntax (Second Edition)*, W3C Recommendation, 11 December 2012.

The manuscript must distinguish declaration syntax, model-theoretic satisfaction, existential entailment, naming, and identity. Do not summarize all OWL behavior as a generic “open-world = unknown” slogan.

### Provenance / W3C PROV

- Timothy Lebo, Satya Sahoo, Deborah McGuinness (eds.), *PROV-O: The PROV Ontology*, W3C Recommendation, 30 April 2013.

PROV-O explicitly represents provenance concepts using OWL 2 and is appropriate for provenance-sensitive comparison. When a claim depends on the PROV data model or constraints rather than the ontology encoding, cite the corresponding `PROV-DM` or `PROV-CONSTRAINTS` Recommendation instead of PROV-O alone.

### Philosophy / Mary's Room source anchor

- Frank Jackson, “Epiphenomenal Qualia,” *The Philosophical Quarterly* 32 (1982), 127–136, DOI `10.2307/2960077`.

Use the original Jackson paper for the source thought experiment. Secondary “knowledge argument” literature should be cited separately for later interpretations and historical-convergence claims.

## Legal and institutional source rule

For law and institutional cases, a correct URL alone is not enough. Record jurisdiction, issuing body, provision/rule/article, and operative version/date.

The existing `LAW-001` cross-jurisdiction revalidation packet is a strong template because it separates, among others:

- UN General Assembly voting rules;
- TFEU Article 238(4);
- Australian Electoral Commission materials;
- UK Electoral Commission guidance;
- UNIDROIT Principles Article 2.1.6;
- Rome Statute Article 66;
- ECHR presumption-of-innocence materials;
- U.S. Ninth Circuit model criminal instructions;
- UK CPS guidance.

Publication use must preserve the fact that these are distinct source regimes. Their convergence may support a structural comparison, but they do not collectively form one universal positive-law rule.

## Mathematics source rule

Elementary identities proved directly in the manuscript need not be overloaded with citations. However:

- standard named constructions (free commutative monoid, quotient, kernel, direct sum, complete invariant, etc.) should be referenced when terminology or a nontrivial theorem is invoked;
- DSD-specific statements must cite the exact DSD definition/proposition/theorem, not just `references/DSD_PAPERS.md`;
- a standard mathematical analogy must never be presented as an identity unless the required structure-preservation theorem has been proved.

## Software / database source rule

For computer-science and database claims, classify each source as one of:

- language/runtime specification;
- security standard/guideline;
- database/SQL standard;
- vendor implementation documentation;
- research literature;
- illustrative incident/example.

Pin versions. Do not use current vendor documentation to make an unqualified statement about all SQL, all parsers, all authorization systems, or all workflow engines.

## Philosophy source rule

Separate four bibliography roles:

1. original thought experiment/source argument;
2. established replies or objections;
3. later interpretive literature;
4. DSD project analysis.

For Mode C, the source chronology must also preserve what literature was available before the prediction was sealed and what was opened only afterward. The bibliography itself must not erase this protocol boundary.

## Citation language rules

Use:

- `the source rule states...`
- `under this jurisdiction/standard/version...`
- `this provides a counterexample to the stronger mapping...`
- `the DSD correspondence is partial...`

Avoid:

- `the field proves DSD...`
- `this standard uses the DSD concept...`
- `the same concept` when only an analogous structural role is established.

## Remaining source work before manuscript freeze

This audit spot-checked representative logic, W3C, law, and philosophy records. It is **not a claim that every citation in every branch has been independently reverified**.

Before submission, each case selected for the manuscript must receive a final line-by-line source audit against its `SOURCE_NOTES.md`, with bibliographic metadata normalized into one BibTeX or equivalent master database.
