# CS-001 Contradiction and Overreach Audit

Status: first-pass audit complete.

## 1. Target hypotheses

### H1. Well typed implies a final runtime value necessarily exists

Verdict: rejected as a universal claim.

PLFA's recursive example is well typed and can reduce forever. Progress and preservation establish non-stuckness/type preservation, not universal termination.

### H2. Successful construction implies every declared operation is applicable

Verdict: rejected.

Java `Iterator.remove()` and `Scanner` operations are state-sensitive. Dafny also permits explicit object validity and operation preconditions.

### H3. Type-correct operation implies runtime evaluation succeeds normally

Verdict: rejected.

Rust `Option::unwrap` and `Result::unwrap` are type-correct method calls that can panic depending on the runtime variant. Java operations can throw state/input-related exceptions despite static method availability.

### H4. Absence, explicit zero/empty, error, and non-applicability can be collapsed without loss

Verdict: rejected as a universal claim.

Rust directly distinguishes `None`, `Some(0)`, `Ok(0)`, and `Err(e)`. Dafny separates a value's type from satisfaction of a precondition. Java separates method existence from supported/currently legal invocation.

Boundary: a later explicit conversion may intentionally collapse states. Such postprocessing is allowed, but the collapse must not be retroactively treated as source-level identity.

### H5. Declared interface capability equals current-state callability

Verdict: rejected.

Java `Iterator.remove()` is the finite counterexample: declaration, implementation support, and temporal call legality are distinct.

### H6. Same returned result implies the same evaluation path/history

Verdict: rejected.

`Ok(0).unwrap_or_default()` and `Err(e).unwrap_or_default()` can both return `0` while preserving distinct pre-output statuses.

### H7. Runtime failure proves static typing failed

Verdict: rejected.

A well-typed computation may diverge, panic, throw an exception, violate an operation precondition in an unchecked environment, or return an explicit error value. These failure/status modes are not equivalent to static type rejection.

## 2. DSD Formation audit

The Formation Axiom System is compatible with the discipline of separating applicability/domain status from defined values and of separating defined zero from undefined assignment or channel absence.

However, one tempting mapping is invalid:

`Rust None = DSD undefined assignment`.

This is false by native semantics. `None` is a fully defined value of `Option<T>`.

Likewise:

`Rust Err(e) = DSD undefined assignment`

is false by identity. `Err(e)` is a defined value of `Result<T,E>`.

A DSD application may encode these states, but only through an explicit interpretation map that preserves their native status.

No contradiction with the current Formation axioms was found.

## 3. Axis-Property audit

The Axis-Property System's distinctions among candidate property kinds, declared kinds, application domains, undefined applications, and defined values are structurally useful for contract/precondition-style comparison.

But the system is explicitly static and pre-dynamical. It cannot by itself justify identifying a changing Java/Dafny object state with a static axis-property application domain across time.

For temporal callability, a dynamic interpretation layer is required.

No contradiction with the Axis-Property axioms was found.

## 4. Static Aggregation audit

The Rust `unwrap_or_default` witness shows generic non-injectivity of postprocessing: distinct statuses can produce the same visible output.

This is compatible with the DSD static-aggregation warning that aggregate equality does not reconstruct support or complete typed structure.

But `unwrap_or_default` is not the DSD aggregation operator and is not evidence that Rust computation instantiates Channel-Indexed Static Aggregation.

Mapping strength: analogy/partial structural correspondence only.

## 5. Structural Reorganization Dynamics audit

The Java iterator and scanner examples create genuine state-transition pressure:

- an operation may be applicable at one state and inapplicable at another;
- normal return, error, close, and recovery paths may need distinct transition labels;
- identity can persist while applicability changes.

This is compatible with the DSD dynamics separation of regular value evolution, status/domain transitions, and higher-level identity-changing transitions.

Important boundary:

not every runtime step should be promoted to a DSD structural-reorganization event. The external source must first say which state/status distinction matters.

No direct contradiction with the current dynamics framework was found.

## 6. New application rules produced by CS-001

Reject these shortcuts:

1. `well typed = formed final value`;
2. `None/error = undefined`;
3. `declared member = currently applicable operation`;
4. `type-correct call = successful normal return`;
5. `same return value = same computational history`;
6. `runtime failure = type-system failure`;
7. `every runtime state change = DSD identity change`.

## 7. Independence from earlier logic cases

CS-001 would be redundant if its only conclusion were `undefined != zero` or `typing precedes applicability`.

It is independent enough for a new cross-domain node because the evidence additionally requires:

- operational reduction and possible nontermination;
- runtime sum/error states as defined values;
- temporal state-sensitive callability;
- contract/invariant satisfaction at use sites;
- non-injective postprocessing of computational outcomes.

These are computational/operational structures rather than merely static logical distinctions.

## 8. Final audit status

- direct contradiction with current DSD axioms: none found;
- overbroad DSD application assumptions: several rejected;
- source-native distinctions preserved: yes;
- independent computational pressure beyond earlier logic cases: yes, first-pass threshold met;
- active falsification: remains open.
