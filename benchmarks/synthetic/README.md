# Synthetic / Controlled Benchmarks

These benchmarks implement Mode D of the DSD Analysis four-mode validation protocol.

## SYNTH-D01 — Synthetic Control Set 01

Path: `benchmarks/synthetic/D01_control_set_01/`

Branch: `benchmark/d01-synthetic-control-set-01`

Ground-truth commitment:

`50af7900f8d4d259a55604097e4774650c7ca1342c4b598a0d9a97559d21f0c4`

Judgment seal:

`808922c00e17ecb06f1c72da119bd12f699b3490`

### Result

Baseline Mode-D calibration passed.

Raw confusion counts:

- TP: **5**
- TN: **3**
- FP: **0**
- FN: **0**
- partial: **0**
- total: **8**

No single accuracy percentage is reported because this is a small hand-constructed calibration set.

The strongest control contrasts were:

1. output equality without injectivity versus output equality with a proved injective bridge;
2. invalid part-to-whole attribution versus a whole-level property explicitly defined compositionally from exhaustive component checks.

The perfect D01 count is not treated as a generalization claim. D02 should use adversarial matched pairs with more similar surface wording and harder clean controls.

Reproduce from repository root:

```bash
python benchmarks/synthetic/D01_control_set_01/repro/verify_d01.py
```

## Next

The four validation modes now all have at least one operational record. PHIL-003 may be opened next. `SYNTH-D02` remains a required stronger follow-up, not a prerequisite for PHIL-003.
