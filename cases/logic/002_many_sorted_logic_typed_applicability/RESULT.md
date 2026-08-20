# Case 002 — Result

## Final case judgment

**No falsification of the tested Axis-Property typing structure was found in Case 002.**

The specific DSD claim tested here is that a property's typed applicability must be resolved before an ordinary property value is evaluated. Standard many-sorted logic supplies a strong independent analogue: function/predicate applications are well formed only when their argument sorts match the declared signature.

However, Case 002 also corrects an earlier roadmap overstatement. A wrong-sort input is not the same as DSD `unavailable input`.

## 1. Mathematical result

Let `d` be any ordinary value in a property codomain. If an encoder maps both

- a valid well-typed application whose value is `d`, and
- an ill-typed attempted application

into the same raw value `d`, then that encoding cannot reconstruct the original application status.

This follows immediately from the two-state collision

`Defined(d) != IllTyped`

but

`E_d(Defined(d)) = E_d(IllTyped) = d`.

Therefore an ordinary fallback value is not a faithful substitute for lost typing metadata.

A status mask or a disjoint status symbol restores the distinction.

## 2. DSD-side result

The current Axis-Property System already avoids the collision structurally.

For a property kind `varpi` with profile `sigma_L(varpi)`, the map

`Xi_{A,p,varpi} : X_{A,p,varpi} ⇀ Z_{L,varpi}`

has the typed profile product as its source. An object of a different input sort is outside that source and receives no property value merely because a numerical fallback exists.

Closure Clause 4.2 reinforces the same rule by requiring the property map to remain typed and forbidding silent zero assignment outside its partial domain.

Thus the tested typing layer is internally coherent and survives the external comparison.

## 3. Important correction: wrong sort is not `unavailable input`

The precise DSD distinctions are:

1. **wrong sort / outside profile product** — the proposed object is not an admissible input of the property map at all;
2. **unavailable input** — the property kind is declared but a carrier required by its profile is unavailable at the configuration;
3. **undefined application** — the full typed product exists, the input is well typed, but the partial assignment is not defined there;
4. **defined zero** — the well-typed input is in the domain and receives the designated zero;
5. **defined nonzero/value** — the well-typed input is in the domain and receives another value.

The earlier lightweight Many-Sorted Logic roadmap grouped item 1 too closely with item 2. Case 002 corrects that mapping.

This is a correction to the analysis roadmap, not a discovered contradiction in the Axis-Property paper.

## 4. What many-sorted logic actually supports

### Strongly supported comparison

- declared input sorts/profiles precede value evaluation;
- wrong-sort expressions are not ordinary false/zero evaluations;
- erasing sort information requires explicit replacement metadata if the original distinction is to be reconstructed.

### Not established by this node

Ordinary many-sorted logic does not by itself establish the DSD distinctions of:

- configuration-relative carrier unavailability;
- partial undefinedness on a well-typed input;
- candidate property kind versus declared property kind.

The partial-undefinedness distinction was independently tested in Case 001. The other two remain separate targets.

## 5. Does this show that the Axis-Property System is wrong?

### Typed profile and property typing

**No.** The tested structure is consistent with standard many-sorted practice and the finite witness produces no contradiction.

### Definition 3.10 status discipline

**No contradiction found.** Its conditions correctly place `undefined application` only after the typed input product is available. The only useful improvement is an explicit clarification that a wrong-sort attempted input lies outside `X_{A,p,varpi}` and is not called `unavailable input` or `undefined application`.

### Primitive Axiom PI

**Not tested by Case 002.** Many-sorted logic says nothing about every selected formation channel realizing exactly one axis line.

### Primitive Axiom PII

**Not tested by Case 002.** Many-sorted logic does not decide the bilinear-dependency compatibility requirement.

### Entire Axis-Property System

**Not proved true by Case 002.** The case validates one typing boundary and finds no local contradiction. Other residual axioms and dependent layers require independent tests.

## 6. Model-existence context

The current Axis-Property paper separately proves that every Stage-VI formation record induced by a full Formation model admits a trivial axis-property extension. This establishes nonemptiness of the admitted extension class relative to the inherited base, but it does not prove that every intended nontrivial interpretation satisfies PI or PII.

Case 002 adds a different result: the typed-property interface itself does not conflict with standard many-sorted typing practice.

## 7. Paper revision status

**No corrective revision is required from Case 002.**

One optional clarification would improve Definition 3.10 or its surrounding remarks:

> An attempted input of the wrong sort lies outside the typed product `X_{A,p,varpi}`. It is therefore neither `unavailable input` nor `undefined application`; no property-application status is evaluated for that attempted input.

This sentence would make an already implicit typing rule explicit and prevent the exact conflation discovered in the earlier roadmap notes.

## 8. Case classification

- Domain: mathematical/philosophical logic
- External node: Many-Sorted Logic
- DSD layer tested: Axis-Property signature, typed input product, property typing/status boundary
- Main DSD distinction: applicability/type correctness before value
- Mapping strength: **direct/strong for typed well-formedness; non-corresponding for carrier unavailability; Case-001-dependent for partial undefinedness**
- Falsification status: **not falsified**
- Correction required to paper: **no**
- Clarification opportunity: **yes**
- Correction required to roadmap: **yes — wrong-sort and unavailable-carrier must be separated**
- Cross-domain node status: **accepted as second provisional node, but narrower than originally expected**

## References

- Kwon Dominicus, *Axioms for the Property Structure of Realized Axes in Dimensional-Structural Describability*, 2026.
- Clark Barrett, Pascal Fontaine, Cesare Tinelli, *The SMT-LIB Standard: Version 2.7*.
- CVC3 User Manual, Type Checking section.
