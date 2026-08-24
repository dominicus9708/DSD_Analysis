# DB-002 Reproducibility

The bundled SQLite witness checks the distinction among match formation, inner-join row loss, outer-join null extension, and post-join WHERE filtering.

## Files

- `repro/check_join_states.py`
- `repro/expected_output.txt`

## Run from repository root

```bash
python cases/database/002_join_row_formation/repro/check_join_states.py
```

## Expected structural checks

- INNER JOIN omits the unmatched left row `id=2`.
- LEFT JOIN preserves `id=2` as a null-extended result row.
- The matched row `id=3` contains a real right-side tuple whose stored `val` is NULL.
- Projecting away `r.id` makes `id=2` and `id=3` both expose `r.val = NULL` even though their match histories differ.
- A WHERE predicate on `r.val` removes both null-bearing rows after join processing.
- Moving a restrictive predicate into ON instead causes all left rows to survive as null-extended rows when no right pair satisfies that ON predicate.

## Scope

This finite witness demonstrates the stated query-state distinctions in SQLite. It does not prove a general theorem about all relational systems and does not identify SQL joins with DSD channel formation. The comparison claim is supported separately by PostgreSQL and SQLite documentation and by the DSD Formation Axiom System.