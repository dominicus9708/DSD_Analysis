# LAW-009 Model — Irreversibility, Uncertainty, and Safeguards

## 1. Rejected universal scalar model

Do not start with a universal scalar function

`I : LegalConsequence -> R`

and a monotone theorem

`I(c1) > I(c2) -> Safeguards(c1) > Safeguards(c2)`.

The source materials do not supply one cross-system scalar order of irreversibility or one common safeguard-strength scale.

## 2. Typed legal transition

Let a source-side legal transition instance be

`tau = (subject, protected_interest, state_before, proposed_act, state_after, time, regime, reviewing_body)`.

Retain separately:

- `Finality(tau)` — whether ordinary merits/review stages are complete;
- `FactStatus(tau)` — unresolved/established source-side factual status;
- `ReviewStatus(tau)` — appeal, reconsideration, clemency or other source review state;
- `Risk(tau)` — source-recognized risk predicate;
- `Irrep(tau)` — source-recognized irreparable/irreversible consequence predicate;
- `Urgent(tau)` — source-recognized urgency/imminence predicate;
- `Safeguard_k(tau)` — each distinct safeguard actually supplied by the source.

These are not one scalar.

## 3. Three irreversibility notions

The analysis distinguishes at least three application-level notions.

### Historical irreversibility

Once an event occurs, its occurrence cannot be made not to have occurred.

`Occurred(e,t) -> historical_record(e)`

This does not mean all consequences are non-restorable.

### Restorative irreversibility

A prior protected state cannot later be adequately restored, replaced, or compensated under the source's relevant criterion.

Represent only after the application supplies a restoration/equivalence relation:

`Restorable_R(s_after,s_before)?`

Do not derive `R` from DSD.

### Adjudicative irreversibility

A threatened transition would occur before merits/review completion and would defeat the practical value of later adjudication or remedy.

This is the structure most directly witnessed by ECHR Rule 39 and ICJ provisional measures.

## 4. Preservation-gate candidate

A source-faithful interim-preservation rule has the generic shape

`ProtectedInterest(tau)`
`and SourceRecognizesIrreparableRisk(tau)`
`and AdditionalSourceConditions(tau)`
`-> PreservationMeasureMayBeAvailable(tau)`.

`AdditionalSourceConditions` may include urgency, imminence, jurisdiction, plausibility/arguability, necessity, procedural posture, or another condition.

LAW-009 therefore does not infer:

`Irrep(tau) -> safeguard`.

The source rule performs the transition.

## 5. Capital-case safeguard package

For retained-death-penalty regimes represented by the selected UN sources, preserve distinct gates such as:

`capital exposure`
`-> heightened defence protection`
`-> heightened evidentiary/fair-trial constraints`
`-> final judgment`
`-> appeal/review exhaustion or availability`
`-> clemency/pardon process where supplied`
`-> execution authorization`.

The exact sequence is source-dependent and should not be universalized beyond the source.

Crucially:

`conviction exists != execution authorized now`.

`death sentence exists != all review complete`.

`review pending != sentence absent`.

## 6. Epistemic uncertainty boundary

Do not encode factual uncertainty as DSD `undefined` by default.

A legal system may have a defined procedural state such as:

- charge pending;
- guilt not established to required standard;
- appeal unresolved;
- new evidence under review;
- credible risk asserted but not finally adjudicated.

These are defined legal statuses, not missing DSD values.

## 7. Functional P/D/J implication

If `P` seeks an irreversible or highly irreparable transition, the source system may require `P` to establish additional gates before `J` may authorize the transition.

`D` can attack any required gate without proving a global opposite proposition.

Therefore:

`failure to authorize irreversible consequence`

`!= proof that no underlying violation/offence occurred`.

Likewise:

`responsibility established`

`!= irreversible consequence automatically authorized`.

## 8. DSD mapping

### Formation

Formation supplies the strongest first-pass correspondence: preserve candidate state, defined legal status, review stage, role-bearing identity, and downstream effect without collapsing them.

No semantic identities are asserted:

`legal irreparability != Formation admission`;

`factual uncertainty != undefined assignment`;

`review pending != channel absence`;

`execution stayed != defined zero`.

### Structural Reorganization Dynamics

Dynamics becomes meaningfully relevant because LAW-009 concerns time-directed state transitions.

A legal application may represent

`S(t0) -> S(t1)`

and add a source-supplied relation `Restorable_R` or `Preservable_R`.

The DSD dynamics layer can carry time-indexed states and succession, but it does not derive the legal restoration relation, irreversibility predicate, or safeguard rule.

### Axis-Property / Static Aggregation

Not required.

Irreversibility and procedural protection are not realized-axis properties or additive numerical weights merely by analogy.
