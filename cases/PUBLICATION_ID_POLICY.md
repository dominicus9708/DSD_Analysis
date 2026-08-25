# DSD Analysis — Publication Case Identifier Policy

Effective for publication preparation: 2026-08-26.

## Rule

The authoritative identifier of a DSD Analysis case is its **domain-local ID**, not its historical `Global Case` number.

Authoritative namespaces:

- `LOGIC-*`
- `COH-*`
- `LAW-*`
- `LING-*`
- `ADMIN-*`
- `MATH-*`
- `CS-*`
- `DB-*`
- `K_R-*`
- `PHIL-*`
- `BENCH-*`
- `SYNTH-*`

## Reason

Historical `Global Case` numbers were allocated independently in parallel branches and are not globally unique.

Confirmed collisions:

- historical law Global `012–025` overlaps linguistics Global `014–023`;
- historical administration Global `026–028` and computer-science Global `029–033` overlap mathematics Global `028–032`.

## Preservation rule

Do not mass-rename historical directories or rewrite old audit trails solely to remove these collisions. Existing Global numbers remain legacy branch-local aliases so old links and audit history remain reproducible.

## Manuscript rule

A paper, appendix, figure, table, dataset, or bibliography cross-reference should cite cases by domain-local ID, for example `LAW-009`, `LING-006`, `MATH-003`, or `PHIL-004`.

If one continuous number series is later required for a publication appendix, create a new publication-only registry with columns:

`publication_no | domain_local_id | legacy_global_alias | title | frozen_commit`

The new registry must not overwrite the historical identifiers.
