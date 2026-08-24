# DB-003 Source Notes

## DSD primary sources

### Formation Axiom System
The current Formation Axiom System uses a regime-global partial assignment
`q_{L,λ}: Q_{L,λ} -> V_{L,λ}` with `Q_{L,λ} ⊆ A^*_L`. Inputs outside the domain are undefined and are not identified with the distinguished zero. Channel formation requires graph membership in the configuration-local assignment graph.

Primary project source: `DSD_Formation_Axiom_System_EN.pdf`.

### Axis-property system
The current axis-property system separates:
- candidate property-kind universe `Π^b_L`;
- globally declared kinds `Π_A ⊆ Π^b_L`;
- availability of typed input carrier products `X_{A,p,ϖ}`;
- partial property assignments `Ξ_{A,p,ϖ}: X_{A,p,ϖ} ⇀ Z_{L,ϖ}`;
- application domains `D_{A,p,ϖ}=Dom(Ξ_{A,p,ϖ})`;
- statuses `undeclared`, `unavailable input`, `undefined`, `defined zero`, `defined nonzero` or `defined value`.

The manuscript explicitly states that unavailable input and undefined application are distinct, and that undefined is not zero.

Primary project source: `DSD_Axioms for the Property Structure of Realized Axes_EN.pdf`.

## External database sources

### PostgreSQL Information Schema — columns
https://www.postgresql.org/docs/17/infoschema-columns.html

The `columns` view records metadata for table/view columns. `is_nullable` is `YES` if a column is possibly nullable and `NO` if it is known not nullable. This is schema/column-level metadata, not a per-row applicability flag.

### PostgreSQL Constraints
https://www.postgresql.org/docs/16/ddl-constraints.html

A `NOT NULL` constraint specifies that a column must not assume the null value. PostgreSQL also notes that a CHECK constraint is satisfied when its expression evaluates to true or null, so CHECK alone does not generally exclude nulls unless null handling is made explicit.

### PostgreSQL CREATE TABLE / inheritance
https://www.postgresql.org/docs/current/sql-createtable.html

PostgreSQL table inheritance permits a child table to inherit parent columns and add additional columns. This is one concrete database design mechanism that can structurally associate additional attributes with a subtype instead of placing one nullable column on every parent row.

## Non-identification rules

- SQL column declaration is not literally a DSD candidate or declared property kind.
- SQL NULL is not DSD undefined assignment.
- Row/subtype membership is not literally DSD typed-carrier availability.
- A separate assignment table is only an encoding witness for layered information structure.

The comparison is limited to whether independently designed database structures benefit from preserving the distinctions among declaration, applicability, assignment-domain membership, and defined values.