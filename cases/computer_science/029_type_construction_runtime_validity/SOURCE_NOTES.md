# CS-001 Source Notes — Type Compatibility, Construction, Runtime Validity, and Evaluation

Status: source review complete for first-pass analysis.

## 1. Source discipline

CS-001 uses four structurally different source families. Programming-language terminology is preserved first; no source concept is renamed as a DSD formation stage by identity.

## 2. Typed operational semantics — PLFA progress/preservation

Source:
- Programming Language Foundations in Agda, `Properties: Progress and Preservation`
- https://plfa.github.io/Properties/

Native claims used:
- for a closed well-typed term, progress gives either a value or a reduction step;
- preservation keeps typing valid across reduction;
- progress + preservation exclude stuck states in the modeled language;
- they do not imply termination;
- the chapter gives a well-typed recursive term `sucμ` that reduces forever.

Boundary:
- `well typed` does not mean `already a value`;
- `well typed` does not imply `eventually returns a value` in a language with general recursion/fixpoint;
- type safety is defined relative to the language's own evaluation rules and notion of stuckness.

## 3. Rust `Option` and `Result`

Sources:
- Rust `std::option`: https://doc.rust-lang.org/stable/std/option/index.html
- Rust `std::result`: https://doc.rust-lang.org/stable/std/result/
- Rust `Result` enum: https://doc.rust-lang.org/stable/std/result/enum.Result.html
- Rust `Option` enum: https://doc.rust-lang.org/core/option/enum.Option.html

Native claims used:
- `Option<T>` is either `Some(T)` or `None`;
- Rust explicitly describes `Option` as useful for partial-function return values and optional values;
- `Result<T,E>` is either `Ok(T)` or `Err(E)`;
- `unwrap` on `None` or `Err` panics;
- `unwrap_or_default` can erase the success/error distinction at the returned-value level.

Critical semantic boundary:
- `None` is a defined variant of the total type `Option<T>`; it is not itself an undefined function application.
- `Err(e)` is a defined `Result<T,E>` value; it is not itself absence or undefinedness.
- therefore a DSD application must not map `None`, `Err`, and DSD undefined assignment to one state merely because all can mean 'no ordinary success value'.

## 4. Java state-sensitive interface operations

Sources:
- Java SE `Iterator`: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html
- Java SE `Scanner`: https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Scanner.html

Native claims used:
- `Iterator.remove()` is an interface operation but can be unsupported;
- even when supported, `remove()` has a state precondition: it is illegal before `next()` and illegal again if repeated without a new `next()`;
- `Scanner.next()` and related operations throw `IllegalStateException` after the scanner is closed;
- token conversion operations can also fail because of exhaustion or input mismatch.

Boundary:
- method membership in a static interface does not establish current-state callability or normal return.

## 5. Dafny preconditions and object validity

Sources:
- Dafny Quick Reference: https://dafny.org/dafny/QuickReference
- Dafny Reference Manual: https://dafny.org/dafny/DafnyRef/DafnyRef.html

Native claims used:
- methods and functions can declare `requires` preconditions and `ensures` postconditions;
- Dafny states that a function precondition says when a partial function is defined and verifies uses against that precondition;
- the standard object-invariant idiom uses an explicit `Valid()` predicate;
- methods may explicitly require `Valid()` and ensure it again after execution.

Boundary:
- ordinary type compatibility and object/reference existence do not by themselves establish that the semantic precondition for an operation holds.

## 6. DSD source lock

Formation Axiom System:
- candidate structural data, admission, realization, assignment, channel formation, and composition are staged;
- undefined assignment, defined zero, defined nonzero value, channel absence, and zero contribution are distinct;
- domain-specific applications require interpretation maps.

Axis-Property System:
- candidate kind, declared kind, application domain, undefined application, defined value, and defined zero are distinct;
- the system is explicitly static and non-dynamical.

Channel-Indexed Static Aggregation:
- aggregate equality does not reconstruct channel support or complete typed property structure;
- declared-but-undefined property applications are not silently represented as zero entries.

Structural Reorganization Dynamics:
- value evolution, status/domain transition, and channel/formation-level transition are separated;
- identity-changing transitions require explicit lineage rather than silent identity mutation.

## 7. Source-family independence judgment

The evidence is not treated as four votes for the same slogan.

- PLFA supplies a formal type-safety/termination distinction.
- Rust supplies explicit algebraic runtime status values and extraction failure.
- Java supplies state-sensitive applicability of statically declared operations.
- Dafny supplies verification-level precondition and invariant separation.

Together they introduce operational computation distinctions that are not reducible to the earlier logic-domain `undefined != zero` result alone.
