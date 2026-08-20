# Finite Witness — Presupposition versus Assertion

Let the possible-world set be

`W = {w1, w2, w3}`.

Let the background proposition `p` be true at `w1,w2` and false at `w3`.
Let the asserted proposition `q` be true at `w1,w3` and false at `w2`.

Take the initial context

`C0 = {w1,w2,w3}`.

Use a simple partial update rule for an utterance `u` with presupposition `p` and asserted content `q`:

`U_u(C)` is defined only if every world in `C` satisfies `p`; when defined, `U_u(C) = C ∩ [[q]]`.

Then `U_u(C0)` is undefined because `w3` violates the presupposition.

This is not the same state as a successfully evaluated false assertion. For example, with

`C1 = {w1,w2}`,

presupposition `p` is satisfied, so the update is defined and gives

`U_u(C1) = {w1}`.

If instead the asserted content were false throughout `C1`, the update would be defined and could yield the empty context. Thus:

- presupposition failure: update not defined under the chosen partial rule;
- successful but rejecting assertion: update defined, possibly with empty output;
- successful assertion: update defined with nonempty output.

## Accommodation variant

Define an explicit repair operation

`ACC_p(C0) = C0 ∩ [[p]] = {w1,w2}`.

Then

`U_u(ACC_p(C0)) = {w1}`.

The accommodated result is therefore produced by an extra context-repair step. It must not be read as evidence that `p` was already in the original context.

## What the witness establishes

The finite witness separates:

1. missing presupposition support;
2. defined semantic update;
3. defined rejection/false-result behavior;
4. explicit accommodation.

It does not prove that all theories of presupposition use this partial update semantics.
