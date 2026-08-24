# CS-003 Contradiction Audit

## 1. Formation Axiom System

### What survives

The Formation Axiom System is static and staged. It preserves typed domains, assignment scope, channel identity, unsuccessful candidates, and the distinction among undefined assignment, defined zero, channel absence, and related statuses.

For CS-003 this provides a useful time-slice discipline: at each time, do not collapse the source-domain identity and status coordinates merely because the same external name or request path appears.

### What Formation does not establish

Formation does not establish temporal persistence:

`valid at t_check => valid at t_use`

is not a Formation theorem.

Therefore a TOCTOU mitigation cannot be derived from Formation alone. The source system must supply a locking, atomicity, versioning, identity, transaction, or equivalent cross-time rule.

### Direct contradiction

None found.

## 2. Axis-Property System

The Axis-Property System explicitly excludes temporal evolution and transition rules. It is therefore not the primary DSD layer for CS-003.

A filesystem property, HTTP entity tag, row version, or transaction snapshot is not thereby an axis property, and no concurrency relation is a realized DSD axis merely because it has an order or hierarchy.

Direct contradiction: none found; primary judgment: non-applicable except under an additional explicit interpretation.

## 3. Structural Reorganization Dynamics

This is the strongest DSD comparison layer.

The Dynamics paper explicitly:

- formulates time-indexed component-resolved states `S(t)`;
- states what remains fixed within a regular epoch and what may evolve;
- does not hide stronger changes of support, application status, formation assignment, or channel set inside ordinary smooth fixed-domain evolution;
- separates value evolution, status/domain transition, and channel/formation-level transition;
- requires explicit cross-time lineage when formation assignments or channel sets change;
- distinguishes a time-indexed family of admissible slices from one literally unchanged frozen static model.

These rules withstand TOCTOU counterpressure well. They already reject the strongest unsafe modeling shortcut:

`same label/name across time => unchanged object and unchanged applicability`.

### Important boundary

This is correspondence, not identity.

- A filesystem inode is not a DSD channel by definition.
- An HTTP entity tag is not DSD lineage by definition.
- A database serialization failure is not a DSD status transition by definition.

The external system first determines what counts as the same resource, version, transaction, or state. DSD may then model the preserved distinction only through an explicit interpretation map.

### New application rule forced by CS-003

Do not infer a later state from an earlier valid slice without an explicit cross-time preservation relation.

In schematic form:

`Valid(S(t_c))` does not entail `ValidForUse(S(t_u))` merely because `t_c < t_u` and the same external name appears.

A safe mapping needs an application-specific relation analogous to

`R_safe(S(t_c), S(t_u))`.

DSD does not supply that relation universally.

### Direct contradiction

None found.

## 4. Static Aggregation

Static aggregation is not needed to explain the core race. It is relevant only to a weaker observation: equal reduced outcomes need not reconstruct different temporal histories.

For example, two mutations can both produce 'no effect' while one fails an HTTP `If-Match` precondition and another is rolled back as a database serialization failure. Equal reduced outcome does not identify the failed stage or temporal history.

This is only a partial analogy; these failure results are not DSD aggregation operators.

## 5. Strong-hypothesis verdicts

1. One successful validation remains valid automatically for later use — rejected.
2. Same name/reference across times implies same resource state/identity — rejected as a general rule.
3. Valid check-time precondition implies valid use-time precondition — rejected.
4. Later failure proves the earlier check was incorrect — rejected; the earlier state may have been correct and later become stale.
5. Better typing or initial validation alone solves TOCTOU — rejected.
6. Every intervening change is ordinary value evolution of one unchanged object — rejected as a universal model; identity/status/version changes may require different treatment.
7. Same final output makes intervening concurrent change irrelevant — rejected for structural reconstruction.

## 6. Overall DSD judgment

Main result class: compatible with strengthened application boundary.

No direct contradiction with the current DSD Formation or Structural Reorganization Dynamics framework was found.

The Dynamics layer gains meaningful external counterpressure because CS-003 tests exactly its distinction between regular evolution and stronger status/domain/identity-sensitive transitions. The framework survives, but only if source-native temporal identity and preservation rules are supplied rather than inferred from names, labels, or prior validity.