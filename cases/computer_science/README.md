# Computer Science, Types, and Program Semantics

Status: CS-001~005 / Global Cases 029~033 first-pass analyses complete; broader computer-science campaign remains open.

This domain tests DSD Analysis against computational structures where static admissibility, runtime state, security policy, temporal validity, parser context, workflow reachability, evaluation, and failure can be formally distinct.

## Method

Use the standard DSD Analysis order:

`external source structure -> strong candidate -> active counterpressure -> finite witness when possible -> DSD mapping -> contradiction audit -> generalization status`.

Preserve programming-language, security, concurrency, parser, protocol/workflow, and formal-method terminology first. Do not rename native concepts as DSD stages or statuses by identity.

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

Important boundary: authorization/security roles are not DSD undefined states or realized axes by identity.

Detailed record: `030_authentication_authorization_execution/`.

## CS-003 / Global Case 031

Topic: check-time/use-time state change, stale validation, resource identity, version preconditions, and concurrent mutation.

Surviving separation:

`check-time condition != cross-time preservation relation != use-time condition != operation admission != committed/effective result`.

Important boundary: no later state may be inferred from an earlier valid slice without a source-native cross-time preservation or revalidation relation.

Detailed record: `031_toctou_state_change/`.

## CS-004 / Global Case 032

Topic: data/value versus downstream syntax/directive interpretation.

Surviving separation:

`upstream value/data status != downstream grammar/context != binding/encoding relation != parsed role != operation/effect`.

Important boundary: parser context is not a DSD role/channel/stage without an explicit interpretation bridge.

Detailed record: `032_data_syntax_reinterpretation/`.

## CS-005 / Global Case 033

Topic: workflow/state-machine reachability, predecessor enforcement, and transition provenance.

Witness families:

- MITRE CWE-841 improper enforcement of behavioral workflow;
- TLS 1.3 protocol-defined handshake ordering and `unexpected_message` handling;
- WebSocket opening-handshake boundary before data transfer.

Surviving separation:

`current state/action form != source transition relation != valid successor reachability != successor state/effect != transition provenance`.

Finite witnesses show that a downstream state or action can be representable, correctly typed, or protocol-grammatical without being validly reachable from the present state.

Important DSD application boundaries:

- DSD Formation stages are static structural stages, not runtime protocol states by identity;
- Formation traces support provenance-sensitive auditing but do not supply arbitrary application workflows;
- Dynamics lineage gives time-directed structural succession, not workflow authorization by itself;
- same final effect does not reconstruct a valid predecessor path.

No direct contradiction with the current DSD systems was found. CS-005 qualifies as an independent node because it adds transition-path/reachability provenance beyond current-state applicability, access control, stale-state transfer, and parser reinterpretation.

Detailed record: `033_workflow_reachability/`.

## Next-case selection rule

Do not open a follow-up merely to repeat undefined/zero, authentication/authorization, ordinary TOCTOU, parser injection boundaries, or another skipped-step workflow.

The next case should be selected only after an overlap audit and must add a genuinely different computational interface or direct falsification pressure.