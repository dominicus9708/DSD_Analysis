from itertools import product


def witness_a_modal_space_separation():
    """Show that epistemic scenario space can strictly exceed admissible modal space.

    This is a structural toy witness only. It does not assert that consciousness obeys
    the constraint q == p. It shows that an inference from scenario-level coherence to
    metaphysical admissibility is not valid without a bridge principle.
    """
    epistemic_space = {(p, q) for p, q in product((0, 1), repeat=2)}
    metaphysical_space = {(p, q) for p, q in epistemic_space if q == p}
    zombie_candidate = (1, 0)

    assert zombie_candidate in epistemic_space
    assert zombie_candidate not in metaphysical_space
    assert metaphysical_space < epistemic_space

    return epistemic_space, metaphysical_space, zombie_candidate


def witness_b_descriptor_incompleteness():
    """Show that equality of a reduced structural descriptor need not be full identity.

    d = structural/dispositional descriptor
    i = intrinsic/categorical coordinate omitted by d
    q = a downstream property fixed here by i

    Again this is not a theory of consciousness. It is a finite witness for the logical
    distinction between reduced-descriptor equality and full-structure equality.
    """
    full_states = {(d, i, i) for d, i in product((0, 1), repeat=2)}
    same_reduced_d1 = sorted(state for state in full_states if state[0] == 1)

    assert len(same_reduced_d1) == 2
    assert same_reduced_d1[0][0] == same_reduced_d1[1][0]
    assert same_reduced_d1[0][2] != same_reduced_d1[1][2]
    assert same_reduced_d1[0][:2] != same_reduced_d1[1][:2]

    return full_states, same_reduced_d1


def main():
    epistemic_space, metaphysical_space, zombie_candidate = witness_a_modal_space_separation()
    full_states, same_reduced_d1 = witness_b_descriptor_incompleteness()

    print("WITNESS A")
    print("epistemic_space:", sorted(epistemic_space))
    print("metaphysical_space:", sorted(metaphysical_space))
    print("zombie_in_epistemic:", zombie_candidate in epistemic_space)
    print("zombie_in_metaphysical:", zombie_candidate in metaphysical_space)
    print("epistemic_outstrips_metaphysical:", metaphysical_space < epistemic_space)

    print("\nWITNESS B")
    print("full_states:", sorted(full_states))
    print("states_with_same_reduced_physical_descriptor_d=1:", same_reduced_d1)
    print("same_reduced_descriptor_can_differ_in_q:", len({state[2] for state in same_reduced_d1}) > 1)
    print("full_underlying_states_equal:", same_reduced_d1[0][:2] == same_reduced_d1[1][:2])


if __name__ == "__main__":
    main()
