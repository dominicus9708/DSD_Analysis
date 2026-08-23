# LAW-005 Reproducibility

## Retrieval date

2026-08-24 (Asia/Seoul).

## External sources

1. UNCITRAL — United Nations Convention on Contracts for the International Sale of Goods (CISG)
   - https://uncitral.un.org/en/texts/salegoods/conventions/sale_of_goods/cisg
   - claim checked: Part II formation; Article 4 generally excludes validity.

2. UNCITRAL Digest of Case Law on CISG, Article 4
   - official UNCITRAL PDF.
   - claim checked: formation/right-obligation scope versus validity/property-effect exclusions.

3. UNIDROIT Principles of International Commercial Contracts 2016
   - https://www.unidroit.org/instruments/commercial-contracts/unidroit-principles-2016/
   - Chapter 1 Article 1.3 and commentary;
   - Chapter 3 Section 1 Article 3.1.2;
   - Chapter 3 Section 2 avoidance rules, especially Articles 3.2.2, 3.2.5, 3.2.6, 3.2.9-3.2.12;
   - Chapter 3 Section 3 Article 3.3.1;
   - Chapter 5 Section 3 Articles 5.3.1-5.3.2.

4. UNCITRAL Model Law on International Commercial Arbitration (1985, amendments 2006)
   - https://uncitral.un.org/en/texts/arbitration/modellaw/commercial_arbitration
   - Articles 35-36 and explanatory note.

## DSD sources

Use the current project Formation Axiom System as the primary structural comparison layer.

Key comparison commitments:

- staged formation;
- partial assignment;
- role-bearing channel identity;
- undefined / defined-zero / absence separation;
- source structure retained beyond downstream results.

No claim in LAW-005 depends on Axis-Property, Static Aggregation, or Dynamics as a theorem source.

## Deterministic check

No Python program is needed for this case.

The finite witness can be checked by inspection:

`A = {a,b,c,d}`

with four distinct status tuples documented in `FINITE_WITNESS.md`.

Attempt any total map

`V : A -> {VALID, INVALID}`

and compare whether it preserves:

- formed-but-conditionally-not-effective versus nonformation;
- ordinarily operative versus operative-but-avoidable;
- source award existence versus downstream enforcement refusal.

A one-bit output cannot encode all distinctions simultaneously.

## Reproduction order

1. Read `FOUNDATIONAL_FRAMEWORK.md` in the parent law directory.
2. Read this case's `PLAN.md`.
3. Verify the external source propositions in `SOURCE_NOTES.md`.
4. Reconstruct `MODEL.md`.
5. Test the four finite states in `FINITE_WITNESS.md`.
6. Check every candidate in `CONTRADICTION_AUDIT.md`.
7. Compare with `RESULT.md` and `SCOPE.md`.
