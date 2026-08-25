# PHIL-001 Independent Follow-up Prediction — Refinement-Stable Physical Duplication

Status: **prediction sealed before dedicated literature comparison for this attack**.

This is not a blind test in the strict sense because prior PHIL-001 work already examined Chalmers, SEP summaries, and established Russellian/Stoljar-style objections. No claim of historical novelty is made here. The purpose is narrower: formulate a DSD-native attack whose inferential target is not merely `P may omit intrinsic properties`, then timestamp the formulation before searching specifically for prior versions of the same argument.

## 1. Target

Chalmers's compact mature formulation lets `P` be the complete microphysical truth about the world and `Q` a phenomenal truth, then uses the conceivability/primary-possibility of `P & ~Q` in an anti-materialist argument.

The present attack asks whether the phrase **physical duplicate** is stable under admissible refinement of the physical descriptor used to compare worlds.

## 2. Descriptor-indexed physical equivalence

Let `Sigma` be a typed physical descriptive signature or comparison regime, and let

`D_Sigma(w)`

denote the complete physical descriptor of world `w` relative to `Sigma`.

Define

`w ~_Sigma z`

iff `D_Sigma(w)` and `D_Sigma(z)` are equivalent under the structure-preserving comparison appropriate to `Sigma`.

This relation is intentionally relative to a signature/regime. Equality at one descriptive granularity is not assumed to be equality under a richer signature.

## 3. Refinement

Let `Sigma <= Sigma'` mean that `Sigma'` is an admissible physical refinement of `Sigma`: it preserves the old coordinates/relations while adding physically admissible distinctions, coordinates, property kinds, supports, or comparison structure.

A pair `(w,z)` is **refinement-stably physically duplicate** over a refinement family `R` iff

`for every Sigma' in R, w ~_{Sigma'} z`.

The full duplicate relation is therefore an intersection of descriptor-relative equivalence relations, not the equality relation of one arbitrarily selected descriptor.

## 4. The new pressure point

A zombie argument intended to establish the possibility of a world physically identical to ours but phenomenally different needs a **single world** `z` such that

`Q(z) != Q(w)`

while

`for every admissible physical refinement Sigma', w ~_{Sigma'} z`.

It is weaker to establish only that, at every considered descriptive level, some zombie-like candidate can be found:

`for every Sigma', there exists z_{Sigma'} such that w ~_{Sigma'} z_{Sigma'} and ~Q(z_{Sigma'})`.

The quantifier order matters:

`forall Sigma' exists z_{Sigma'}`

does not imply

`exists z forall Sigma'`.

Thus a sequence or family of description-relative zombie candidates does not automatically provide one refinement-stable full physical duplicate.

## 5. Refinement-stability requirement

The anti-materialist use of the zombie contrast therefore appears to require at least one of the following:

1. **Descriptor finality:** a physical signature `Sigma*` is independently shown to be complete such that no admissible physical refinement can distinguish worlds already equivalent under `Sigma*`;
2. **Refinement invariance:** physical-duplicate equivalence is proven invariant under all admissible physical descriptor extensions;
3. **Uniform witness:** one and the same zombie world is shown to preserve physical equivalence across the entire admissible refinement family.

Without one of these, `physical duplicate` risks being only regime-relative.

## 6. Why this is not merely the earlier completeness objection

The earlier descriptor-completeness attack asked whether `P` omits intrinsic/categorical physical facts.

The present attack is formally different:

- even if every `D_Sigma` is complete **relative to its own signature**, equivalence may fail under `Sigma'`;
- even if a zombie-like candidate exists for each signature separately, the candidates may be different worlds;
- therefore the required issue is **coherent preservation of one witness under refinement**, not only whether one known coordinate is omitted.

The new target is the stability of the equivalence relation and the order of quantifiers over refinements and witnesses.

## 7. DSD origin of the test

The DSD Formation Axiom System defines full descriptors and strict equivalence relative to declared typed structure rather than inferring full equivalence from a reduced output.

The axis-property extension explicitly says that its complete descriptor is complete **relative to the fixed Stage-VI base and declared core axis-property signature**, and does not include undeclared application-level semantic extensions.

The static aggregation paper separately proves that equality of a reduced aggregate does not reconstruct support-tagged records or the complete typed structure.

These internal distinctions motivate a general audit rule:

`equivalent relative to declared descriptor Sigma`

is not automatically

`equivalent relative to every admissible refinement Sigma'`.

No DSD primitive is identified with metaphysical possibility or consciousness.

## 8. Finite falsification witness to be constructed

The planned witness will have an actual state with physical coordinates `(p1,p2,p3)` and phenomenal marker `q`, together with zombie-like candidates that preserve successively richer physical descriptors but do not survive the terminal refinement.

It will also construct a family in which

`forall refinement R_i, exists candidate z_i matching R_i`

is true while

`exists one candidate z matching every R_i`

is false.

This proves only the logical non-equivalence of the quantifier patterns. It does not prove that consciousness behaves like the witness coordinates.

## 9. Falsification conditions for this attack

The refinement-stability attack should be rejected or collapsed into the older completeness objection if any of the following is established:

1. `P` is given a theory-independent semantic definition as literally all physical truths, and that definition by itself fixes a final refinement-closed physical equivalence relation without relying on the anti-materialist conclusion.
2. Chalmers supplies an explicit uniform-witness principle showing that the same conceived world satisfies every admissible physical refinement rather than merely the primary intension of a selected physical description.
3. Any admissible extension that would distinguish the worlds is, by an independently justified criterion, nonphysical.
4. The proposed refinement family changes the subject by adding nonphysical or conclusion-dependent coordinates.

## 10. Predicted outcome before dedicated literature comparison

The likely result is **not** a proof that Chalmers is wrong.

The predicted surviving claim is narrower:

> A physical-duplicate premise strong enough for the anti-materialist conclusion should be refinement-stable. Conceivability relative to a selected or successively enriched physical descriptor does not by itself establish a single world that remains physically equivalent under every admissible refinement.

If Chalmers's `complete microphysical truth P` already semantically guarantees this stability, the attack reduces to a challenge about how that completion/finality is justified and should not be counted as an independent refutation.
