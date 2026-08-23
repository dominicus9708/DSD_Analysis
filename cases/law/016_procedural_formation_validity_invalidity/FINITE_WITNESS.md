# LAW-005 Finite Witness

## 1. Purpose

Show with a minimal finite state set that a binary `valid/invalid` variable cannot preserve the distinctions independently present in the witness sources.

## 2. Carrier

Let

`A = {a, b, c, d}`

be four legal-act instances.

Each act has coordinates

`(formed, presently_effective, defect, remedial_status, downstream_status)`.

## 3. Four states

### State a — formed and ordinarily operative

`a = (yes, yes, none, none, available)`.

Example class: an ordinarily concluded and binding agreement with no identified defect.

### State b — formed, but effect is conditional

`b = (yes, not_yet, suspensive_condition_pending, none, not_yet_applicable)`.

UNIDROIT Articles 5.3.1-5.3.2 provide a witness class in which effect depends on a future uncertain event.

### State c — formed and operative, but avoidable

`c = (yes, yes, mistake_or_fraud_ground, avoidance_right_exists, presently_available)`.

UNIDROIT Chapter 3 Section 2 supplies this witness class. Confirmation may later remove the avoidance right.

### State d — award exists, but downstream enforcement is refused

`d = (yes, binding_or_award_exists, enforcement_ground, refusal_possible, enforcement_refused)`.

UNCITRAL Model Law Articles 35-36 supply the witness class.

## 4. Binary collapse test

Suppose a total binary map

`V : A -> {VALID, INVALID}`

is required to encode every legally relevant status.

### Collapse option 1

Set `b = INVALID` because it has no present effect.

Then the model loses the distinction between a formed condition-dependent relation and nonformation.

### Collapse option 2

Set `c = VALID` because it presently operates.

Then the model loses the existing right of avoidance and cannot distinguish it from `a`.

### Collapse option 3

Set `c = INVALID` because a defect exists.

Then the model falsely treats a presently operative but defeasible contract as equivalent to a never-formed or already-null act.

### Collapse option 4

Set `d = INVALID` because enforcement is refused.

Then the model erases the award event and the distinction between award existence/binding status and downstream enforcement.

Therefore no one-bit encoding preserves all four states.

## 5. Rule-indexed witness

Let a single defect label `delta = rule_violation` occur in two different regimes.

- Regime R1 expressly prescribes no effect.
- Regime R2 leaves consequences to a reasonableness or remedial analysis.

Then

`C_R1(delta) != C_R2(delta)`

is possible without contradiction.

UNIDROIT Article 3.3.1 directly preserves this kind of rule-dependence.

## 6. Temporal witness

At time `t1` let

`R(c,t1) = avoidable`.

After valid confirmation at `t2`, let

`R(c,t2) = no_longer_avoidable`.

The underlying conclusion event need not disappear.

Thus

`same act provenance + different legal status over time`

is coherent.

## 7. DSD comparison

The witness is compatible with keeping separate typed statuses and partial downstream assignments.

It would be a bad DSD application to encode:

- `not presently effective` as channel absence;
- `avoidable` as nonexistence;
- `recognition refused` as no award event;
- every defect as the same defined zero.

## 8. Failure condition

The finite witness would fail as a general support node if the source materials actually required these states to be legally identical. They do not.

The witness does not establish that every legal system must instantiate all four states.
