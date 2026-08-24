# DB-001 / Global Case 034 — Row Absence, NULL, Empty Value, and Defined Zero

## 1. Classification

- Domain: database systems / information structures
- DSD Analysis field: database and information structures
- Status: first-pass analysis opened
- Branch: `analysis/db-001-absence-null-zero`

## 2. Core question

When a database distinguishes no row, a present row with NULL, an empty-but-defined value, and a defined numeric zero, which distinctions are structurally necessary for correct filtering and aggregation, and how far do those distinctions correspond to DSD's separation of absence, undefined assignment, defined zero, and later zero contribution?

## 3. Anti-identification rule

SQL `NULL` is not identified with DSD `undefined` by name alone. A SQL row can exist while one column is NULL, whereas a DSD partial assignment is undefined when no graph pair exists for the input. Only structural correspondences are recorded.

## 4. Tests

1. Compare an absent row, a NULL field, a zero field, and an empty string.
2. Compare `COUNT(*)` with `COUNT(expr)`.
3. Compare an empty input relation with a relation containing a defined zero under `SUM`.
4. Test what is lost when `COALESCE(NULL, 0)` is applied before counting or aggregating.
5. Compare implementation boundaries, especially Oracle's current treatment of zero-length character strings as NULL.

## 5. Decision classes

- direct structural support
- partial structural support
- implementation-dependent boundary
- non-corresponding but compatible
- contradiction / counterexample to DSD distinction

## 6. Reproducibility

A deterministic SQLite/Python witness is included to demonstrate the state separations and one information-loss operation. It is illustrative only; cross-DBMS claims are sourced from vendor documentation.