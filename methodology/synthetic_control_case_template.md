# Synthetic Control Validation Template

Purpose: test whether DSD Analysis can correctly discriminate known hidden mechanisms rather than only interpret historical cases.

## Control-set metadata

- control set ID:
- generation date:
- ground-truth custodian:
- analyst blindness status:
- branch:
- commit sealing ground truth:

## A. Hidden ground-truth specification

This section must be inaccessible to the analyst until unblinding.

For each case, assign exactly one primary hidden condition and optional secondary conditions.

Allowed examples:

- premise loading present;
- premise loading absent;
- observer-information leakage;
- part/whole attribution error;
- descriptor incompleteness;
- status conflation: undefined / absent / zero;
- bridge explicitly valid;
- bridge absent;
- clean control: no intended defect.

The control set should include at least one clean case and, when practical, multiple cases with similar surface wording but different hidden structure.

## B. Blinded case statements

Present only the information an analyst is allowed to use.

### Case S-001

Statement:

### Case S-002

Statement:

### Case S-003

Statement:

## C. Sealed DSD judgments

For each case record:

- detected issue(s):
- predicted clean/surviving components:
- confidence category: high / medium / low;
- evidence used:
- explicit conditions that would reverse the judgment:

Do not reveal ground truth before all judgments are committed.

## D. Unblinding matrix

| Case | Ground truth | DSD judgment | Result |
|---|---|---|---|
| S-001 | hidden until unblinding | sealed judgment | TP / TN / FP / FN / partial |
| S-002 | hidden until unblinding | sealed judgment | TP / TN / FP / FN / partial |
| S-003 | hidden until unblinding | sealed judgment | TP / TN / FP / FN / partial |

## E. Minimum metrics

Report at least:

- true positives;
- true negatives;
- false positives;
- false negatives;
- partial/mixed classifications;
- total controls.

Do not report a single accuracy percentage when the sample is too small to be meaningful. Preserve the raw confusion counts.

## F. Failure analysis

For every FP or FN:

1. identify which DSD rule or interpretation caused the error;
2. determine whether the problem is in the rule, encoding, scope, or analyst application;
3. decide whether the rule should be revised, narrowed, or retained;
4. rerun only in a new version, never by overwriting the failed sealed result.

## G. Anti-overfitting rule

A synthetic set must not be designed so that the wording directly mirrors DSD terminology. Surface vocabulary should vary independently of the hidden mechanism.

Do not tune the cases after seeing which ones DSD misses unless a new versioned control set is created.

## H. Final record

- control set result:
- strongest successful discrimination:
- strongest false positive:
- strongest false negative:
- rule changes triggered:
- next control-set requirements: