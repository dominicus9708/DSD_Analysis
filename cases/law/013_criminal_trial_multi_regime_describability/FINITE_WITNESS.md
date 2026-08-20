# Finite Witness — LAW-002 / Global Case 013

## Purpose

Show, with a finite toy model, that one admitted evidentiary record need not identify a unique world state and that acquittal under a proof standard need not encode a positive proof of factual innocence.

This is a structural witness, not an empirical model of a real trial.

## World states

Let

- `omega_G`: the defendant committed the charged act;
- `omega_N`: the defendant did not commit the charged act.

These are distinct elements of `Omega`.

## Evidence-source output

Assume both worlds yield the same limited source package:

`S(omega_G) = e`

`S(omega_N) = e`

where `e` contains only:

- defendant was near the scene;
- a witness gives a non-unique identification;
- no source record uniquely establishes commission of the charged act.

Thus `S` is non-injective on `{omega_G, omega_N}`.

## Prosecution and defence descriptions

Prosecution builds:

`P(e) = {proximity, identification, guilt hypothesis}`.

Defence builds:

`D(e) = {proximity conceded, identification challenged, alternative compatibility with non-guilt}`.

Neither record is identified with the world state.

## Evidence filter

Assume the relevant items are legally usable:

`R_E(P(e),D(e)) = E_adm`.

No excluded item is needed for this witness.

## Judicial record

The court therefore receives the same admitted evidentiary core in both worlds:

`J(omega_G) = J(omega_N) = j`.

The court record is consequently insufficient to invert the world map:

`j` has at least two compatible preimages.

## Decision rule

Let the supplied legal rule require proof of the charged fact without reasonable doubt.

Assume `j` does not meet that standard.

Then

`R_L(j) = NOT_GUILTY`.

This result occurs whether the inaccessible world state is `omega_G` or `omega_N`.

## Consequences

1. `NOT_GUILTY` is a legal verdict state and does not, in this model, identify a unique world state.
2. Failure to prove guilt does not construct the world proposition `omega_N`.
3. The defence need not prove `omega_N`; it is sufficient that the prosecution-side route to the guilty verdict fail the supplied proof gate.
4. The same evidentiary record can be compatible with mutually exclusive world states.
5. The witness demonstrates non-identifiability, not which world state actually occurred.

## DSD relevance

The witness supports the application-level rule that a missing or unformed later-stage state cannot be filled from another regime's absence alone.

In particular:

`not(ProsecutionProof(G))` does not imply `DefenceProof(FactualInnocence)`;

and

`not(DefenceProof(FactualInnocence))` does not imply `ProsecutionProof(G)`.

The legal system's burden allocation determines which failed route controls the verdict; DSD does not supply that allocation.