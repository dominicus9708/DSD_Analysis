# CS-005 / Global Case 033 — Source Notes

## MITRE CWE-841

Source: https://cwe.mitre.org/data/definitions/841.html

CWE-841 describes a session in which multiple behaviors must be performed but the product fails to ensure that the actor performs them in the required sequence. Its extended description explicitly includes unexpected ordering, omitted steps, and entry into an invalid state.

Source-native lesson: individual action availability does not imply workflow-valid reachability.

## TLS 1.3 — RFC 8446

Source: https://www.rfc-editor.org/info/rfc8446/

TLS 1.3 requires handshake messages to be sent in the order defined by the protocol. A peer receiving a handshake message in an unexpected order must abort with an `unexpected_message` alert. Application Data is also constrained relative to Finished, with explicitly specified early-data exceptions.

Source-native lesson: message syntax/type and protocol-state admissibility are distinct. The early-data exceptions are important: the rule is not a universal linear state machine but a protocol-defined transition relation with explicit exceptional paths.

## WebSocket — RFC 6455

Source: https://www.rfc-editor.org/info/rfc6455/

RFC 6455 separates the opening handshake from the data-transfer phase. Data frames may be transmitted after opening-handshake completion and before the endpoint has sent a Close frame.

Source-native lesson: a data frame can be perfectly well-formed as a frame while still being unavailable at a pre-handshake protocol state.

## DSD source lock

### Formation Axiom System

The Formation Axiom System is explicitly a **static typed set-theoretic axiom system**. It orders seven formation stages and makes that order explicit through truncations and reductions. The truncations are extracted from one full model and are not asserted to be full formation models on their own. Formation traces characterize admitted channels by witness histories. Domain-specific applications require interpretation maps.

Critical boundary: a DSD formation stage is not automatically a runtime protocol state or transition event.

### Structural Reorganization Dynamics

The dynamics paper defines time-indexed admissible structural states, admissible trajectories, temporal lineage, and distinct reorganization classes. Changes of formation assignments or channel sets require explicit lineage rather than silent identity mutation.

Critical boundary: the paper does not supply the transition graph of TLS, WebSocket, checkout flows, or arbitrary application workflows. Such source-native reachability rules must be supplied externally.

### Axis Property / Static Aggregation

Neither is a primary layer for workflow reachability. Ordered property profiles or aggregate equality do not themselves define legal runtime transition paths.