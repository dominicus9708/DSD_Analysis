# LAW-010 Reproducibility

Status: completed first-pass reproducibility record.

## 1. Objective

Allow another reviewer to reconstruct the LAW-010 analysis without accepting DSD terminology as legal authority.

## 2. Source-first procedure

1. Read each external source in its own terminology.
2. Record separately:
   - responsibility/conviction;
   - sanction/penalty;
   - victim status;
   - restitution/compensation/rehabilitation/satisfaction/non-repetition;
   - public/victim attitudes;
   - historical state-abuse context;
   - formal legal status;
   - actual enforcement/execution practice.
3. Do not map any source term to DSD until the source-side structure is fixed.
4. Test whether a one-value encoding loses a source distinction.
5. Only then compare with Formation/Dynamics as structural carriers.

## 3. External source checklist

### ICC

Verify in the Rome Statute / ICC materials:

- Article 75 reparations to victims;
- Article 77 penalties;
- the separate placement and objects of the two regimes.

### UN human-rights redress

Verify:

- restitution;
- compensation;
- rehabilitation;
- satisfaction;
- guarantees of non-repetition;
- victim status not universally conditioned on perpetrator conviction in CAT General Comment No. 3.

### South Africa

Read `S v Makwanyane`, especially the public-opinion discussion and the Court's treatment of irrevocability, error/arbitrariness, inequality, life and dignity.

### Germany

Verify:

- Basic Law Article 102;
- Bundestag historical account of 1952 reintroduction debates;
- Federal Constitutional Court statement that Nazi-era abuse was decisive for Article 102.

### Comparative death-penalty status

Verify current classification that distinguishes abolition in law from abolition in practice.

### Victim-family heterogeneity

Verify a source documenting murder-victim family members who oppose capital punishment and the institutional consequences of treating all victim families as one preference class.

## 4. Finite-witness reconstruction

Rebuild states `a` through `g` from `FINITE_WITNESS.md`.

Attempt these totalizations:

- `JUSTICE_DONE in {YES,NO}`;
- `DEATH_PENALTY in {ON,OFF}`;
- one scalar `SOCIAL_SUPPORT`;
- one scalar `SOCIAL_COST`.

For each attempted totalization, identify the source distinction lost.

## 5. DSD comparison checklist

Confirm that the application does not identify:

- legal responsibility with Formation realization;
- punishment with a DSD channel value;
- victim grief or public anger with Static-Aggregation weight;
- social cost with one DSD coefficient;
- formal non-use/de facto abolition with channel absence;
- temporal legal change with Dynamics-generated law.

## 6. Falsification checklist

Try to find counterexamples to the surviving candidate:

- a source that expressly defines punishment and reparation as one legally indivisible status;
- a system where victim status exists only after conviction and no separate route is possible;
- a regime where public opinion is itself legally dispositive by source rule;
- a jurisdiction where law-on-the-books and practice are legally stipulated to be identical;
- a source that gives a justified common scalar for all relevant social costs/emotions.

If found, retain the counterexample and narrow the universal candidate instead of normalizing it away.

## 7. Current reproducibility judgment

The first-pass result can be reproduced from the cited source families using only qualitative typed-state comparison.

No Python or numerical pipeline is required because LAW-010 does not make a numerical empirical claim.
