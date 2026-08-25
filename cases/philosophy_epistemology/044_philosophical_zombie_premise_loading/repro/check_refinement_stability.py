from __future__ import annotations

from typing import Dict, Iterable, List, Sequence

State = Dict[str, int]


def agrees_on(actual: State, candidate: State, coordinates: Sequence[str]) -> bool:
    return all(actual[c] == candidate[c] for c in coordinates)


def names(states: Iterable[State]) -> List[str]:
    return [str(s["name"]) for s in states]


def nested_refinement_witness() -> None:
    actual: State = {"name": "actual", "p1": 0, "p2": 0, "p3": 0, "q": 1}
    candidates: List[State] = [
        {"name": "z1", "p1": 0, "p2": 1, "p3": 1, "q": 0},
        {"name": "z2", "p1": 0, "p2": 0, "p3": 1, "q": 0},
    ]

    stages = [
        ("Sigma1", ("p1",)),
        ("Sigma2", ("p1", "p2")),
        ("Sigma3", ("p1", "p2", "p3")),
    ]

    print("WITNESS A — NESTED REFINEMENT")
    for label, coords in stages:
        matching = [
            z for z in candidates if z["q"] == 0 and agrees_on(actual, z, coords)
        ]
        print(f"{label} {list(coords)} zombie_like_matches: {names(matching)}")

    full_matches = [
        z
        for z in candidates
        if z["q"] == 0 and agrees_on(actual, z, ("p1", "p2", "p3"))
    ]
    print("terminal_full_descriptor_has_zombie_like_match:", bool(full_matches))
    print()


def quantifier_order_witness() -> None:
    actual: State = {"name": "actual", "p1": 0, "p2": 0, "p3": 0, "q": 1}
    candidates: List[State] = [
        {"name": "a", "p1": 0, "p2": 1, "p3": 1, "q": 0},
        {"name": "b", "p1": 1, "p2": 0, "p3": 1, "q": 0},
        {"name": "c", "p1": 1, "p2": 1, "p3": 0, "q": 0},
    ]

    refinements = [
        ("R1", ("p1",)),
        ("R2", ("p2",)),
        ("R3", ("p3",)),
    ]

    print("WITNESS B — QUANTIFIER ORDER")
    per_refinement_matches = {}
    for label, coords in refinements:
        matching = [
            z for z in candidates if z["q"] == 0 and agrees_on(actual, z, coords)
        ]
        per_refinement_matches[label] = names(matching)
        print(f"{label} {list(coords)} matches: {names(matching)}")

    forall_exists = all(per_refinement_matches[label] for label, _ in refinements)
    exists_forall = any(
        z["q"] == 0
        and all(agrees_on(actual, z, coords) for _, coords in refinements)
        for z in candidates
    )

    print("forall_refinement_exists_matching_candidate:", forall_exists)
    print("exists_one_candidate_matching_all_refinements:", exists_forall)
    print("quantifier_patterns_equivalent_in_witness:", forall_exists == exists_forall)


if __name__ == "__main__":
    nested_refinement_witness()
    quantifier_order_witness()
