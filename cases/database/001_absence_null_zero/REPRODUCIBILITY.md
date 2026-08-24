# DB-001 Reproducibility

## Files

- `repro/check_sqlite_states.py`
- `repro/expected_output.txt`

## Run from repository root

```bash
python cases/database/001_absence_null_zero/repro/check_sqlite_states.py
```

## Expected structural checks

The witness contains exactly two rows:

- one row with numeric zero and empty string;
- one row with numeric NULL and string NULL.

It additionally queries a missing key and an empty input relation.

Expected distinctions:

- `COUNT(*)` sees both present rows;
- `COUNT(x)` sees only the non-NULL numeric field;
- `COUNT(COALESCE(x,0))` becomes 2 and therefore loses the original NULL/non-NULL distinction;
- `SUM(x)` over the two rows is 0;
- `SUM(x)` over no rows is represented by Python `None`, corresponding to SQLite NULL;
- row absence, NULL field, zero field, empty string, and NULL string remain separately queryable in this SQLite witness.

## Scope

This script is not a proof of SQL-standard semantics and is not used to infer Oracle behavior. Cross-engine claims are taken from vendor documentation in `SOURCE_NOTES.md`. The script only reproduces one finite information-structure witness.