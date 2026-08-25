# DB-005 Reproducibility

## Requirements

- Python 3
- Standard-library `sqlite3` only

## Run from repository root

```bash
python cases/database/005_aggregation_reconstruction_loss/repro/check_aggregate_loss.py
```

Compare with:

```text
cases/database/005_aggregation_reconstruction_loss/repro/expected_output.txt
```

## What the witness checks

1. relation-row support, target-reference support, and defined-weight support produce different counts;
2. raw `SUM(weight)` distinguishes groups with no non-NULL weights from groups whose defined numeric sum is zero;
3. `COALESCE(SUM(weight),0)` collapses no-support, missing-value, defined-zero, and cancellation cases to the same scalar zero;
4. an empty selected relation returns `SUM(weight)=NULL` while the defaulted sum is zero;
5. equal reduced aggregate values do not reconstruct the source support structure.

The script is deterministic and uses an in-memory SQLite database.