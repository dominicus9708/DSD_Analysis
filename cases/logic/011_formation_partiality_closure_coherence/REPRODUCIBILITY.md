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

## 2026-08-25 execution check

The checker was executed during the COH-001 analysis pass and reproduced `expected_output.txt` exactly:

```text
Axiom I: True
Axiom II: True
Axiom III: True
Axiom V: True
Describable configurations: ['p']
A*: ['a']
Channels: [('p', 'a', 'lambda', 0, 'rho')]
```

## Interpretation

Success means only that this displayed finite primitive dataset is jointly satisfiable under the implemented checks and that the derived configuration/channel data agree with the prepared expectation.

It does **not** establish general consistency by computation, does not enumerate all finite formation models, and does not replace the manuscript's general set-theoretic proofs of model existence, independence, or unique relative closure.

If later work requires exhaustive finite search, add a separate bounded-search script and record the exact bounds and completeness claim.