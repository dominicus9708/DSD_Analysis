from __future__ import annotations


def main() -> None:
    t0, t1, t2 = 0, 1, 3

    physical_facts = {
        t0: {"f_a", "f_b"},
        t1: {"f_a", "f_b", "f_remote"},
        t2: {"f_a", "f_b", "f_remote"},
    }

    mary_known_targets = {
        t0: {"f_a", "f_b"},
        t1: {"f_a", "f_b"},
        t2: {"f_a", "f_b", "f_remote"},
    }

    snapshot_complete_t0 = physical_facts[t0] <= mary_known_targets[t0]
    snapshot_complete_t1 = physical_facts[t1] <= mary_known_targets[t1]
    world_changed = bool(physical_facts[t1] - physical_facts[t0])
    remote_fact_unknown_t1 = (
        "f_remote" in physical_facts[t1]
        and "f_remote" not in mary_known_targets[t1]
    )
    later_update = "f_remote" in mary_known_targets[t2]

    witness_passed = (
        snapshot_complete_t0
        and world_changed
        and not snapshot_complete_t1
        and remote_fact_unknown_t1
        and later_update
    )

    print(f"snapshot_complete_t0: {snapshot_complete_t0}")
    print(f"world_changed_after_t0: {world_changed}")
    print(f"snapshot_complete_t1: {snapshot_complete_t1}")
    print(f"remote_fact_unknown_t1: {remote_fact_unknown_t1}")
    print(f"later_update_t2: {later_update}")
    print(f"witness_passed: {witness_passed}")

    if not witness_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
