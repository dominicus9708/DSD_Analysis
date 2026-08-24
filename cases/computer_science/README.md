# Computer Science, Types, and Program Semantics

Status: roadmap prepared; first case selected but not yet analyzed.

This domain tests DSD Analysis against computational structures where static admissibility, construction, runtime state, operation applicability, evaluation, and failure can be formally distinct.

## Method

Use the standard DSD Analysis order:

`external source structure -> strong candidate -> active counterpressure -> finite witness when possible -> DSD mapping -> contradiction audit -> generalization status`.

Preserve programming-language and formal-method terminology first. Do not rename native concepts as DSD stages by identity.

## First prepared case

### CS-001 / Global Case 029

Topic: static type compatibility, construction, runtime validity, operation applicability, evaluation, and result.

Primary target separation:

`type-compatible candidate != successfully constructed value != valid runtime state != operation applicable != evaluation success != returned result`.

The point is not to repeat the logic-domain `undefined != zero` result. CS-001 must test whether operational computation introduces independent distinctions involving construction, evaluation, state, failure, and transition.

### Planned witness families

Use at least three structurally different source families when the analysis starts:

1. typed operational semantics or type-safety literature, including progress/preservation style distinctions;
2. a production language with explicit sum/option/error types and construction/evaluation rules;
3. a formal specification, contract, or model-checking framework that separates state admissibility from transition/execution validity.

Multiple programming languages from the same conceptual family are supporting examples, not independent cross-domain nodes by themselves.

## Planned follow-up cases

Only open these after CS-001 is completed and audited for overlap:

- CS-002: `null` / `None` / empty / zero / absent / error-state separation;
- CS-003: authentication, authorization, capability, and execution permission;
- CS-004: check-time versus use-time state change and stale validation;
- CS-005: data/code or value/syntax reinterpretation boundaries;
- CS-006: state-machine transition bypass and illegal downstream reachability.

These are candidates, not commitments.
