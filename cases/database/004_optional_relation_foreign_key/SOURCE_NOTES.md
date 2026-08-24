# Source Notes — DB-004

## DSD internal sources

### Formation Axiom System
Current Formation distinguishes undefined assignment, defined zero, defined nonzero, channel absence, and zero contribution. Operational channel identity includes the assigned value, and absent channels are not replaced by zero-valued channels.

Source: `DSD_Formation_Axiom_System_EN.pdf` (current project source).

### Axis-property system
The current axis-property paper treats typed partial assignments by their graphs, distinguishes unavailable input from undefined application, and retains zero-valued applications without conflation. It begins after Stage-VI formation and does not identify property records with formation channels.

Source: `DSD_Axioms for the Property Structure of Realized Axes_EN.pdf` (current project source).

## External database sources

### PostgreSQL 18 — CREATE TABLE
https://www.postgresql.org/docs/current/sql-createtable.html

Relevant points:

- A foreign key normally requires non-null referencing values to match a referenced row.
- Under default `MATCH SIMPLE`, if any foreign-key column is NULL, the row is not required to have a referenced-table match.
- `MATCH FULL` permits the all-NULL case but forbids a partially NULL composite foreign key.
- `NOT NULL` can be added when a null reference is not acceptable.
- Referential actions include `SET NULL`, `CASCADE`, `NO ACTION`, `RESTRICT`, and `SET DEFAULT`.

### SQLite — Foreign Key Support
https://www.sqlite.org/foreignkeys.html

Relevant points:

- The foreign-key constraint is satisfied when the child key is NULL or when a matching parent row exists.
- `NOT NULL` is needed if the application requires a mandatory parent relation.
- SQLite supports `SET NULL` and `CASCADE`; these actions have different effects on child-row survival.
- SQLite handles foreign keys as `MATCH SIMPLE` for NULL handling.

## Non-identification rule

Do not identify SQL `NULL`, a nullable foreign key, a relationship table row, or a referential action with DSD primitives by name. The comparison concerns only layered status preservation and dependency structure.
