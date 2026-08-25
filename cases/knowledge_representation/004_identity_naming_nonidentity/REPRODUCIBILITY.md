# Reproducibility — K_R-004 / Global Case 042

## Purpose

Reproduce the finite semantic witness used to separate lexical naming, annotation labels, denotational equality, explicit inequality, and structure-implied equality.

The script is not an OWL 2 reasoner. It implements only the finite equality/inequality patterns required for this case.

## Run from repository root

```bash
python cases/knowledge_representation/004_identity_naming_nonidentity/repro/check_identity_naming.py
```

## Expected output

See:

`cases/knowledge_representation/004_identity_naming_nonidentity/repro/expected_output.txt`

## Interpretation

- The base case retains one co-denoting and one distinct-denotation model, so neither equality nor inequality is entailed.
- `SameIndividual` filters to the co-denoting model.
- `DifferentIndividuals` filters to the distinct-denotation model.
- Equal denotation makes relation substitution work.
- Equal annotation/display labels do not filter the logical model set.
- A functionality-style constraint on two edges from one source can eliminate the distinct-target model and thereby force co-denotation.

## Verification status

The script was executed during analysis and matched the committed expected output.