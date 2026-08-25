# PHIL-002 Reproducibility Record

Status: **textual / logical reproduction; no Python created**.

Reason: the case is an attribution-level argument audit. A numerical or toy Python script would not add evidential value and could create a misleading impression of computational verification.

## Required sources

1. John R. Searle, “Minds, Brains, and Programs,” Behavioral and Brain Sciences 3 (1980), 417–457.
   - scan: https://home.csulb.edu/~cwallis/382/readings/482/searle.minds.brains.programs.bbs.1980.pdf
2. Stanford Encyclopedia of Philosophy, “The Chinese Room Argument,” current revision.
   - https://plato.stanford.edu/entries/chinese-room/
3. B. Jack Copeland, “The Chinese Room from a Logical Point of View,” in Views into the Chinese Room, Oxford University Press, 2002.
   - https://academic.oup.com/book/49991/chapter/422643552
4. Current DSD Formation Axiom System.
5. Current DSD Axis-Property Axiom System.

## Reproduction procedure

1. Read the original operator setup and record only what is explicitly established about the operator.
2. Introduce separate bearer labels:
   - operator `o`;
   - program/rules `r`;
   - memory/store `m`;
   - I/O organization `io`;
   - implemented system `S`.
3. Record Searle’s operator-level premise:
   - `not U(o)`.
4. Test whether pure logic yields:
   - `not U(S)`;
   - `not exists x [RealizedBy(x,S) and U(x)]`.
5. Verify from the 1980 paper that Searle explicitly presents the Systems Reply.
6. Reconstruct the Systems Reply without strengthening it:
   - concede `not U(o)`;
   - deny that this determines `U(S)`.
7. Reconstruct Searle’s internalization response:
   - rules, memory, and calculation are internalized;
   - host still reports no Chinese understanding.
8. Distinguish containment/implementation from bearer identity:
   - `HostedIn(S_int,h)` does not by itself imply `h = S_int` for every property-attribution purpose.
9. Verify from SEP that later Systems/Virtual-Mind replies explicitly distinguish implementer, whole system, and potentially realized virtual agent.
10. Separate the part/whole objection from Searle’s stronger syntax/semantics thesis.
11. Apply the PLAN falsification conditions before assigning the final verdict.
12. Classify the result as historical convergence if the DSD objection matches the established Systems/Virtual-Mind family.

## Expected logical judgments

```text
OPERATOR_NONUNDERSTANDING_ESTABLISHED: YES
OPERATOR_TO_SYSTEM_NONUNDERSTANDING_BY_LOGIC: NO
SYSTEMS_REPLY_ALREADY_PRESENT_IN_1980: YES
SEARLE_INTERNALIZATION_ADDRESSES_SYSTEMS_REPLY: YES
INTERNALIZATION_PROVES_BEARER_IDENTITY: NO
PART_WHOLE_ATTACK_SURVIVES_AS_BURDEN_SHIFT: YES
SYSTEMS_REPLY_PROVES_SYSTEM_UNDERSTANDS: NO
SEARLE_STRONGER_SYNTAX_SEMANTICS_THESIS_REFUTED_BY_DSD: NO
HISTORICAL_CONVERGENCE_WITH_SYSTEMS_VIRTUAL_MIND_FAMILY: YES
NOVEL_DSD_OBJECTION: NO
WHOLESALE_REFUTATION_OF_SEARLE: NO
```

## DSD comparison boundaries

The following are methodological analogies only:

- role-tag preservation;
- bearer-specific property assignment;
- non-identity of reduced behavior and complete structural identity.

Do not identify:

- DSD channel roles with cognitive roles;
- axis-property records with intentional states;
- structural equivalence with semantic equivalence;
- DSD describability with understanding or consciousness.

## Robustness conditions

The DSD part/whole criticism must be narrowed if an independent theory establishes that:

1. the only legitimate bearer of understanding in the setup is exactly the conscious host/operator; or
2. a formal computational organization cannot instantiate a distinct semantic/cognitive bearer for reasons independent of the operator’s introspective ignorance.

Conversely, merely showing that the operator does not understand is insufficient to discharge either condition.