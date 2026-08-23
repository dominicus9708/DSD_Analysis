# LAW-004 Finite Witnesses

These are source-faithful finite state constructions, not legal advice and not claims that DSD derives the legal rules.

## Witness A — exists but not offered

Evidence item `e1` exists in the world and is held by a party.

State:

- exists = yes
- offered/submitted = no
- investigated = no
- legal-use status in the proceeding = not reached
- probative evaluation = not reached
- finding contribution = none

Purpose: distinguish existence from procedural participation.

Failure condition: a model that automatically turns every existing item into submitted evidence.

## Witness B — offered but excluded in criminal procedure

Evidence item `e2` is offered by a party but falls under a source-law exclusion rule, such as an item barred by Article 308-2 or a hearsay item not satisfying the statutory route for use.

State:

- exists = yes
- offered = yes
- legal-use/admissibility = no
- probative-force evaluation for substantive proof = not reached
- ultimate fact = cannot be established from `e2` as usable evidence

Purpose: distinguish submission from admissibility/use.

Failure condition: encoding `submitted = admissible`.

## Witness C — admissible but weak

Evidence item `e3` is legally usable but only weakly supports proposition `P`.

State:

- exists = yes
- offered = yes
- usable = yes
- probative force = insufficient alone
- proposition `P` = not established under the governing standard

Purpose: distinguish admissibility from probative force and final finding.

Failure condition: encoding every usable item as a positive final fact value.

## Witness D — same broad defect, different civil result

Use the structure highlighted by Supreme Court 2024Da222212.

Two submitted civil items are both associated with unlawful collection conduct.

`e4a`: secretly recorded non-public conversation covered by a special statutory prohibition on evidentiary use.

`e4b`: photographed digital material collected through conduct violating a statute that, in the analyzed setting, did not itself contain a separate evidentiary-exclusion rule.

State table:

| Item | Broad collection defect | Special exclusion rule | Civil admissibility result |
|---|---|---|---|
| e4a | yes | yes | excluded |
| e4b | yes | no | not automatically excluded; case-specific balancing permits use in the cited case |

Purpose: show that `unlawfully collected` is not a sufficient total function to one universal admissibility value.

Failure condition: any mapping that predefines

`unlawful_collection -> inadmissible`

without retaining the governing statute/procedural regime.

## Witness E — evidence application declined as unnecessary in civil procedure

A party applies for evidence `e5`, but the court determines under Civil Procedure Act Article 290 that the evidence need not be investigated, subject to the statutory proviso.

State:

- exists = yes
- application = yes
- investigation = no
- probative evaluation from investigation = not formed

Purpose: distinguish application from investigation even without using the criminal admissibility concept.

## Minimal DSD comparison record

For each witness use a distinct typed evidence-use instance

`a_i = (item, proposition, proceeding, purpose)`.

Do not encode the physical item alone as the complete Formation material carrier when one item appears in multiple proceedings or legal roles.

The witness passes the DSD compatibility test if the application can preserve each source-side status without replacing undefined/not-reached states by zero, admissible, inadmissible, or proved values.
