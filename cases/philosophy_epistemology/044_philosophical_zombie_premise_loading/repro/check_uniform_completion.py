from __future__ import annotations


def matches_prefix(candidate_index: int, prefix_length: int) -> bool:
    """
    Actual world has p_i = 0 for every positive integer i.

    Zombie-like candidate z_k has q = 0 and matches the actual world at every
    p_i except p_k, where it has value 1. Therefore z_k matches the first n
    physical coordinates exactly iff k > n.
    """
    return candidate_index > prefix_length


def finite_prefix_demo(max_prefix: int = 8) -> None:
    print("UNIFORM COMPLETION WITNESS")
    print("actual: p_i=0 for all i, q=1")
    print("candidate z_k: p_i=0 for i != k, p_k=1, q=0")
    print()

    all_finite_prefixes_have_candidate = True
    for n in range(1, max_prefix + 1):
        k = n + 1
        survives = matches_prefix(k, n)
        all_finite_prefixes_have_candidate &= survives
        print(f"prefix Sigma_{n}: choose z_{k} -> matches first {n} physical coordinates: {survives}")

    print()
    print("all_displayed_finite_prefixes_have_zombie_like_candidate:", all_finite_prefixes_have_candidate)
    print("single_z_k_matches_every_physical_coordinate:", False)
    print("reason: every z_k differs from actual at its own coordinate p_k")
    print("logical_pattern: (forall n exists z_k matching Sigma_n) does not imply (exists z forall n z matches Sigma_n)")


if __name__ == "__main__":
    finite_prefix_demo()
