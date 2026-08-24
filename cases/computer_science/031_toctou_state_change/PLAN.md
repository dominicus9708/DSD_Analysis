# CS-003 / Global Case 031 — Check-Time, Use-Time, and State Change

Status: completed first-pass analysis.

## Question

When a system validates a property, permission, identity, version, or resource state at time `t_check`, can that validation be treated as if it remains valid automatically at a later use or mutation time `t_use`?

## Strong hypotheses attacked

1. If a resource passed validation once, a later use may rely on that validation without re-establishing the relevant state.
2. Equality of resource name/reference at two times implies equality of the resource state or identity actually used.
3. A valid check at `t_check` implies the corresponding precondition remains true at `t_use`.
4. If use fails after an earlier successful check, the earlier check must have been incorrect.
5. Preventing TOCTOU requires only better static typing or better initial validation.
6. A state transition between check and use can always be modeled as ordinary value evolution of one unchanged object without explicit identity/status/version discipline.
7. If two executions have the same final output, intervening concurrent changes are irrelevant to the structural analysis.

## Source families

- MITRE CWE-367: technology-neutral TOCTOU weakness definition.
- SEI CERT POS35-C: concrete filesystem/symlink check-use race and identity-preserving mitigation.
- HTTP conditional request semantics (RFC 9110 `If-Match` / `If-Unmodified-Since`): stale-state prevention by validating the current representation at mutation time.
- PostgreSQL concurrency control / Serializable isolation: concurrent state change may invalidate a transaction's earlier view and force rollback/retry.

## DSD scope

- Formation Axiom System: static source-state typing and identity discipline only; it does not itself solve temporal races.
- Axis-Property System: not a primary layer; it is explicitly non-dynamical.
- Static Aggregation: only for the auxiliary result-equality/history distinction.
- Structural Reorganization Dynamics: primary DSD comparison layer because the case is intrinsically time-indexed.

## Independence requirement

CS-003 counts as a new node only if it establishes a genuinely temporal distinction beyond CS-001 runtime applicability and CS-002 access-control staging. In particular, it must show that a condition valid at one time does not transfer by default to another time, and that safe use requires an explicit cross-time relation, atomic operation, lock, version precondition, or retry discipline.