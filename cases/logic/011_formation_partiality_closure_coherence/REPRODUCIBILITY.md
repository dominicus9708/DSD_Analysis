# COH-001 Reproducibility

The bundled checker verifies one explicit nonempty finite Formation witness. It is a sanity check only and is not a general proof.

## Files

- `repro/check_finite_witness.py`
- `repro/expected_output.txt`

## Run from repository root

`python cases/logic/011_formation_partiality_closure_coherence/repro/check_finite_witness.py`

## Expected checks

- Primitive Axioms I, II, III, V return `True`.
- The describable configuration set is `['p']`.
- The active union `A*` is `['a']`.
- One defined-zero admitted channel is produced.

## Interpretation

Success means only that this displayed finite primitive dataset is jointly satisfiable under the implemented checks. General coherence, independence, and closure claims still require the mathematical analysis in `RESULT.md`.

If later work requires exhaustive finite search, add a separate bounded-search script and record the exact bounds and completeness claim.