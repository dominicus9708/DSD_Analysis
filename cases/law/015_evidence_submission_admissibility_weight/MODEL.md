# LAW-004 Typed Model

## 1. Source-side evidence record

For an evidence item `e`, use the application record

`E(e) = (origin, item, offered, investigated, usable, weight_status, finding_role, regime)`.

These coordinates are source-law bookkeeping only. They are not DSD primitives.

The model intentionally avoids a single scalar `evidence_value`.

## 2. Non-collapse conditions

The source structure requires at least:

`exists(e) != offered(e)`

`offered(e) != investigated(e)`

`investigated(e) != legally_usable(e)` in regimes with admissibility/use restrictions

`legally_usable(e) != high_probative_force(e)`

`high_probative_force(e) != ultimate_fact_found`

and, critically,

`same collection-defect label != same admissibility result across regimes`.

## 3. Criminal regime

A minimal criminal record uses:

- `O`: source existence/collection state;
- `S`: party submission/application state;
- `A_crim`: criminal legal-use/admissibility state;
- `W_crim`: probative-force evaluation state;
- `F_crim`: factual finding under Article 307 standard.

An item may satisfy `S=1` while `A_crim=0`, for example if Article 308-2 or the hearsay rules exclude its use.

Even with `A_crim=1`, Article 308 leaves probative force to judicial evaluation, and Article 307 requires the ultimate criminal fact to reach the governing proof threshold.

Thus the criminal source does not permit the collapse

`submitted -> admissible -> sufficiently probative -> fact proved`.

## 4. Civil regime

A minimal civil record uses:

- `O`: existence/collection state;
- `S`: application/submission state under Article 289;
- `I_civ`: whether evidence investigation occurs under Articles 290-292 and related rules;
- `A_civ`: source-law admissibility/use status when such a question arises;
- `W_civ`: evaluative contribution under Article 202;
- `F_civ`: resulting factual finding.

Article 290 alone already shows that an application does not force investigation.

Supreme Court 2024Da222212 adds a regime-sensitive admissibility layer: unlawful collection does not create one universal civil admissibility output. A special statutory prohibition can exclude one item while another unlawfully collected item without such a statutory rule may remain admissible after balancing.

## 5. DSD Formation bridge

### 5.1 Application carrier

The faithful carrier is not `the physical evidence object as such` when different proceedings, propositions, or purposes are involved.

Use a typed evidence-use instance:

`a_e = (item_id, proposition, proceeding, purpose, source_status)`.

This prevents a false conflict where the same physical file is assigned contradictory legal statuses merely because it is used in different regimes or for different propositions.

### 5.2 Role coordinate

A Formation role `rho` may preserve an application-supplied role such as:

- offered-for-prosecution proposition;
- offered-for-defense proposition;
- civil plaintiff evidence;
- civil defendant evidence;
- impeachment/limited-purpose use where separately justified.

This is an encoding bridge, not a claim that legal evidence roles are DSD-derived roles.

### 5.3 Partiality

If a source rule has not yet determined legal usability or probative status, the application should not silently assign a positive or negative value.

The Formation discipline is useful here because partial assignment and channel absence are already distinct from defined zero.

However, legal `inadmissible` should normally be encoded as an explicit application status on an existing evidence-use record, not as nonexistence of the evidence item.

### 5.4 Stage analogy boundary

The following is only structural correspondence:

`source existence -> procedural offer -> legal-use gate -> evaluation -> finding`

is comparable to a staged typed formation path.

It is not an identity with DSD Stages I-VII. Legal admissibility is not Formation admission, and factual finding is not Clause-VII composition by definition.

## 6. Static Aggregation audit

The phrase `probative weight` tempts a numerical mapping, but current source law does not supply a universal scalar coefficient for each item.

Criminal Article 308 and Civil Article 202 describe judicial evaluation, not an additive normalized weighting rule.

Current DSD Static Aggregation likewise says later coefficients and normalized statistics require an explicitly supplied application operator; they are not automatically the core finite composition.

Therefore:

`legal probative weight != DSD analytic weight w_c`

unless a separate legal-analytic model is independently justified.

Static Aggregation is useful only for a negative boundary result: even if a later application builds a scalar evidence score, aggregate equality cannot by itself reconstruct the evidence support and procedural statuses.

## 7. Axis-Property and Dynamics audit

Axis-Property: not required. No realized-axis semantics is supplied by the legal source.

Dynamics: not required for the first-pass static status comparison. Temporal changes such as later admission rulings or new evidence can be represented as separate descriptors; a true procedural transition model would require an additional application dynamic layer.
