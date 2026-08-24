# CS-004 / Global Case 032 — Scope

Status: first-pass scope fixed.

## Included

- upstream data/value admissibility versus downstream syntactic role;
- parser/sink context as an independent determinant of interpretation;
- SQL parameter binding versus mixed query-string construction;
- browser text versus markup/script/output contexts;
- process argument boundaries versus shell parsing;
- context-specific encoding/binding as a structural interface;
- DSD Formation interpretation audit;
- limited Static Aggregation and Dynamics boundary checks.

## Excluded as primary topics

- exploit construction or payload optimization;
- bypass techniques;
- vulnerability exploitation procedures;
- authorization and access control already covered by CS-002;
- stale-state/TOCTOU transfer already covered by CS-003;
- general parser theory beyond what the witnesses require;
- empirical vulnerability prevalence or benchmark measurement.

## Boundary against CS-001

CS-001 concerns static typing, runtime state, applicability, evaluation, and result. CS-004 can occur even when the host-language string is perfectly well-typed and the relevant API call is type-correct. The new issue is how a downstream grammar assigns a new structural role.

## Boundary against CS-002

CS-002 concerns authentication/authorization/admission policy. CS-004 does not require any access-control failure.

## Boundary against CS-003

CS-003 concerns validity transfer across time. CS-004 does not require a state change between check and use; the role difference can arise immediately from entering a different interpreter context.

## Completion criterion

The case qualifies as independent only if source-native evidence shows that role/context is not derivable from the input value alone and that structured binding/context preservation is independently necessary.