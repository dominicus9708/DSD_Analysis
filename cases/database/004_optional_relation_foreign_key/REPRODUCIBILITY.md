# Reproducibility — DB-004

## Environment

- Python 3
- standard-library `sqlite3`
- in-memory databases only
- SQLite foreign-key enforcement explicitly enabled with `PRAGMA foreign_keys = ON`

## Command

From repository root:

```bash
python cases/database/004_optional_relation_foreign_key/repro/check_relation_states.py
```

## Verified output

```text
RELATION STATES
(1, None, None, None, None, 'NO_RELATION_ROW')
(2, 2, None, None, None, 'RELATION_ROW_NO_TARGET')
(3, 3, 30, 30, None, 'TARGET_RELATION_VALUE_MISSING')
(4, 4, 40, 40, 0.0, 'TARGET_RELATION_DEFINED_ZERO')
(5, 5, 50, 50, 7.0, 'TARGET_RELATION_DEFINED_VALUE')
INVALID TARGET: FOREIGN KEY constraint failed
SET NULL AFTER PARENT DELETE: [(10, None, 7.0)]
CASCADE AFTER PARENT DELETE: []
```

## Interpretation limits

This script is a finite deterministic database witness, not a proof of all SQL implementations or all database schemas. SQLite is used to make the status distinctions executable. PostgreSQL and SQLite official documentation are used separately to verify the external foreign-key semantics cited in the analysis.

The witness does not identify SQL NULL with DSD undefined and does not identify a database relationship row with a DSD channel or axis-property record.
