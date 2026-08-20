# DSD Analysis

This repository records structured applications of DSD Analysis (DSD 분석론).

The repository is not a numerical benchmark repository and does not treat cross-domain similarity as a proof of the DSD axioms. Each case preserves the source discipline first, then tests which DSD distinctions are directly preserved, partially preserved, recoverable only after explicit encoding, or not preserved.

## Current first case

- Domain: Mathematical and philosophical logic
- Topic: Partial functions and undefinedness
- Core test: compare a domain-preserving partial assignment with totalization by a default value (especially zero), and identify which distinctions are lost.
- Primary DSD target: undefined assignment vs defined zero; downstream channel absence vs admitted zero-valued channel.
- Initial result: **not falsified**. Naive zero-totalization is non-injective when domain/status information is discarded; status-preserving encodings remain possible.

## Repository structure

- `methodology/` — common analysis protocol and case template
- `cases/` — case-by-case analysis records
- `cross_domain/` — recurring patterns and cross-domain convergence records (added after multiple completed cases)

## Status

Case 001 has completed its initial mathematical analysis on branch `prep/partial-functions-undefined-zero`. The branch contains source notes, a rigorous finite witness, strengthened totalization theorems, the Stage-VI channel consequence, and the case verdict.
