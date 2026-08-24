# DB-002 Source Notes

## DSD primary source

Kwon Dominicus, *Formation Axiom System: Dimensional-Structural Describability*.

Relevant clauses and results:

- Primitive Axiom V: regime-global partial assignment.
- Definitional Closure Clause VI: channel membership requires configuration describability, assignment-graph membership, and role; failure of any required condition yields channel absence, not a zero-valued channel.
- Formation trace: records the restriction-realization witness that forms an operational channel.
- Proposition 5.12: an absent channel is not a zero term.

The comparison in DB-002 uses only the dependency/status pattern. A SQL result row is not identified with a DSD channel.

## External database sources

### PostgreSQL 17 — Table Expressions

https://www.postgresql.org/docs/17/queries-table-expressions.html

Claims used:

- INNER JOIN produces one joined row for each pair satisfying the join condition.
- LEFT OUTER JOIN adds a null-extended output row for each unmatched left row.
- WHERE is applied after FROM processing; rows are kept only when the condition is true, while false or null conditions discard the row.
- ON and WHERE are not generally interchangeable for outer joins.

### PostgreSQL 17 — EXPLAIN

https://www.postgresql.org/docs/17/using-explain.html

Claim used as corroboration:

- An outer-join Join Filter can fail while the row is still emitted as a null-extended row, whereas a plain Filter is applied after outer-join rules and removes rows unconditionally.

### SQLite — SELECT

https://www.sqlite.org/lang_select.html

Claims used:

- LEFT JOIN adds one output row with NULL right-side columns for each unmatched left row after ON/USING filtering.
- WHERE is processed after outer-join null-extension.
- For outer joins, moving a condition between ON and WHERE can change the result.

## Reproducibility boundary

SQLite is used only for the deterministic finite witness because it is available in the Python standard library. The semantic claims are checked against PostgreSQL and SQLite documentation rather than inferred from the witness alone.