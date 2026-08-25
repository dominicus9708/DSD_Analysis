# PHIL-003 Reproducibility

## Branch

`analysis/phil-003-marys-room-epistemic-regime-audit`

PHIL-003 preserves two independent finite checks.

## Argument 1 — record novelty versus fact-target novelty

### Core claim checked

`new epistemic record !=> new world-fact target`.

The witness does not model consciousness or prove physicalism.

### Run

From the repository root:

```bash
python cases/philosophy_epistemology/046_marys_room_epistemic_regime_audit/repro/check_record_target_nonimplication.py
```

Expected output:

```text
new_records: ['k_phen']
new_targets: []
new_record_without_new_target: True
all_targets_physical: True
witness_passed: True
```

### Interpretation

The witness fixes one physical fact target about another person's red experience and two distinct epistemic records targeting it: one pre-release physical-description record and one post-release phenomenal-mode record.

The post-release record is new while the target set is unchanged. This is sufficient to refute the bare set-theoretic implication from record novelty to target novelty.

To restore Jackson's stronger conclusion an additional fact-individuation / new-fact bridge must exclude this model.

Argument 1 is not counted as a new philosophical objection. It is a DSD-specific formal sharpening of the established New Knowledge / Old Fact and phenomenal-representation families.

## Argument 2 — snapshot completeness versus sustained completeness

### Core claim checked

`snapshot physical completeness at t0 !=> snapshot completeness at a later time t1 when the physical fact set evolves`.

This witness checks only the logical non-preservation of a time-indexed completeness predicate. It does not simulate physical signal propagation, cognition, relativity, or the speed of light.

### Run

From the repository root:

```bash
python cases/philosophy_epistemology/046_marys_room_epistemic_regime_audit/repro/check_snapshot_completeness_nonpreservation.py
```

Expected output:

```text
snapshot_complete_t0: True
world_changed_after_t0: True
snapshot_complete_t1: False
remote_fact_unknown_t1: True
later_update_t2: True
witness_passed: True
```

### Interpretation

At `t0`, Mary knows every fact in the declared physical fact set. At `t1`, a new remote physical fact has entered the world-fact set while Mary's known target set has not yet been updated. At `t2`, the new fact has been incorporated.

Thus one-time completeness can be lost and later restored. To rule out this witness, an additional diachronic update/completeness condition must require every new physical fact to become known to Mary with the stipulated timing.

### Propagation boundary

The DSD dynamics paper permits finite structural-information propagation only under explicit localization, metric-time, constitutive, locality, and support-faithfulness assumptions. Therefore the finite witness above does not infer any empirical propagation speed. A later application may add such a model, but it must do so explicitly.

Argument 2 is currently recorded as a DSD-constructed dynamic extension; historical novelty has not yet been audited and is not claimed.

## Combined rule

The two witnesses test different implications and must not be merged:

1. fixed target domain: `new record !=> new target`;
2. evolving target domain: `complete now !=> complete later`.

A defense of Jackson may answer them with different bridges: a fact-individuation bridge for Argument 1 and a time-indexed update/completeness bridge for Argument 2.