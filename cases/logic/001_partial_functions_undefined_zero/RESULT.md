# Case 001 — Result

## Final case judgment

**No falsification of the Formation Axiom System was found in Case 001.**

The specific Formation-Axiom-System distinction tested here—undefined assignment versus defined zero—survives the mathematical analysis. The zero-padding proposition is correct and can be strengthened to an exact non-injectivity/reconstruction statement.

This is a local result about the tested structure, not a proof that every primitive axiom of the Formation Axiom System is true under every intended interpretation.

## 1. Internal mathematical status

The Formation Axiom System treats a Stage-V quantity assignment as a partial map

`q_{L,λ}: Q_{L,λ} -> V_{L,λ}`

with the assignment domain recorded separately. This is mathematically coherent. The current paper also supplies an explicit set-sized full model in ZFC, so its declared model class is nonempty relative to the background set theory.

Therefore Case 001 does not reveal an internal contradiction.

## 2. Tested claim: undefined is not defined zero

The tested claim is valid in the precise set-theoretic sense:

- if `u ∉ Q`, then `q(u)` has no value in `V`;
- if `z ∈ Q` and `q(z)=0`, then `z` has a defined value;
- these are different partial-function states even when a later zero-padding representation sends both to the same number.

The distinction is carried by domain membership, not by numerical output alone.

## 3. Stronger theorem obtained in this analysis

For naive zero-totalization `T0`, two partial assignments have the same totalized function exactly when they agree on their common domain and every point belonging to only one domain is assigned zero there.

Hence zero-totalization forgets precisely which zero-valued points were genuinely defined.

Consequences:

- globally, naive zero-totalization is non-injective whenever the input carrier is nonempty;
- on the subclass with no defined zero values it is recoverable;
- pairing the totalized value with a domain/status mask makes the representation injective;
- using a disjoint bottom symbol `⊥` outside the original value carrier also preserves the distinction.

Therefore the correct DSD conclusion is **not** “total functions are wrong.” It is:

> A representation that maps undefinedness to an ordinary legitimate value and discards the original status/domain information is not faithful to the partial assignment structure.

## 4. Channel-level consequence

The distinction matters downstream in DSD. Closure Clause VI uses assignment-graph membership when admitting a channel.

In the finite witness:

- a defined-zero item forms a zero-valued channel when the other channel conditions hold;
- an undefined item forms no channel;
- if the same undefined item is first zero-totalized and then incorrectly treated as genuinely assigned, an extra zero-valued channel appears.

Thus the difference can change the Stage-VI channel set. It is not merely a notation preference inside the DSD model.

## 5. Comparison with established partial-function logic

Fitzgerald and Jones (2008) explicitly treat undefined terms arising from partial functions as a formal reasoning problem and compare classical first-order reasoning with a Logic of Partial Functions. Jones and Lovert's semantic work likewise treats terms that can fail to denote proper values as an explicit semantic phenomenon.

This is an independent external precedent for preserving a distinction between proper values and non-denotation/undefinedness.

However, it does **not** prove the DSD formation chain or Primitive Axiom V. LPF and DSD have different objects, semantics, and purposes.

### Mapping judgment

**Partial structural correspondence, strong on the tested distinction.**

The shared structure is that failure to receive/denote a proper value is not safely interchangeable with one ordinary value unless extra encoding retains the lost status. The systems should not be identified beyond that correspondence.

## 6. Does Case 001 show that the Formation Axiom System is wrong?

### Internal consistency

**No.** The case finds no contradiction, and the current Formation paper already gives an explicit full model in ZFC.

### Proposition 5.4 and related zero/undefined claims

**No.** They pass the test. Proposition 5.4 can in fact be strengthened mathematically.

### Primitive Axiom V as a universal modeling principle

**Not decided by this case.** The external partial-function literature supports partiality and explicit handling of undefinedness, but it does not establish DSD's additional requirement that one regime use a single regime-global partial assignment for a quantity kind.

### Entire Formation Axiom System

**Not proved true by this case.** Axioms are modeling constraints; nonempty models and correct derived propositions establish coherence and local mathematical validity, not universal empirical truth. Further independent cases are required to test the remaining formation distinctions.

## 7. Revision status of the Formation paper

No correction is required from Case 001.

A future revision could optionally strengthen Proposition 5.4 by defining the zero-totalization operator formally and adding:

1. a non-injectivity theorem;
2. the exact fiber/equivalence characterization;
3. the zero-free recovery corollary;
4. a status-mask or lifted-codomain reconstruction proposition.

These would sharpen the current result but do not repair an error.

## 8. Case classification

- Domain: mathematical/philosophical logic
- External node: partial functions / LPF
- DSD layer tested: Formation Stage V and downstream Stage VI consequence
- Main DSD distinction: undefined assignment vs defined zero
- Mapping strength: **partial correspondence, strong on the tested distinction**
- Falsification status: **not falsified**
- Correction required: **no**
- Strengthening opportunity: **yes**
- Cross-domain node status: **accepted as first provisional node**

## References

- Kwon Dominicus, *Formation Axiom System — Dimensional-Structural Describability*, 2026, especially Primitive Axiom V, Closure Clause VI, and Propositions 5.2–5.4, 5.9, 5.12–5.13.
- Fitzgerald, J. S.; Jones, C. B. (2008), *The connection between two ways of reasoning about partial functions*, Information Processing Letters 107(3–4), 128–132. DOI: 10.1016/j.ipl.2008.02.005.
- Jones, C. B.; Lovert, M. J. (2010/2011), *Semantic Models for a Logic of Partial Functions*, Newcastle University CS-TR-1220 / International Journal of Software and Informatics 5(1–2), 55–76.
