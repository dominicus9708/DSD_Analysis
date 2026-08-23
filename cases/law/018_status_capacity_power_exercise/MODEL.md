# LAW-007 Model

## 1. Vocabulary-neutral source record

Use a typed legal-capacity/power instance

`kappa = (subject, legal_context, status_or_capacity, specific_power_or_right, enabling_conditions, authority_or_support, time, regime)`.

Do not assume that every source uses the same words for these coordinates.

For a given `kappa`, keep separate source-side predicates/relations where the source actually distinguishes them:

- `Recognized(kappa)` — the status/capacity/right is legally attributed or recognized;
- `Exercisable(kappa,t)` — the right/power can presently be exercised under the governing conditions;
- `SupportedOrAuthorized(kappa,t)` — required support, authority, competence, notice prerequisite, or other enabling condition is present;
- `ExerciseEvent(kappa,e,t)` — an actual exercise event occurred;
- `Effective(e,regime,t)` — the exercise produced the relevant downstream legal effect;
- `Confirmed(e,t2)` — a later source-side rule confirms or cures a prior ineffective/unauthorized act.

These are application coordinates, not universal legal vocabulary.

## 2. Surviving universal candidate

The candidate is not a mandatory ladder shared by all law.

It is:

**source-distinct possession/recognition, present exercisability, enabling support/authority, actual exercise, and legal effect must not be collapsed into a single binary capacity/power value unless the source rule performs that identification.**

Formally, none of the following implications is assumed universally:

`Recognized -> Exercisable-now`;

`Exercisable-now -> Exercised`;

`Exercised -> Effective`;

`not exercised -> no right`;

`exercise ineffective -> no underlying capacity`.

## 3. Witness-specific readings

### CRPD

The source uses `legal capacity` broadly enough to contain legal standing and legal agency. Therefore the model must not force a narrow external taxonomy onto Article 12.

Article 12 nevertheless distinguishes recognition of legal capacity from support and safeguards connected with its exercise.

### UNIDROIT

A right may exist while not yet exercisable; exercise may require notice; expiry of a limitation period may bar enforcement without extinguishing the right.

### VCLT

The State has treaty-making capacity, but a natural person still needs the relevant authority/full-powers route. An unauthorized act can occur yet remain without legal effect unless later confirmed.

## 4. Relation to LAW-003

LAW-003 asked whether one person or mandate relationship automatically creates authority and attributed effect.

LAW-007 asks a different question: even when a legal status/right/power exists, does that already imply present exercisability, actual exercise, and effect?

The answer from the selected sources is no.

## 5. DSD bridge

Formation is used only as a structural discipline for typed identity, partiality, stage separation, and preservation of absent/undefined/defined states.

Do not identify:

`legal capacity = Formation admission`;

`legal power = Formation realization`;

`nonexercise = undefined assignment`;

`ineffective act = channel absence`.

A legally ineffective exercise event may still be a fully existing and describable event and must remain represented.
