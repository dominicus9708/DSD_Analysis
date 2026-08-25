# Synthetic Control Set 01 — Result

Status: **completed and unblinded after sealed judgments**.

Validation mode: **Mode D — synthetic / controlled discrimination**.

Branch: `benchmark/d01-synthetic-control-set-01`.

Ground-truth SHA-256 commitment:

`50af7900f8d4d259a55604097e4774650c7ca1342c4b598a0d9a97559d21f0c4`

Judgment-seal commit:

`808922c00e17ecb06f1c72da119bd12f699b3490`

## 1. Integrity check

The hidden `GROUND_TRUTH.json` was generated before analyst judgments and withheld locally.

Before unblinding, only its SHA-256 commitment was committed to GitHub. After all eight DSD judgments were sealed, the hidden JSON was disclosed.

The disclosed file hashes to the exact pre-seal commitment.

Therefore the ground-truth assignment was not changed to fit the sealed judgments.

## 2. Unblinding matrix

| Case | Ground truth | Sealed DSD judgment | Result |
|---|---|---|---|
| S-001 | valid compositional bridge / clean | clean | TN |
| S-002 | inverse reconstruction without injectivity | defect | TP |
| S-003 | undefined/zero status conflation | defect | TP |
| S-004 | valid injective bridge / clean | clean | TN |
| S-005 | clean no-defect uniqueness inference | clean | TN |
| S-006 | premise/criterion loading | defect | TP |
| S-007 | observer-information leakage | defect | TP |
| S-008 | part/whole attribution error | defect | TP |

## 3. Raw counts

- true positives: **5**
- true negatives: **3**
- false positives: **0**
- false negatives: **0**
- partial/mixed: **0**
- total controls: **8**

No single accuracy percentage is reported because the sample is too small and hand-constructed for such a number to be meaningful.

## 4. Strongest discrimination

The most informative matched contrast is `S-002` versus `S-004`.

Both cases concern equality at an output/encoding level and an attempted identity conclusion.

- `S-002`: external measurements are equal but no injective reconstruction bridge is supplied. DSD rejects internal-process identity.
- `S-004`: injectivity on the declared domain is explicitly proved and domain membership is established. DSD accepts `f(x)=f(y) -> x=y`.

This matters because the framework did not mechanically reject every inverse-looking inference. It distinguished an invalid reconstruction from a valid one when the missing bridge was supplied.

A second useful contrast is `S-001`/`S-008`.

- `S-001`: the whole-level property is explicitly defined as exhaustive satisfaction of component-level requirements, so the part-to-whole step is licensed.
- `S-008`: individual components lack a whole-system forecast, but no rule states that the assembled system cannot aggregate one; the negative part-to-whole inference is therefore invalid.

## 5. What the set supports

SYNTH-D01 supports the limited methodological statement:

> Under a small blinded control set with precommitted hidden labels, DSD Analysis correctly distinguished several intended structural defects from explicit valid bridges and clean controls without a false positive or false negative in this set.

It also demonstrates that the adopted DSD rules are not purely one-directional attack heuristics: an explicit injectivity, uniqueness, or compositional bridge can make an inference survive the audit.

## 6. What the set does not support

This set does **not** establish:

- a general error rate for DSD Analysis;
- performance on ambiguous natural-language arguments;
- robustness against adversarial wording;
- independence from analyst familiarity with the DSD rules;
- superiority over standard logic, statistics, philosophy, or software-analysis methods;
- truth of the Formation Axiom System or Axis-Property Axiom System.

The cases were hand-authored to instantiate known mechanisms and are relatively separable. A perfect result on this first calibration set is therefore informative but weak evidence about generalization.

## 7. Failure analysis

There were no FP or FN cases in D01, so no rule revision is triggered.

Absence of errors in this set must not be interpreted as evidence that the current rules need no refinement.

## 8. Next control-set requirement

`SYNTH-D02` should be materially harder.

It should include adversarial matched pairs with nearly identical surface wording, including:

1. same-output inference with and without a valid injectivity theorem;
2. part-to-whole inference with and without an explicit compositional definition;
3. blank/missing/undefined values contrasted with a schema where blank is explicitly defined as zero;
4. observer information that is actually transmitted through a permitted channel versus information available only to the experimenter;
5. premise loading contrasted with a superficially similar but independently validated criterion;
6. at least two clean/no-defect controls whose vocabulary resembles known DSD failure patterns.

## 9. Reproducibility

From the repository root run:

```bash
python benchmarks/synthetic/D01_control_set_01/repro/verify_d01.py
```

Expected final lines include:

```text
commitment_matches: True
counts: {'TP': 5, 'TN': 3, 'FP': 0, 'FN': 0}
total: 8
verification_passed: True
```

## 10. Overall judgment

**Mode-D baseline calibration passed.**

The important result is not the perfect small-sample count by itself. The important result is that DSD accepted explicit valid bridges while rejecting structurally similar cases lacking those bridges, and preserved clean controls rather than treating every case as defective.

The four-mode validation program now has at least one operational record in all four modes. The next philosophy case may proceed, while D02 remains a required stronger follow-up rather than a prerequisite for opening PHIL-003.
