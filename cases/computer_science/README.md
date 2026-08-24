# Computer Science, Types, and Program Semantics

Status: CS-001 / Global Case 029 first-pass analysis complete; broader computer-science campaign remains open.

This domain tests DSD Analysis against computational structures where static admissibility, construction, runtime state, operation applicability, evaluation, and failure can be formally distinct.

## Method

Use the standard DSD Analysis order:

`external source structure -> strong candidate -> active counterpressure -> finite witness when possible -> DSD mapping -> contradiction audit -> generalization status`.

Preserve programming-language and formal-method terminology first. Do not rename native concepts as DSD stages by identity.

## CS-001 / Global Case 029

Topic: static type compatibility, construction, runtime validity, operation applicability, evaluation, and result.

Witness families:

- PLFA progress/preservation and well-typed divergence;
- Rust `Option` / `Result` and panic/defaulting behavior;
- Java `Iterator` / `Scanner` state-sensitive operation legality;
- Dafny preconditions, postconditions, and `Valid()` object-invariant discipline.

Surviving source-sensitive separation:

`static type compatibility != constructed runtime value/status != valid runtime state != operation applicability != evaluation behavior != returned result`.

Additional surviving constraints:

- `well typed != guaranteed termination`;
- `declared operation != currently applicable operation`;
- `type-correct call != guaranteed normal return`;
- `same returned value != same computational status/history`.

Important DSD application boundary:

**Rust `None` and `Err(e)` are defined enum values and must not be identified with DSD undefined assignment by identity.**

The case also rejects treating every runtime exception as DSD channel absence or every runtime state change as a DSD identity-changing transition.

No direct contradiction with the current DSD axioms was found. The main result is restriction of overbroad mappings and confirmation that operational computation adds distinctions beyond the earlier static logic-domain cases.

Detailed record:

- `029_type_construction_runtime_validity/PLAN.md`
- `029_type_construction_runtime_validity/SOURCE_NOTES.md`
- `029_type_construction_runtime_validity/MODEL.md`
- `029_type_construction_runtime_validity/CONTRADICTION_AUDIT.md`
- `029_type_construction_runtime_validity/RESULT.md`

## Next-case selection rule

Do not open a follow-up merely to repeat `undefined != zero` or to collect another programming language with the same `Option`/`Result` pattern.

A follow-up should add independent pressure such as:

- authentication versus authorization/capability;
- check-time versus use-time state change;
- data/value versus command/syntax reinterpretation;
- state-machine transition bypass or illegal downstream reachability;
- another source-native distinction that directly falsifies the CS-001 surviving candidate.

Candidate labels remain provisional until overlap audit is performed.
