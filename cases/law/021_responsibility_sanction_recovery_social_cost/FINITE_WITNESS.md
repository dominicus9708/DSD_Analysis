# LAW-010 Finite Witness — Responsibility, Sanction, Recovery, Emotion, and Social Cost

Status: completed first-pass finite witness.

## 1. Purpose

Construct a small witness set showing that no single scalar or one-dimensional legal status preserves the source distinctions among responsibility, punishment, reparation, victim response, public response, social cost and law/practice status.

## 2. Witness states

Let `X = {a,b,c,d,e,f,g}`.

### a — Conviction plus punishment, limited victim restoration

A perpetrator is convicted and sentenced.

- `R = established`
- `S = imposed`
- `Rest/Comp = absent or partial`
- victim loss remains non-restored

This defeats:

`punishment -> victim restored`.

### b — Conviction plus reparations route distinct from sentence

ICC-type structure:

- conviction exists;
- sentencing/penalty is governed through one route;
- victim reparations are governed through Article 75 through a distinct route.

This defeats:

`punishment = reparation`.

### c — Victim/redress status without perpetrator conviction

UN human-rights remedial structure:

- victim status and redress are legally defined;
- perpetrator may not yet be identified, prosecuted or convicted.

This defeats:

`responsibility established is a universal prerequisite for victim status or redress`.

### d — Strong public retention pressure but constitutional abolition

South Africa `S v Makwanyane` witness:

- assume majority support for death penalty in extreme murder cases;
- public opinion is relevant but non-decisive;
- constitutional adjudication rejects the death penalty.

This defeats:

`strong public condemnation/support -> death penalty legally required`.

### e — Historical abuse pressure against capital punishment while reintroduction demand persists

Germany witness:

- Nazi-era abuse of capital punishment is a decisive constitutional-historical reason for Article 102;
- postwar parliamentary actors still invoke retribution, deterrence and public agitation for reintroduction.

This defeats both:

`historical abuse -> all public demand disappears`

and

`public retributive demand -> legal reintroduction`.

### f — Formal retention with non-execution/de facto abolition

Comparative death-penalty status witness:

- legal authorization may remain;
- executions may not occur for a sustained period;
- the jurisdiction can be classified as abolitionist in practice rather than abolitionist in law.

This defeats:

`law on books -> use in practice`

and

`non-use -> legal abolition`.

### g — Bereaved family opposes execution

Victim-family heterogeneity witness:

- a family member has suffered homicide bereavement;
- the family member opposes capital punishment;
- another family member in another case may support it.

This defeats:

`bereavement/grief -> one mandatory punishment preference`.

## 3. Failed one-value encodings

### 3.1 `JUSTICE_DONE = {YES,NO}`

If state `a` is YES because punishment occurred, the model hides that victim restoration may still be absent.

If state `b` is YES because both punishment and reparations exist, the model hides the legal independence of those routes.

### 3.2 `DEATH_PENALTY = {ON,OFF}`

State `f` cannot be represented faithfully:

- `ON` hides non-execution/de facto abolition;
- `OFF` hides continuing legal authorization.

### 3.3 `SOCIAL_SUPPORT = scalar`

States `d`, `e`, and `g` show actor and institution heterogeneity:

- public majority support can coexist with constitutional invalidity;
- historical state-abuse distrust can coexist with present retributive demand;
- bereaved families can disagree with one another.

A scalar social-support value erases source-relevant actor and institutional distinctions unless an external aggregation rule is supplied.

### 3.4 `SOCIAL_COST = money`

The following are not naturally interchangeable without additional modelling:

- fiscal maintenance;
- wrongful-execution risk;
- political-abuse risk;
- discrimination/arbitrariness;
- legitimacy loss from perceived under-punishment;
- legitimacy loss from coercive overreach;
- historical institutional distrust.

Money may measure some consequences, but does not supply a universal cross-coordinate equivalence.

## 4. Minimal structural conclusion

The finite witness supports the necessity of at least a typed relation package:

`(responsibility, sanction, reparation/restoration, prevention, actor-indexed emotion, institutional/social-cost family, legal status, practice status, time, regime)`.

The witness does not prove a universal theory of punishment.

It proves only that the selected source structures cannot be faithfully represented by a single `justice`, `punishment`, `death-penalty`, `social support`, or `social cost` value without additional source-side operators.
