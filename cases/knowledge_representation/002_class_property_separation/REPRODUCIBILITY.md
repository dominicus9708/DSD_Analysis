# Reproducibility — K_R-002 / Global Case 040

## Purpose

Reproduce the finite semantic witness showing that class membership plus object-property domain/range/functionality does not force a concrete property assertion.

The script is not a complete OWL 2 reasoner. It instantiates the relevant Direct-Semantics clauses over a two-object finite domain.

## Run from repository root

```bash
python cases/knowledge_representation/002_class_property_separation/repro/check_class_property_separation.py
```

## Expected output

See `repro/expected_output.txt`.

## Interpretation

Both `M_empty` and `M_edge` satisfy:

- `ClassAssertion(C a)`;
- `ObjectPropertyDomain(P C)`;
- `ObjectPropertyRange(P D)`;
- `FunctionalObjectProperty(P)`.

Only `M_edge` contains `P(a,b)`. Since both models satisfy the constraint set, the constraint set does not entail the property assertion.

The reverse-direction statement records that, once `P(a,b)` is actually present, the domain and range axioms classify its endpoints. This prevents overreading the result as complete independence between class and property structure.

## Verification

The script was executed during analysis and matched `expected_output.txt`.