# CS-001 Scope — Type, Construction, Runtime State, and Evaluation

Status: preparation.

## Included

- static typing or admissibility judgments;
- value/object construction and initialization;
- explicit absence/error/sum-type states where source semantics distinguishes them;
- runtime invariants or state-dependent operation applicability;
- evaluation success/failure and returned values;
- finite counterexamples showing why one stage cannot be inferred from another;
- DSD correspondence and non-correspondence audit.

## Excluded from CS-001

- detailed exploit construction;
- database NULL semantics as a primary subject;
- authentication/authorization as the main subject;
- concurrency/TOCTOU as the main subject;
- parser/injection semantics as the main subject;
- model-checking reachability except as a supporting formal witness;
- performance, optimization, or compiler benchmarking.

These belong to later cases if they add independent structure.

## Boundary against prior DSD Analysis

Logic cases already established important distinctions involving typing, partial functions, undefinedness, and applicability. CS-001 must therefore establish or falsify an additional operational layer involving construction, runtime state, evaluation, and failure.

A useful candidate decomposition is:

`static admissibility -> construction -> runtime state -> operation applicability -> evaluation -> result`.

The arrows are only workflow placeholders. The analysis must actively test whether they are total, deterministic, monotone, or inferentially reversible.

## Completion criterion

CS-001 is complete only when:

1. source-native distinctions are documented from independent source families;
2. at least one explicit finite program/state witness is given;
3. DSD mapping strength is classified as direct / partial / after encoding / no mapping;
4. overlap with logic cases is explicitly audited;
5. what DSD adds and what it merely renames are separately stated;
6. contradiction status is recorded.
