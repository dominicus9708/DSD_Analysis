# PHIL-001 Reproducibility Record

This case began as a source-and-argument audit. The later follow-ups include small Python witnesses. Every script is a structural-logic aid only; none is a simulation or model of consciousness.

## Required sources

1. David J. Chalmers, “Does Conceivability Entail Possibility?” (2002):
   https://consc.net/papers/conceivability.html
2. Stanford Encyclopedia of Philosophy, “Zombies”:
   https://plato.stanford.edu/entries/zombies/
3. Daniel Stoljar, “The Conceivability Argument and Two Conceptions of the Physical” (2001), DOI 10.1111/0029-4624.35.s15.18.
4. Adam Elga, “A Conceivability Argument” (1998 online manuscript), used only as close prior art for complete-physical-specification worries.
5. Current DSD Formation Axiom System, used only for candidate/admission, full-descriptor, and comparison-boundary checks.
6. Current DSD Axis-Property Axiom System, used only for signature-relative descriptor completeness.
7. Current DSD Channel-Indexed Static Aggregation paper, used only for reduced-output/non-reconstruction comparison boundaries.

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

## Modal-bridge / descriptor-completeness follow-up

1. In Chalmers 2002, locate the section on **strong necessities** and verify that he explicitly formulates a counterexample to weak modal rationalism as a positively conceivable situation that corresponds to no possible world.
2. Locate the zombie appendix and verify:
   - `P & ~Q` is the target scenario;
   - the argument is called unsound *as it stands* at the primary/secondary step;
   - Chalmers acknowledges that structural/dispositional physical concepts may refer to underlying categorical properties;
   - a primary-P zombie world may therefore be structurally/dispositionally isomorphic while differing in categorical base;
   - the repaired conclusion becomes approximately `materialism is false OR panprotopsychism is true`.
3. Cross-check SEP on phenomenal concepts and Russellian monism.
4. Cross-check Stoljar's theory-based versus object-based conceptions of the physical.
5. Run the structural witness below.
6. Apply the two-horn completeness-conceivability test:
   - if `P = P_T` is theory-based/structural-dispositional, ask whether sameness of P establishes full physical identity;
   - if `P = P_F = P_T + I` includes all intrinsic/categorical physical facts, ask whether ideal positive conceivability of `P_F & ~Q` has been independently established.
7. Do not promote either witness into a theory of consciousness or a proof of physicalism.

### Command

```bash
python cases/philosophy_epistemology/044_philosophical_zombie_premise_loading/repro/check_modal_space_separation.py
```

### Expected judgment

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

## Refinement-stability / uniform-completion follow-up

This third attack was formulated and committed in `REFINEMENT_STABILITY_PREDICTION.md` before a dedicated search for the same attack form.

It tests whether repeated successful completion of increasingly detailed physical descriptions establishes one **uniform** full physical duplicate.

Let `Sigma_1 <= Sigma_2 <= ...` be increasingly rich physical descriptor regimes. The weak pattern is

`for every Sigma_n there exists some zombie-like z_n matching the actual world at Sigma_n`.

The strong pattern required for a refinement-stable full duplicate is

`there exists one z such that for every Sigma_n, z matches the actual world at Sigma_n`.

The scripts witness that these quantifier patterns are not generally equivalent.

### Finite refinement command

```bash
python cases/philosophy_epistemology/044_philosophical_zombie_premise_loading/repro/check_refinement_stability.py
```

This script contains:

1. a nested finite refinement witness in which zombie-like candidates disappear as the descriptor becomes complete; and
2. a finite quantifier-order witness where each requested coordinate-wise refinement has some matching candidate but no one candidate matches all refinements.

### Uniform completion command

```bash
python cases/philosophy_epistemology/044_philosophical_zombie_premise_loading/repro/check_uniform_completion.py
```

Expected central output:

```text
all_displayed_finite_prefixes_have_zombie_like_candidate: True
single_z_k_matches_every_physical_coordinate: False
reason: every z_k differs from actual at its own coordinate p_k
logical_pattern: (forall n exists z_k matching Sigma_n) does not imply (exists z forall n z matches Sigma_n)
```

### Mathematical witness

Let the actual state satisfy

`p_i = 0` for every positive integer `i`, with `q = 1`.

For each `k`, let `z_k` satisfy

- `q = 0`;
- `p_i = 0` when `i != k`;
- `p_k = 1`.

At the finite prefix `Sigma_n = {p_1,...,p_n}`, candidate `z_{n+1}` matches the actual state. Thus every finite prefix has a zombie-like candidate. But every candidate differs from the actual state at one physical coordinate, so no candidate is a full physical duplicate.

This establishes only

`forall finite refinement exists local witness`

`!=`

`exists one witness surviving all refinements`.

It does not establish that actual microphysics has this form.

## Dedicated literature-comparison rule

The refinement-stability formulation was sealed before a dedicated search for the exact objection. That search found close existing families about the obscurity/completeness of the physical specification and positive conceivability, including Elga, Aydede, Malec, and later discussions.

The retrieved literature did not supply an exact match for the particular quantifier-order / decreasing-family formulation used here. This absence must **not** be treated as proof of novelty.

Current conservative classification:

`DSD-specific formal sharpening/recasting of an established family of complete-specification and positive-conceivability objections`.

## Final expected status

```text
NAIVE PREMISE-LOADING ATTACK: FAIL
SIMPLE MODAL-SPACE ATTACK AS NEW REFUTATION: FAIL
DESCRIPTOR-COMPLETENESS SQUEEZE: SURVIVES, BUT CONVERGES WITH STOLJAR/RUSSELLIAN FAMILY
REFINEMENT-STABILITY / UNIFORM-COMPLETION ATTACK: PARTIALLY SURVIVES AS UNDER-JUSTIFICATION CHALLENGE
FULL ZOMBIE ARGUMENT REFUTED: NO
IDEAL POSITIVE CONCEIVABILITY PREMISE REQUIRES A UNIFORM GLOBAL COMPLETION OR COMPLETION PRINCIPLE: YES
HISTORICAL NOVELTY ESTABLISHED: NO
```

## Robustness conditions

The descriptor-completeness challenge must be narrowed if a non-question-begging account establishes both (a) completeness of the physical base `P` and (b) ideal positive conceivability of that complete `P & ~Q`.

The refinement-stability challenge must be rejected if Chalmers's ideal positive conceivability is independently shown to provide one uniform globally complete witness, or if a justified compactness/completion principle guarantees that all relevant local coherent refinements have a common global completion.

Conversely, merely demonstrating that arbitrarily many finite elaborations remain coherent is insufficient by itself, because the quantifier-order witness shows that local witnesses need not be one common global witness.
