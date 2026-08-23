# Structural Model — LAW-002 / Global Case 013

## 1. Functional sorts and regimes

Let:

- `Omega` be the set of possible world/event states;
- `S_i` be information/evidence-source carriers for victim, witness, device, document, physical trace, or other source roles;
- `P` be attribution/prosecution-function records;
- `D` be defence/counterargument-function records;
- `J` be judgment-function evidentiary/fact-finding records;
- `V_J` be institutionally operative decision states.

`Omega` is not a descriptive agent. It is the reference layer against which information loss and non-identifiability can be discussed.

The symbols `P`, `D`, and `J` are now defined **functionally before jurisdictional office**:

- `P`: constructs and advances a case for specified responsibility or attribution;
- `D`: challenges formation conditions, evidence, inference, applicability, or attribution, or supplies an alternative account;
- `J`: forms the operative decision under the governing evidence/ground-use and decision rules.

A prosecutor, accused, defence counsel, judge, jury, tribunal, disciplinary committee, administrative body, or other office may instantiate one or more parts of these functions depending on the legal or institutional system. No one-to-one mapping is assumed universally.

## 2. Source observation

For each information source `i`, use a partial observation map

`O_i : Omega ⇀ S_i`.

The map may be partial and non-injective.

- partiality: not every world state produces a usable output at that source;
- non-injectivity: different world states may generate the same source output.

Therefore source description need not identify the world state.

## 3. Attribution-side and defence-side constructions

The `P` and `D` functions receive overlapping but not necessarily identical information and form different structured records:

`T_P : S* ⇀ P`

`T_D : S* ⇀ D`

where `S*` abbreviates the finite package of available source records.

No symmetry is assumed.

- `P` may seek to establish the elements required for responsibility;
- `D` may deny a link, challenge usability/reliability, challenge applicability, or provide an alternative account;
- `D` need not produce a complete factual-opposite world model merely because `P` advances a responsibility model.

The familiar criminal-trial roles of prosecution and defence are one jurisdictional implementation of these functions, not their definition.

## 4. Ground/evidence-use rule

Let

`R_E : CandidateGrounds(P,D,S*) ⇀ E_use`

be an application-level rule supplied by the governing legal or institutional regime that determines what grounds/evidence may enter the judgment process and for what purpose.

This map is not DSD Formation admission itself. It is an external rule that can be encoded using analogous staged distinctions if desired.

For the Korean criminal-procedure witness used in the original LAW-002 analysis, statutory evidence and admissibility rules supply concrete reasons for this filter to be nontrivial. Those rules are retained as a jurisdictional witness rather than generalized into the definition of `R_E`.

## 5. Judgment-function descriptive state

The judgment state is built from usable inputs, arguments, procedural records, and the governing assessment rule:

`J = Assess_J(E_use, function_records, procedural_record)`.

`J` is not identified with `Omega`.

The same judgment record may be compatible with more than one world state, and a world fact may fail to enter `J` because it was never observed, never submitted, excluded, outside the relevant purpose, or insufficiently supported.

## 6. Decision rule

Let

`R_L : J ⇀ V_J`

be the external legal/institutional decision rule.

`R_L` may include burdens, presumptions, proof thresholds, voting rules, competence rules, or other decision gates depending on the system.

For the Korean criminal-trial witness used here, the instantiated rule includes presumption-of-innocence and criminal-proof requirements. Those are external legal norms and are not included in the universal definition of `R_L`.

## 7. Overall functional pipeline

A schematic path is:

`Omega --O_i--> S* --T_P/T_D--> P,D --R_E--> E_use --Assess_J--> J --R_L--> V_J`.

This skeleton is deliberately more general than one criminal code. It represents a candidate architecture for responsibility-attribution procedures.

A concrete legal system may:

- split one function among several offices;
- combine functions in one institutional actor;
- omit a familiar office name;
- use different evidence or decision gates;
- provide additional review or appeal functions.

Such differences are test cases for the general model, not deviations to be normalized away.

## 8. Korean criminal-procedure instantiation

The original LAW-002 source notes and finite witness are retained as one concrete implementation:

- prosecutor-side conduct instantiates part of `P`;
- accused/defence-counsel conduct instantiates part of `D`;
- court fact-finding and judgment instantiate part of `J`;
- statutory evidence rules instantiate part of `R_E`;
- presumption, burden, proof threshold, and verdict rules instantiate part of `R_L`.

Victim/witness/device/document roles remain source-side or statement-side unless a particular procedural rule gives them an additional function.

This mapping is jurisdiction-specific. It is evidence that the abstract separation can be instantiated, not proof that the abstract structure is universally mandatory.

## 9. DSD correspondence

### Formation correspondence

An application may encode distinctions such as:

- candidate material;
- realized statement/submission;
- legally/institutionally usable ground;
- defined ground/evidentiary status;
- downstream fact finding;
- final judgment.

The correspondence is structural, not terminological identity.

The role coordinate `rho` in Formation channel identity is sufficient to preserve many role distinctions before any Axis-Property extension is added.

### Axis-Property correspondence

Axis-Property data become useful only if the application needs additional typed, tag-sensitive properties or relations attached to already formed role-tagged channels, e.g. a declared relation between a source statement and a specific evidentiary role.

They are not required merely to distinguish `P`, `D`, `J`, or concrete office-holders.

## 10. Central non-implications

`world truth -> legally/institutionally usable ground` is not automatic.

`source statement -> world truth` is not automatic.

`P allegation -> established responsibility` is not automatic.

`D failure to prove the opposite proposition -> established responsibility` is not automatic.

`non-responsibility verdict -> metaphysical proof of the opposite factual proposition` is not automatic.

`same judgment record -> unique world state` is not automatic.

Every arrow that an application wants to strengthen requires an explicit legal, evidentiary, institutional, or semantic bridge.

## 11. Generalization status

This model is a **universal candidate under active falsification**.

The Korean criminal-procedure materials remain a strong jurisdictional witness, but cross-jurisdictional corroboration and counterexamples are required before stronger universality claims are made.
