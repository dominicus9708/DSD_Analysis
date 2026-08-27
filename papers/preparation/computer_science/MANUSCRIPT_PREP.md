# Computer Science, Types, and Program Semantics — Manuscript Preparation

Canonical scope: `CS-001–005`.

## Central question

What errors arise when value, type, access relation, runtime context, temporal preservation, and workflow reachability are collapsed into one program state, and how can DSD audit them without replacing programming-language semantics?

## Recommended angle

**Context, Type, Access, and Reachability: A DSD Non-Collapse Audit for Program Semantics**.

## Core mechanisms

- value != type/state;
- access authority is an actor-resource-action-context relation;
- snapshot equality != diachronic preservation;
- same code/expression != same runtime context;
- transition availability != actual reachability/execution.

## Proposed sections

1. Language/runtime-independent scope.
2. Five non-overlapping `CS-001–005` mechanisms.
3. Type, access, context, time, reachability.
4. Small execution examples and negative controls.
5. Security policy versus semantics.
6. Implementation/version boundaries.
7. Conclusion.

## Source freeze

Pin versions/dates for programming-language, runtime, and security documentation. Distinguish implementation behavior from language semantics.

## Overclaim guards

Do not identify undefined/null/error globally, infer runtime behavior from static type alone, or infer execution from permission alone.