# Synthetic Control Set 01 — Sealed DSD Judgments

Status: **sealed before ground-truth disclosure**.

Ground-truth commitment available at `GROUND_TRUTH_COMMITMENT.txt`.

The analyst used only `BLINDED_CASES.md` plus the previously adopted DSD Analysis rules. No hidden labels were consulted before this seal.

## S-001

- Judgment: **clean / no intended structural defect detected**.
- Reason: the target property `complete` is explicitly defined compositionally: every required compartment contains its required item. The inspectors verify every required compartment, so the conclusion follows by the stated definition.
- Confidence: **high**.
- Reverse condition: if the definition of `complete` included additional batch-level requirements not checked at compartment level, or if the inspection were not exhaustive.

## S-002

- Judgment: **defect detected — inverse reconstruction / non-identifiability**.
- Reason: equality of five external measurements establishes equality only at that observation level. No injectivity or reconstruction theorem connects the measurement vector to a unique internal process. Distinct machinery or workflows may map to the same measured outputs.
- Confidence: **high**.
- Reverse condition: prove that the admitted process-to-measurement map is injective on the relevant process domain.

## S-003

- Judgment: **defect detected — status conflation**.
- Reason: a blank field from a period before recording began is not evidence of a measured numerical zero. Replacing unrecorded/undefined entries by `0` and then concluding no donations occurred collapses status into value.
- Confidence: **high**.
- Reverse condition: establish by registry semantics and independent coverage evidence that blank is defined to mean verified zero rather than unrecorded/unavailable.

## S-004

- Judgment: **clean / valid bridge explicitly supplied**.
- Reason: `x,y in D`, `f` injective on `D`, and `f(x)=f(y)` legitimately imply `x=y`. The reconstruction bridge that DSD normally demands is explicitly proved.
- Confidence: **high**.
- Reverse condition: failure to establish domain membership or injectivity on the actual admitted domain.

## S-005

- Judgment: **clean / valid uniqueness bridge explicitly supplied**.
- Reason: both objects are in the same active registry at the same time and the registry guarantees unique serial numbers. Equal serials therefore identify one permit record under the stated rule.
- Confidence: **high**.
- Reverse condition: serial reuse, alias records, temporal mismatch, or a uniqueness rule weaker than one-to-one identity.

## S-006

- Judgment: **defect detected — premise/criterion loading**.
- Reason: membership in the evaluated `robust group` is defined by passing the new screening rule. Observing that every member of that group passed the rule merely recovers the selection criterion. It does not independently establish the stronger external property `genuinely robust`.
- Confidence: **high**.
- Reverse condition: supply an independent robustness criterion or outcome measurement not defined by the screening rule itself.

## S-007

- Judgment: **defect detected — observer-information leakage**.
- Reason: the participant's admitted information is local junction/door data, while `two turns from the exit` is available only to the experimenter through the full plan. Treating the latter as participant evidence mixes observer regimes.
- Confidence: **high**.
- Reverse condition: provide the participant with the map/distance information through an admitted channel before the inference.

## S-008

- Judgment: **defect detected — part/whole attribution error**.
- Reason: absence of a nationwide forecast in every individual local agent does not imply absence of a nationwide forecast at the assembled-system level. Aggregation or composition may realize a whole-system property not stored in any single component.
- Confidence: **high**.
- Reverse condition: establish that system output is definitionally restricted to the content of one individual agent, or prove that no composition/aggregation operation exists.

## Pre-unblinding summary

Predicted defective cases:

`S-002, S-003, S-006, S-007, S-008`

Predicted clean cases:

`S-001, S-004, S-005`

No judgment above may be rewritten after ground-truth disclosure. Any later correction must be appended as a versioned post-seal analysis.
