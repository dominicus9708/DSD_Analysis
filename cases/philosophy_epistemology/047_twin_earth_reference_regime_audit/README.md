# PHIL-004 / Global 047 — Twin Earth Reference-Regime Audit

Status: **first-pass analysis completed**.

Current branch:

`analysis/phil-004-twin-earth-reference-regime-audit`

## Files

- `PLAN.md` — original Q1–Q7 audit plan and failure conditions.
- `SOURCE_NOTES.md` — Putnam source reconstruction plus post-analysis literature comparison.
- `RESULT.md` — completed DSD analysis and verdict.
- `REPRODUCIBILITY.md` — finite-witness scope and rerun instructions.
- `repro/check_semantic_signature_fork.py` — finite semantic-signature witness.

## Core result

PHIL-004 does **not** refute Putnam's Twin Earth argument.

The naive attack

`same narrow/internal state -> same broad reference`

fails when reference is explicitly defined as an environment-sensitive relational property. Putnam's source argument is precisely constructed to deny that narrow psychological state alone fixes natural-kind extension.

The DSD audit instead preserves a typed distinction between semantic layers.

### Narrow/internal signature

An internal-only semantic property may satisfy:

`R_N(O_E) = R_N(O_T)`.

### Broad/externalist signature

An environment-sensitive reference property may satisfy:

`R_B(O_E) != R_B(O_T)`.

There is no contradiction because `R_N` and `R_B` are different typed properties with different input signatures.

## Semantic-Signature Fork

The retained DSD synthesis has three branches.

1. **Narrow/internal signature** — internal/surface inputs only; Earth and Twin-Earth records may agree.
2. **Broad/externalist signature** — environment, causal history, and/or linguistic-community inputs are constitutive; reference values may differ.
3. **Underspecified `meaning`** — equality or inequality is not yet a well-posed comparison until the semantic property signature is fixed.

This is a formal sharpening rather than a novel philosophical distinction.

## Key failed attack

Internal indistinguishability is **not** a counterexample to Putnam. The thought experiment deliberately makes the H2O/XYZ difference cognitively unavailable to the 1750 speakers while proposing that their references still differ.

DSD therefore records the attempted objection as a failure rather than rewriting it as a success.

## Source-scope boundary

Putnam's 1975 Twin Earth argument first targets linguistic reference/extension. Later philosophers extend the pattern to broad mental content.

PHIL-004 therefore requires a separate content-individuation bridge before moving from:

`different linguistic reference`

to

`different belief/mental content`.

This distinction is already standard in the literature and is not claimed as historically new.

## Reconstruction boundary

Constitutive externalism must be separated from inverse reconstruction.

Putnam's main move is constitutive: environmental relations are part of what fixes broad reference.

A different and invalid task would attempt to recover the hidden environment from the shared internal/surface descriptor alone. The Twin Earth setup itself provides a non-injectivity witness against that inverse reconstruction.

## Literature classification

Post-analysis comparison shows strong overlap with established:

- broad versus narrow content;
- Fodor-style narrow-content responses;
- two-factor / two-dimensional approaches;
- source-level distinctions between Putnam's linguistic-reference argument and later mental-content externalism.

Final classification:

**Putnam core survives; Mode-A-style failed attack preserved; Mode-B strong convergence; DSD Semantic-Signature Fork retained as typed formal sharpening; no historical novelty claim.**

## Reproduce

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

## Next case

`PHIL-005 / Global 048 — Brain in a Vat`.

The next audit will test what, if anything, internally accessible experience licenses about reconstruction of an external world, while preserving the difference between semantic self-reference arguments and ordinary skeptical inverse inference.