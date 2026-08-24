# Model — ADMIN-002

## Organizational authority coordinates

Use a source-sensitive tuple only for bookkeeping:

`A = (actor, formal_role, reporting_line, delegated_authority, scope, retained_responsibility, review_authority, technical_authority, escalation_right, risk_acceptance_authority, transfer_state, implementation_authority, regime, time)`.

A source system need not expose every coordinate.

## Core non-identities

`formal rank != operative decision authority`.

`delegated authority != automatically delegated responsibility`.

`programmatic authority != technical/review authority`.

`review/concurrence != implementation`.

`dissent/escalation != disobedience by identity`.

`transfer of command != deletion of prior state/history`.

## Graph model

Represent authority and review as a directed multigraph rather than one hierarchy:

`G_A = (V, E_delegate, E_report, E_review, E_escalate, E_transfer, E_execute)`.

Different edge types may connect the same actors in different ways.

Parallel authority chains are possible.

For example, a project manager can carry programmatic authority while an independent Technical Authority holds a separate waiver/concurrence function.

## Temporal boundary

Delegation and transfer can be time-bounded.

`authority(actor, issue, t)`

must not be inferred from authority at another time unless the source supplies continuity.

Transfer of command should therefore preserve:

- previous authority state;
- effective transfer time;
- briefing/information handoff;
- new authority state.

## Responsibility boundary

Do not infer:

`decision executed -> reviewer approved`

or

`subordinate exercised delegated authority -> superior responsibility vanished`.

Responsibility/accountability relations must be source-indexed rather than copied from the authority graph.
