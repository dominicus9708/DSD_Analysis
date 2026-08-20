# DSD Analysis

This repository records structured applications of DSD Analysis (DSD 분석론).

The repository is not a numerical benchmark repository and does not treat cross-domain similarity as a proof of the DSD axioms. Each case preserves the source discipline first, then tests which DSD distinctions are directly preserved, partially preserved, recoverable only after explicit encoding, or not preserved.

## Case 001 — Partial functions and undefinedness

- Domain: Mathematical and philosophical logic
- Core test: compare a domain-preserving partial assignment with totalization by a default value, especially zero.
- Primary DSD target: undefined assignment vs defined zero; downstream channel absence vs admitted zero-valued channel.
- Initial result: **not falsified**. Naive zero-totalization is non-injective when domain/status information is discarded; status-preserving encodings remain possible.

## Case 002 — Many-Sorted Logic and typed applicability

- Domain: Mathematical and philosophical logic
- Core test: compare a well-sorted defined-zero application with an ill-sorted attempted application after type erasure.
- Primary DSD target: typed property profile and applicability-before-value discipline in the Axis-Property System.
- Initial result: **not falsified** for the tested typing layer.
- Roadmap correction: a wrong-sort input is not DSD `unavailable input`; it is outside the property's typed input product. `Unavailable input` means a required profile carrier is unavailable at the configuration.
- Boundary: ordinary many-sorted logic does not by itself establish DSD carrier-unavailability or partial undefinedness.

## Case 003 — Institution Theory and strict equivalence

- Domain: Mathematical and philosophical logic
- Core test: separate pure renaming, same-output/different-structure, and satisfaction-preserving translation across signatures.
- Primary DSD target: strict base-fixed formation isomorphism.
- Initial result: **not falsified**. Pure renaming is preserved; aggregate coincidence does not collapse distinct channel structures; satisfaction-preserving translation is a different and generally weaker comparison notion.
- Roadmap refinement: Institution Theory is retained only as a methodological/structural partial correspondence, not as an identity with DSD strict equivalence.
- Future design opportunity: a separate weaker translation/reduct or observational-equivalence layer could be studied without replacing strict equivalence.

## Case 004 — Free Logic and existential/formation import

- Domain: Mathematical and philosophical logic
- Core test: determine whether candidacy, admission, or realization silently promotes a record to stronger formation status.
- Primary DSD target: Primitive Axioms I–III and Closure Clause IV.
- Initial result: **not falsified**.
- Exact expression-status result: under Primitive Axiom I the permitted `(Adm,Des)` states are `(0,0)`, `(1,0)`, and `(1,1)`; `(0,1)` alone is excluded.
- Realization result: a sound `Realize(h,p)` relation does not by itself imply `Descfg(p)`.
- DSD Analysis significance: adding `candidate => admitted`, `admitted => describable`, or `realized => describable configuration` strictly removes models currently admitted by the system. Such promotion rules are genuine extra assumptions rather than hidden consequences.
- External mapping: Free Logic supplies a partial structural analogue by rejecting automatic existential import from individual constants, but its term/denotation/existence notions are not identified with DSD formation statuses.
- Roadmap refinement: replace the oversimplified unary `candidate -> admitted -> realized` mnemonic with the actual typed expression/restriction/configuration structure.

## Case 005 — Strong Kleene K3 and undefined-as-value

- Domain: Mathematical and philosophical logic
- Core test: determine whether DSD domain-exclusion undefinedness can be identified with the third semantic truth value of Strong Kleene K3.
- Primary DSD target: Formation Stage V–VI and Axis-Property application status.
- Initial result: **not falsified**; classified as an important **non-correspondence** node.
- Type result: DSD undefinedness is absence of an assigned value because an input lies outside a partial-map domain, whereas K3's third state is an element of a semantic truth-value carrier.
- Encoding result: adjoining a fresh disjoint sentinel can faithfully totalize and reconstruct a partial map; therefore `undefined is not a value` must be scoped to the original assignment/value carrier, not all possible external representations.
- Operational result: feeding the external sentinel back into Stage V as an ordinary value changes the assignment graph and can create an additional Stage-VI channel.
- Roadmap refinement: distinguish original partial semantics, faithful lifted representation, and semantic identification.

## Repository structure

- `methodology/` — common analysis protocol and case template
- `cases/` — case-by-case analysis records
- `cross_domain/` — recurring patterns and cross-domain convergence records after multiple completed cases

## Status

Case 001 completed its initial mathematical analysis on branch `prep/partial-functions-undefined-zero`.

Case 002 completed its initial mathematical analysis on branch `analysis/case-002-many-sorted-logic`.

Case 003 completed its initial mathematical analysis on branch `analysis/case-003-institution-theory`.

Case 004 completed its initial mathematical analysis on branch `analysis/case-004-free-logic`, including source notes, finite status-space witnesses, a realization-without-describability witness, and the predefinition/promotion-rule test.

Case 005 completed its initial mathematical analysis on branch `analysis/case-005-strong-kleene`, including a faithful lifted-totalization theorem, a three-state non-equivalence witness, and the Stage-VI sentinel-substitution test.
