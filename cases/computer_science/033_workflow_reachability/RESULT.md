# CS-005 / Global Case 033 — Result

Status: first-pass cross-subfield analysis complete.

## Answer-first result

The source systems reject treating a downstream state or message as valid solely because it is representable, well-formed, typed, or authorized. Where a source workflow defines predecessor constraints, valid reachability depends on the transition relation and path provenance.

Surviving audit separation:

`current state/action form != source transition relation != valid successor reachability != successor state/effect != transition provenance`.

This is not a universal five-stage architecture. It is a rule against inferring lawful reachability from isolated state or action properties.

## External witness summary

### CWE-841

Required behaviors may be omitted or performed out of order, allowing a product to enter an invalid state. This establishes workflow order as an independent correctness/security condition.

### TLS 1.3

Handshake messages must follow the protocol-defined order; unexpected handshake messages cause abort. TLS also contains explicit exceptional paths such as 0-RTT, showing that legal reachability is defined by a transition relation, not by one simple universal linear order.

### WebSocket

The opening handshake precedes the data-transfer phase. Data frames become admissible after successful handshake completion and before the relevant closing boundary.

## Finite witnesses

1. Minimal workflow: declared `S0 -> S1 -> S2`, implementation wrongly accepts `S0 -> S2`.
2. TLS: a handshake message of a valid TLS message type arrives in an unexpected protocol position and must be rejected.
3. WebSocket: a data frame class is valid after handshake completion but not as a pre-handshake data-transfer action.

## Strong hypotheses

All seven totalizing hypotheses were rejected as general rules.

Most important rejected implication:

`RepresentableOrWellFormed(x) => ReachableByValidPath(x)`.

## DSD result

### Formation

Compatible, but the correspondence must be stated carefully. The Formation Axiom System is a static typed system with a seven-stage structural order, coherent truncations/reductions, and formation traces for admitted channels. Those structures prevent the later formation coordinates from being conceptually detached from their supporting formation structure.

However:

**DSD stages are not runtime protocol states by identity.**

The Formation paper itself states that it is static and that domain-specific applications require interpretation maps. Therefore formation staging can support a reachability/provenance audit only after an external workflow is explicitly interpreted into the DSD framework.

### Structural Reorganization Dynamics

Compatible and useful for temporal provenance, but insufficient to define arbitrary workflow legality. The dynamics paper defines coherent lineage and lineage-connected succession while explicitly allowing application-specific additional transition rules.

Therefore:

`lineage-connected successor != workflow-authorized successor`

unless an external transition-admissibility rule is supplied.

### Axis Property / Static Aggregation

Not primary. Neither property structure nor aggregate output defines legal runtime reachability.

## New DSD application boundaries

Reject:

- `external workflow step = DSD formation stage`;
- `later external state exists = predecessor DSD conditions were satisfied`;
- `lineage relation = workflow authorization`;
- `same final effect = same valid path`;
- `typing/authentication/authorization = workflow reachability`.

## Independence judgment

CS-005 is independent of CS-001~004. It isolates **path/reachability provenance**: a system can be correctly typed, correctly authorized, temporally current, and parser-safe while still accepting an operation from a state that the declared workflow says should not reach it.

## Final classification

`compatible + stage/runtime boundary strengthening + independent reachability/provenance computational node`.

No direct contradiction with the current DSD systems was found.