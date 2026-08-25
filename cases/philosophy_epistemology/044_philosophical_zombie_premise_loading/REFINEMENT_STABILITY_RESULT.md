# PHIL-001 Independent Follow-up Result — Refinement Stability and Uniform Completion

Status: **independent DSD-formulated attack executed and literature-compared**.

Judgment: **survives as a nontrivial under-justification challenge to the ideal positive conceivability premise, but does not by itself refute Chalmers's mature zombie argument**.

## 1. Source target

Chalmers's compact anti-materialist formulation lets `P` be the complete microphysical truth about the world and `Q` a phenomenal truth.

In his account of positive conceivability, ordinary thought experiments do not imagine microphysical details exhaustively. A subject imagines important features and judges that the remaining details can in principle be filled in to obtain a full coherent situation. Ideal positive conceivability strengthens this: the positive conception must survive ideal rational reflection, including attempts to fill arbitrary details without revealing contradiction or misverification.

This creates a precise structural question for the zombie premise `P & ~Q`:

**What kind of completion claim is actually supported when the imagined situation does not contain the complete microphysical detail represented by P?**

## 2. Finite-detail versus global-completion distinction

Let the complete physical base be represented schematically as

`P = conjunction_{i in I} p_i`,

where `I` indexes the physical facts/coordinates needed for the comparison.

For a finite `F subset I`, let

`P_F = conjunction_{i in F} p_i`.

A weak detail-filling result is:

`for every finite F, there exists a zombie-like candidate z_F satisfying P_F & ~Q`.

The full zombie premise requires a stronger uniform witness:

`there exists one z satisfying P & ~Q`,

or equivalently

`there exists one z such that for every finite F, z satisfies P_F & ~Q`.

The two quantifier patterns are:

`forall F exists z_F`

and

`exists z forall F`.

They are not logically equivalent.

## 3. Nested refinement formulation

Let

`Sigma_1 <= Sigma_2 <= ...`

be increasingly fine physical descriptive regimes, and let `Z_n` be the set of zombie-like candidates that match the actual world under `Sigma_n`.

The evidence that every finite refinement remains locally completable yields at most

`Z_n != empty for every n`.

A full physical duplicate requires

`intersection_n Z_n != empty`.

Even if the `Z_n` form a decreasing nested family, nonemptiness of each stage does not in general imply nonempty total intersection without an additional compactness/completion principle.

## 4. Explicit infinite witness

Define the actual state by

- `p_i(actual) = 0` for every positive integer `i`;
- `Q(actual) = 1`.

For every `k >= 1`, define a zombie-like candidate `z_k` by

- `Q(z_k) = 0`;
- `p_i(z_k) = 0` for every `i != k`;
- `p_k(z_k) = 1`.

Let `Sigma_n` retain only `p_1,...,p_n`.

For every finite `n`, choose `z_{n+1}`. Then

`z_{n+1} ~_{Sigma_n} actual`

and `Q(z_{n+1}) = 0`.

Therefore every finite descriptive stage has a zombie-like candidate.

But every `z_k` differs from the actual state at `p_k`. Hence there is no `z_k` that is physically identical under the complete infinite descriptor.

Thus:

`forall n exists z_n matching Sigma_n`

is true in the witness, while

`exists z forall n z matches Sigma_n`

is false.

This is a formal logical witness only. It is not a model of consciousness and does not claim that actual microphysics has this form.

## 5. Uniform Completion Dilemma

Chalmers's phrase that arbitrary details can be filled in can now be read in two ways.

### Reading A — local/refinement-wise fillability

For every requested finite refinement, some coherent elaboration can be supplied.

This is too weak for the zombie argument. The witness above shows that all finite levels may remain nonempty while no single globally complete duplicate exists.

### Reading B — uniform/global fillability

There already exists one coherent full situation that simultaneously realizes every physical detail while lacking Q.

This is strong enough to avoid the witness. But then the epistemic burden is correspondingly stronger: the conceivability premise must establish the existence of a **uniform complete scenario**, not merely repeated failure to find contradiction in successively richer partial descriptions.

The thought-experiment intuition by itself does not automatically provide this global witness.

## 6. Relation to Chalmers's own definition

This attack does not show that Chalmers confuses the two readings explicitly.

His notion of **ideal positive conceivability** is naturally intended to use the stronger reading: the imagined situation must in principle admit coherent filling of arbitrary details and survive ideal reflection.

Therefore the attack does **not** refute the conditional principle:

`if P & ~Q is ideally positively conceivable in the full uniform sense, then ...`

