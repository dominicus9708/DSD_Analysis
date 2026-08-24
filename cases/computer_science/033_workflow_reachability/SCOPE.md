# CS-005 / Global Case 033 — Scope

## In scope

- required predecessor steps and legal transition paths;
- workflow/state-machine reachability;
- protocol message admissibility relative to current state;
- path provenance versus current state/effect;
- comparison with DSD staged formation and temporal lineage.

## Out of scope

- exploit construction or offensive bypass instructions;
- detailed TLS cryptography;
- payment/business-specific policy design;
- generic authorization already covered by CS-002;
- stale-state races already covered by CS-003;
- parser/injection semantics already covered by CS-004.

## DSD interpretation boundary

The Formation Axiom System's seven stages are static structural stages, not a universal runtime state machine. Structural Reorganization Dynamics supplies time-indexed state and lineage discipline but does not determine arbitrary application transition graphs. External workflow semantics must therefore be preserved first and mapped only through an explicit application bridge.