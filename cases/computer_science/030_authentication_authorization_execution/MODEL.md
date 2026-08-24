# Structural Model — CS-002 / Global Case 030

## 1. Source-sensitive separation

The source families support the following non-totalization, without requiring every system to implement every stage:

`identity evidence/status != authenticated principal != authorization decision != bounded privilege/credential != request admission != execution/effect`.

A more operational request model is:

`request -> authentication context -> authorization context -> optional delegated credential/scope check -> admission/policy gate -> execution/effect`.

These are source-domain states and relations, not DSD Formation stages by identity.

## 2. Authorization as a relation, not a unary identity property

A minimal authorization predicate can be represented as

`Allow(subject, object, operation, environment, policy)`.

NIST ABAC shows why reducing this to `Allow(subject)` loses relevant information. The same subject may be allowed on one tuple and denied on another.

## 3. Finite witness

Take one authenticated principal `alice` and three requests in a Kubernetes-like policy pipeline.

| Request | Authentication | Authorization | Admission | Effect |
|---|---|---|---|---|
| R1: read allowed workload | success | allow | not blocking | read succeeds |
| R2: delete protected secret | success | deny | not reached | no deletion |
| R3: create policy-forbidden workload | success | allow | reject | no creation |

This finite witness separates three claims at once:

1. same authenticated principal can have different authorization decisions (`R1` vs `R2`);
2. authorization allow does not imply admission (`R3`);
3. no effect can arise from different upstream failure points (`R2` vs `R3`).

The witness is schematic and source-faithful; it does not claim a particular Kubernetes cluster has exactly these rules.

## 4. OAuth scope witness

Let a bearer token be valid but scoped only to resource set `A`. A request for protected resource `B` may fail with `insufficient_scope` even though the token itself is not invalid.

Hence:

`valid token != sufficient scope for requested resource`.

Also:

`invalid_token != insufficient_scope`.

These are defined protocol outcomes and must not be collapsed into one generic undefined state.

## 5. Surviving candidate

The sources support the audit rule:

**Do not infer later access states from earlier identity or credential states unless the source system supplies the relevant policy, object, operation, scope, environment, and downstream gate conditions.**

This is a non-totalization principle, not a universal security architecture.
