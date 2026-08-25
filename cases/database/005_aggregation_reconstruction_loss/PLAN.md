# DB-005 / Global Case 038 — Aggregation and Reconstruction Loss

## Goal

Test whether reduced SQL aggregates preserve the structural distinctions established in DB-001 through DB-004.

## Questions

1. Can `COUNT(*)`, `COUNT(target_id)`, `COUNT(weight)`, and `SUM(weight)` distinguish relation support, target support, missing values, defined zero, and cancellation?
2. What information is lost when `NULL` is replaced by zero through `COALESCE`?
3. Can different support structures produce the same numerical aggregate?
4. Does `GROUP BY` preserve enough metadata to reconstruct the original relation/value states?
5. How does this compare with the DSD Formation Axiom System and Channel-Indexed Static Aggregation, where aggregate equality is explicitly not a reconstruction theorem?

## Witness design

Construct six groups:

- A: no relation row;
- B: relation row exists, but target and weight are NULL;
- C: valid target exists, but weight is NULL;
- D: valid target and defined weight 0;
- E: two valid targets with weights +5 and -5;
- F: valid target and defined weight 7.

Aggregate each group under a left join and compare support-sensitive counts with reduced sums.

## Falsification targets

- If equal aggregate value always reconstructed support, A–E should not collide after reduction.
- If missing value and defined zero were structurally interchangeable, C and D should remain indistinguishable even when assignment counts are retained.
- If zero aggregate implied zero component structure, D and E should be structurally interchangeable.

## Expected scope

This is a structural comparison only. SQL aggregate semantics is not identified with DSD channel composition.