# Finite witness — scalar implicature and cancellation

Let the literal sentence be:

`S = Some students passed.`

Use the following two conversational contexts while keeping the same literal asserted proposition:

## Context C1 — ordinary scalar-implicature context
- Literal assertion: at least one student passed.
- Stronger alternative available: all students passed.
- Pragmatic inference licensed under ordinary Quantity-style assumptions: not all students passed.

State:
- `Assert(S) = SOME`
- `Implicature_C1(S) = NOT_ALL`

## Context C2 — explicit cancellation
Utter:

`Some students passed — in fact, all of them did.`

State:
- literal `SOME` assertion remains compatible with the continuation;
- `NOT_ALL` implicature is cancelled;
- asserted content and conversational implicature therefore cannot be identical.

Formally, for fixed asserted content A:

`A_C1 = A_C2 = SOME`

but

`Imp_C1 = NOT_ALL`

and

`Imp_C2 = NONE`.

Hence the projection from full pragmatic state to literal asserted content is many-to-one.
The literal assertion alone does not reconstruct whether the `NOT_ALL` implicature was active.

## Hearer-inference separation
Add a third state C3 where a hearer infers `NOT_ALL` despite contextual evidence that the speaker did not intend that implication.

Then:
- `HearerInference_C3 = NOT_ALL`
- `SpeakerImplicature_C3 = NONE`

This shows that hearer reconstruction must not be identified with speaker implicature by definition.

## DSD-relevant conclusion
The finite witness supports status preservation:
- absence of a stronger assertion is not itself the asserted weaker negation of that stronger proposition;
- a pragmatic bridge can license an implicature;
- cancellation can remove the implicature while leaving literal assertion fixed;
- therefore pragmatic output should not be back-filled into semantic input as if it had been explicitly present from the start.