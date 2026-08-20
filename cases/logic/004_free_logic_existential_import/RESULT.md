# Case 004 — Result

## Final case judgment

**No falsification of the Formation Axiom System was found in Case 004.**

The specific DSD structure tested here is the refusal to infer a stronger formation status merely from earlier candidate or relation data. Free Logic supplies an independent external analogue at the level of inference discipline: singular terms need not carry existential import merely because they occur in the language.

The correspondence is partial only. DSD candidacy is not non-denotation, DSD admission is not existence, and DSD realization is not semantic reference.

## 1. Exact status result for candidate expressions

For any candidate expression `x`, write

- `A(x)=1` iff `Admexpr_L(x)`;
- `D(x)=1` iff `Desexpr_L(x)`.

Primitive Axiom I is exactly

`D(x) <= A(x)`.

Hence the allowed status pairs are

- `(0,0)` candidate but non-admitted and non-describable;
- `(1,0)` admitted but non-describable;
- `(1,1)` admitted and describable.

The sole forbidden pair is `(0,1)`.

All three allowed states have explicit finite extensions of a valid active kernel. Therefore the distinctions are semantically/model-theoretically real inside the admitted model class and not merely verbal labels.

### Consequence

Neither

`candidate => admitted`

nor

`admitted => describable`

is derivable from the current system.

## 2. Realization does not smuggle in describability

A second finite witness uses a sound realization `Realize_L(h,p)` with matching active material and anchors, while one configuration-admission predicate is false.

Primitive Axiom III is satisfied, but `Psi_L(p)` is false and Closure Clause IV therefore gives `Descfg_L(p)=false`.

Thus

`Realize_L(h,p) !=> Descfg_L(p)`.

This confirms the paper's explicit statement that realization alone does not imply configuration describability.

## 3. Predefinition/promotion rules are genuine extra assumptions

Adding any of the following rules strictly reduces the admitted model class:

1. `candidate => admitted`;
2. `admitted => describable`;
3. `realization => describable configuration`.

Each rule eliminates a finite model currently admitted by the Formation Axiom System.

Therefore these promotion rules are not hidden consequences of the current formalism. Treating them as 'obvious' would be an additional modeling assumption.

This gives a precise Case-004 instance of the DSD Analysis concern about **unjustified predefinition**: a later status must not be inserted merely because an earlier representation is already available.

## 4. Free Logic comparison

Meyer and Lambert characterize free logics by making no existence assumptions with respect to individual constants. This independently demonstrates that formal logic can treat the presence of a term separately from an existential commitment associated with that term.

The structural correspondence with DSD is:

- Free Logic rejects automatic existential import from term occurrence;
- DSD rejects automatic formation import from candidate/admission/realization occurrence.

### Non-correspondence

The following equations are invalid:

- `free-logical term = DSD candidate expression`;
- `denotation/existence = DSD admission`;
- `denotation = DSD realization`;
- `truth = DSD describability`.

Free Logic therefore does not prove Primitive Axioms I–III or Closure Clause IV. It is an external node showing that the general discipline of separating representation from stronger status has independent logical precedent.

## 5. Important correction to the simplified DSD roadmap

The informal phrase

`candidate -> admissible -> realized -> assigned -> channel`

is useful only as a mnemonic.

The actual Formation system has different sorts and relations:

- candidate expressions `E^L_B`;
- expression admission/describability;
- expression restrictions;
- candidate configurations `P^L_B`;
- realization relation from expression to configuration;
- configuration admission/coherence and derived describability;
- active material and Stage-V assignment;
- Stage-VI channels.

Case 004 therefore records the exact typed chain rather than treating all words as unary states of one object.

This is a roadmap precision correction, not a paper defect.

## 6. Does Case 004 show that the Formation Axiom System is wrong?

### Primitive Axiom I
**No.** Its one-way implication is coherent, and all three permitted expression-status pairs are realizable.

### Primitive Axiom II
**No contradiction found.** Identity restriction is triggered by admission; it does not force candidacy to become admission.

### Primitive Axiom III
**No.** A sound realized configuration can still fail later configuration-describability conditions.

### Closure Clause IV
**No.** It correctly requires the full witness formula rather than realization alone.

### Entire Formation Axiom System
**Not proved by this case.** The analysis tests formation-status promotion and does not independently retest assignment-globality, channel closure, composition, or all equivalence results.

## 7. Paper revision status

**No corrective revision is required from Case 004.**

Optional clarification only:

> Membership in a candidate carrier records availability as formation input data and has no automatic admission, describability, realization, assignment, or channel consequence beyond the declared predicates, relations, axioms, and closure clauses.

The formal paper already behaves this way; the sentence would merely make the anti-promotion principle more explicit for readers.

## 8. Case classification

- Domain: mathematical/philosophical logic
- External node: Free Logic
- DSD layer tested: Formation Stages I–IV, with downstream Stage-V boundary consequence
- Main distinction: candidate/representational availability vs stronger formation status
- Mapping strength: **partial structural correspondence**
- Falsification status: **not falsified**
- Correction required to Formation paper: **no**
- Roadmap refinement required: **yes — replace the oversimplified unary promotion chain with the typed expression/restriction/configuration structure**
- DSD Analysis target supported: **unjustified predefinition/promotion is a genuine extra assumption, not a theorem of the current system**
- Cross-domain node status: **accepted as fourth provisional node**

## References

- Kwon Dominicus, *Formation Axiom System — Dimensional-Structural Describability*, 2026, especially Sections 2–4.
- Meyer, R. K.; Lambert, K., “Universally free logic and standard quantification theory,” *Journal of Symbolic Logic*.
- Lambert, K. (1963), “Existential Import Revisited,” *Notre Dame Journal of Formal Logic* 4(4), 288–292. DOI: 10.1305/ndjfl/1093957655.
- Kürbis, N. (2024), “Normalisation for Negative Free Logics without and with Definite Descriptions,” *Review of Symbolic Logic*.