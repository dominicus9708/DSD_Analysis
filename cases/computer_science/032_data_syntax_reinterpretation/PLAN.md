# CS-004 / Global Case 032 — Data, Syntax, and Downstream Reinterpretation

Status: analysis started.

## Question

Can an input/value that was accepted as ordinary data at an upstream interface be treated as preserving that same semantic role when it is later inserted into another parser, query language, markup context, or command interpreter?

## Strong hypotheses to attack

1. If an input string is valid data at ingestion, it remains data in every downstream context.
2. Input validation alone fixes the later syntactic role of the value.
3. A string's characters have one context-independent operational meaning.
4. If two systems receive the same string, they must interpret the same structural role.
5. Escaping/encoding/parameter binding are merely cosmetic transformations and do not protect a semantic boundary.
6. A downstream parser reinterpreting data as syntax means the upstream value was undefined or invalid in itself.
7. If the final visible/output value is unchanged, the intermediate data/syntax boundary is structurally irrelevant.

## Required source families

- SQL/data-query boundary and parameter binding;
- browser markup/script/output-context interpretation;
- process/shell command argument interpretation;
- at least one implementation/API source that explicitly preserves data/code separation.

## DSD scope

- Formation Axiom System: primary comparison for typed role, assignment, and staged application; no identity mapping from external strings to DSD channels.
- Axis-Property System: secondary only if a realized-axis interpretation is independently supplied; syntax roles are not axes by default.
- Structural Reorganization Dynamics: secondary. Reinterpretation may occur without temporal evolution; if a role/application-status transition is modeled dynamically, it must be explicit.
- Static Aggregation: not primary; use only for information-loss/output-equivalence observations.

## Independence requirement

CS-004 counts as an independent node only if it establishes a parser/context-dependent role transformation that is not reducible to CS-001 type/runtime applicability, CS-002 access-control decisions, or CS-003 stale-state transfer.