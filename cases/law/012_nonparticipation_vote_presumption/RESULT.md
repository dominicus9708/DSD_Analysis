# Result — LAW-001 / Global Case 012

## 1. Meeting nonattendance and opposition

Let `M` be the set of persons eligible to participate in a meeting and let

`vote : M ⇀ {YES, NO}`

be the partial vote assignment for the motion under consideration.

For a member `x`, the following states are structurally different:

1. `x` is absent and no vote is formed;
2. `x` is present but abstains;
3. `vote(x)=NO`;
4. `vote(x)=YES`.

The first two states both fail to supply a NO vote, but they are not identical because presence may matter to quorum or to rules based on members present. The third state is a defined negative vote.

Therefore

`x ∉ dom(vote)` does not imply `vote(x)=NO`.

Any rule that automatically fills every non-vote with `NO` is an additional totalization rule. It is not recoverable from the original partial vote record.

Under ordinary Robert's Rules majority/two-thirds rules based on votes cast, abstention is not a vote. This independently supports the structural separation between a member's possible private attitude and a formed institutional vote.

### DSD correspondence
A private attitude or mere eligibility is not an admitted operational vote channel merely because the person exists in the candidate population. A domain-specific interpretation may model actual participation, valid vote formation, vote-value assignment, and downstream tally as distinct stages.

**Judgment: structural correspondence.**

## 2. Voting right not exercised versus invalid ballot

Let `E` be the eligible electorate and

`ballot : E ⇀ B`

be the partial map that exists only for electors who actually submit a ballot in the modeled voting regime. Let `Valid : B → {true,false}` be the regime's validity predicate.

Then

- non-exercise: `x ∉ dom(ballot)`;
- submitted invalid ballot: `x ∈ dom(ballot)` and `Valid(ballot(x)) = false`;
- submitted valid ballot: `x ∈ dom(ballot)` and `Valid(ballot(x)) = true`.

Thus

`x ∉ dom(ballot)`

and

`x ∈ dom(ballot) ∧ ¬Valid(ballot(x))`

are disjoint states. Treating non-exercise as an invalid ballot creates an event that did not occur.

Robert's Rules supplies a concrete parliamentary example in which abstention-like ballots and illegal votes are treated differently. The exact classification is regime-specific, so DSD must preserve the status distinction without pretending to choose the legal category in advance.

### DSD correspondence
This is the cleanest correspondence with the Formation system's separation between absence/out-of-domain status, defined assignment, and downstream channel formation. A submitted-but-invalid object may be represented as a candidate or realized object that fails a later admissibility condition; a never-submitted ballot is not the same object with a special value.

**Judgment: strong structural correspondence, regime-dependent encoding.**

## 3. Presumption of innocence

The legal rule is asymmetric. A criminal charge does not itself constitute a guilty judgment, and the burden of establishing guilt lies with the prosecution under the cited international standard.

A minimal staged legal representation is:

`accusation → admissible evidence → fact finding → proof threshold → guilty judgment`

The DSD-relevant point is that the existence of an earlier-stage candidate condition does not itself create a later-stage admitted result.

If `Proved_Guilt(x)` is the legal predicate indicating that the prosecution has satisfied the applicable proof standard, then the legal regime imposes a gate of the form

`Guilty_Judgment(x) ⇒ Proved_Guilt(x)`.

Equivalently, while the proof condition is unsatisfied, the system must not promote the accused into the legal guilty state.

However, two distinctions must be retained:

1. failure to prove guilt is not a DSD proof of the factual proposition `Innocent(x)`;
2. the choice to place the burden on the prosecution, use the beyond-reasonable-doubt standard, and accord the benefit of doubt is supplied by law, not derived from the Formation axioms.

The Republic of Korea Constitution Article 27(4) provides a domestic instance of the same legal-status asymmetry.

### DSD correspondence
DSD provides a useful staged explanation of why accusation, suspicion, evidence, proof, and guilty judgment must not be collapsed. It does not independently derive the normative burden of proof.

**Judgment: conditional structural correspondence; no derivation of the legal norm from DSD.**

## 4. Common structural result

The three cases share a common form:

`eligibility / candidacy / accusation`

is not identical to

`realized act / valid institutional input / proved condition`,

which is not identical to

`downstream tally / legal judgment`.

A generic partial-state formulation is:

`x ∉ dom(f)  ≠  (x ∈ dom(f) and f(x)=0)  ≠  (x ∈ dom(f) and f(x)=v)`.

The institutional meaning of these states differs by regime, but collapsing them requires an additional completion rule. Such a rule may be legitimate if explicitly adopted; it is not logically forced by absence itself.

## 5. What this analysis supports

1. DSD's staged and partial distinctions have a genuine external analogue in parliamentary procedure and criminal procedure.
2. The distinction is operational rather than merely terminological: collapsing nonparticipation into a vote or accusation into guilt changes institutional outcomes or burden allocation.
3. The analysis supports the DSD Analysis principle of predefinition restraint: an unformed or unproved state must not be assigned a later-stage value merely because a decision system would find that convenient.
4. The result is corroborative, not a proof that the DSD axioms are uniquely correct. Existing institutional theories can state the same distinctions in their own vocabulary.

## 6. Boundary / attempted counterpressure

The strongest limitation found is that some institutional regimes explicitly define nonaction to have an outcome effect. For example, a threshold based on the entire membership can make abstention operationally disadvantage one side. This does not turn abstention into a NO vote; it shows that downstream effect and input identity are separate.

Likewise, legal systems may use rebuttable presumptions or limited burden shifts. These are explicit regime rules and therefore do not refute the DSD distinction; they demonstrate that a later-stage default can be added only by specifying the rule that creates it.

## Final judgment

**No contradiction with the Formation Axiom System was found.**

**External corroboration was found for the distinction between nonformation/nonparticipation, formed-but-invalid or abstaining states, defined choices, and downstream institutional results.**

**The presumption of innocence supplies a stronger normative example, but its burden-of-proof asymmetry is external legal data and must not be advertised as a theorem of DSD.**
