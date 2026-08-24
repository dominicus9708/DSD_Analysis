# Computer Science, Types, and Program Semantics

Status: CS-001~003 / Global Cases 029~031 first-pass analyses complete; broader computer-science campaign remains open.

This domain tests DSD Analysis against computational structures where static admissibility, runtime state, security policy, temporal validity, evaluation, and failure can be formally distinct.

## Method

Use the standard DSD Analysis order:

`external source structure -> strong candidate -> active counterpressure -> finite witness when possible -> DSD mapping -> contradiction audit -> generalization status`.

Preserve programming-language, security, concurrency, and formal-method terminology first. Do not rename native concepts as DSD stages or statuses by identity.

## CS-001 / Global Case 029

Topic: static type compatibility, construction, runtime validity, operation applicability, evaluation, and result.

Surviving separation:

`static type compatibility != constructed runtime value/status != valid runtime state != operation applicability != evaluation behavior != returned result`.

Important boundary: Rust `None` and `Err(e)` are defined enum values and are not DSD undefined assignment by identity.

Detailed record: `029_type_construction_runtime_validity/`.

## CS-002 / Global Case 030

Topic: authentication, authorization, bounded privilege/credential, request admission, and execution/effect.

Surviving separation:

`authentication status != authorization relation/decision != bounded privilege/credential != downstream admission != execution/effect`.

Important boundaries:

- authorization denial is a defined source-domain decision, not automatically DSD undefined;
- security roles and permission hierarchies are not realized DSD axes merely because they are ordered.

Detailed record: `030_authentication_authorization_execution/`.

## CS-003 / Global Case 031

Topic: check-time/use-time state change, stale validation, resource identity, version preconditions, and concurrent mutation.

Witness families:

- MITRE CWE-367 technology-neutral TOCTOU definition;
- SEI CERT POS35-C pathname/symlink check-use race;
- RFC 9110 `If-Match` / `If-Unmodified-Since` lost-update preconditions;
- PostgreSQL transaction isolation, serialization failure, and retry.

Surviving separation:

`check-time condition != cross-time preservation relation != use-time condition != operation admission != committed/effective result`.

Finite witnesses show that:

- a check may have been correct and later become stale;
- the same pathname/designator can refer to a changed effective resource;
- an earlier representation/version is not automatically valid for a later mutation;
- a transaction may have a valid earlier view and still be rolled back after concurrent change.

Important DSD application boundaries:

- Formation is static and does not itself prove temporal persistence;
- the Axis-Property System is explicitly non-dynamical and is not the primary layer;
- Structural Reorganization Dynamics is the strongest correspondence because it uses time-indexed slices, separates regular evolution from status/domain and stronger transitions, and requires explicit lineage for identity-sensitive change;
- external file identity, ETags, and transaction snapshots are not DSD lineage by identity;
- no later state may be inferred from an earlier valid slice without a source-native cross-time preservation or revalidation relation.

No direct contradiction with the current DSD axioms or Structural Reorganization Dynamics was found.

Detailed record: `031_toctou_state_change/`.

## Next-case selection rule

Do not open a follow-up merely to repeat undefined/zero, authentication/authorization, or another ordinary TOCTOU example.

The strongest remaining independent candidates are:

- data/value versus command/syntax reinterpretation;
- state-machine transition bypass or illegal downstream reachability;
- a concurrency/memory-model case only if it adds pressure beyond CS-003's stale-state relation;
- another source-native distinction that directly falsifies a surviving CS-001~003 candidate.

Candidate labels remain provisional until overlap audit is performed.