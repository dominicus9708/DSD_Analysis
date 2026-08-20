# Finite Witness — LING-006 / Global Case 019

## Purpose
Exhibit a minimal order-sensitive discourse update in which the same pronoun expression has different interpretation availability depending on the prior context.

## State space
Let a discourse state be a pair

C = (R, K)

where `R` is a finite set of discourse-referent tags and `K` is a finite set of conditions on those tags.

Initial state:

C0 = (∅, ∅).

## Utterance u1
`A woman walked in.`

Define the update U1 on C0 by introducing one discourse referent x:

U1(C0) = C1

with

R1 = {x}

and

K1 = {Woman(x), WalkedIn(x)}.

## Utterance u2
`She sat down.`

For the intended anaphoric reading, define U2 only on discourse states containing an accessible compatible discourse referent. On C1, x is available, so

U2(C1) = C2

with

R2 = {x}

and

K2 = {Woman(x), WalkedIn(x), SatDown(x)}.

On the empty initial state C0, the intended co-referential update is unavailable:

U2(C0) is undefined / fails for that reading.

## Order result
Therefore

(U2 ∘ U1)(C0) = C2

while

(U1 ∘ U2)(C0)

is not defined on the same anaphoric interpretation.

Hence update composition is not generally commutative.

## No retroactive repair
The later arrival of u1 does not show that the earlier occurrence of u2 already had x available. A later context can support a later interpretation; it does not retroactively alter the earlier input context.

## DSD use
A faithful DSD application may encode C0, C1, C2 as separate static snapshot structures L0, L1, L2 and use external utterance bridges

B_u1 : L0 -> L1,
B_u2 : L1 -> L2.

The Formation Axiom System may validate the structure inside each Li, but it does not derive B_u1 or B_u2. Treating the update sequence as one unchanged Formation model would erase the change of available discourse structure.