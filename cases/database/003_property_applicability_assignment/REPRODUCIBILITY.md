# DB-003 Reproducibility

## Environment

Python 3 standard library only. The witness uses `sqlite3` with an in-memory database.

## Run

From the repository root:

```bash
python cases/database/003_property_applicability_assignment/repro/check_property_layers.py
```

## Expected result

See `repro/expected_output.txt`.

The key observations are:

- entities 2 and 3 both appear as `NULL` in the wide nullable-column projection;
- the layered schema reconstructs entity 2 as applicable but unassigned;
- it reconstructs entity 3 as inapplicable;
- entity 1 has an actual assignment row whose defined value is zero;
- declaration count, applicability count, assignment count, and defined-zero count remain separately measurable.

## Interpretation limit

This witness is an encoding demonstration, not a theorem about all relational schemas and not an implementation of DSD semantics. SQLite NULL is not identified with DSD undefined assignment. The point is only that an explicitly layered schema can preserve distinctions that one nullable field erases.

## Execution check

The script logic was executed against Python's standard-library SQLite engine on 2026-08-25 and produced the expected rows and counts. Assertions passed.