# Computer Science, Types, and Program Semantics

Status: CS-001~004 / Global Cases 029~032 first-pass analyses complete; broader computer-science campaign remains open.

This domain tests DSD Analysis against computational structures where static admissibility, runtime state, security policy, temporal validity, parser context, evaluation, and failure can be formally distinct.

## Method

Use the standard DSD Analysis order:

`external source structure -> strong candidate -> active counterpressure -> finite witness when possible -> DSD mapping -> contradiction audit -> generalization status`.

Preserve programming-language, security, concurrency, parser, and formal-method terminology first. Do not rename native concepts as DSD stages or statuses by identity.

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

Surviving separation:

`check-time condition != cross-time preservation relation != use-time condition != operation admission != committed/effective result`.

Important boundary: no later state may be inferred from an earlier valid slice without a source-native cross-time preservation or revalidation relation.

Detailed record: `031_toctou_state_change/`.

## CS-004 / Global Case 032

Topic: data/value versus downstream syntax/directive interpretation.

Witness families:

- MITRE CWE-89 data/directive boundary;
- OWASP SQL parameterization and output-context encoding;
- Python `sqlite3` bound parameters;
- MDN `textContent` versus `innerHTML`;
- Python `subprocess` argument boundaries versus shell parsing.

Surviving separation:

`upstream value/data status != downstream grammar/context != binding/encoding relation != parsed role != operation/effect`.

Finite witnesses use benign values only:

- `O'Reilly` as a bound SQL parameter versus query-source text;
- `<b>A</b>` as plain text versus HTML markup;
- `report 2026.txt` as one argv item versus material parsed by a shell command language.

Important DSD application boundaries:

- the same external value is not automatically the same DSD operational role;
- parser contexts are not DSD roles, channels, or stages without an explicit interpretation bridge;
- injection-like reinterpretation is not automatically DSD undefined assignment;
- parser handoff is not automatically a Structural Reorganization Dynamics event;
- no primary Axis-Property mapping is justified.

No direct contradiction with the current DSD systems was found. CS-004 qualifies as an independent node because it adds context-dependent grammar/role reinterpretation beyond type/runtime, access-control, and temporal-validity distinctions.

Detailed record: `032_data_syntax_reinterpretation/`.

## Next-case selection rule

Do not open a follow-up merely to repeat undefined/zero, authentication/authorization, ordinary TOCTOU, or another injection technology with the same data/directive boundary.

The strongest remaining independent candidate is:

- state-machine transition bypass or illegal downstream reachability;
- a concurrency/memory-model case only if it adds pressure beyond CS-003;
- another source-native distinction that directly falsifies a surviving CS-001~004 candidate.

Candidate labels remain provisional until overlap audit is performed.