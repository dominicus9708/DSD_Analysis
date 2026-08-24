# CS-001 Structural Model and Finite Witnesses

## 1. Surviving separation candidate

The first-pass external evidence supports preserving at least the following distinctions when the source system itself distinguishes them:

`static type compatibility != constructed runtime value != valid runtime state != operation applicability != evaluation step/success != returned result`.

This is not claimed as one universal programming-language pipeline. It is a source-sensitive audit decomposition.

Additional constraints:

- `well typed != guaranteed termination`;
- `declared operation != currently applicable operation`;
- `type-correct call != guaranteed normal return`;
- `absence/status variant != undefined application by identity`;
- `same returned value != same prior computational status or path`.

## 2. Witness A — well typed but nonterminating

PLFA gives the recursively defined term

`sucμ = μ "x" => suc x`.

It is well typed at natural-number type, yet repeatedly unfolds to another well-typed term and can reduce forever.

Therefore:

`well typed -/-> eventually produces a final value`.

This does not contradict progress. Every non-value state can continue to step.

## 3. Witness B — `Option<u32>` status separation

Consider three values of one static type:

- `None : Option<u32>`;
- `Some(0) : Option<u32>`;
- `Some(1) : Option<u32>`.

They share the same static type but differ in variant and contained-value status.

The key distinctions are:

`None != Some(0)`;

`Some(0) != Some(1)`.

`None` is still a defined `Option<u32>` value. Therefore it must not be identified with an undefined semantic application merely because it contains no `u32` success value.

## 4. Witness C — type-correct extraction can fail

Let

- `r_ok = Ok(0) : Result<u32, &str>`;
- `r_err = Err("e") : Result<u32, &str>`.

The expression `r.unwrap()` is available for the relevant `Result` type, but Rust specifies that it panics on `Err`.

Therefore:

`method/type compatibility != normal-return guarantee`.

The runtime variant matters.

## 5. Witness D — same returned value, different status history

Use `unwrap_or_default()` with integer default `0`.

- `Ok(0).unwrap_or_default()` returns `0` through the success variant.
- `Err("e").unwrap_or_default()` also returns `0`, but through the error-to-default path.

Thus:

`same returned value = 0`

while

`prior Result status differs`.

Therefore:

`same output != same computational path/status history`.

This is a non-injective postprocessing witness. It is not by itself an instance of DSD static aggregation.

## 6. Witness E — declared method, state-sensitive applicability

For Java `Iterator.remove()`:

- the operation exists in the interface;
- before a successful `next()`, `remove()` is not legally applicable and throws `IllegalStateException`;
- after one legal removal, another `remove()` without a new `next()` is again illegal;
- some iterators do not support the operation at all and throw `UnsupportedOperationException`.

A minimal state sketch is:

`S0 --next--> S1 --remove--> S2`

with

- `remove` invalid at `S0`;
- `remove` conditionally valid at `S1`;
- `remove` invalid again at `S2` until another `next`.

Therefore:

`interface declaration != source-level support != current-state applicability`.

## 7. Witness F — verification-level applicability

In Dafny, a function or method can have a `requires Pre` clause. The Quick Reference explicitly describes a function precondition as saying when a partial function is defined, and Dafny verifies that uses satisfy it.

For object-oriented verification, a `Valid()` predicate can represent an object invariant and can be required by operations.

Therefore the verification state can distinguish:

`reference/type exists`

from

`operation precondition/invariant holds`.

## 8. Source-sensitive computational graph

A useful audit representation is:

`G_CS = (S, E_construct, E_step, E_return, E_error, E_state, E_recover)`.

The graph is not a claim about every language. Edge types are introduced only when the source semantics distinguishes them.

At a state `s`, operation applicability is represented separately as a predicate or partial-domain relation:

`App(op, s)`.

This prevents inference of `App(op,s)` merely from the fact that `op` belongs to the static interface or type.

## 9. Failure condition for the CS-001 candidate

The candidate would be too strong if interpreted as saying every language must implement all six layers explicitly.

A source may intentionally encode some distinctions into one sum type, eliminate some states statically, or define an operation total by returning an error/status value rather than throwing.

The surviving rule is therefore preservation of distinctions that the source semantics itself makes, not mandatory multiplication of states.
