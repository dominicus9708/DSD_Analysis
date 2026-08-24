# CS-003 Scope and Nonclaims

## Included

- temporal invalidation between a check and later use;
- resource identity/state change under a stable external designator;
- atomicity, locking, version matching, post-open identity checks, transaction isolation, conflict detection, and retry as source-native ways to establish safe cross-time use;
- DSD comparison focused on time-indexed state, status/domain transition, and explicit lineage discipline.

## Excluded

- a complete taxonomy of race conditions;
- exploit construction or offensive race-window optimization;
- a universal concurrency semantics for all operating systems, HTTP servers, or databases;
- a claim that files, entity tags, database rows, or transactions literally are DSD channels or axes;
- a claim that every change between check and use is an identity-changing transition;
- a claim that DSD itself supplies locks, transactions, compare-and-swap, entity tags, or synchronization primitives;
- probabilistic timing analysis or scheduler modeling;
- distributed consensus, linearizability, or memory-model analysis except where needed as later independent cases.

## Source-sensitive rule

The external system decides first:

- what state was checked;
- what object/version is later used;
- which intervening changes matter;
- what mechanism preserves or revalidates the required condition.

Only then may a DSD interpretation classify the temporal difference as regular value evolution, status/domain transition, identity-sensitive succession, or non-correspondence.

## Independence from earlier computer-science cases

CS-001: static typing/runtime applicability/evaluation.

CS-002: authentication/authorization/admission/effect staging.

CS-003: validity transfer across time under concurrent mutable state.

CS-003 is independent enough to count as a new computational node because the failure can occur even when the earlier type, validation, identity authentication, and authorization decisions were all correct at their respective check times.