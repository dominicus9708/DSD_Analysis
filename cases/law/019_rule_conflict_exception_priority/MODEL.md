# LAW-008 Model — Typed Rule Conflict and Source-Supplied Resolution

## 1. Typed normative instance

Use a source-side legal instance

`tau = (subject, actor, act_or_issue, role, context, time, parties, jurisdiction, regime)`.

Let `R` be the set of source rules.

For each `r in R`, retain separately:

- `Valid(r,t)` — whether the source treats the rule as legally valid/in force at time `t`;
- `Applies(r,tau)` — whether the rule applies to this typed instance;
- `Out(r,tau)` — the source-side legal direction/consequence if applicable.

## 2. Apparent difference is not yet conflict

Define a broad difference relation:

`Different(r1,r2,tau)`

when the texts, source categories or outputs are not identical.

Do not infer:

`Different -> Conflict`.

A first-pass unresolved-conflict candidate requires at least:

`Valid(r1,t) and Valid(r2,t)`

`and Applies(r1,tau) and Applies(r2,tau)`

`and Incompatible(Out(r1,tau), Out(r2,tau))`

with no already-applicable source rule that harmonizes, subordinates, excepts, invalidates, suspends or otherwise resolves the relationship for the issue being decided.

## 3. Source-side relation operator

Let the source supply, where available, a relation package

`Rel(r1,r2,tau) in {harmonize, special-over-general, charter-priority, later-treaty-limited-priority, invalidity, suspension, exception, no-resolution-supplied, other}`.

This is not a universal legal taxonomy. It is an application container for source-specific relations.

The resulting decision state is computed only through the source relation:

`Resolve_source(r1,r2,tau,Rel)`.

DSD Analysis must not invent `Rel`.

## 4. Distinguish priority from deletion and invalidity

At minimum preserve:

`Priority(r1,r2,tau) != Invalid(r2)`

and

`SpecialGoverns(r_s,r_g,tau) != Deleted(r_g)`.

UN Charter Article 103 supplies a `prevail` relation for conflicting obligations.

VCLT Article 53 supplies a different consequence: a conflicting treaty is void when the conflict is with a peremptory norm under the Article's conditions.

ILC lex-specialis analysis supplies another possibility: the special rule governs the relevant matter while the general rule normally remains valid and available outside the special rule's coverage.

## 5. Party-sensitive treaty relation

VCLT Article 30 shows that the same pair of treaty texts need not produce one global priority ordering independent of party relations.

A faithful treaty instance therefore needs at least:

`tau_treaty = (subject_matter, state_pair_or_party_relation, time, earlier_treaty, later_treaty)`.

The governing relation can differ across party pairs when the treaties do not have identical party sets.

Therefore:

`Priority(T2,T1)`

without party/regime indexing is under-typed.

## 6. Exception model

An exception or exclusion may be represented source-faithfully as a condition on applicability:

`Except(e,r,tau) -> not Applies(r,tau)`

when the source structures it that way.

But no universal identity is asserted:

`exception != nonexistence of r`

`exception != invalidity of r`

`exception != affirmative permission in every regime`.

## 7. Functional P/D/J model

Suppose attribution/prosecution function `P` argues:

`Valid(r1) and Applies(r1,tau) and Out(r1,tau)=Forbidden`.

Defence function `D` may respond by attacking distinct links:

- `r1` does not apply;
- an exception applies;
- another valid rule `r2` is more specific under the source system;
- a source hierarchy gives `r2` priority;
- a later-rule relation applies only for these parties;
- the apparent conflict can be harmonized;
- the source leaves a real unresolved conflict that prevents the asserted single-rule conclusion.

Judgment function `J` must not infer the final result until the source-side relation is resolved.

## 8. DSD Formation mapping

Formation is used only as a typed non-totalization discipline.

A possible application encoding may retain separate records for:

- `r1` and `r2`;
- their role/context indices;
- applicability states;
- source-supplied relation/priority state;
- downstream result.

Do not identify:

`legal validity != Formation admission`

`rule applicability != Formation realization`

`exception != channel absence`

`priority loss != channel deletion`

`unresolved conflict != undefined because DSD cannot decide`.

The last distinction matters: if the source itself contains a conflict, the source conflict should be represented as a defined legal relation/status, not erased as an application failure.

## 9. DSD layer boundary

- Formation: sufficient for first-pass typed separation.
- Axis-Property: not required; no realized-axis semantics supplied.
- Static Aggregation: not required; legal priority is not a numeric weight.
- Dynamics: not required for first pass; may matter later for repeal, temporal succession, suspension or reactivation.
