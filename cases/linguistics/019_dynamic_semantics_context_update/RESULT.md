# LING-006 / Global Case 019 — Result

## Question
Can discourse meaning and anaphoric accessibility be represented faithfully by one static semantic value, or must the current information state and ordered update history be preserved?

## External result
Dynamic semantics and DRT provide an independent structural node:

- discourse interpretation is state-sensitive;
- an utterance can alter the context in which later utterances are interpreted;
- discourse referents introduced earlier can become available for later anaphora;
- reversing discourse order can destroy the same anaphoric reading;
- therefore update composition need not commute.

A minimal witness is:

`A woman walked in. She sat down.`

versus

`She sat down. A woman walked in.`

on the intended co-referential reading.

## Strongest structural statement

Availability of a later interpretation depends on the input discourse state:

Interpret(u, C0) != Interpret(u, C1)

can hold for the same surface utterance u.

More strongly, for suitable updates U1, U2,

(U2 ∘ U1)(C0)

may be defined while

(U1 ∘ U2)(C0)

is not defined on the same reading.

Thus later information does not retroactively prove that an earlier interpretation was available.

## Relation to predefinition restraint
The relevant restraint is not merely `undefined != false`. It is:

> A later context state cannot be used to preassign to an earlier utterance an interpretation whose prerequisites were unavailable in the earlier state.

This is a temporally/order-indexed version of predefinition restraint.

## DSD mapping
The Formation Axiom System is explicitly static. Therefore the cleanest mapping is snapshot-based:

L0 --B_u1--> L1 --B_u2--> L2

where each Li is a separately evaluated static descriptive snapshot and each B_ui is an external linguistic update bridge.

Formation may encode the staged status of material inside each snapshot, but it does not derive discourse update rules, discourse referents, anaphoric accessibility, or the bridge B_u.

## Why Structural Reorganization Dynamics is not automatically the right layer
The DSD dynamics paper concerns time-indexed component-resolved structural evolution, constitutive operator bridges, propagation, relaxation, lineage, and typed state/domain transitions. Its core regular dynamics fixes a Stage-VI formation background; formation assignment or channel changes require explicit cross-time lineage.

Linguistic dynamic semantics instead models ordered interpretation/information update. Therefore:

linguistic dynamic update != DSD Structural Reorganization Dynamics

unless an explicit cross-domain interpretation is supplied.

Using the dynamics paper automatically would overstate the correspondence and import physical/analytic structure not supplied by linguistics.

## Secondary correspondence: reduced output versus update structure
Dynamic semantics provides cases in which static truth-conditional equivalence does not guarantee identical discourse behavior or anaphoric potential. This is structurally consonant with DSD's broader warning that reduced/static output equality need not reconstruct complete underlying structure, but the two results arise in different theories and are not identified.

## Axis-Property
Not needed for the core result. Role-sensitive discourse or institutional speech acts may require it later.

## Verdict
- Formation contradiction: **not found**.
- Structural reinterpretation: **established after explicit snapshot/update encoding**.
- Coherence: **confirmed within scope**.
- Predefinition restraint: **independently corroborated in an order-indexed form**.
- DSD dynamics required: **no**.
- New DSD dynamic-semantics theory: **not claimed**.
- New application boundary: **confirmed — distinguish static formation snapshots from external context-update maps, and do not retroactively apply later context to earlier interpretation states.**