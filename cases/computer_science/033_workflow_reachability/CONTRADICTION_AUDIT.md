# CS-005 / Global Case 033 — Contradiction Audit

## External strong-hypothesis audit

### H1. Representable downstream state implies valid reachability

Rejected.

CWE-841 explicitly covers products that allow actors to omit required behaviors or perform them out of sequence and thereby enter invalid states. A state can therefore be representable or externally produced without being validly reached under the declared workflow.

### H2. A syntactically valid message may be accepted independently of protocol state

Rejected.

TLS 1.3 requires handshake messages to occur in protocol-defined order and requires abort on an unexpected handshake message. WebSocket data frames are available only after opening-handshake completion and before the relevant Close boundary.

### H3. Required predecessor steps may be omitted when the final operation is otherwise valid

Rejected.

This is the central CWE-841 failure mode. The validity of the requested downstream action does not erase required predecessor conditions.

### H4. Same final state/effect implies same valid transition history

Rejected.

Distinct paths may converge on the same visible state or effect, and an incorrectly skipped-step path can mimic the output of a valid path. Final-state equality therefore does not establish transition provenance.

### H5. Correct typing or authorization is sufficient for workflow-valid reachability

Rejected.

TLS/WebSocket ordering constraints are independent of whether a message has the correct message/frame type. Likewise, an application can authenticate and authorize an actor while still requiring a separate workflow predecessor state.

### H6. Current state label is sufficient to establish lawful provenance

Rejected.

CWE-841 specifically targets missing enforcement of the path that should have produced the state. Provenance/history is therefore not generally reconstructible from the current label alone.

### H7. DSD formation stages are directly identical to runtime workflow states/transitions

Rejected by DSD's own scope.

The Formation Axiom System is explicitly static. Its seven stages are staged structural coordinates and closure dependencies represented by truncations/reductions. Domain-specific runtime interpretation requires an additional map. Treating them as a universal clock-time state machine would exceed the paper.

## DSD layer audit

### Formation Axiom System

No direct contradiction found.

Positive pressure:

- the system explicitly preserves a seven-stage order;
- later truncations retain all earlier-stage coordinates;
- formation traces retain witness histories for admitted operational channels;
- a Stage-VI channel is not defined as an isolated value detached from the formation structure that supports it.

Boundary:

This does **not** mean DSD proves arbitrary application workflows or runtime sequence safety. The formation chain is static and structural, not a universal execution-state machine.

Reject:

- `external workflow step = Formation stage` by identity;
- `external terminal state = Stage-VI/Stage-VII formation state` without interpretation;
- `DSD stage order = sufficient runtime control-flow enforcement`.

### Structural Reorganization Dynamics

No direct contradiction found.

The dynamics paper supports time-directed lineage-connected succession and explicitly states that different reorganization classes may require different carriers and transition rules. It also says application-specific uniqueness or transport constraints must be added separately.

Therefore it is compatible with source-defined workflow reachability, but it does not provide the TLS/WebSocket/business-workflow transition relation by itself.

Important boundary:

`lineage-connected successor != workflow-authorized successor` unless an application supplies the relevant transition admissibility relation.

### Axis-Property System

No primary mapping. Property declarations and ordered input profiles do not define runtime workflow reachability.

### Static Aggregation

Secondary only. Same aggregate/output cannot reconstruct the path, but the aggregation operator is not a workflow validator.

## Independence audit

CS-005 is not reducible to:

- CS-001: current-state operation applicability;
- CS-002: authentication/authorization/admission;
- CS-003: stale validity across time;
- CS-004: parser/context reinterpretation.

A workflow bypass can occur with correct typing, current authorization, no stale state, and no parser reinterpretation. Its distinctive failure is that the **declared predecessor relation/path was not satisfied**.

## Verdict

`compatible + stage/runtime boundary strengthening + independent reachability/provenance node`.

No direct contradiction with the current DSD systems was found.