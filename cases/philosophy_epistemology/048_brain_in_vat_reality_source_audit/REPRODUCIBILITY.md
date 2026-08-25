# PHIL-005 Reproducibility

## Branch

`analysis/phil-005-brain-in-vat-reality-source-audit`

## Run

From the repository root:

```bash
python cases/philosophy_epistemology/048_brain_in_vat_reality_source_audit/repro/check_biv_regime_noninjectivity.py
```

Expected output:

```text
worlds_different: True
weak_indistinguishable: True
weak_projection_noninjective: True
strong_indistinguishable: False
added_discriminator_breaks_equivalence: True
same_surface: True
different_reference_regime: True
witness_passed: True
```

## What the witness establishes

The witness is deliberately finite and non-empirical.

1. Under a weak declared accessible-channel signature, two different full world records can share one accessible projection.
2. Adding one previously omitted discriminator breaks that equality, showing that `indistinguishable` is relative to a declared comparison signature.
3. One surface sentence can be retained while ordinary-English and vat-English reference assignments differ.

## What it does not establish

The witness does not simulate consciousness, hallucination, neurophysiology, electrical stimulation, or semantic truth. It does not show that any real brain-computer interface can produce complete BIV equivalence.

Its sole role is to verify the set-theoretic non-injectivity and signature-relative comparison claims used in PHIL-005.