# LAW-013 Model — Source-Indexed Legal Time

## 1. Temporal record

A source-faithful record may require:

`(rule, adoption_time, commencement_time, provisional_status, subject/event_time, accrual_time, amendment_time, repeal_or_termination_time, savings_or_transition_rule, retrospective_scope, residual_state, proceeding_status, regime)`.

Not every regime uses every coordinate.

## 2. Non-identities

`enacted/adopted != in force`.

`in force now != applicable to every earlier event`.

`not yet in force != necessarily no provisional operation`.

`repealed/terminated != never existed`.

`repealed/terminated != all accrued rights/liabilities/proceedings extinguished`.

`past applicability != current continued applicability`.

`same text at t1 and t2 != same legal temporal relation if commencement/transition rules differ`.

## 3. Temporal graph

Do not use simple replacement:

`S_old -> S_new` with deletion of `S_old`.

Use source-indexed relations among time-stamped states:

`G_T = (V_T, E_R)`.

Edges may include commencement, provisional application, retroactive application, savings, continuation, mitigation, suspension, repeal, termination and residual-effect relations.

## 4. Historical versus operative state

A rule can be no longer operative prospectively while legal consequences from its earlier operation remain relevant.

Therefore historical legal-state retention is not the same as current normative force.
