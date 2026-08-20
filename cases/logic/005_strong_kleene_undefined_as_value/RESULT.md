# Case 005 — Result

## Final case judgment

**No falsification of the Formation Axiom System or Axis-Property undefinedness discipline was found in Case 005.**

Strong Kleene K3 is an important **non-correspondence node**. Its third state is a semantic truth value inside a three-valued carrier, whereas DSD undefinedness is produced by exclusion from a partial assignment/application domain.

The case also identifies a useful wording boundary: DSD may faithfully encode undefinedness externally by adjoining a fresh sentinel value, but that sentinel is not an ordinary value of the original DSD assignment map and must not be fed back as though it were one.

## 1. Type-level non-identity

Let `q:Q -> V` be a DSD Stage-V partial assignment.

For `a notin Q`, the expression `q(a)` has no value in `V`. The status is represented by domain exclusion.

By contrast, Strong Kleene semantics uses a three-element truth-value carrier containing false, true, and a third unknown/indeterminate value. The third value participates in the semantic algebra.

Therefore

`DSD undefined assignment != Strong-Kleene third truth value`.

This is not a disagreement between two theories. They assign the word `undefined/unknown` to different mathematical roles.

## 2. Faithful lifted encoding theorem

Let `bot notin V` and define the disjoint extension

`V^bot = V disjoint-union {bot}`.

For a fixed ambient input set `A superset Q`, define

`L_bot(q)(a) = q(a)` for `a in Q`, and `L_bot(q)(a)=bot` otherwise.

Then the original partial assignment is reconstructible by

`Q = {a in A : L_bot(q)(a) != bot}`

and

`q = L_bot(q)|_Q`.

Hence `L_bot` is injective as an encoding of partial assignments.

### Consequence

The broad slogan

`undefined can never be represented by a value`

would be false if interpreted across all possible external encodings.

The precise DSD statement is instead:

> An undefined application is not an assigned value of the original partial map/value carrier. A faithful external representation may adjoin a disjoint status symbol, provided that the representation is not confused with the original assignment semantics.

This precision is fully compatible with Formation Corollary 5.3, whose formal content says that an input outside `Q_{L,lambda}` has no `q_{L,lambda}` value and cannot be inferred to equal the distinguished zero.

## 3. Strong-Kleene cardinality coincidence is not structural equivalence

For the finite witness `V={0,1}`, the lifted set `V^bot={0,bot,1}` has three elements. One may define a bare set bijection with `{false,unknown,true}`.

That bijection does not preserve semantic role:

- DSD `0` is a distinguished quantity value, not falsity;
- DSD nonzero values are not truth;
- the adjoined `bot` is representation metadata, not a value supplied by the original Formation model;
- DSD does not define Strong-Kleene truth operations on assignment values/statuses.

Therefore a three-element encoding does not turn DSD into K3.

## 4. Stage-VI obstruction

In DSD, if `u notin Q_{L,lambda}(p)`, then no local graph pair `(u,v)` exists. Even if all other channel conditions hold, Stage VI cannot admit a channel for `u`.

If the lifted sentinel is instead inserted into the actual Stage-V value space and the domain is totalized, `(u,bot)` becomes a genuine graph pair and may support an additional channel.

Thus

`faithful external representation != semantics-preserving replacement of Stage V`.

This is the operational reason why the distinction matters.

## 5. Axis-property consequence

The same distinction survives in the Axis-Property System.

For a typed property input `x`:

- `x notin D_{A,p,varpi}` means undefined application and no value in `Z_{L,varpi}`;
- `x in D_{A,p,varpi}` with value `0_{L,varpi}` is defined zero.

A K3-like third semantic value can encode the first status externally only after an explicit codomain extension. It is not already one of the property values.

## 6. What Strong Kleene actually contributes

Strong Kleene logic supplies a useful counterpressure against imprecise DSD language:

- it proves by example that a formal system may intentionally internalize an `unknown` state as a semantic value;
- therefore DSD must not claim that every mathematically respectable treatment of undefinedness must use partial functions;
- DSD's stronger and defensible claim is local: **its own formation/property semantics chooses domain exclusion, and collapsing that choice into an ordinary original value changes the structure.**

This makes Strong Kleene a valuable non-correspondence node rather than supporting evidence for identity.

## 7. Does Case 005 show that DSD is wrong?

### Formation Corollary 5.3
**No.** In context it concerns the original partial map and original value carrier. It remains correct.

### Proposition 5.4
**Strengthened.** Existing-value padding is non-faithful, while fresh-sentinel lifting is faithful as an external encoding. The distinction between these two totalizations should be retained.

### Stage VI
**No contradiction.** Domain exclusion correctly prevents an undefined assignment from generating a channel.

### Axis-Property Definition 3.10 / Proposition 3.11
**No contradiction.** Undefined application remains outside the assignment domain, while defined zero remains inside.

### Entire DSD systems
**Not proved by this case.** The analysis is limited to undefinedness/status representation and downstream channel consequences.

## 8. Revision status

**No corrective revision is required.**

An optional clarification would make Corollary 5.3's heading and nearby prose resistant to an overbroad reading:

> Here `not a value` means not a value assigned by the original partial map in its declared value carrier. A separate faithful encoding may adjoin an external status symbol, but that symbol is not thereby an ordinary assignment value of the formation model.

This is a clarification of scope, not a correction of the formal result.

## 9. Case classification

- Domain: mathematical/philosophical logic
- External node: Strong Kleene K3
- DSD layer tested: Formation Stage V–VI and Axis-Property application status
- Main distinction: domain-exclusion undefinedness vs internalized third semantic value
- Mapping strength: **important non-correspondence**
- Falsification status: **not falsified**
- Correction required to papers: **no**
- Clarification opportunity: **yes — scope `not a value` to the original partial-map semantics**
- Roadmap refinement: **yes — distinguish faithful lifted encoding from semantic identification**
- Cross-domain node status: **accepted as fifth provisional node and first explicit non-correspondence stress test**

## References

- Kwon Dominicus, *Formation Axiom System — Dimensional-Structural Describability*, 2026.
- Kwon Dominicus, *Axioms for the Property Structure of Realized Axes in Dimensional-Structural Describability*, 2026.
- Melvin Fitting, *Kleene's Logic, Generalized*, Journal of Logic and Computation 1(6), 797–810 (1991), DOI 10.1093/logcom/1.6.797.
