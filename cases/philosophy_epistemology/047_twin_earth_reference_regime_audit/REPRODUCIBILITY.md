# PHIL-004 Reproducibility

## Branch

`analysis/phil-004-twin-earth-reference-regime-audit`

## Core witness

The finite witness checks a typed semantic-signature fork, not a complete semantic theory.

It verifies that the same selected internal and surface descriptors can coexist with:

1. equal narrow/internal semantic records under an internal-only signature; and
2. unequal broad references under an environment-sensitive signature.

It also verifies that the projection from the full Earth/Twin-Earth records to the selected internal/surface descriptor is non-injective.

## Run

From the repository root:

```bash
python cases/philosophy_epistemology/047_twin_earth_reference_regime_audit/repro/check_semantic_signature_fork.py
```

Expected output:

```text
same_internal: True
same_surface: True
narrow_equal: True
broad_reference_equal: False
projection_noninjective_witness: True
witness_passed: True
```

## What this establishes

The witness is sufficient for the structural consistency claim:

`same narrow/internal record + different broad reference`

is not contradictory when `narrow record` and `broad reference` are different typed properties with different signatures.

The witness also shows:

`same internal/surface projection != unique full semantic-environmental reconstruction`.

## What this does not establish

The witness does not prove:

- that Putnam's externalist semantic theory is uniquely correct;
- that a narrow content property exists in every defensible philosophy of language or mind;
- that `H2O` and `XYZ` are physically realizable with every stipulated macroscopic property;
- that all mental content is broad or narrow;
- that DSD supplies a theory of linguistic meaning.

Those questions require external semantic theory and philosophical argument beyond the finite structural witness.

## Literature classification

Post-analysis comparison places the result near established narrow/broad-content and two-factor/two-dimensional response families. Therefore the Semantic-Signature Fork is retained as a DSD formal sharpening and bookkeeping device, not as a historically novel philosophical objection.