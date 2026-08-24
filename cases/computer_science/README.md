# Computer Science, Types, and Program Semantics

Status: CS-001~002 / Global Cases 029~030 first-pass analyses complete; broader computer-science campaign remains open.

This domain tests DSD Analysis against computational structures where static admissibility, runtime state, evaluation, security policy, authorization, admission, and failure can be formally distinct.

## Method

Use the standard DSD Analysis order:

`external source structure -> strong candidate -> active counterpressure -> finite witness when possible -> DSD mapping -> contradiction audit -> generalization status`.

Preserve programming-language, security, and formal-method terminology first. Do not rename native concepts as DSD stages or statuses by identity.

## CS-001 / Global Case 029

Topic: static type compatibility, construction, runtime validity, operation applicability, evaluation, and result.

Witness families:

- PLFA progress/preservation and well-typed divergence;
- Rust `Option` / `Result` and panic/defaulting behavior;
- Java `Iterator` / `Scanner` state-sensitive operation legality;
- Dafny preconditions, postconditions, and `Valid()` object-invariant discipline.

Surviving source-sensitive separation:

`static type compatibility != constructed runtime value/status != valid runtime state != operation applicability != evaluation behavior != returned result`.

Important DSD application boundary:

**Rust `None` and `Err(e)` are defined enum values and must not be identified with DSD undefined assignment by identity.**

No direct contradiction with the current DSD axioms was found.

Detailed record: `029_type_construction_runtime_validity/`.

## CS-002 / Global Case 030

Topic: authentication, authorization, bounded privilege/credential, request admission, and execution/effect.

Witness families:

- NIST SP 800-63-4 digital authentication versus authorization;
- NIST SP 800-162 ABAC subject/object/operation/environment policy evaluation;
- OAuth 2.0 scoped access tokens and `invalid_token` versus `insufficient_scope`;
- Kubernetes authentication -> authorization -> admission pipeline.

Surviving source-sensitive separation:

`authentication status != authorization relation/decision != bounded privilege/credential != downstream admission != execution/effect`.

Finite witness: one authenticated principal can be allowed for one request, denied for another, and authorized yet rejected by a downstream admission policy for a third.

Important DSD application boundaries:

- authorization denial is a defined source-domain decision and is not automatically DSD undefined assignment;
- `invalid_token`, `insufficient_scope`, and admission rejection must not be mapped to DSD absence/zero/undefined labels by superficial similarity;
- security principals, roles, groups, tokens, and permission hierarchies are not realized DSD axes merely because they have relations or ordering.

No direct contradiction with the current DSD axioms was found. CS-002 qualifies as an independent node because it adds request-specific relational policy, scoped delegation, and post-authorization gates beyond CS-001's type/runtime interface.

Detailed record: `030_authentication_authorization_execution/`.

## Next-case selection rule

Do not open a follow-up merely to repeat `undefined != zero`, another Option/Result language, or another authentication-versus-authorization example.

The strongest remaining independent candidates are:

- check-time versus use-time state change and stale validation;
- data/value versus command/syntax reinterpretation;
- state-machine transition bypass or illegal downstream reachability;
- another source-native distinction that directly falsifies a surviving CS-001/002 candidate.

Candidate labels remain provisional until overlap audit is performed.
