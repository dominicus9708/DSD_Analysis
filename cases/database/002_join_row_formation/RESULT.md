# DB-002 / Global Case 035 — JOIN, Filter, and Row Formation

Status: **first-pass analysis completed**.

Final judgment: **strong partial structural support**, with a non-identity boundary between SQL query-result construction and DSD formation semantics.

## 1. Core distinction

SQL join processing separates at least four structurally different situations:

1. a source row has a matching partner and produces a joined result row;
2. a source row has no partner and disappears under an inner join;
3. a source row has no partner but is preserved by an outer join through a null-extended result row;
4. a row exists after join processing but is later removed by a WHERE predicate.

These cases can produce overlapping visible cell values, but they do not have the same formation history.

## 2. Authoritative SQL behavior

PostgreSQL documents that an INNER JOIN produces rows only for matching pairs. A LEFT OUTER JOIN first performs the inner join and then adds one null-extended output row for each unmatched left row. PostgreSQL also documents that WHERE is applied after FROM/join processing; rows whose WHERE condition is false or null are discarded.

SQLite states the same ordering explicitly: unmatched outer-join rows are null-extended after ON/USING processing and before WHERE processing. Consequently, moving a predicate between ON and WHERE can change whether an unmatched left row survives.

## 3. Reproducible witness

Use left table L:

- `(1, 'A')`
- `(2, 'B')`
- `(3, 'C')`

and right table R:

- `(1, 10)`
- `(3, NULL)`

The deterministic SQLite witness gives:

```text
INNER JOIN: [(1, 1, 10), (3, 3, None)]
LEFT JOIN: [(1, 1, 10), (2, None, None), (3, 3, None)]
LEFT JOIN + WHERE r.val > 5: [(1, 1, 10)]
LEFT JOIN + ON r.val > 20: [(1, None, None), (2, None, None), (3, None, None)]
Projected LEFT JOIN: [(1, 10), (2, None), (3, None)]
```

The crucial pair is `l.id=2` versus `l.id=3` under LEFT JOIN:

- `id=2`: no right-hand tuple matched; NULLs were introduced by outer-join extension.
- `id=3`: a right-hand tuple did match; its stored `val` is actually NULL.

If the projection keeps only `(l.id, r.val)`, both appear with `r.val = NULL`. The visible field value no longer identifies whether a matching right-hand witness existed.

## 4. DSD comparison

The Formation Axiom System states that channel formation requires all Clause-VI conditions. Failure of any required condition yields channel absence rather than a zero-valued channel. It also defines a formation trace that records the restriction-realization witness without inserting that history into operational channel identity.

This provides a useful structural comparison:

| Database situation | DSD comparison | Judgment |
| --- | --- | --- |
| matching join pair produces result row | all required formation conditions jointly satisfied | partial structural correspondence |
| INNER JOIN unmatched source row disappears | required relation/witness missing, so no downstream result row | partial structural correspondence |
| LEFT JOIN unmatched source row is null-extended | explicit downstream placeholder preserving one side despite failed match | non-identical, useful boundary case |
| matched right row whose value is NULL | relation witness exists but a downstream field is null | structurally distinct from unmatched null-extension |
| WHERE removes an already joined/null-extended row | later-stage filter removes a previously available intermediate row | order-sensitive downstream operation, not literal DSD formation |

The correspondence is therefore about **dependency and status discipline**, not about equating a SQL row with a DSD channel.

## 5. Projection and provenance loss

The strongest information-structure result is not merely that INNER and LEFT JOIN differ. It is that projection can erase the evidence that made two NULL-bearing output rows different.

`(2, NULL)` after projection may mean “no partner existed and NULL was synthesized by the outer join”.

`(3, NULL)` may mean “a partner existed and its stored value was NULL”.

A retained non-nullable right-side identifier, match flag, or provenance record separates them. Without such support information, equal visible values do not imply equal relational histories.

This is closely analogous to the DSD discipline that reduced output equality must not be promoted to full structural identity when formation/support information has been discarded.

## 6. ON versus WHERE as an ordering witness

For an outer join, `ON` and `WHERE` are not interchangeable.

- An ON predicate participates in deciding which pairs count as matches before null-extension.
- A WHERE predicate is evaluated after the joined virtual table exists and can delete the null-extended rows.

Thus the same predicate text placed at a different stage can change the result relation. This independently supports the broader DSD analysis principle that a condition's **position in the formation pipeline** matters; a later failure is not generally identical to an earlier non-formation.

## 7. Falsification attempt

Counter-hypothesis: if two query outputs show the same NULL values, the match history is operationally irrelevant and DSD-style support distinctions are unnecessary.

The witness rejects the general form of this claim. `l.id=2` and `l.id=3` can expose the same projected NULL value while differing in whether a right-side tuple existed. Retaining `r.id`, a match flag, or provenance restores the distinction. Therefore value equality alone is insufficient for reconstruction.

A second counter-hypothesis is that join predicates and later filters can be treated as one undifferentiated condition. Outer joins reject this too: ON and WHERE have different positions and therefore different row-preservation effects.

## 8. Final judgment

**Strong partial structural support.** Relational query semantics independently exhibits:

- prerequisite-sensitive result formation;
- genuine result absence;
- explicit placeholder/null-extension that is not the same as source-value NULL;
- stage-sensitive filtering;
- loss of provenance under projection.

No contradiction to the DSD formation/status distinctions was found.

The non-identity boundary remains important: SQL joins are relational query operators constructing result tables, whereas DSD Formation Clause VI defines membership in an admitted operational-channel set. The analogy must not be upgraded to semantic identity.

## 9. Next case

DB-003 should analyze **schema property existence versus per-row applicability/value assignment**, including nullable columns, optional attributes, and relation-dependent fields. This moves naturally from row-formation provenance to the distinction between declared property kind and actual property application.