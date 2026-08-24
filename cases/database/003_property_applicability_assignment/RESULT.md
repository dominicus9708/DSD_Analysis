# DB-003 / Global Case 036 — Property Existence, Applicability, and Assignment

Status: **first-pass analysis completed**.

Final judgment: **strong partial structural support with an explicit encoding requirement**.

## 1. Core distinction

A database design may need to distinguish at least four levels:

1. the schema or metadata contains a property kind;
2. the property is applicable to a particular entity/context;
3. an assignment record exists for that applicable entity;
4. the assigned value is zero or nonzero.

These levels are not automatically identical in SQL.

## 2. Wide nullable-column pressure test

Consider a wide table with one nullable column `score`:

- entity 1: kind A, `score = 0`;
- entity 2: kind A, `score = NULL` because the property is applicable but currently unassigned;
- entity 3: kind B, `score = NULL` because the property is inapplicable;
- entity 4: kind A, `score = 7`.

The visible column projection makes entities 2 and 3 look the same at the value level:

```text
(2, 'A', NULL)
(3, 'B', NULL)
```

But their intended structural statuses differ. A single nullable cell therefore cannot, by itself, reconstruct whether NULL means inapplicable, applicable-but-unassigned, unknown, withheld, or another application-defined state.

## 3. Layered relational witness

The same data can be represented by three explicit relations:

- `property_kind(name)` — global declaration;
- `property_applicability(entity_id, property_name)` — entity/context applicability;
- `property_assignment(entity_id, property_name, value NOT NULL)` — assignment-domain membership and defined value.

For property `score`:

- applicability rows exist for entities 1, 2, and 4;
- assignment rows exist for entities 1 and 4 only;
- entity 1 has the defined value 0;
- entity 4 has the defined value 7;
- entity 2 is applicable but unassigned;
- entity 3 is inapplicable.

The resulting status query is:

```text
(1, 'A', applicable=1, assigned=1, value=0.0)
(2, 'A', applicable=1, assigned=0, value=None)
(3, 'B', applicable=0, assigned=0, value=None)
(4, 'A', applicable=1, assigned=1, value=7.0)
```

Thus the layered encoding separates two states that the wide nullable projection collapses.

## 4. PostgreSQL structural evidence

PostgreSQL exposes nullability as column-level metadata through `information_schema.columns.is_nullable`. A NOT NULL constraint likewise applies to the column's row values as a schema constraint. Neither mechanism alone expresses the separate semantic proposition "this property kind exists globally but is inapplicable to this particular entity".

PostgreSQL table inheritance provides one alternative structural mechanism: child tables inherit parent columns and may add additional columns. Therefore subtype-specific properties can be represented structurally rather than by putting one universally present nullable column on every base row.

This does not make inheritance the required solution. Separate subtype tables, relation tables, explicit applicability flags, constraints, and other schemas can encode the distinction as well.

## 5. DSD comparison

The current axis-property system already separates more levels than a single nullable SQL column:

1. candidate property kind `ϖ ∈ Π^b_L`;
2. declared kind `ϖ ∈ Π_A`;
3. availability of the required typed input product `X_{A,p,ϖ}`;
4. application-domain membership `x ∈ D_{A,p,ϖ}`;
5. defined zero / defined nonzero / defined value.

It explicitly distinguishes unavailable input from undefined application: the former lacks a required carrier, whereas the latter has an available input product but the chosen input is outside the partial assignment domain.

The Formation Axiom System supplies the earlier analogous distinction between membership in a partial assignment domain and a defined zero value.

Database correspondence is therefore structural rather than terminological:

| Database layer | DSD comparison | Boundary |
| --- | --- | --- |
| schema/property metadata exists | candidate/declared property kind | not identical |
| subtype or applicability relation admits property | typed input/product availability or declared applicability | encoding-dependent |
| assignment relation contains entity-property pair | partial assignment-domain membership | close structural analogy |
| assignment value 0 | defined zero | close structural analogy |
| no assignment row after applicability is known | undefined application-style status | analogy only; not SQL NULL identity |

## 6. Counterpressure against DSD

The strongest counterpressure is that SQL does **not** force these distinctions. A perfectly valid application may intentionally use one nullable column and collapse several semantic reasons for NULL. Therefore database practice does not prove that the DSD status hierarchy is mandatory in every information system.

However, once reconstruction, validation, provenance, subtype logic, or status-sensitive analysis requires those distinctions, the collapsed encoding is insufficient and explicit schema structure is needed.

This is supportive of DSD's non-conflation discipline while showing that the discipline is a modeling requirement, not a free consequence of relational syntax.

## 7. Falsification attempt

Counter-hypothesis: property declaration, applicability, and assignment can always be represented without loss by one nullable column.

The witness rejects the general form of the claim. Entity 2 and entity 3 both project to NULL under the wide encoding, but one is applicable/unassigned and the other inapplicable. The distinction becomes recoverable only after another coordinate or relation is retained.

Counter-hypothesis: a zero value can safely stand in for missing assignment.

This also fails under the layered encoding. Entity 1 belongs to the assignment relation and has value 0; entity 2 is applicable but has no assignment row. Replacing entity 2 by 0 would erase assignment-domain membership information.

## 8. Final judgment

**Strong partial structural support with explicit encoding requirement.** Database schema design independently exhibits a practical need to separate global attribute declaration, per-entity applicability, assignment presence, and defined values when those distinctions matter to reconstruction or validation.

No contradiction to the Formation or axis-property status separations was found.

The boundary is important: SQL does not natively impose the DSD hierarchy, and SQL NULL is not DSD undefined. The support lies in the fact that faithful database representations often require the same kind of layered status preservation once a single nullable field is shown to be information-losing.

## 9. Next case

DB-004 should analyze **foreign-key and optional-relation states**: no relationship row, relationship row with missing target/value information, valid target relation, and relation metadata/provenance. This will test the roadmap distinction `relation absence ≠ relation exists but value absent ≠ defined zero relation`.