# PHIL-004 / Global 047 — Twin Earth Reference-Regime Audit

Status: **first-pass analysis completed; precedent-convergence case**.

Current branch:

`analysis/phil-004-twin-earth-reference-regime-audit`

## Files

- `PLAN.md` — original Q1–Q7 audit plan and failure conditions.
- `SOURCE_NOTES.md` — Putnam source reconstruction plus post-analysis literature comparison.
- `RESULT.md` — completed DSD analysis and verdict.
- `REPRODUCIBILITY.md` — finite-witness scope and rerun instructions.
- `repro/check_semantic_signature_fork.py` — finite semantic-signature witness.
- `../PRECEDENT_CONVERGENCE.md` — project classification for rare precedent-convergence cases.

## Primary classification

PHIL-004 is **not primarily an attack case**.

Putnam's Twin Earth argument is retained as a **precedent-convergence case**: an established external argument that independently preserves structural distinctions strongly aligned with DSD's Formation, Axis-Property, and reconstruction disciplines.

The source argument and DSD are not the same theory. Putnam is making a semantic-externalist argument about natural-kind reference; DSD provides a more general typed structural/describability discipline. The relevant result is independent structural convergence, not theoretical identity.

## Core structural convergence

The source setup permits:

`I(O_E) = I(O_T)`

and

`U(O_E) = U(O_T)`

while

`E(O_E) != E(O_T)`.

If broad reference is an environment-sensitive relational property, for example

`R_B = g(I, U, E, H, C)`,

then

`R_B(O_E) != R_B(O_T)`

is structurally coherent.

This aligns with the DSD rule that equality of one reduced/internal descriptor does not force equality of a fuller typed structure or of a property whose signature contains additional inputs.

## Semantic-Signature Fork

The retained DSD restatement keeps three branches distinct.

1. **Narrow/internal signature** — internal/surface inputs only; Earth and Twin-Earth records may agree.
2. **Broad/externalist signature** — environment, causal history, and/or community inputs are constitutive; broad references may differ.
3. **Underspecified `meaning`** — equality or inequality is not yet a well-posed comparison until the semantic property signature is fixed.

Thus:

`same narrow/internal semantic record`

and

`different broad reference/extension`

can coexist without contradiction because they concern different typed properties.

This is recorded as a DSD formal restatement/sharpening of a structure already present in the precedent argument, not as a new philosophical refutation.

## Observer/regime convergence

The narrator can be stipulated to distinguish Earth `H2O` from Twin-Earth `XYZ` while the 1750 speakers cannot.

Putnam intentionally preserves that difference between analyst-level environmental information and subject-accessible information. This strongly parallels the DSD requirement not to collapse external/narrator information into an internal subject's admitted description.

## Reconstruction convergence

The same surface form `water` and the same selected internal state do not uniquely reconstruct the full semantic-environmental record.

Twin Earth therefore independently exhibits the same kind of non-injectivity discipline that DSD uses when warning that a reduced descriptor or aggregate need not reconstruct its support-tagged/full typed source structure.

## Source-scope boundary

Putnam's 1975 argument first concerns linguistic reference/extension. Later externalist literature extends the Twin-Earth structure to propositional-attitude content.

PHIL-004 therefore preserves a separate content-individuation bridge before moving from linguistic reference to broad mental content. This scope distinction is established literature and is not claimed as historically new.

## Subordinate negative-control check

The hypothetical inference

`same narrow/internal state -> same broad reference`

is invalid when the target reference property explicitly includes environmental or causal-historical inputs.

This is retained only as a **subordinate negative-control check on DSD itself**: DSD must not infer equality of a relational property from equality of only one component of its signature.

It is not the headline characterization of PHIL-004 and is not presented as an attack that Putnam had to survive.

## Final classification

**Precedent convergence: Putnam's Twin Earth independently preserves structural distinctions congenial to DSD Formation/Axis-Property/reconstruction rules; DSD Semantic-Signature Fork is a typed formal sharpening/restatement; no historical novelty or priority claim.**

Within the current philosophy-analysis sequence, this is treated as a relatively uncommon and especially informative outcome because the external argument is better understood as a structurally aligned predecessor than as an adversarial target.

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