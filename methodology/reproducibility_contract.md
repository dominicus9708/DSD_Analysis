# DSD Analysis Reproducibility Contract

This file defines the minimum reproducibility standard for DSD Analysis cases.

## 1. Source lock

A completed case must identify:

- the external source actually used;
- the DSD paper and exact section/definition/axiom/theorem/closure clause used;
- any interpretation rule added by the case author rather than supplied by either source.

## 2. Separation of setup and conclusion

`PLAN.md` must state the question and decision criteria before `RESULT.md` states the outcome.

The setup must not encode the desired conclusion through an unexamined type, default value, hidden promotion rule, or source substitution.

## 3. Explicit finite evidence when available

When the issue is finite or combinatorial, record:

- carriers/sets;
- domains and codomains;
- primitive predicates/relations;
- defined and undefined inputs;
- expected derived structures;
- the exact condition that would count as a contradiction, collision, or non-correspondence.

A hand-checkable witness is preferred when computation adds no value.

## 4. Script requirement

Use a script only when it improves auditability, enumeration, search coverage, or repeated checking.

When a script is used, record:

- language and version assumptions;
- input path;
- output path;
- exact command;
- deterministic seed if randomness is used;
- expected summary output;
- failure conditions.

Python scripts should be committed with the completed case and invoked from repository-relative paths.

## 5. Status fidelity

Do not silently collapse any of the following when the source or DSD layer distinguishes them:

- absent
- inapplicable/unavailable
- undefined
- defined zero
- defined nonzero
- same aggregate with different underlying structure

If a numerical encoding introduces sentinels or zero-padding, preserve a status mask or prove the encoding is injective on the relevant records.

## 6. Result classes

A completed case must distinguish at least:

- `compatible`
- `conditionally compatible`
- `non-corresponding`
- `boundary/design limitation`
- `internal contradiction or countermodel found`

`Not falsified` is not interchangeable with `proved true`.

## 7. Cross-check

Before synthesis, verify that the case can be reconstructed from the repository without relying on the Notion summary alone. Notion is the research navigation and interpretation layer; GitHub is the reproducibility and versioned evidence layer.