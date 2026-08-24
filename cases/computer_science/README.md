# Computer Science, Types, and Program Semantics

Status: CS-001~005 / Global Cases 029~033 first-pass foundational series provisionally closed; active falsification and specialized extensions remain open.

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

Surviving separation:

`current state/action form != source transition relation != valid successor reachability != successor state/effect != transition provenance`.

Important DSD application boundaries:

- DSD Formation stages are static structural stages, not runtime protocol states by identity;
- Formation traces support provenance-sensitive auditing but do not supply arbitrary application workflows;
- Dynamics lineage gives time-directed structural succession, not workflow authorization by itself;
- same final effect does not reconstruct a valid predecessor path.

Detailed record: `033_workflow_reachability/`.

## First-pass synthesis

Detailed synthesis: `CS_001_005_FIRST_PASS_SYNTHESIS.md`.

The five nodes are convergent but non-duplicative:

1. CS-001 — local computational semantics;
2. CS-002 — relational access policy;
3. CS-003 — temporal persistence/currentness;
4. CS-004 — interpretation grammar/context;
5. CS-005 — transition reachability/path provenance.

Conservative common audit rule:

`local status != relational admissibility != temporal validity != interpretation role != path reachability/provenance != effect/result`.

This is an audit schema, not a universal literal software pipeline.

No direct contradiction with the current DSD systems was found. The campaign instead removed multiple naive mappings and strengthened the requirement that source-native semantics, identity, persistence, parser role, and transition rules be supplied before DSD interpretation.

## Campaign closure rule

The CS-001~005 foundational first-pass series is provisionally closed.

Do not open a follow-up merely to repeat undefined/zero, authentication/authorization, ordinary TOCTOU, parser injection boundaries, or another skipped-step workflow.

A later CS case should be opened only if overlap audit identifies a genuinely new computational interface or direct falsification pressure that cannot be reduced to the five retained nodes.
