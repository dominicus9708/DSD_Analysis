# PHIL-001 Reproducibility Record

This case began as a source-and-argument audit. The modal-bridge follow-up additionally includes a finite Python witness. The script is a structural logic aid only; it is not a simulation or model of consciousness.

## Required sources

1. David J. Chalmers, “Does Conceivability Entail Possibility?” (2002):
   https://consc.net/papers/conceivability.html
2. Stanford Encyclopedia of Philosophy, “Zombies”:
   https://plato.stanford.edu/entries/zombies/
3. Daniel Stoljar, “The Conceivability Argument and Two Conceptions of the Physical” (2001), DOI 10.1111/0029-4624.35.s15.18.
4. Current DSD Formation Axiom System, used only for the candidate/admission and descriptor-completeness comparison boundaries.
5. Current DSD Channel-Indexed Static Aggregation paper, used only for the reduced-output/non-reconstruction comparison boundary.

## First-pass reproduction procedure

1. Separate the simple zombie argument from Chalmers's mature modal formulation.
2. Record separately:
   - prima facie vs. ideal conceivability;
   - positive vs. negative conceivability;
   - primary vs. secondary conceivability;
   - the restricted bridge `ideal primary positive conceivability -> primary possibility`.
3. Verify that Chalmers explicitly rejects a trivial definition of conceivability in terms of possibility.
4. Verify that observer access and inverse reconstruction from behavioral observations are not part of the core modal inference.
5. Record the first-pass verdict: simple premise-loading criticism fails against the mature formulation.

## Follow-up reproduction procedure

1. In Chalmers 2002, locate the section on **strong necessities** and verify that he explicitly formulates a counterexample to weak modal rationalism as a positively conceivable situation that corresponds to no possible world.
2. Locate the zombie appendix and verify:
   - `P & ~Q` is the target scenario;
   - the argument is called unsound *as it stands* at the primary/secondary step;
   - Chalmers acknowledges that structural/dispositional physical concepts may refer to underlying categorical properties;
   - a primary-P zombie world may therefore be structurally/dispositionally isomorphic while differing in categorical base;
   - the repaired conclusion becomes approximately `materialism is false OR panprotopsychism is true`.
3. Cross-check SEP on phenomenal concepts and Russellian monism.
4. Cross-check Stoljar's theory-based versus object-based conceptions of the physical.
5. Run the finite structural witness below.
6. Apply the two-horn completeness-conceivability test:
   - if `P = P_T` is theory-based/structural-dispositional, ask whether sameness of P establishes full physical identity;
   - if `P = P_F = P_T + I` includes all intrinsic/categorical physical facts, ask whether ideal positive conceivability of `P_F & ~Q` has been independently established.
7. Do not promote either finite witness into a theory of consciousness or a proof of physicalism.

## Python witness

Repo-root command:

```bash
python cases/philosophy_epistemology/044_philosophical_zombie_premise_loading/repro/check_modal_space_separation.py
```

Expected output:

```text
WITNESS A
epistemic_space: [(0, 0), (0, 1), (1, 0), (1, 1)]
metaphysical_space: [(0, 0), (1, 1)]
zombie_in_epistemic: True
zombie_in_metaphysical: False
epistemic_outstrips_metaphysical: True

WITNESS B
full_states: [(0, 0, 0), (0, 1, 1), (1, 0, 0), (1, 1, 1)]
states_with_same_reduced_physical_descriptor_d=1: [(1, 0, 0), (1, 1, 1)]
same_reduced_descriptor_can_differ_in_q: True
full_underlying_states_equal: False
```

## Meaning of Witness A

Witness A proves only that, in a finite abstract system, a scenario space can contain a candidate excluded by a stricter admissibility space. It therefore demonstrates that a bridge rule is logically necessary.

It does **not** refute Chalmers, because Chalmers explicitly anticipates this structure as the strong-necessity problem and argues against strong necessities.

## Meaning of Witness B

Witness B proves only that two complete states can share a reduced descriptor while differing in an omitted intrinsic coordinate and a downstream property.

It therefore witnesses:

`same reduced descriptor != same complete underlying structure`.

It does **not** prove that physical theory is incomplete in precisely this way, that categorical properties exist, or that consciousness equals the omitted coordinate.

## Follow-up expected judgment

```text
SIMPLE MODAL-SPACE ATTACK AS NEW REFUTATION: FAIL
CHALMERS ANTICIPATES STRONG NECESSITY ISSUE: YES
P DESCRIPTOR-COMPLETENESS QUESTION SURVIVES: YES
STRUCTURAL P MAY BE INSUFFICIENT FOR FULL PHYSICAL IDENTITY: CONDITIONAL YES
FULLER P REQUIRES RENEWED IDEAL-CONCEIVABILITY JUSTIFICATION: YES
WHOLESALE REFUTATION OF MATURE ZOMBIE ARGUMENT: NO
CONVERGENCE WITH STOLJAR / RUSSELLIAN FAMILY: YES
DSD CONTRIBUTION: DESCRIPTOR-COMPLETENESS AUDIT, NOT CONSCIOUSNESS METAPHYSICS
```

## Robustness condition

If a non-question-begging account establishes both (a) completeness of the physical base `P` and (b) ideal positive conceivability of that complete `P & ~Q`, the current descriptor-completeness challenge must be narrowed.

If the physicalist counterposition merely stipulates an unknowable intrinsic coordinate without independent reason to count it as physical or consciousness-relevant, it does not by itself defeat Chalmers either.
