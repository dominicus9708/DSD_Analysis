# DB-004 / Global Case 037 — Optional Relations and Foreign-Key States

Status: **first-pass analysis completed**.

Final judgment: **strong partial structural support**, with a database-encoding boundary and no semantic identification between foreign keys and DSD relations.

## 1. Core state separation

The witness separates five states for one candidate source entity:

1. `NO_RELATION_ROW` — no relationship tuple exists;
2. `RELATION_ROW_NO_TARGET` — a relationship tuple exists, but its nullable target reference is NULL;
3. `TARGET_RELATION_VALUE_MISSING` — a valid target exists, but an auxiliary relation value is NULL;
4. `TARGET_RELATION_DEFINED_ZERO` — a valid target exists and the auxiliary value is explicitly 0;
5. `TARGET_RELATION_DEFINED_VALUE` — a valid target exists and the auxiliary value is nonzero.

These are different database facts even when a projection can make some visible cells coincide.

## 2. Foreign-key evidence

PostgreSQL documents that the default `MATCH SIMPLE` foreign-key rule does not require a referenced-row match if any referencing column is NULL. SQLite likewise states that a child row satisfies its foreign-key requirement when the child key is NULL or a matching parent row exists.

Therefore:

- child/relationship row existence does not imply target-row existence;
- target-reference absence does not imply relationship-row absence;
- `NOT NULL` is an additional modeling constraint when a mandatory reference is intended.

An invalid non-NULL target is different again: with foreign-key enforcement enabled, it is rejected rather than converted to NULL or treated as relationship absence.

## 3. Reproducible witness

The deterministic SQLite witness yields:

```text
RELATION STATES
(1, None, None, None, None, 'NO_RELATION_ROW')
(2, 2, None, None, None, 'RELATION_ROW_NO_TARGET')
(3, 3, 30, 30, None, 'TARGET_RELATION_VALUE_MISSING')
(4, 4, 40, 40, 0.0, 'TARGET_RELATION_DEFINED_ZERO')
(5, 5, 50, 50, 7.0, 'TARGET_RELATION_DEFINED_VALUE')
INVALID TARGET: FOREIGN KEY constraint failed
```

The pair `source=1` and `source=2` is a useful projection counterexample. If only `target_id` and `weight` are kept after a left join, both can appear as `(NULL, NULL)`, but one has no relationship tuple and the other has an actual relationship tuple whose target is NULL. Retaining relationship-row identity restores the distinction.

The pair `source=3` and `source=4` separates missing auxiliary value from defined zero. Replacing the missing weight with zero would erase assignment/value-status information.

## 4. Referential actions as a second witness

For one parent deletion, two valid schemas can deliberately produce different downstream relationship states:

```text
SET NULL AFTER PARENT DELETE: [(10, None, 7.0)]
CASCADE AFTER PARENT DELETE: []
```

`ON DELETE SET NULL` preserves the relationship row and auxiliary value while removing the target reference. `ON DELETE CASCADE` removes the relationship row itself.

Thus "the referenced target disappeared" does not uniquely determine "the relationship row disappeared". The schema's referential-action rule is part of the transformation semantics.

## 5. DSD comparison

The current Formation Axiom System explicitly separates absent channel, undefined assignment, defined zero, defined nonzero, and zero contribution. The current axis-property system likewise distinguishes unavailable input, undefined application, and defined zero-valued applications while retaining typed partial-assignment structure.

Database correspondence is structural:

| Database state | DSD comparison | Boundary |
| --- | --- | --- |
| no relationship row | absence of a relation/application record at the chosen modeling layer | analogy only |
| relationship row with NULL target | record exists while required/optional target coordinate is absent | no direct primitive identity |
| valid target, NULL auxiliary value | relation support exists while one value remains missing/undefined in the database encoding | SQL NULL is not DSD undefined |
| valid target, weight 0 | relation support plus defined zero value | close non-conflation analogy |
| invalid non-NULL foreign target | integrity constraint failure | database-specific admissibility mechanism |
| SET NULL vs CASCADE | preservation of record with changed coordinate vs record deletion | useful transformation boundary, not DSD dynamics |

The strongest common principle is that **support existence, reference existence, and value assignment are independent coordinates unless a stronger constraint explicitly couples them**.

## 6. Counterpressure against DSD

A database designer can intentionally choose a simpler schema in which some of these states are impossible or deliberately collapsed. For example, putting `NOT NULL` on the foreign key eliminates the `RELATION_ROW_NO_TARGET` state. Using no separate relation table may collapse relationship-row existence into a nullable column on the source row.

Therefore DBMS behavior does not prove that every DSD application must use all status layers. The support is conditional: when reconstruction, provenance, optional relationships, or status-sensitive logic matters, collapsing the layers loses information.

## 7. Falsification attempts

### Hypothesis A — nullable foreign key NULL means there is no relationship record

Rejected. A relationship tuple may exist with its target foreign key NULL, while another source may have no relationship tuple at all. A left-join projection can hide the difference, but row identity/provenance recovers it.

### Hypothesis B — missing relation value can be safely identified with zero

Rejected in the general structural sense. A relation with `weight=NULL` and one with `weight=0` have different value-status information even if later application logic chooses a common default.

### Hypothesis C — deleting the parent necessarily deletes the relationship

Rejected. `ON DELETE SET NULL` preserves the row; `ON DELETE CASCADE` deletes it. Referential action is an explicit schema choice.

## 8. Final judgment

**Strong partial structural support.** Standard relational-database mechanisms independently separate relationship-row support, target-reference support, referential validity, auxiliary-value assignment, and defined zero. Projection or default substitution can collapse these distinctions, but that collapse is information-losing unless additional reconstruction information is retained.

No contradiction to the Formation or axis-property non-conflation rules was found.

The non-identity boundary remains essential: a SQL foreign key is an integrity constraint over relational data, not a DSD operational channel or axis-property primitive.

## 9. Next case

DB-005 should analyze **aggregation and reconstruction loss across missing/optional relation states**. It should test `COUNT(*)`, `COUNT(target_id)`, `COUNT(weight)`, `SUM(weight)`, default substitution, and grouping to determine which support distinctions survive a reduced aggregate and which become unrecoverable.
