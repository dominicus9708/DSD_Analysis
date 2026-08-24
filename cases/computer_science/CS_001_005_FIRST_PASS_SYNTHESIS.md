# Computer Science First-Pass Synthesis — CS-001~005 / Global Cases 029~033

Status: first-pass foundational computer-science series provisionally closed; active falsification and specialized extensions remain open.

## 1. Scope

This synthesis combines five independently tested interfaces from the first computer-science campaign without treating cross-case recurrence as proof.

- CS-001 / Global Case 029: static typing, runtime construction/status, current applicability, evaluation, result.
- CS-002 / Global Case 030: authentication, authorization, scoped privilege, admission, effect.
- CS-003 / Global Case 031: check-time validity, cross-time preservation/revalidation, use-time validity, effect.
- CS-004 / Global Case 032: upstream value, downstream parser context, binding/encoding, parsed role, effect.
- CS-005 / Global Case 033: current state/action form, transition relation, valid reachability, successor state/effect, path provenance.

The campaign asks whether DSD survives when external computer-science systems require these distinctions, and whether the cases are genuinely independent rather than repetitions of `undefined != zero` or a generic staging metaphor.

## 2. Cross-case surviving separations

### CS-001 — local computational status

`static type compatibility != constructed runtime value/status != valid runtime state != operation applicability != evaluation behavior != returned result`

### CS-002 — relational security policy

`authentication status != authorization relation/decision != bounded privilege/credential != downstream admission != execution/effect`

### CS-003 — temporal preservation

`check-time condition != cross-time preservation relation != use-time condition != operation admission != committed/effective result`

### CS-004 — interpretation context

`upstream value/data status != downstream grammar/context != binding/encoding relation != parsed role != operation/effect`

### CS-005 — reachability and path provenance

`current state/action form != source transition relation != valid successor reachability != successor state/effect != transition provenance`

## 3. Independence / overlap audit

### CS-001 vs CS-005

Overlap: both can discuss whether an operation is allowed.

Difference: CS-001 concerns **local/current applicability** of an operation to an already existing runtime state; CS-005 concerns whether that state/action is **reachable through a source-declared valid path**. A locally well-typed and callable operation can still be forbidden by the workflow predecessor relation.

Verdict: independent.

### CS-002 vs CS-005

Overlap: both contain gates before an effect.

Difference: CS-002 tests subject/request-specific security-policy relations and downstream admission. CS-005 tests protocol/workflow predecessor constraints even when authentication and authorization are already correct.

Verdict: independent.

### CS-003 vs CS-005

Overlap: both require cross-state relations and can use provenance language.

Difference: CS-003 asks whether earlier validity persists to a later time. CS-005 asks whether a successor is lawful under a transition relation. A lineage-connected or temporally current successor is not automatically workflow-authorized.

Verdict: independent, with an explicit boundary:

`lineage-connected successor != workflow-authorized successor`.

### CS-004 vs the others

CS-004 can fail with correct typing, correct authorization, no intervening state change, and a valid workflow path. Its pressure comes from a receiving grammar assigning a different role to the same host-language value.

Verdict: independent.

### Overall

The five nodes share a common anti-totalization pattern, but their source-native failure interfaces differ: local semantics, policy relation, temporal preservation, parser context, and transition reachability.

They therefore count as five convergent but non-duplicative nodes.

## 4. First-pass common audit structure

The campaign supports the following conservative rule:

> When a source system independently distinguishes local status, relational permission, temporal validity, interpretation context, path provenance, and outcome, do not infer one from another merely because they occur in one computational flow or produce the same visible result.

A compact non-identity form is:

`local status != relational admissibility != temporal validity != interpretation role != path reachability/provenance != effect/result`

This is an audit schema, not a claim that every software system implements six literal pipeline stages.

## 5. DSD survival result

No direct contradiction with the current DSD systems was found in CS-001~005.

The strongest recurring DSD contribution is not a replacement for programming-language semantics, security models, concurrency control, parsers, or protocol state machines. It is the discipline of preserving source-native distinctions before interpretation/composition and refusing unsupported totalization.

### Formation Axiom System

Survived all five cases as a static typed/formation discipline.

But the campaign fixed several boundaries:

- `None` / `Err` are not DSD undefined assignment by identity;
- security stages are not DSD formation stages by identity;
- Formation staging does not prove temporal persistence or solve TOCTOU;
- parser context is not DSD role/channel/stage without an interpretation bridge;
- DSD's seven formation stages are not runtime protocol states.

Therefore Formation remains compatible, but domain-specific interpretation maps are mandatory rather than optional conveniences.

### Axis-Property System

No contradiction was found, but it was not the primary explanatory layer in this campaign. Security roles, parser contexts, versions, workflow states, and protocol positions do not become realized DSD axes merely because they are ordered, tagged, or stateful.

The campaign therefore strengthens the non-mapping rule: no automatic axis interpretation from external hierarchy or ordering.

### Structural Reorganization Dynamics

CS-003 and CS-005 supplied the strongest pressure.

The dynamics framework survived the temporal-validity and succession/provenance tests because it can distinguish time-indexed slices, ordinary evolution, stronger status/domain/formation changes, and explicit lineage.

But the campaign fixed two strong limits:

- external handles, ETags, snapshots, or labels are not DSD lineage by identity;
- DSD lineage does not by itself define application-specific workflow authorization.

The source domain must supply persistence, identity, and transition-admissibility rules.

### Channel-Indexed Static Aggregation

Only secondary support was needed. Several cases show that equal visible outputs do not reconstruct prior runtime status, failure point, parser path, or transition provenance. This is compatible with the static aggregation paper's non-reconstruction warning, but none of the external operations is identified with the DSD aggregate operator by identity.

## 6. Application mappings rejected during the campaign

The first-pass campaign explicitly rejects at least the following automatic identifications:

1. `well typed = terminating / normal-returning`;
2. `None or Err = DSD undefined`;
3. `authentication = authorization = admission = effect`;
4. `valid token = universal access`;
5. `past valid = currently valid`;
6. `same external name across time = same DSD object`;
7. `parser context = DSD role`;
8. `same external string = same operational role`;
9. `external workflow step = DSD formation stage`;
10. `lineage relation = workflow authorization`;
11. `same final effect/result = same prior state, path, or provenance`.

These rejected mappings are part of the result, not failures of the campaign: they narrow the legitimate application surface of DSD.

## 7. Falsification status

The campaign does **not** prove DSD.

What it establishes at first pass is:

- five independent computer-science interfaces were used as counterpressure;
- all produced nontrivial constraints and rejected naive DSD mappings;
- none produced a direct contradiction with the current Formation, Axis-Property, Static Aggregation, or Structural Reorganization systems within their stated scopes;
- Structural Reorganization Dynamics survived its first direct temporal/concurrency and transition-provenance pressure, but only with application-specific identity/persistence/transition rules supplied externally.

Classification:

`first-pass computer-science foundational series: survived active counterpressure + application boundaries sharpened + five independent nodes retained`.

## 8. Campaign closure decision

The foundational CS-001~005 series is provisionally closed.

Reason:

The current five nodes already cover five distinct failure interfaces:

1. local computational semantics;
2. relational access policy;
3. temporal persistence/currentness;
4. interpretation grammar/context;
5. transition reachability/path provenance.

A CS-006 should be opened only if an overlap audit identifies a genuinely new interface that cannot be reduced to these five. Repeating another language, authentication mechanism, TOCTOU technology, injection family, or protocol state machine is not enough.

Active falsification remains open, and specialized cases may reopen the computer-science domain when they create new pressure.
