# Finite Witness — LING-004 / Global Case 017

## Witness A — lexical ambiguity
Let one surface-form token be

`u = "bank"`.

Let the legitimate interpretation-candidate set be

`Cand(u) = {m_financial, m_river}`.

Assume both are individually well formed and semantically defined:

`Interp(u,m_financial) = FINANCIAL_INSTITUTION`,

`Interp(u,m_river) = RIVER_EDGE`.

Before disambiguation, the state is not

`Interp(u) = undefined`

and not

`Interp(u) = FINANCIAL_INSTITUTION`.

Instead it is the candidate family

`Cand(u) = {m_financial,m_river}`.

A later context can select one candidate, e.g.

`Select_C(Cand(u)) = m_financial`.

The selection operation is additional data; it does not prove that `m_financial` was the unique pre-context meaning.

## Witness B — scope ambiguity
Let surface sentence `s` be:

`Every woman squeezed a man.`

Two candidate readings are:

`m1 = forall x (Woman(x) -> exists y (Man(y) and Squeezed(x,y)))`

`m2 = exists y (Man(y) and forall x (Woman(x) -> Squeezed(x,y)))`.

Take a finite world with two women `w1,w2` and two men `a,b` such that

`Squeezed(w1,a)` and `Squeezed(w2,b)` are true,

with no single man squeezed by both women.

Then

`m1 = TRUE`

but

`m2 = FALSE`.

Thus silently preselecting one reading can change the truth value of the same surface sentence.

## DSD pressure
A naive application

`q(u) = m1` and `q(u) = m2`

for one exact input `u` violates single-valued function structure.

A faithful application must instead distinguish candidate interpretation objects, for example

`u_fin = (u, lexical/scope-candidate-id 1)`,

`u_riv = (u, lexical/scope-candidate-id 2)`,

or distinct configurations/channels whose identities preserve the candidate distinction.

This is not a modification of the Formation axiom system. It is a requirement on the linguistic interpretation bridge supplied by the application.
