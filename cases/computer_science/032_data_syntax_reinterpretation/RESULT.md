# CS-004 / Global Case 032 — Result

Status: first-pass cross-subfield analysis complete.

## Answer-first result

The source systems reject a context-free identity between an upstream value and its downstream operational role.

Surviving audit separation:

`upstream value/data status != downstream grammar/context != binding/encoding relation != parsed role != operation/effect`.

This is not a universal five-stage software architecture. It is a rule against inferring role preservation from value equality alone.

## External witness summary

### SQL

MITRE CWE-89 and OWASP describe the failure as mixing or mis-separating data and SQL directives. Parameterized queries preserve query structure separately from bound values.

### Browser contexts

OWASP distinguishes HTML, attribute, JavaScript, CSS, and URL contexts because browser parsers assign different meanings to the same characters depending on where they occur. MDN similarly distinguishes `textContent` from `innerHTML`: one inserts text, the other invokes HTML parsing.

### Process execution

Python `subprocess` preserves argument boundaries when no shell is involved. Explicit shell invocation introduces shell parsing and therefore context-specific quoting requirements.

## Finite witnesses

1. SQL: benign `O'Reilly` as a separately bound parameter versus the same host string spliced into SQL source text.
2. Browser: `"<b>A</b>"` passed to `textContent` versus `innerHTML`.
3. Process: `"report 2026.txt"` passed as one argv element versus inserted into a shell command string without an argument-preserving interface.

The witnesses do not depend on malicious payloads. They establish that interpretation role is determined by the receiving grammar and binding interface.

## Strong hypotheses

All seven initial totalizing hypotheses were rejected as general rules.

Most important rejected implication:

`ValidData(v) => DataRole(v, C)` for arbitrary downstream context `C`.

## DSD result

### Formation

Compatible and useful as an audit discipline, but not a parser-security mechanism. The formation system already keeps typed domains, assigned values, roles, channels, and stages distinct; operational channel identity includes role data. It therefore does not require one context-independent role for the same value.

Application boundary strengthened:

**External parser context and syntax role must be supplied by an interpretation map; they are not automatically DSD role/channel/stage coordinates.**

### Axis Property

No primary mapping. Parser contexts and grammar positions are not realized DSD axes by default.

### Structural Reorganization Dynamics

Secondary only. Reinterpretation can occur without temporal evolution. If an application explicitly models a cross-time role/application-status change, it must not hide that change inside fixed-domain smooth evolution; but parser handoff alone is not automatically a DSD reorganization event.

### Static Aggregation

Secondary only. Equal visible or reduced outputs do not reconstruct the parser path or role history, but external parser operations are not DSD aggregation operators by identity.

## New DSD application boundaries

Reject:

- `same external string = same DSD operational role`;
- `input validation success = downstream syntax safety`;
- `parser context = DSD role` without an explicit bridge;
- `injection-like reinterpretation = DSD undefined assignment`;
- `same output = same intermediate structural interpretation`.

## Independence judgment

CS-004 is independent of CS-001~003.

- CS-001: type/runtime/evaluation distinction.
- CS-002: authentication/authorization/admission relation.
- CS-003: state validity transfer across time.
- CS-004: **context-dependent reinterpretation of a value as data, markup, query syntax, or command-language material.**

The failure can occur with correct host typing, correct authorization, and no intervening state change.

## Final classification

`compatible + interpretation-boundary strengthening + independent parser/context computational node`.

No direct contradiction with the current DSD systems was found.