# Case 004 — Free Logic and Existential/Formation Import

## Status
Initial mathematical analysis in progress.

## Research question
Does the mere presence of a term/candidate force a later existence, admission, describability, realization, assignment, or channel status? Or must those later statuses be justified by separate conditions?

## Scope correction
The DSD Formation Axiom System is not literally a unary chain in which one object changes state from `candidate -> admitted -> realized`.

- candidate structural expressions belong to `E^L_B`;
- candidate configurations belong to `P^L_B`;
- expression admission/describability are predicates on expressions;
- restriction relates expressions;
- realization relates a restricted expression to a configuration;
- configuration describability is determined by a witness formula plus configuration-admission/coherence conditions;
- assignment applies to active material in describable configurations;
- channel formation is downstream.

Therefore Free Logic is compared only at the level of the shared inference discipline: **mere linguistic/model-record availability must not silently import a stronger downstream status.**

## DSD targets
1. Primitive Axiom I: `Desexpr(x) => Admexpr(x)`, with no converse.
2. Primitive Axiom II: restriction targets must be admitted, but candidacy alone does not imply admission.
3. Primitive Axiom III: realization preserves material/anchor data, but realization alone does not imply configuration describability.
4. Closure Clause IV: configuration describability requires the full witness formula.
5. Downstream consequence: non-describable configurations do not enter the admitted structural domain used by Stage V.

## External comparison target
Primary literature:

- Robert K. Meyer and Karel Lambert, “Universally free logic and standard quantification theory,” *Journal of Symbolic Logic*. Their defining criterion for free logic is that no existence assumptions are made with respect to individual constants.
- Karel Lambert, “Existential Import Revisited,” *Notre Dame Journal of Formal Logic* 4(4), 288–292 (1963), DOI: 10.1305/ndjfl/1093957655.
- Nils Kürbis, “Normalisation for Negative Free Logics without and with Definite Descriptions,” *Review of Symbolic Logic* (2024), as a modern proof-theoretic example in which singular terms need not refer.

The external notion of non-denotation/existential import is not identified with any DSD formation status.

## Planned finite tests
### Test A — Expression-status triangle
For a candidate expression, test the three statuses allowed by Primitive Axiom I:

- non-admitted and non-describable;
- admitted but non-describable;
- admitted and describable.

Verify that describable but non-admitted is exactly the forbidden state.

### Test B — Realization without configuration describability
Construct a sound realization relation into a candidate configuration while making one configuration-admission predicate false. Verify that realization alone does not force `Descfg`.

### Test C — Predefinition/promotion rules
Add hypothetical rules such as

- `candidate => admitted`,
- `admitted => describable`,
- `realized => describable configuration`.

Show that each rule removes models otherwise admitted by the Formation Axiom System, so none is a harmless restatement of the current theory.

## Falsification criteria
A problem would be found if the current Formation axioms or closure clauses silently derived any of the above promotion rules despite claiming the stages are distinct, or if a candidate record necessarily acquired downstream status without the declared witness conditions.

## Success criterion
The case passes only if the formal theory preserves the separation it claims, while the comparison with Free Logic is explicitly limited to the methodological pattern of avoiding unjustified existential/formation import.