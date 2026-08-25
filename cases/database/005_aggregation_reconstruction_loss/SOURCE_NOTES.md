# DB-005 Source Notes

## External database semantics

### PostgreSQL aggregate functions

Current PostgreSQL documentation states:

- `count(*)` counts input rows.
- `count(expression)` counts rows for which the expression is non-NULL.
- `sum(expression)` sums non-NULL input values.
- Except for `count`, aggregates such as `sum` return NULL when no rows are selected.
- `COALESCE` may be used to substitute zero for such NULL results when an application wants that representation.

Source: PostgreSQL current Aggregate Functions documentation.

### SQLite aggregate functions

SQLite documents the same core distinction:

- `count(X)` counts non-NULL X values.
- `count(*)` counts rows.
- `sum(X)` sums non-NULL X values and returns NULL when there are no non-NULL inputs.
- SQLite's non-standard `total(X)` instead returns 0.0 when there are no non-NULL inputs, explicitly illustrating a convenience totalization that changes the visible reduced result.

Source: SQLite Built-in Aggregate Functions documentation.

## DSD sources

### Formation Axiom System

Relevant established results:

- undefined assignment is not a value;
- zero-padding is not assignment-faithful;
- absent channel is not a zero term;
- zero-extension loses channel membership;
- distinct finite channel families may have equal composite values (Proposition 5.14).

### Channel-Indexed Static Aggregation

Relevant established results:

- support-tagged channel/property records are separated from their sums;
- summation has a nontrivial kernel when at least two independent coordinates can cancel;
- aggregate equality is not a general reconstruction theorem (Corollary 11.5);
- across varying supports, equal aggregate values do not identify which channel/property support produced them.

## Comparison boundary

SQL `NULL`, SQL row support, and DSD undefined/channel absence are not semantically identical. The comparison concerns loss of support/status information under reduced aggregation.