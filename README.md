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

- Domain: Mathematical and philosophical logic.
- Core test: separate pure renaming, equal downstream composite, and satisfaction-preserving signature translation/reduct.
- Primary DSD target: Formation Definition 6.10 strict base-fixed formation isomorphism and its relation to composite coincidence.
- Initial result: **not falsified** for the tested equivalence layer.
- Renaming test: strict equivalence is invariant under structure-preserving relabeling over the fixed anchored base.
- Same-output test: equal composites do not force strict formation equivalence.
- Roadmap refinement: Institution-Theory satisfaction preservation is not DSD strict equivalence; it is only a methodological/structural comparison node.
- Boundary: a future weaker signature-translation/reduct or observational-equivalence layer could be studied without replacing strict equivalence.

## Repository structure

- `methodology/` — common analysis protocol and case template
- `cases/` — case-by-case analysis records
- `cross_domain/` — recurring patterns and cross-domain convergence records after multiple completed cases

## Status

Case 001 has completed its initial mathematical analysis on branch `prep/partial-functions-undefined-zero`.

Case 002 has completed its initial mathematical analysis on branch `analysis/case-002-many-sorted-logic`, including source notes, a finite type-erasure witness, a corrected correspondence map, and the local verdict.

Case 003 has completed its initial mathematical analysis on branch `analysis/case-003-institution-theory`, including source notes, three comparison witnesses, an additional strictness-boundary witness, and the local verdict.
