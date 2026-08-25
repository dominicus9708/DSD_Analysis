# Reproducibility — K_R-001 / Global Case 039

## Purpose

Reproduce the finite countermodel argument used in the analysis.

The script is intentionally small and uses only the Python standard language/runtime. It is not an OWL 2 reasoner and does not claim OWL conformance. It instantiates the relevant model-theoretic condition for one object-property pair.

## Run from repository root

```bash
python cases/knowledge_representation/001_open_world_nonassertion_falsity/repro/check_open_world_models.py
```

## Expected output

See:

`cases/knowledge_representation/001_open_world_nonassertion_falsity/repro/expected_output.txt`

## Interpretation

The base ontology leaves the truth of `P(a,b)` unconstrained, so two candidate models remain: one with the pair in the property extension and one without it. Universal entailment therefore yields neither polarity.

Adding a positive assertion keeps only the positive model. Adding an explicit negative assertion keeps only the negative model.

The class-only line represents the fact that asserting `C(a)` does not by itself constrain an unrelated property pair `P(a,b)`.

The final closed-world line is a comparison policy only; it is deliberately labeled as an extra rule rather than OWL entailment.

## Verification status

The script was executed during case preparation and its output matched `expected_output.txt`.