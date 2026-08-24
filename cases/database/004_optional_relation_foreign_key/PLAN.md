# DB-004 / Global Case 037 — Optional Relations and Foreign-Key States

Status: analysis executed in this branch.

## Question

Test whether the following database states are structurally distinguishable and whether collapsing them loses information:

1. no relationship row exists;
2. a relationship row exists but has no target reference;
3. a valid target relationship exists but an auxiliary relation value is missing;
4. a valid target relationship exists with a defined zero auxiliary value;
5. a valid target relationship exists with a defined nonzero auxiliary value.

Additional pressure test: compare `ON DELETE SET NULL` with `ON DELETE CASCADE` to determine whether target disappearance and relationship-row disappearance are the same event.

## DSD comparison boundary

The comparison is structural only. A SQL foreign key is not identified with a DSD channel, property application, or typed relation. The audit asks whether database practice independently requires separation among relationship existence, target existence, assignment/value status, and defined zero.

## Reproducibility

Run from repository root:

```bash
python cases/database/004_optional_relation_foreign_key/repro/check_relation_states.py
```
