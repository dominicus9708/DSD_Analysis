# LAW-004 Result — Evidence Submission, Admissibility, Probative Weight, and Finding

Status: first-pass analysis complete.

Primary purpose: reinterpretation.

Secondary purposes: coherence, predefinition audit, regime-boundary analysis.

## 1. Answer-first result

No direct contradiction was found between the selected Korean criminal/civil evidence structures and the DSD Formation distinctions after the evidence-use instance, proposition, procedural regime, legal stage, and status were typed separately.

The source law independently requires a stronger separation than a one-dimensional `evidence value` model can preserve:

`existence/collection`

`!= submission/application`

`!= investigation/legal usability`

`!= probative evaluation`

`!= final factual finding`.

A second result is equally important:

`same broad defect label != same legal-use result across regimes`.

The 2026 Supreme Court civil-evidence decision shows that even the label `unlawfully collected` does not by itself determine one admissibility output without the governing statute and procedural regime.

## 2. Source-law findings

### 2.1 Submission is a distinct procedural event

Criminal Procedure Act Article 294 gives the prosecutor, accused, and defense counsel a route to submit documentary/physical evidence or apply for examination of persons. This is a procedural act, not an automatic admissibility or fact-finding rule.

Civil Procedure Act Article 289 likewise regulates evidence applications, while Article 290 permits the court in specified circumstances not to investigate an applied-for item.

Therefore:

`exists -> submitted/applied`

is not an identity, and

`submitted/applied -> investigated/used`

is not an identity.

### 2.2 Admissibility/legal use and probative force are separate

Criminal Procedure Act Article 308-2 excludes illegally collected evidence from evidentiary use, while Article 310-2 and related provisions condition the use of hearsay and documentary statements.

Separately, Article 308 assigns probative force to judicial evaluation, and Article 307 requires the ultimate criminal fact to reach proof beyond reasonable doubt.

Thus an item can be:

- submitted but unusable;
- usable but weak;
- one of several usable items that still fail to establish the ultimate fact.

### 2.3 Civil evidence has a different admissibility architecture

Civil Procedure Act Article 202 adopts free evaluation based on the whole purport of pleadings and results of evidence investigation.

Supreme Court 2024Da222212 (2026-04-30) adds a decisive regime boundary. The Court explained that civil procedure, unlike criminal procedure, does not have a general statutory exclusion rule for unlawfully collected evidence. Where a special statute expressly bars evidentiary use, the item is inadmissible; otherwise unlawful collection does not automatically decide admissibility and the court weighs specified interests and circumstances.

In the cited case, one secretly recorded category was excluded by the Protection of Communications Secrets Act, while another unlawfully obtained digital category was not automatically excluded and was accepted after balancing.

Therefore the source law rejects the total function:

`unlawfully_collected -> inadmissible`.

The governing rule must be retained.

## 3. DSD Formation comparison

### 3.1 Typed evidence-use instances are required

The same physical file may be offered:

- in different proceedings;
- for different propositions;
- by different parties;
- under different evidentiary purposes or rules.

Using only the physical item as the application carrier can create artificial contradictory assignments.

The faithful application carrier is instead a typed evidence-use instance such as

`(item, proposition, proceeding, purpose, source_status)`.

This is analogous to the LAW-003 type-audit result: the underlying object remains common provenance, while legally operative uses are typed separately.

### 3.2 Partiality prevents premature legal values

Before an evidence item is offered, investigated, or ruled on, later legal statuses may simply not yet be formed.

The Formation system's partial-assignment and status distinctions are compatible with preserving those not-yet-reached states rather than silently filling them with:

- admissible;
- inadmissible;
- zero weight;
- proved;
- disproved.

Judgment: **strong structural correspondence to non-totalization discipline**.

### 3.3 Inadmissibility is not evidence nonexistence

This is the most important encoding boundary.

A recording can exist, be collected, be submitted, and still be legally unusable for substantive proof. Therefore source-side inadmissibility must not be represented by deleting the evidence-use record or pretending the source item never existed.

Judgment: **direct structural compatibility with absence/defined-status separation after explicit application encoding**.

### 3.4 Regime-specific admissibility is compatible

The 2026 Supreme Court civil case might appear to conflict with a universal staged admission model if one assumes that the collection defect itself must determine the later status.

