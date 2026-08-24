# LAW-010 Plan — Responsibility, Sanction, Recovery, Emotion, and Social Cost

Status: planned / scope fixed before full analysis.

Global case: 021.

## 1. Core distinction

LAW-010 will test the non-identity among:

`responsibility attribution`

`!= sanction/punishment`

`!= victim restoration`

`!= compensation/reparation`

`!= offender rehabilitation`

`!= future-risk prevention`

`!= emotional/social response`

`!= institutional/social cost`.

The case will not assume one theory of punishment as the correct answer.

## 2. New social-emotional input layer

The analysis must explicitly preserve at least these non-equivalent inputs:

- `E_victim` — grief, anger, condemnation, forgiveness, opposition, or other responses among victims and bereaved families;
- `E_public` — broader public condemnation, fear, demand for retribution, demand for restraint, or other collective attitudes;
- `C_maint` — source-supplied institutional, procedural, fiscal, administrative, diplomatic, or legitimacy costs of maintaining a sanction regime;
- `C_error` — cost/risk of irreversible error such as wrongful execution or wrongful severe punishment;
- `C_abuse` — cost/risk created by political killings, discriminatory punishment, authoritarian abuse, or a historical record of state violence;
- `C_legit_keep` — legitimacy cost that may arise if the public or victims regard non-use/abolition as intolerably insufficient;
- `C_legit_use` — legitimacy cost that may arise if the punishment is regarded as arbitrary, discriminatory, abusive, or incompatible with constitutional/human-rights commitments;
- `H_state` — historically supplied memory/context of state violence, political execution, police/military abuse, massacre, or other coercive misuse relevant to institutional trust.

These are structured coordinates, not additive numerical weights by default.

## 3. Symmetry rule

Emotion and social cost can push in opposite directions.

A source system may experience pressure toward retention or use because of:

- intense condemnation after severe crimes;
- bereaved-family demands for retribution;
- perceived deterrence or incapacitation needs;
- perceived legitimacy cost of punishment regarded as too weak.

The same or another system may experience pressure toward non-use, de facto abolition, moratorium, constitutional invalidation, or complete abolition because of:

- wrongful-conviction / wrongful-execution risk;
- political execution or authoritarian abuse history;
- discriminatory enforcement;
- police/military/state-violence memory;
- irreversibility and impossibility of remedy after error;
- procedural and institutional burden;
- constitutional, human-rights, diplomatic, or legitimacy costs.

No direction is preselected by DSD.

## 4. Death-penalty witness family

Capital punishment will be used as a high-contrast witness because the same institution can carry opposing social pressures.

### South Africa

`S v Makwanyane` is especially useful because the Constitutional Court expressly treated public opinion as relevant but not decisive, while also considering irredeemability, error/arbitrariness, inequality, dignity and life.

This prevents the model from becoming:

`strong public condemnation -> death penalty required`.

### Germany

Official Bundestag and Federal Constitutional Court materials record that Nazi-era abuse of capital punishment was a decisive historical reason for Article 102 of the Basic Law abolishing capital punishment.

This supplies a direct witness for:

`historical state-abuse memory -> legally relevant abolition pressure`.

It does not establish a universal causal law.

### Law-versus-practice status

Current comparative death-penalty reporting distinguishes abolition in law from abolition in practice. LAW-010 will use this to represent systems that formally retain the penalty while not carrying out executions, rather than collapsing them into either `retentionist` or `abolitionist` as one bit.

## 5. Victim-family heterogeneity guardrail

Do not model `victims' families` as one homogeneous emotional actor.

Source material documents both support for and opposition to capital punishment among bereaved families.

Therefore:

`victim-family grief/anger`

`!= one mandatory sentencing preference`.

Each relevant preference or testimony remains source- and actor-indexed.

## 6. Candidate structural record

A first-pass nonnumeric record is:

`L = (harm, responsibility, sanction, restoration, compensation, rehabilitation, prevention, E_victim, E_public, C_maint, C_error, C_abuse, C_legit_keep, C_legit_use, H_state, regime, time)`.

The record is deliberately not a scalar utility function.

A later quantitative model would require an external normative or empirical aggregation operator.

## 7. Main falsification targets

Reject or test these premature implications:

- `responsibility established -> punishment restores victim`;
- `severe public condemnation -> maximum punishment legally required`;
- `victim-family grief -> death penalty preference`;
- `death penalty retained in statute -> executions occur`;
- `death penalty not executed -> legally abolished`;
- `historical state abuse -> abolition necessarily follows`;
- `social cost -> one monetary quantity`;
- `emotion -> irrational/no legal relevance`;
- `public opinion -> constitutional outcome`;
- `abolition -> absence of social demand for retribution`.

## 8. DSD boundary

Formation may help preserve the non-collapse among responsibility, sanction, victim recovery, emotional response, institutional cost and final legal status.

Dynamics may be useful for post-event transitions, victim recovery, offender rehabilitation, recidivism/prevention, moratorium, repeal, and abolition/retention changes over time.

Static Aggregation must **not** be used to sum grief, life, legitimacy, punishment and institutional cost without an independently justified operator.

Axis-Property is not expected to be required.

## 9. Expected next step

Full LAW-010 analysis will proceed in this order:

`universal candidate -> counterpressure -> death-penalty and non-capital witnesses -> victim/public heterogeneity -> social-cost decomposition -> DSD mapping -> contradiction audit -> generalization status`.
