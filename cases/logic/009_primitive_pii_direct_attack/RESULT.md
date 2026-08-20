# Case 009 — Result

## Final judgment

**No internal contradiction of Primitive Axis-Property Axiom PII was found.**

The direct attack does, however, identify the exact mathematical strength of PII more sharply than its informal label may suggest:

> PII is primarily an **availability/dependency compatibility condition**. It guarantees that a configuration carrying an actually defined bilinear-dependent property application, or an active formal closure explicitly declared bilinear-dependent, belongs to the bilinear-data domain and therefore has a supplied symmetric bilinear form. It does not by itself require the property values or closure outputs to be derived from, or semantically agree with, that form.

This distinction is the principal result of Case 009.

## 1. Missing bilinear data is correctly rejected

The paper's Countermodel 9.7 remains a valid minimal failure witness. A bilinear-dependent kind may have a nonempty defined application domain while `K_bil_A` is empty. PI and the remaining typing can hold, but PII fails exactly at that point.

Thus the axiom does real work: defined dependency cannot silently coexist with absence of the declared dependency carrier.

## 2. Empty-domain declarations do not trigger PII

A globally declared kind `varpi in Pi_bil_A` with an available but empty partial assignment domain does not force `p in K_bil_A`.

This is coherent with the system's status discipline. Global kind declaration is not the same as a defined local property application. Requiring bilinear data at every configuration merely because the kind is globally declared would add a stronger rule than the current axiom.

Therefore

`declared bilinear-dependent kind != locally instantiated bilinear-dependent claim`.

No underconstraint was found here relative to the paper's stated partial-application semantics.

## 3. PII is always locally satisfiable by a zero symmetric form

For any supplied vector space `E_amb_A,p`, the map

`b(x,y)=0`

is a symmetric bilinear form. Hence whenever a PII antecedent is true, one can satisfy the axiom at the dependency level by putting `p in K_bil_A` and supplying the zero form.

Therefore PII alone has no obstruction based on:

- realized-axis rank;
- number of selected channels;
- degeneracy;
- positive definiteness;
- metric signature;
- invertibility.

This shows that PII is intentionally weak as geometry. Stronger geometric requirements must come from separate declarations or compatibility laws.

## 4. Semantic-value compatibility is not enforced by PII

Take `E_amb=R^2` with the Euclidean form and two nonorthogonal realized lines. Declare a Boolean binary property kind as bilinear-dependent and assign the pair an arbitrary value such as `1`.

PII is satisfied as soon as the symmetric bilinear form is present. PII does not contain an equation requiring

`Xi(t1,t2) = f(b, l1, l2)`

for any specified `f`.

Thus an application-level interpretation such as “1 means orthogonal” could disagree with the actual bilinear form while PII still holds.

This does **not** contradict the paper because Remark 3.12 explicitly states that a property name alone has no mathematical content and that additional compatibility laws may be supplied. Definition 8.3 separately defines orthogonality directly from `b` when that standard relation is intended.

### Exact wording boundary
The formal content of PII should therefore be read as

`bilinear-dependent application/declared formal dependency => bilinear datum available`,

not as

`every declared bilinear-dependent property value is semantically validated by the bilinear datum`.

## 5. Dependency granularity is kind-level, not application-level

Membership in `Pi_bil_A` is global at the property-kind level. If one defined application of that kind exists at `p`, PII requires bilinear data at `p` even if that particular assigned value happens to be constant or computable without inspecting `b`.

This is not inconsistent. It is a declaration-granularity choice: the model says the interpretation of that property kind requires the symmetric bilinear datum.

A future system needing some applications of one kind to be bilinear-dependent and others not would require an application-level dependency predicate or a split into distinct property kinds.

## 6. Normal-input properties do not create a circular PII proof

The normal carrier exists only for `p in K_bil_A`. Therefore a property profile containing `normal` cannot become available and acquire a defined application while `p notin K_bil_A`.

Consequently, for such profiles the first antecedent of PII is already protected by typing. The nontrivial part of that antecedent concerns bilinear-dependent property kinds whose input profiles are available independently of the bilinear layer, such as tag-, line-, or subspace-based profiles.

There is no circular construction: P3 primitive data select `K_bil_A` and supply `b`; P4 derives normal carriers; P5 may then supply normal-input assignments. PII is a final cross-layer admissibility constraint.

## 7. Formal-closure trigger is intentionally stronger than mere property declaration

If `ClDecl(p)=1` and `FormalBilDep(p)=1`, PII triggers even if the resulting finite requirement set is empty. The local bit itself declares that the active formal-closure subrecord depends on bilinear data.

By contrast, a global bilinear property-kind declaration with no defined local application does not trigger PII.

This asymmetry is coherent with the different meanings of the two primitive declarations and does not create a contradiction.

## 8. Triadic/subspace omission from PII is coherent

Cyclic-triadic and subspace declarations are omitted from PII because their typing already requires `p in K_bil_A`. Including them again in the residual axiom would be redundant. Their contribution to the derived uniform closure-dependency flag is therefore compatible with the layered construction.

## 9. Pre-axiom scope choice: symmetric bilinear data only

Definition 8.1 fixes the dependency carrier to a **symmetric bilinear form**. Properties whose natural dependency is alternating, nonsymmetric, sesquilinear, nonlinear, cone-valued, or otherwise different are outside this particular bilinear layer unless separately encoded.

This is a signature/type scope choice, not a consequence proved by PII and not an internal contradiction.

Case 008 and Case 009 therefore exhibit a common pattern:

- Case 008: single-line functionality is fixed before PI;
- Case 009: symmetric-bilinear dependency type and kind-level dependency classification are fixed before PII.

## 10. Revision status

**No corrective revision is required.**

For the planned falsification-analysis paper, however, the following wording is important:

> Primitive PII was not falsified as a dependency-consistency axiom. The stress test showed that its formal strength is availability compatibility rather than semantic-value compatibility: it requires a symmetric bilinear datum when a declared dependency is locally instantiated, but additional laws are needed to relate particular property values or closure outputs to that datum.

An optional clarification in a future version of the source paper could say the same, but the present project plan is to report this as a stress-test result rather than revise the original paper solely for clarification.

## 11. Case classification

- Domain: direct internal axiom stress test
- DSD layer: Axis-Property Primitive PII / bilinear dependency
- Falsification status: **PII not falsified**
- Internal contradiction: **none found**
- Main result: **availability compatibility != semantic-value compatibility**
- Local satisfiability: **always possible at PII level via a zero symmetric bilinear form**
- Nondegeneracy/positive-definiteness forced by PII: **no**
- Dependency granularity: **global kind-level declaration with local nonempty-domain trigger**
- Normal-profile circularity: **none; typing pre-gates the carrier**
- Pre-axiom scope choice found: **symmetric bilinear form and kind-level dependency classification**
- Corrective revision required: **no**
- Falsification-analysis significance: **high; exposes exact weakness/strength of the second residual primitive axiom**
- Direct-attack campaign status: **Case 009 complete; next target is integrated Formation + Axis-Property countermodel search**
