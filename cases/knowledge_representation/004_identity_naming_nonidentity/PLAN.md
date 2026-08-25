# K_R-004 / Global Case 042 — Identity, Same-As, and Naming Non-Identity

Status: **first-pass analysis completed**.

## Primary question

In OWL 2, do different names necessarily denote different individuals, and do equal display labels imply identity? What semantic content is added by `SameIndividual` and `DifferentIndividuals`?

## Pressure tests

1. **Different names without identity axioms** — construct models where names `a` and `b` co-denote and models where they denote distinct objects.
2. **Explicit equality** — add `SameIndividual(a b)` and test whether only co-denoting models remain.
3. **Explicit inequality** — add `DifferentIndividuals(a b)` and test whether only distinct-denotation models remain.
4. **Identity substitution** — test whether an assertion about `a` transfers to `b` when `a` and `b` are explicitly equal.
5. **Equal annotation/display labels** — verify that annotations do not create Direct-Semantics identity.
6. **Structure-implied equality** — test whether functional/cardinality constraints can force two different names to co-denote even without an explicit `SameIndividual` axiom.

## DSD comparison target

Compare only the structural rule that literal names, compressed readouts, or surface labels are not by themselves sufficient identity criteria. In the Formation Axiom System, operational channel identity is the typed five-tuple `(p,a,lambda,v,rho)`, while cross-model strict descriptive equivalence is defined by structure-preserving bijections rather than literal name equality.

## Required non-identity statement

OWL individual equality is equality of denotations inside an interpretation. DSD operational channel identity and strict formation isomorphism are different relations in a typed staged formation framework. They must not be identified.

## Expected deliverables

- `SOURCE_NOTES.md`
- `RESULT.md`
- `REPRODUCIBILITY.md`
- `repro/check_identity_naming.py`
- `repro/expected_output.txt`