That assumption is external to DSD.

Once the application retains:

- collection status;
- governing special statute;
- criminal/civil regime;
- admissibility/use rule;
- downstream result;

the apparent conflict disappears.

Judgment: **apparent conflict resolved by rule/regime separation**.

## 4. Static Aggregation audit

The phrase `증명력 / probative weight` does not justify mapping legal evaluation directly to the analytic weight field of Channel-Indexed Static Aggregation.

The legal statutes do not give every evidence item a universal scalar coefficient that is linearly summed. Criminal Article 308 and Civil Article 202 specify judicial evaluation under legal standards, not a Banach-space aggregation rule.

The DSD static paper itself states that later coefficients or normalized weighted statistics are separately supplied postprocessing operators and are not automatically the core Formation composition.

Therefore:

`legal probative weight != analytic weight w_c`

and

`judicial factual finding != DSD finite sum`

without an additional application-specific formalization.

This is a useful negative result: DSD can preserve evidence states without pretending that legal proof is already a numerical aggregation theory.

## 5. Aggregate/finding non-reconstruction

Different evidence structures can lead to the same final factual finding, and the same submitted set can be evaluated differently under different legal rules or purposes.

Formation Section 6.5 and the Static Aggregation record-retention results provide a compatible structural warning: downstream equality is weaker than equality of the complete typed support structure.

The legal conclusion is source-side; DSD merely offers a matching non-reconstruction discipline.

## 6. Axis-Property and Dynamics audit

Axis-Property is not required. The legal sources do not provide a realized-axis interpretation.

Dynamics is not required for the first-pass status comparison. If a later study models procedural time — new evidence, exclusion rulings, reopening, appeal, or changed admissibility status — that would require an explicit transition layer rather than retroactively altering one static descriptor.

## 7. Direct contradiction audit summary

No direct contradiction remained after type, proposition, proceeding, source rule, and stage alignment.

Rejected apparent contradictions:

1. `existing evidence must already have legal-use status`;
2. `submitted evidence must be admissible`;
3. `inadmissible evidence must be structurally absent`;
4. `same collection defect must yield the same result`;
5. `admissible evidence must be sufficiently probative`;
6. `legal probative weight must equal DSD analytic weight`;
7. `same final finding implies same evidence structure`.

## 8. Relation to LAW-001 through LAW-003

LAW-001: nonparticipation/invalid input/downstream result were not collapsed.

LAW-002: one legal regime's descriptive gap could not be filled by another regime's desired positive result.

LAW-003: one person/relationship did not automatically generate every role-specific authority or legal effect.

LAW-004 adds a new independent node:

**one evidence item's existence or submission does not automatically generate legal usability, probative sufficiency, or factual conclusion; and even a common defect label does not determine a universal downstream status without the governing rule/regime.**

The recurring DSD-compatible form is now more general:

`source state`

`!= rule-conditioned applicability`

`!= formed downstream status`

unless a rule explicitly performs that promotion.

## 9. Predefinition relevance

LAW-004 strengthens the predefinition result in two directions.

Do not predefine:

`submitted -> admissible`.

Do not predefine:

`admissible -> proved`.

And do not predefine:

`unlawfully collected -> universally inadmissible`.

The correct structural rule is:

**retain the source status, governing regime, and transition rule separately; promote one status into another only through the rule that actually licenses that promotion.**

## 10. Final classification

- Source discipline preserved: **yes**.
- Formation mapping meaningful: **yes, with typed evidence-use instances**.
- Formation direct contradiction found: **no**.
- Static Aggregation required: **no**.
- Static Aggregation boundary result: **yes; legal probative force is not automatically an analytic weight or sum**.
- Axis-Property required: **no**.
- Dynamics required: **no for first-pass static analysis**.
- Main result class: **external coherence node + structural reinterpretation**.
- Secondary result: **predefinition/non-totalization and regime-sensitivity support**.

## 11. Boundary statement

LAW-004 does not prove evidence law from DSD, does not make Formation admission identical to legal admissibility, does not assign numerical DSD weights to evidence, and does not claim that judicial fact-finding is a DSD aggregation operator.

It establishes only that the selected source-law distinctions can be represented jointly with the relevant DSD distinctions without direct contradiction under an explicit typed application bridge, while several tempting collapsed mappings are rejected.
