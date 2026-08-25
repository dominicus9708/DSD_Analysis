# Reproducibility — K_R-003 / Global Case 041

## Purpose

Reproduce the finite two-model witness used to show that an OWL-style existential restriction can force existence of some suitable filler without entailing that an arbitrarily chosen named individual is that filler.

## Run from repository root

```bash
python cases/knowledge_representation/003_existential_anonymous_witness/repro/check_existential_anonymous_witness.py
```

## Expected output

See `repro/expected_output.txt` in this case directory.

## Interpretation

`M_UNNAMED` satisfies the existential using domain element `W`, which is not the interpretation of named individual `b`.

`M_NAMED_B` satisfies the same existential using `b`'s interpretation.

Because both satisfy the same existential condition while disagreeing on `P(a,b)` and `C(b)`, those named facts are not entailed by the existential condition alone.

## Scope

The script is a finite semantic witness, not an OWL 2 implementation or conformance test. It directly instantiates the `ObjectSomeValuesFrom(P C)` existential condition from the W3C Direct Semantics.