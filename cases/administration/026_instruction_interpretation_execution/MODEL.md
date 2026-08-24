# Model — ADMIN-001

## Source-sensitive instruction tuple

Use a non-universal bookkeeping tuple:

`I = (issuer, purpose, directive, constraints, recipient, authority, receipt, acknowledgement, interpretation, verification, discretion, action, feedback, outcome, regime, time)`.

The tuple is analytical bookkeeping only. A source system need not expose every coordinate.

## Core non-identities

`issuer intent != communicated wording`.

`communicated wording != recipient interpretation`.

`receipt != acknowledgement != demonstrated shared understanding`.

`instruction != authorized method/discretion boundary`.

`execution != outcome`.

`outcome != retrospective proof of instruction quality`.

## Specificity is not one scalar optimum

Reject a universal monotone model:

`more detail -> less ambiguity -> better outcome`.

A more adequate source-indexed form is:

`ExecutionPolicy = F(purpose, safety-critical coordinates, uncertainty, competence, timing, synchronization needs, discretion, feedback rules, regime)`.

Army mission command supplies a regime where purpose/end state can be highly explicit while method remains deliberately underdetermined.

FAA ATC supplies a regime where selected safety-critical coordinates require closed-loop confirmation and correction.

FEMA ICS supplies a regime where objectives, strategies, tactics, assignments, reporting lines, execution, evaluation, and revision are separated.

## Instruction graph

Represent the source relation as a graph rather than a universal chain:

`G_I = (V_I, E_R)`

Possible vertices include intent, directive, acknowledgement, clarification, interpretation, assigned task, discretionary action, feedback, revised directive, and outcome.

Edges exist only where the source regime supplies a rule/practice such as readback, backbrief, supervision, amendment, revision, or authorized initiative.

## Responsibility boundary

A failed outcome does not by itself identify which edge failed.

Possible failure locations include:

- unclear purpose;
- ambiguous or malformed directive;
- wrong recipient or authority relation;
- non-receipt;
- misleading acknowledgement;
- interpretation divergence;
- missing clarification opportunity;
- contradictory supervisory inputs;
- improper restriction of necessary discretion;
- excessive discretion where precise synchronization was required;
- execution error;
- environmental change;
- inadequate feedback/revision.

Therefore:

`bad outcome -> subordinate execution fault`

is not a valid universal inference.
