# ADMIN-003 Structural Model

## 1. Purpose

This model is a source-sensitive bookkeeping device for revision and correction. It is not asserted as a universal organizational ontology.

## 2. Version/state graph

Let `V` be the set of source-defined directive, plan, clearance, configuration, or execution states relevant to one organizational process.

Use a typed directed graph

`G_R = (V, E_review, E_amend, E_correct, E_hold, E_resume, E_supersede, E_implement, E_verify, E_release, E_close)`.

The edge labels are intentionally non-interchangeable.

- `E_review`: a state is examined without presupposing a change.
- `E_amend`: an operative content element is changed while some predecessor lineage may remain in force.
- `E_correct`: an identified discrepancy or erroneous representation is rectified relative to the source regime.
- `E_hold`: execution or release is suspended without by itself deciding the final disposition.
- `E_resume`: execution/release is explicitly restarted or rejoined under source-defined conditions.
- `E_supersede`: a later state replaces an earlier operative state in the relevant scope.
- `E_implement`: an approved or otherwise authorized change is enacted.
- `E_verify`: implementation is checked against the required condition.
- `E_release`: a changed item or instruction becomes the operative released state where the source distinguishes release.
- `E_close`: the review/change/problem process is administratively or technically closed where the source distinguishes closure.

## 3. Minimal non-totalization

The cross-domain evidence supports the negative structure

`review != approval != amendment != correction != implementation != verification != release != closure != resumption`.

It also supports

`revision != total replacement`

because Army FRAGORDs and FAA amended clearances can explicitly preserve unchanged portions.

## 4. Three revision outcomes

A review operation must not be encoded as `review -> change` by definition.

At minimum, the FEMA witness requires that a source may permit outcomes analogous to:

`review -> validate existing state`,

`review -> modify existing state`,

`review -> formulate new state`.

The exact dispositions remain source-specific.

## 5. Correction versus substantive change

The NASA and FAA witnesses pressure a useful distinction:

- correction can rectify an identified error, discrepancy, or incorrect transmission/readback;
- amendment/change can modify the operative instruction, requirement, route, design, objective, or configuration.

The two can overlap in a particular regime, but they are not identical by definition.

## 6. Lineage requirement

When an identity-defining directive coordinate changes, preserve predecessor/successor linkage explicitly rather than silently rewriting one object in place.

A simple version lineage can be written

`d0 --amend--> d1 --verify/release--> d2`

or

`d0 --hold--> h --resume--> d1`.

No claim is made that every organization uses version numbers, nor that every hold creates a new formal directive. The requirement is epistemic/bookkeeping: if the source regime treats the states as distinct, the analysis must preserve that distinction.

## 7. Outcome collision

Two organizational paths may reach the same final task result while differing in review, correction, authority, timing, or verification history.

Therefore

`same final result != same organizational path`.

This is especially important for responsibility, auditability, and reproducibility.
