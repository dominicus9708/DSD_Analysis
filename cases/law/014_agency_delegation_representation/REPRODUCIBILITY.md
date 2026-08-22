# LAW-003 Reproducibility

## 1. Execution date

2026-08-22 (Asia/Seoul).

## 2. External source baseline

Primary legal text was checked against the Korean National Law Information Center. The Civil Act version used in the analysis is the version effective 2026-03-17, Act No. 21454.

Authoritative judicial interpretations used:

- Supreme Court 2024-03-12, 2023Da288772;
- Supreme Court 2008-06-12, 2008Da11276;
- Supreme Court 2025-06-05, 2023Da232526.

The exact provisions and official source URLs are recorded in `SOURCE_NOTES.md`.

## 3. DSD source baseline

Project references:

- Formation Axiom System — `Kwon2026DSDFormation`;
- Realized-Axis Property Axiom System — `Kwon2026DSDAxisProperties` used only for the negative mapping/boundary audit.

Exact Formation targets used:

- Definition 2.1 / Section 2.2 typed vocabulary;
- Primitive Axiom V;
- Definitional Closure Clause VI;
- operational channel identity `c=(p,a,lambda,v,rho)`;
- Proposition 5.12 and neighboring status-separation results;
- Section 6 role-preserving comparison structure.

## 4. Deterministic rerun procedure

No numerical code is required for LAW-003. Reproduction is a source-and-model audit.

Rerun in this order:

1. verify the current Civil Act text for Articles 59-62, 114, 126, 128-134, and 680;
2. verify the holdings summarized from Supreme Court 2023Da288772, 2008Da11276, and 2023Da232526;
3. rebuild the source-side propositions without DSD terminology;
4. check `MODEL.md` mappings against the current Formation definitions;
5. instantiate witnesses W1-W6 in `FINITE_WITNESS.md`;
6. test each contradiction candidate C1-C5 in `RESULT.md`;
7. reject any mapping that equates legal validity with Formation admission or equates unauthorized legal-act existence with channel absence;
8. record any changed source rule as a source-version difference rather than silently retaining the old result.

## 5. Expected invariant checks

A successful rerun under the same source rules should preserve these distinctions:

- `same human` vs `same legal capacity`;
- `mandate` vs `agency authority`;
- `actual authority/scope` vs `principal effect/responsibility`;
- `unauthorized attempted act exists` vs `effective against principal`;
- `ordinary agency` vs `apparent-agency exception`;
- `pre-ratification` vs `post-ratification` status;
- `director representation` vs `specific appointed agent`.

## 6. Failure conditions

The result must be reopened if any authoritative source establishes one of the following in the selected scope:

- mandate and agency authority are required to be literally identical statuses in a way inconsistent with the model;
- personal and representative capacity are required to collapse for the same act and context;
- an unauthorized act is legally treated as no event at all, invalidating the retained-act witness;
- the Formation source changes so role is no longer preserved in channel identity or the relevant partial/status distinction is removed;
- a matched source relation genuinely cannot be represented without violating a DSD primitive axiom or definition.

## 7. No-code note

A Python witness is unnecessary because the finite cases are typed state tables with no computational search. Adding code would not strengthen reproducibility unless LAW-003 is later expanded into a rule-engine or automated model-checking benchmark.
