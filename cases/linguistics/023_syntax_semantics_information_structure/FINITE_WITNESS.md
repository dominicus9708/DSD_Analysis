# LING-010 / Global Case 023 — Finite Witness

## Witness A — same words, different focus structure
Use the same lexical sequence:

`John only introduced Bill to Sue.`

Represent two information-structural markings:

- U1: `John only introduced BILL to Sue.`
- U2: `John only introduced Bill to SUE.`

Under a Rooth-style toy focus interpretation, let the focused constituent determine the relevant alternative family.

For U1, alternatives vary the introduced person:

Alt1 = {
`John introduced Bill to Sue`,
`John introduced Mary to Sue`,
`John introduced Alex to Sue`
}.

For U2, alternatives vary the recipient:

Alt2 = {
`John introduced Bill to Sue`,
`John introduced Bill to Ann`,
`John introduced Bill to Kim`
}.

Choose a finite world W where:

- John introduced Bill to Sue = true;
- John introduced Mary to Sue = false;
- John introduced Alex to Sue = false;
- John introduced Bill to Ann = true;
- John introduced Bill to Kim = false.

Then a simplified `only` condition can make U1 true while U2 is false.

Therefore the following can all be fixed:

- lexical items,
- lexical denotations,
- linear word order,
- ordinary asserted base proposition `John introduced Bill to Sue`,

while the focus-sensitive full interpretation differs.

Hence:

`same lexical material + same linear order != same complete interpretation`.

## Witness B — same truth conditions, different discourse compatibility
Not every information-structural contrast changes ordinary truth conditions.

Two utterances may express the same at-issue proposition while differing in which constituent is treated as given, topic, or focus. Their discourse felicity or question–answer congruence can therefore differ even if the base proposition is identical.

Thus:

`same truth-conditional proposition != same information-structural state`.

## Witness C — reduction loss
Define a deliberately coarse reduction R that keeps only the bag of lexical tokens, or only the ordinary at-issue proposition.

Then:

R(U1) = R(U2)

while the complete focus-sensitive structures differ.

Therefore R is non-injective on the selected information-structural states.

This is an application-level analogue of the DSD static warning that reduced aggregate equality does not reconstruct complete support/tagged structure. It is not claimed to be the same theorem.