# CS-004 / Global Case 032 — DSD Contradiction Audit

Status: first-pass contradiction audit complete.

## 1. Formation Axiom System

### Source pressure

The external systems show that one accepted host-language value can acquire different downstream roles depending on parser context and binding mechanism.

### DSD comparison

The Formation Axiom System is typed and staged. Its operational channel identity includes configuration, material item, quantity-kind, assigned value, and role. It also separates admissibility, assignment domain, defined/undefined assignment, channel formation, and later composition.

This architecture does not force one context-independent role for a value.

If an application chooses to represent two downstream roles inside a DSD formation model, the interpretation map must explicitly distinguish those roles or other relevant typed coordinates. The same external string value does not force strict DSD identity when its mapped role/context data differ.

### Boundary

The external parser's categories are not automatically DSD `rho` roles, channels, or formation stages. SQL parameter binding, HTML text insertion, and shell argument passing are source-domain mechanisms. DSD does not supply their grammars or escaping rules.

Reject:

- `accepted input = admitted DSD channel` by identity;
- `SQL value = DSD assigned value` without a supplied interpretation map;
- `parser context = DSD role` automatically;
- `injection = undefined assignment` automatically.

### Contradiction result

No direct contradiction found.

The Formation system survives if application mappings preserve the source-domain context/role distinction rather than collapsing it.

## 2. Axis-Property System

No primary mapping is justified.

A query context, DOM sink, shell token, or parser grammar is not a realized DSD axis merely because it constrains interpretation. The axis-property system remains an inherited realized-axis/property layer, while syntax and parser roles belong to an external computational interpretation layer unless an additional model explicitly links them.

No contradiction found; non-mapping is the correct default.

## 3. Structural Reorganization Dynamics

CS-004 does not require time evolution: reinterpretation can occur in one request pipeline because the same value is handed to a different interpreter.

The dynamics framework is therefore not the primary explanation.

However, if an application models a role/application-status change across time, the current dynamics paper already forbids silently changing formation assignment, channel identity, or application status inside a smooth fixed-domain evolution. Such a change requires an explicit transition/lineage treatment.

This is compatible with CS-004, but it does not turn every parser handoff into a DSD reorganization event.

No contradiction found.

## 4. Static Aggregation

Not required for the primary result.

Two pipelines may produce the same visible scalar/text output while having different parser structures and intermediate roles. This is compatible with the static layer's warning that reduced output equality does not reconstruct component structure, but the browser/SQL/shell operations are not DSD aggregation operators by identity.

Mapping strength: partial, secondary only.

## 5. Strong-hypothesis verdicts

1. `valid upstream string => data in every downstream context` — rejected.
2. `input validation fixes all later syntactic roles` — rejected.
3. `characters have one context-independent operational meaning` — rejected.
4. `same string across systems => same structural role` — rejected.
5. `binding/encoding are merely cosmetic` — rejected.
6. `downstream syntax reinterpretation => upstream value was undefined/invalid` — rejected.
7. `same final visible/output value => intermediate boundary irrelevant` — rejected.

## 6. DSD application rule added by CS-004

**A source-domain value that is admissible at one interface cannot be assigned a stable DSD-interpreted operational role across downstream interpreters merely from value equality. The application must preserve or explicitly transform the context/role relation.**

Equivalently:

`same external value != same interpreted role != same formed operational object` unless the application-specific mapping proves those identifications.

## 7. Final contradiction status

`compatible + interpretation-boundary strengthening`.

No direct contradiction with the current Formation Axiom System, Axis-Property System, Static Aggregation layer, or Structural Reorganization Dynamics was found.