# DB-003 / Global Case 036 — Property Existence, Applicability, and Assignment

Status: first-pass analysis in progress.

## Question

Test whether database information structure independently requires separation among:

1. a property kind being present in the schema or metadata;
2. that property being applicable to a particular entity/row/context;
3. an assignment being present for that applicable entity;
4. a defined zero versus a defined nonzero value.

A special falsification target is the common wide-table encoding in which one nullable column is used for both "not applicable" and "applicable but unassigned/unknown".

## DSD comparison targets

Formation layer:
- regime-global partial assignment domain versus undefined assignment;
- defined zero remains distinct from undefined assignment.

Axis-property layer:
- candidate property kind universe;
- globally declared property kinds;
- profile-carrier availability;
- application domain of a partial property assignment;
- undefined, defined zero, defined nonzero/defined value status.

No SQL construct will be identified with a DSD construct by definition. Only the structural separation pattern is compared.

## External database witnesses

- PostgreSQL information-schema column metadata (`columns.is_nullable`).
- PostgreSQL NOT NULL and CHECK constraint semantics.
- PostgreSQL table inheritance as one structural way to place additional attributes only on a subtype/child relation.
- A deterministic SQLite witness contrasting a single nullable wide column with an explicitly layered schema.

## Reproducibility target

The witness uses four entities. A wide table makes two rows both display `NULL` even though one is property-applicable but unassigned and the other is property-inapplicable. A layered schema separately records declaration, applicability, assignment, and defined zero/nonzero value.