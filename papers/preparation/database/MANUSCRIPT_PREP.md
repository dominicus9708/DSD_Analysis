# Databases and Information Structures — Manuscript Preparation

Canonical scope: `DB-001–005`.

## Central question

How should record absence, NULL, empty value, zero, constraints, provenance, aggregation, support, and reconstruction be separated across relational and practical DBMS settings?

## Recommended angle

**Absence, NULL, Support, and Reconstruction in Database Information States: A DSD Audit**.

## Core mechanisms

- record absence != NULL != empty != zero;
- schema/constraint declaration != row assertion;
- query result != source provenance;
- aggregate equality != support identity;
- non-reconstructability should not be hidden by an equal reduced result.

## Proposed sections

1. SQL standard and DBMS implementation boundaries.
2. Three conservative convergence families from `DB-001–005`.
3. Absence/NULL controls.
4. Constraint versus assertion.
5. Provenance, aggregation, support non-identifiability.
6. Cross-DBMS counterexamples.
7. Conclusion.

## Source freeze

Pin exact SQL-standard or vendor-document versions. Never equate SQL NULL and DSD undefined by label alone.

## Overclaim guards

Do not universalize one DBMS's NULL behavior or infer provenance identity from output equality.