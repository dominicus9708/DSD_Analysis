# DB-001 Source Notes

## DSD sources

### Formation Axiom System
Kwon Dominicus, *Formation Axiom System: Dimensional-Structural Describability*.

Relevant distinctions:
- quantity assignment is a genuine partial assignment with an explicit domain;
- defined zero can support an admitted channel;
- absence of a channel does not imply a zero term;
- zero-extending absent channels loses channel-membership information.

### Channel-Indexed Static Aggregation
The downstream static layer retains the same status rule: an absent channel is not assigned a zero term, while a present admitted channel may have a defined zero term.

## External database sources

### PostgreSQL
Current PostgreSQL documentation states that SQL logical expressions use three-valued logic with NULL representing unknown. It also distinguishes `COUNT(*)`, which counts input rows, from `COUNT(expr)`, which counts rows in which `expr` is non-null. Most built-in aggregates ignore null inputs. PostgreSQL also documents that `SUM` over no selected rows returns NULL rather than zero.

Sources:
- https://www.postgresql.org/docs/current/functions-logical.html
- https://www.postgresql.org/docs/current/functions-aggregate.html
- https://www.postgresql.org/docs/17/sql-expressions.html

### Oracle Database
Oracle documents NULL as a column with no value and explicitly warns not to use NULL for numeric zero because they are not equivalent. Oracle currently treats a zero-length character value as NULL, while also warning users not to rely on empty string and NULL being permanently identical.

Sources:
- https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Nulls.html
- Oracle SQL Language Reference, Nulls section

### SQLite
SQLite documents implementation-level NULL behavior and historical cross-engine comparisons, including the fact that NULL treatment differs by operation and engine. This is used only as an implementation-boundary witness, not as a normative SQL-standard claim.

Source:
- https://sqlite.org/nulls.html

## Source-use rule

No external database state is declared identical to a DSD state. The analysis asks only which distinctions are preserved, collapsed, or require explicit extra encoding.