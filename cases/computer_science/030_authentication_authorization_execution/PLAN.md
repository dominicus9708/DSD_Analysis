# CS-002 / Global Case 030 — Authentication, Authorization, Admission, and Execution

Status: first-pass cross-subfield analysis complete.

## Question

Can identity proof/authentication, authorization, granted privilege or token possession, request admission, and successful execution/effect be collapsed into one security state merely because they occur in one access path?

## Strong hypotheses tested

1. Successful authentication implies authorization for the requested operation — rejected.
2. A known identity or role determines one stable permission state across resources and operations — rejected.
3. Possession of a valid credential or access token implies access to every protected resource reachable through that credential — rejected.
4. An authorization allow decision implies the request will be admitted and executed successfully — rejected.
5. Access denial implies authentication failure — rejected.
6. Two requests by the same authenticated principal have the same effective permission — rejected.
7. An authorization outcome can be inferred from subject identity alone without object, operation, policy, or environment information — rejected as a general claim.

## Source families used

- NIST SP 800-63-4 digital identity/authentication;
- NIST SP 800-162 ABAC;
- OAuth 2.0 authorization and bearer-token scope semantics;
- Kubernetes authentication, authorization, and admission pipeline.

## DSD scope result

- Formation Axiom System: compatible under explicit interpretation only.
- Axis-Property System: no default mapping; security roles/permissions are not realized axes by themselves.
- Static Aggregation: not required.
- Structural Reorganization Dynamics: not required for this atemporal case.

## Independence result

CS-002 qualifies as an independent computer-science node because it adds request-specific policy relations, scoped delegated credentials, and post-authorization admission gates beyond CS-001's type/runtime/applicability interface.

Detailed evidence and conclusions are in `SOURCE_NOTES.md`, `MODEL.md`, `CONTRADICTION_AUDIT.md`, `SCOPE.md`, and `RESULT.md`.
