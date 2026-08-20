# Result — LAW-002 / Global Case 013

## 1. Main finding

A criminal trial is better modeled as a multi-regime descriptive system than as one shared description of one event.

The minimal useful decomposition is:

`W + S + P + D + J + R_E + R_L`

where:

- `W` is the world/event reference layer;
- `S` is the evidence-source layer, including victim/witness/physical trace roles;
- `P` is the prosecution descriptive regime;
- `D` is the defence descriptive regime;
- `J` is the judicial descriptive regime;
- `R_E` is the evidentiary-use/admissibility rule;
- `R_L` is the legal decision rule.

The important correction is that these components are not symmetric.

## 2. The world is not a describer

The actual event layer must not be treated as just another observer with complete information.

If `omega in Omega` is a world state, evidence sources receive only partial outputs `O_i(omega)`.

Therefore the model distinguishes:

`what occurred`

from

`what any source recorded`

from

`what a party can formulate`

from

`what the court may legally use`

from

`what the court finally finds or decides`.

This prevents an external analyst's knowledge of the toy world's ground truth from being silently inserted into the internal trial record.

## 3. Victim/source is not prosecution

The victim may supply testimony and, under Korean law, has a statutory opportunity to make statements in trial, but the victim is not simply the prosecution's descriptive regime.

Korean criminal procedure separately gives prosecutor, defendant, and defence counsel evidence-application powers, while Article 294-2 separately structures the victim's statement right.

Therefore:

`victim experience/statement != prosecution claim != admitted evidence != judicial fact finding`.

This is a genuine role separation, not merely a vocabulary choice.

## 4. Prosecution and defence are asymmetric

The prosecution's relevant route is constructive:

`charge -> evidence -> legally usable evidence -> proof of elements -> guilty judgment request`.

The defence can operate in several non-equivalent ways:

- dispute that a source record is reliable;
- dispute that a record is legally usable;
- dispute a link in the prosecution's inference;
- introduce exculpatory material;
- present an alternative compatible account;
- simply show that the prosecution has not satisfied the legal proof gate.

The defence therefore need not create a complete factual-innocence world description in order for the prosecution's guilt route to fail.

The two crucial non-implications are:

`not(Proved_P(Guilt))` does not imply `Proved_D(FactualInnocence)`;

`not(Proved_D(FactualInnocence))` does not imply `Proved_P(Guilt)`.

The legal burden rule decides the consequence of this asymmetry. DSD alone does not.

## 5. Evidence rules are a real formation boundary

Korean Criminal Procedure Act Article 307 requires fact finding by evidence and proof of crime facts to the degree of no reasonable doubt. Article 308-2 excludes illegally collected evidence; Articles 309-310 constrain use of confessions; Articles 294-295 distinguish evidence application from the court's decision on the application.

This independently demonstrates that:

`source material -> judicially usable evidence`

is not an identity map.

Some source material can exist in the world or in an investigative/party record without becoming usable evidence at trial.

This is strongly analogous to staged formation, but legal admissibility is not literally Formation admission. It is an application-supplied rule `R_E`.

## 6. Judicial description is not the world state

The finite witness gives two distinct states:

`omega_G != omega_N`

but the same admitted judicial record:

`J(omega_G) = J(omega_N) = j`.

Therefore the court-record map is non-injective on this finite fragment.

Consequently:

- legal evidence can underdetermine the world state;
- a verdict need not reconstruct the actual event uniquely;
- an acquittal under the proof rule can be compatible with both factual guilt and factual innocence in the inaccessible world layer.

This does not undermine the verdict. It distinguishes legal judgment from omniscient world reconstruction.

## 7. Presumption of innocence becomes a cross-regime non-totalization rule

The earlier LAW-001 result can now be sharpened.

It is not merely:

`charge != guilt`.

The stronger multi-regime statement is:

**A gap in the defence regime cannot be totalized into a positive prosecution result, and a gap in the prosecution regime cannot be totalized into a positive factual-innocence result.**

Which gap controls the legal verdict is supplied by the legal system's burden and proof rules.

Under the cited presumption-of-innocence rule, failure of the prosecution to form the legally required guilt proof blocks the guilty verdict; the defendant's failure to construct an affirmative innocence proof does not repair that missing prosecution proof.

This is the strongest DSD-relevant result of the case.

## 8. Formation Axiom System correspondence

The Formation source supports the following distinctions:

- staged formation;
- partial assignment;
- role retained in channel identity;
- undefined / defined-zero / absent-channel separation;
- richer structural comparison than aggregate equality.

These provide a coherent structural language for the legal application.

However, the core Formation system does not supply:

- a theory of testimony;
- evidentiary reliability;
- a burden of proof;
- cross-agent information transfer;
- legal admissibility;
- a criminal proof threshold.

All of those remain application-level bridges or rules.

**Judgment: strong structural correspondence after explicit legal encoding; no conflict found.**

## 9. Axis-Property System correspondence

The initial expectation that prosecutor/defendant/victim separation would require the Axis-Property System was too strong.

Formation channels already retain a role coordinate `rho`, so basic legal-role separation can be represented before Axis-Property extension.

Axis-Property machinery becomes useful only if the application needs additional tag-sensitive typed properties or relations over already formed channels, such as a specific declared relation between a statement-channel, source role, and evidentiary-use role.

**Judgment: optional extension, not required for the core 5+2 result.**

## 10. Counterpressure / limitations

1. A legal system may adopt presumptions or burden shifts. Such rules are additional `R_L` structure; they do not make the underlying descriptive states identical.
2. Some evidence can be excluded despite being factually accurate. This confirms that legal usability and world truth differ, but DSD does not tell the court what evidence rule to adopt.
3. A victim can also be a witness or occupy multiple procedural roles. The model must preserve role tags rather than forcing one person into exactly one global category.
4. Police/investigators are omitted from the minimal model. They can be inserted as an additional regime between source records and prosecution if later analysis requires investigative procedure.
5. `NOT_GUILTY` is a legal verdict state. This analysis does not define it as metaphysical proof of innocence.

## 11. Final judgment

- **No contradiction with the current Formation or Axis-Property systems was found.**
- **The legal domain provides an external corroborative case for staged formation, role preservation, and refusal to fill one regime's missing state with another regime's desired positive value.**
- **The 5+2 decomposition is materially stronger than LAW-001 because it identifies information loss and non-identifiability between the world, evidence sources, parties, and court.**
- **The strongest new boundary is equally important: DSD does not itself provide cross-regime transfer, evidentiary admissibility, burden allocation, or legal decision standards.**

Overall classification: `structural reinterpretation = supported`, `coherence = supported`, `predefinition restraint = independently corroborated`, `DSD derivation of legal norms = not supported`.