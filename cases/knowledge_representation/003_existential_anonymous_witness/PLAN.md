# K_R-003 / Global Case 041 — Existential Restriction and Anonymous Witness

Status: **first-pass analysis completed**.

## Primary question

Can a formal knowledge-representation constraint require that some relation target exist without requiring that the target be a particular named individual?

## Main OWL 2 construct

`ObjectSomeValuesFrom(P C)`.

Under OWL 2 Direct Semantics this class denotes the individuals `x` for which there exists some domain element `y` such that `(x,y)` is in the interpretation of `P` and `y` is in the interpretation of `C`.

## Pressure tests

1. Show that an existential restriction forces at least one suitable successor.
2. Show that the restriction does not entail `P(a,b)` for an arbitrarily chosen named individual `b`.
3. Construct one model whose witness is unnamed and another whose witness is the named individual `b`.
4. Test whether the identity/name of the witness is part of what the existential restriction itself determines.
5. Compare carefully with DSD formation traces, where nonempty witness history characterizes an admitted channel but witness history is not inserted into operational channel identity.

## Anti-overlap rule

K_R-003 is not merely K_R-001 repeated. K_R-001 established that silence does not entail falsity. K_R-003 instead studies a positive existential constraint that **does entail existence**, while leaving the witness identity underdetermined.

## Non-identity boundary

An OWL existential filler is not a DSD formation-trace witness. OWL uses domain elements in a model-theoretic existential condition; DSD traces are explicit restriction-realization witness records inside the formation architecture.

## Deliverables

- `SOURCE_NOTES.md`
- `RESULT.md`
- `REPRODUCIBILITY.md`
- `repro/check_existential_anonymous_witness.py`
- `repro/expected_output.txt`
- Notion case page and roadmap updates