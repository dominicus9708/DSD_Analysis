# LAW-006 Reproducibility Notes

## 1. Analysis type

This is a source-structure and formal-model audit. No numerical computation or Python code is required.

## 2. Reproduction order

1. Read `PLAN.md` and record the universal candidate before consulting DSD.
2. Verify each source family independently.
3. Record whether the source distinguishes rule applicability from normative consequence.
4. Apply counterpressure from formal deontic logic before fixing a taxonomy.
5. Build the typed normative carrier from `MODEL.md`.
6. Run each witness in `FINITE_WITNESS.md`.
7. Run each contradiction candidate in `CONTRADICTION_AUDIT.md`.
8. Compare only after actor, action, role, context, time, rule, applicability, and regime are aligned.
9. Reproduce the final classification in `RESULT.md` without treating witness completion as universal proof.

## 3. Primary witness sources

### ILO Forced Labour Convention No. 29

Official NORMLEX text:
https://normlex.ilo.org/dyn/nrmlx_en/f?p=NORMLEXPUB:12100:0::NO::P12100_ILO_CODE:C029

Verify Articles 1, 2, and 25.

### UNIDROIT Principles — public permission

Official Chapter 6, Section 1:
https://www.unidroit.org/instruments/commercial-contracts/unidroit-principles-2010/chapter-6-section-1/

Verify Articles 6.1.14 through 6.1.17.

### ICCPR / Human Rights Committee

Verify General Comment No. 29 on derogations and General Comment No. 34 on freedom of expression/restrictions from OHCHR sources.

### Formal deontic counterpressure

Stanford Encyclopedia of Philosophy archive entries:
https://plato.stanford.edu/archives/spr2021/entries/logic-deontic/
https://plato.stanford.edu/archives/fall2006/entries/logic-modal/

Use these only to audit the formal assumptions `O/P/F/exemption`, not as positive law.

## 4. Reproduction questions

A rerun should answer:

- Does the source distinguish a rule's applicability from its consequence?
- Is `not granted` distinguishable from `refused`?
- Is an exception an exclusion from scope, a permission, a defence, or something else in that source?
- Does exemption remove a duty, confer a permission, or both?
- Are obligation and permission disjoint in the source logic?
- Can the same action description receive different status under different rules/actors/times?
- If rules conflict, is there an explicit priority mechanism?
- Does any remaining conflict actually contradict Formation rather than the application encoding?

## 5. Expected reproducible result

A faithful rerun should not recover a universal total map:

`Action -> {OBLIGATORY, PERMITTED, PROHIBITED, EXEMPT}`.

It should instead recover a rule-indexed structure in which normative consequence depends on typed action instance, rule applicability, and source semantics.