Instead it challenges the epistemic support for the antecedent:

`P & ~Q is ideally positively conceivable`.

The challenge is especially sharp because `P` is the **complete** microphysical truth, while the ordinary positive-imagination procedure deliberately leaves microphysical details unspecified.

## 7. Compactness/completion burden

The move from all finite partial completions to a global completion is valid in some formal settings only when an appropriate compactness, completeness, inverse-limit, or consistency theorem is available.

No such general theorem follows merely from the psychological/rational fact that successive finite elaborations remain apparently coherent.

Accordingly, a mature defense has two options:

1. establish a global/uniform conceivability witness directly; or
2. supply an independent principle guaranteeing that local coherent extensions have a global coherent completion in the relevant epistemic scenario space.

If such a principle is supplied, it must be counted as an additional bridge condition rather than hidden inside the informal phrase `arbitrary details can be filled in`.

## 8. DSD-specific origin

This attack is motivated by three current DSD distinctions.

### Formation descriptor

The Formation Axiom System defines strict descriptive equivalence over a full declared formation descriptor and does not infer strict equivalence from reduced composite equality.

### Axis-property descriptor

The axis-property system explicitly says that its complete descriptor is complete **relative to the fixed Stage-VI base and declared core axis-property signature**, while undeclared semantic extensions are outside that descriptor.

This makes signature-relative completeness explicit rather than absolute by default.

### Static aggregation

The static aggregation paper proves that aggregate equality does not reconstruct support-tagged records or complete typed property structure without injectivity conditions.

These yield the methodological rule:

`agreement at every inspected reduced/refined stage does not automatically produce one globally identical complete structure`.

No DSD notion is identified with metaphysical possibility or phenomenal consciousness.

## 9. Dedicated literature comparison after prediction seal

The attack was timestamped in `REFINEMENT_STABILITY_PREDICTION.md` before a dedicated search for prior versions of this exact formulation.

The search found substantial **close prior art**:

- Adam Elga's 1998 online manuscript *A Conceivability Argument* argues that the exact zombie statement based on a complete physical specification cannot be explicitly written or grasped: the fundamental physical concepts are not yet known, the specification may be infinite, and a shorter schematic statement introduces further semantic problems.
- Murat Aydede argues that sufficiently rich descriptions make positive zombie conceivability difficult and at best open.
- Maja Malec explicitly emphasizes Chalmers's requirement that arbitrary details be fillable without contradiction and challenges the adequacy of the conceivability-to-possibility route.
- Later objections to the 'obscurity of the physical' similarly challenge the claim that present understanding warrants ideal zombie conceivability.

The dedicated searches did **not** return a source that, in the material retrieved, formulates the objection exactly as the refinement-stable uniform-witness condition

`forall finite refinement exists local zombie candidate` versus `exists one zombie candidate surviving all refinements`,

or as the decreasing-family/intersection condition `Z_n != empty for all n` versus `intersection Z_n != empty`.

This absence is not evidence of historical novelty. The safe classification is:

**DSD-specific formal sharpening/recasting of an established family of worries about complete physical specification and positive conceivability.**

## 10. What this attack actually establishes

### Established

1. Local/refinement-wise zombie survivability does not logically entail a uniform full-duplicate witness.
2. A finite-prefix or repeated detail-filling procedure needs an additional global-completion principle before it can establish complete physical duplication.
3. Chalmers's ideal positive conceivability is strong enough in intention to avoid the simple logical counterexample, but this shifts the burden onto establishing the strong global form for `P & ~Q`.
4. The attack is structurally distinct from the earlier intrinsic/categorical-coordinate completeness squeeze, although historically it belongs to a nearby objection family.

### Not established

1. That `P & ~Q` is impossible.
2. That no ideal reasoner can possess a uniform positive conception of `P & ~Q`.
3. That metaphysical possibility space is noncompact in the relevant sense.
4. That physicalism is true.
5. That the refinement-stability formulation is historically unprecedented.

## 11. Final judgment

**The independent attack partially survives.**

It does not defeat Chalmers's mature argument by contradiction. Instead it forces a sharper reading of Premise 1:

> The relevant zombie conceivability cannot be supported merely by a potentially endless sequence of compatible partial physical elaborations. It requires one refinement-stable, globally coherent completion of the complete physical truth `P` together with `~Q`, or an independent theorem/principle guaranteeing such a completion.

This is stronger and more formal than the previous generic claim that `P` might be incomplete, but it remains an attack on the justification of ideal positive conceivability rather than a proof of zombie impossibility.
