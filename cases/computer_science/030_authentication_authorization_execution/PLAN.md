# CS-002 / Global Case 030 — Authentication, Authorization, Admission, and Execution

Status: active analysis.

## Question

Can identity proof/authentication, authorization, granted privilege or token possession, request admission, and successful execution/effect be collapsed into one security state merely because they occur in one access path?

## Strong hypotheses to attack

1. Successful authentication implies authorization for the requested operation.
2. A known identity or role determines one stable permission state across resources and operations.
3. Possession of a valid credential or access token implies access to every protected resource reachable through that credential.
4. An authorization allow decision implies the request will be admitted and executed successfully.
5. Access denial implies authentication failure.
6. Two requests by the same authenticated principal have the same effective permission.
7. An authorization outcome can be inferred from subject identity alone without object, operation, policy, or environment information.

## Required source families

- digital identity/authentication definitions;
- access-control policy semantics such as ABAC;
- delegated authorization/token scope semantics;
- a real API access pipeline that separates authentication, authorization, and post-authorization admission.

## DSD scope

- Formation Axiom System: primary comparison layer, with explicit interpretation map only.
- Axis-Property System: not presumed applicable; organizational/security roles are not realized DSD axes.
- Static Aggregation: not required unless a later reduced-output ambiguity becomes essential.
- Structural Reorganization Dynamics: not required for the core case; temporal permission changes belong to a later check-time/use-time case.

## Independence requirement

CS-002 counts as an independent computer-science node only if it adds security-policy relations and staged access-control decisions beyond CS-001's type/runtime/applicability distinctions.
