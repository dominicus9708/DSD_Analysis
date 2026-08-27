# DSD Analysis — Domain Paper Preparation

Status: manuscript-preparation layer; not publication-frozen.

Base state: `synthesis/free-speech-structural-analysis-draft`, itself descended from `synthesis/global-prepublication-audit`.

This directory converts completed or provisionally closed first-pass DSD Analysis domains into manuscript-ready planning packages. It does not rewrite detailed case records.

## Canonical domain scope

- Logic/coherence: main analyses 001–010 + `COH-001`.
- Law/institutions/decision: `LAW-001–014`.
- Linguistics/formal semantics: `LING-001–010`.
- Administration/organization/instructions: `ADMIN-001–003`.
- Mathematical structures/algebra: `MATH-001–005`.
- Computer science/types/program semantics: `CS-001–005`.
- Databases/information structures: `DB-001–005`.
- Knowledge representation/ontology/classification: `K_R-001–005`.
- Philosophy/epistemology/thought experiments: `PHIL-001–005`.
- Free speech/listener autonomy/social non-equivalence: exploratory `SYNTH-*` candidate only; no formal ID yet.

## Identifier rule

Publication-authoritative IDs are domain-local (`LOGIC-*`, `COH-*`, `LAW-*`, `LING-*`, `ADMIN-*`, `MATH-*`, `CS-*`, `DB-*`, `K_R-*`, `PHIL-*`, `BENCH-*`, `SYNTH-*`). Historical `Global Case` numbers are branch-local aliases and must not be used as publication identifiers.

## Common manuscript skeleton

1. Research question and scope.
2. Minimal DSD Analysis method.
3. External-domain source semantics and source rules.
4. Case-selection and failure controls.
5. Representative mechanisms/cases.
6. DSD correspondence and non-correspondence.
7. Counterexamples, bridge requirements, undetermined cases.
8. Discussion and novelty limits.
9. Conclusion.
10. Appendices: case registry, claim-source matrix, reproducibility.

## Common publication gate

- freeze master BibTeX and claim-source matrix;
- pin editions, versions, clauses, standards, and access dates;
- freeze case registry and commit SHAs;
- preserve failed mappings, counterexamples, `EXTRA-BRIDGE REQUIRED`, and `UNDETERMINED` outcomes;
- separate source-derived claims, DSD interpretation, and normative bridge claims;
- perform prior-art audit before novelty wording is frozen.

See each domain subdirectory for the manuscript angle and remaining gates.