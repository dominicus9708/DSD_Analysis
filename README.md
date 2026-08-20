# DSD Analysis

This repository records structured applications of DSD Analysis (DSD 분석론).

The repository is not a numerical benchmark repository and does not treat cross-domain similarity as a proof of the DSD axioms. Each case preserves the source discipline first, then tests which DSD distinctions are directly preserved, partially preserved, recoverable only after explicit encoding, or not preserved.

## Current first case

- Domain: Mathematical and philosophical logic
- Topic: Partial functions and undefinedness
- Core test: compare a domain-preserving partial assignment with totalization by a default value (especially zero), and identify which distinctions are lost.
- Primary DSD target: undefined assignment vs defined zero; downstream channel absence vs admitted zero-valued channel.

## Repository structure

- `methodology/` — common analysis protocol and case template
- `cases/` — case-by-case analysis records
- `cross_domain/` — recurring patterns and cross-domain convergence records (added after multiple completed cases)

## Status

The first case is in preparation on branch `prep/partial-functions-undefined-zero`.
