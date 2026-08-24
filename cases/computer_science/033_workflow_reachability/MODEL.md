# CS-005 / Global Case 033 — Model and Finite Witnesses

## Audit graph

For a source-defined workflow, use the conceptual separation

`current state + proposed action + source transition relation -> successor reachability -> successor validity/effect`.

This is not claimed as a universal implementation architecture. It records the minimum information needed to avoid treating a state label or action in isolation as proof of legal reachability.

## Witness A — Minimal skipped-step workflow

Let a source workflow require

`S0 --a--> S1 --b--> S2`.

Suppose an implementation also accepts

`S0 --b--> S2`.

Then `S2` is representable and may even produce the expected external output, but the path is invalid relative to the declared workflow.

This witnesses:

`state existence != valid reachability` and `same final state/effect != same valid provenance`.

## Witness B — TLS 1.3 unexpected handshake order

TLS defines an ordered handshake with explicit exceptions. If a handshake message arrives in an unexpected order, the peer must abort with `unexpected_message`.

Thus a message can belong to the TLS handshake grammar and still be inadmissible at the current protocol state.

Witness:

`well-formed protocol message != state-admissible next message`.

## Witness C — WebSocket pre-handshake data

The WebSocket opening handshake precedes the data-transfer phase. A data frame is permitted after successful handshake completion and before the sender has sent Close.

Therefore the same frame class has different admissibility before and after the handshake boundary.

Witness:

`frame validity != protocol-state reachability`.

## DSD-sensitive witness

A full Formation Stage-VI record contains all earlier-stage coordinates through the staged truncation construction. Erasing later coordinates maps it coherently back to earlier truncations.

However, this must not be read as a runtime trace in which an implementation literally executed Stage I, then II, then III in clock time. The Formation paper is static and explicitly requires application-specific interpretation maps.

Therefore:

`DSD staged dependency != external runtime transition graph by identity`.

For dynamic applications, lineage can preserve cross-time identity once a trajectory and application transition semantics are supplied, but lineage alone does not decide whether an external workflow transition was legal.