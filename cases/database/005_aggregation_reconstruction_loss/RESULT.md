# DB-005 / Global Case 038 — Aggregation and Reconstruction Loss

Status: **first-pass analysis completed**.

Final judgment: **very strong partial structural support** for the DSD distinction between support/status structure and reduced aggregate value.

## 1. Core result

The witness constructs six database groups whose underlying relation/value structures differ but whose reduced numerical aggregates can coincide.

The strongest collision occurs after totalization with `COALESCE(SUM(weight),0)`:

```text
A  no relation row                         -> 0
B  relation row, no target, no weight     -> 0
C  valid target, missing weight           -> 0
D  valid target, defined zero             -> 0
E  +5 and -5 on two valid relations       -> 0
```

Five structurally different states therefore collapse to the same scalar output.

## 2. Aggregate coordinates retain different amounts of support information

The reproducible SQLite output is:

```text
('A', 1, 0, 0, 0, None, 0, 0)
('B', 1, 1, 0, 0, None, 0, 0)
('C', 1, 1, 1, 0, None, 0, 0)
('D', 1, 1, 1, 1, 0.0, 0.0, 0.0)
('E', 2, 2, 2, 2, 0.0, 0.0, 0.0)
('F', 1, 1, 1, 1, 7.0, 7.0, 7.0)
```

The coordinates are:

1. group id;
2. `COUNT(*)` after the left join;
3. `COUNT(relation_id)`;
4. `COUNT(target_id)`;
5. `COUNT(weight)`;
6. `SUM(weight)`;
7. `SUM(COALESCE(weight,0))`;
8. `COALESCE(SUM(weight),0)`.

Each support-sensitive count answers a different question:

- `COUNT(*)` counts joined result rows and, under a left join, does not directly measure relationship-row support;
- `COUNT(relation_id)` detects actual relationship rows when the relation id is non-NULL;
- `COUNT(target_id)` detects non-NULL target references;
- `COUNT(weight)` detects defined/non-NULL weight values;
- `SUM(weight)` reduces the defined numeric values and ignores NULL inputs.

No single reduced scalar reconstructs all preceding coordinates.

## 3. Missingness and defined zero

Groups C and D differ only at the weight-assignment level:

- C: a valid target exists but weight is NULL;
- D: a valid target exists and weight is explicitly 0.

`COUNT(weight)` separates them (`0` versus `1`), while `COALESCE(SUM(weight),0)` makes them equal (`0` versus `0`).

Thus a defaulted aggregate can erase assignment-status information even when it preserves a convenient numerical convention.

## 4. Zero by absence, zero by definition, and zero by cancellation

Groups A, D, and E give three particularly important mechanisms for the same displayed zero:

- A: no relationship support exists;
- D: one supported relation has a defined zero value;
- E: two supported nonzero relations cancel, +5 and -5.

Hence

`aggregate = 0`

does not determine whether the source structure had no support, explicit zero support, or nonzero cancelling support.

This is a direct database analogue of non-injective summation.

## 5. Empty relation versus zero-valued relation

An aggregate over no selected rows yields:

```text
COUNT(*) = 0
COUNT(weight) = 0
SUM(weight) = NULL
COALESCE(SUM(weight),0) = 0
```

Therefore the raw `SUM` preserves one distinction between no/non-defined inputs and an explicit zero-valued input, but `COALESCE(SUM(...),0)` deliberately removes that distinction.

This is not an error in SQL; it is a modeling choice. The information loss begins when the reduced representation is treated as if it were the full source structure.

## 6. DSD comparison

The Formation Axiom System already establishes that:

- undefined assignment is not defined zero;
- absent channel is not a zero term;
- zero-extension is not channel-faithful;
- distinct finite channel families can have the same composite value (Proposition 5.14).

The Channel-Indexed Static Aggregation paper strengthens the same point analytically. It separates support-tagged records from their sums, proves a nontrivial summation kernel under cancellation, gives an exact injectivity criterion, and states that aggregate equality is not a general reconstruction theorem (Corollary 11.5).

The database witness reproduces the same structural obstruction independently:

| Database collision | DSD comparison | Judgment |
| --- | --- | --- |
| no relation support -> defaulted sum 0 | absent channel/support totalized to zero | close non-conflation analogy |
| missing weight -> defaulted sum 0 | undefined application padded by zero | close non-conflation analogy |
| defined weight 0 -> sum 0 | admitted/defined zero term | close analogy |
| +5 and -5 -> sum 0 | nontrivial summation-kernel cancellation | strong algebraic analogy |
| equal scalar across distinct groups | aggregate equality without support reconstruction | strong structural correspondence |

## 7. Counterpressure and boundary

SQL does not require an application to retain all support coordinates. Reduced aggregates are intentionally useful summaries. If only the numerical total matters, collapsing multiple structures to one value can be correct for that application.

Therefore this case does **not** show that every aggregate must be injective or that SQL should preserve all provenance automatically.

The structural claim is narrower: when the analysis later needs to distinguish absence, applicability, assignment, defined zero, multiplicity, or cancellation, the scalar aggregate is insufficient unless support/status metadata is retained or an additional reconstruction theorem applies.

SQL `NULL` is not DSD undefined, and SQL relation rows are not DSD channels.

## 8. Falsification attempts

### Hypothesis A — aggregate zero implies zero source structure

Rejected. Groups A, D, and E have no support, defined-zero support, and nonzero cancelling support respectively, yet all reduce to zero under the selected aggregate.

### Hypothesis B — COALESCE only changes presentation, not recoverable structure

Rejected in the reconstruction sense. C and D are separated by `COUNT(weight)` and raw `SUM`, but become identical under the defaulted scalar. The original assignment status cannot be reconstructed from that scalar alone.

### Hypothesis C — GROUP BY plus SUM is enough to reconstruct group structure

Rejected. Group identity is retained, but within-group relation multiplicity, target support, missingness, and cancellation remain unrecoverable from the sum alone.

## 9. Final judgment

**Very strong partial structural support.** DB-005 provides an external relational-database witness for the exact distinction already formalized in the DSD static layer: reduced aggregate equality is weaker than equality of support-tagged structure.

The particularly strong point is that the database witness exhibits both kinds of information loss relevant to DSD:

1. **status totalization loss** — absence/missingness/defined zero collapse under zero substitution;
2. **summation-kernel loss** — distinct nonzero component structures cancel to the same aggregate.

No contradiction to the Formation Axiom System, axis-property system, or Channel-Indexed Static Aggregation was found.

## 10. Next step

DB-001 through DB-005 now form a coherent first-pass database sequence. The next step should be a **database-field synthesis/closure note** that separates what was independently confirmed, what remains encoding-dependent, and what should not be counted as an independent confirmation because multiple cases rely on the same SQL NULL mechanism. After that, the roadmap can move to **knowledge representation, ontology, and classification**.