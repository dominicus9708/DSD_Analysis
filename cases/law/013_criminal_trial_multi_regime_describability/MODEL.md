# Structural Model — LAW-002 / Global Case 013

## 1. Sorts and regimes

Let:

- `Omega` be the set of possible world/event states;
- `S_i` be evidence-source carriers for victim, witness, device, document, or physical trace;
- `P` be prosecution-side descriptive records;
- `D` be defence-side descriptive records;
- `J` be judicially available evidentiary/fact-finding records;
- `V_J` be legal verdict states.

`Omega` is not a descriptive agent. It is the reference layer against which information loss and non-identifiability can be discussed.

## 2. Source observation

For each evidence source `i`, use a partial observation map

`O_i : Omega ⇀ S_i`.

The map may be partial and non-injective.

- partiality: not every world state produces a usable output at that source;
- non-injectivity: different world states may generate the same source output.

Therefore source description need not identify the world state.

## 3. Party-side constructions

The prosecution and defence receive overlapping but not necessarily identical information and form different structured records:

`T_P : S* ⇀ P`

`T_D : S* ⇀ D`

where `S*` abbreviates the finite package of available source records.

No symmetry is assumed.

- prosecution may seek to establish the charged elements;
- defence may deny a link, challenge admissibility/reliability, or provide an alternative account;
- defence need not produce a complete factual-innocence world model merely because prosecution advances a guilt model.

## 4. Evidence rule

Let

`R_E : CandidateEvidence(P,D,S*) ⇀ E_adm`

be an application-level evidentiary filter supplied by the legal regime.

This map is not DSD Formation admission itself. It is a legal map that can be encoded using analogous staged distinctions if desired.

Korean criminal procedure supplies concrete reasons for the filter to be nontrivial: facts must be based on evidence, illegally collected evidence is excluded, some confessions cannot be used for guilt, and evidence applications are decided by the court.

## 5. Judicial descriptive state

The court's evidentiary state is built from legally usable inputs and the court's assessment:

`J = Assess_J(E_adm, party_arguments, procedural_record)`.

`J` is not identified with `Omega`.

The same judicial record may be compatible with more than one world state, and a world fact may fail to enter `J` because it was never observed, never submitted, excluded, or insufficiently supported.

## 6. Decision rule

Let

`R_L : J ⇀ V_J`

be the legal decision rule.

For the Korean criminal-trial instantiation used here, the rule includes at least:

- presumption of innocence;
- requirement that crime facts be proved without reasonable doubt;
- judicial evaluation of probative value.

The international presumption-of-innocence standard additionally places the burden of proving the charge on the prosecution.

These are external legal norms.

## 7. Overall pipeline

A schematic path is:

`Omega --O_i--> S* --T_P/T_D--> P,D --R_E--> E_adm --Assess_J--> J --R_L--> V_J`

with the victim occupying one or more source/statement roles rather than being collapsed into the prosecution.

## 8. DSD correspondence

### Formation correspondence

An application may encode distinctions such as:

- candidate material;
- realized statement/submission;
- legally usable evidence;
- defined evidentiary status;
- downstream fact finding;
- final judgment.

The correspondence is structural, not terminological identity.

The role coordinate `rho` in Formation channel identity is sufficient to preserve many role distinctions before any Axis-Property extension is added.

### Axis-Property correspondence

Axis-Property data become useful only if the application needs additional typed, tag-sensitive properties or relations attached to already formed role-tagged channels, e.g. a declared relation between a source statement and a specific evidentiary role.

They are not required merely to say `prosecutor != defendant != victim`.

## 9. Central non-implications

`world truth -> legally admitted evidence` is not automatic.

`victim statement -> world truth` is not automatic.

`prosecution allegation -> proved guilt` is not automatic.

`defence failure to prove innocence -> proved guilt` is not automatic.

`legal acquittal -> metaphysical proof of factual innocence` is not automatic.

`same court record -> unique world state` is not automatic.

Every arrow that an application wants to strengthen requires an explicit legal, evidentiary, or semantic bridge.