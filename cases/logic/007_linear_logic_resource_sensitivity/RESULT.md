# Case 007 — Result

## Final case judgment

**No internal contradiction of the Formation Axiom System or Axis-Property System was found in Case 007.**

However, Linear Logic exposes a genuine **scope boundary** in the current Stage-VII data type:

> DSD preserves multiplicity of distinct operational channel tags, but its core finite-composition domain does not represent repeated occurrence of one identical tag within a single composite family.

This boundary is already explicit in the paper because Closure Clause VII uses `Pfin(C_L)` and states that a core channel family is an unordered set without repetition. Therefore it is not a hidden contradiction. It becomes a limitation only for applications that require occurrence-sensitive or consumable-resource semantics.

## 1. External Linear-Logic pressure

Linear Logic restricts the ordinary structural rules of weakening and contraction and thereby makes resource occurrence significant. Its exponential machinery restores controlled reuse/discard behavior for marked formulas.

The comparison with DSD is methodological only. DSD channels are not formulas in a proof context, and `Pfin(C_L)` is not a sequent antecedent.

Accordingly, the following identifications are rejected:

- Linear-Logic resource = DSD operational channel;
- contraction = DSD set extensionality;
- weakening = selection of a smaller channel family;
- exponential `!` = DSD role or weight.

## 2. Distinct-tag multiplicity is preserved

Formation Proposition 5.11 gives an explicit route to distinct channel multiplicity: different role coordinates can produce distinct channels even when configuration, material item, quantity kind, and assigned value agree.

If `c1 != c2` and `T(c1)=T(c2)=1`, then

`Comp({c1})=1`,

`Comp({c1,c2})=2`.

Therefore the set-based core does not collapse multiplicity of **distinct elements**.

The axis-property layer independently confirms this distinction: distinct inherited channel tags may realize the same line, and channel multiplicity is not identified with realized-axis rank.

## 3. Same-tag occurrence multiplicity is outside the core

Let one admitted channel `c` satisfy `T(c)=1`.

An external finite-multiset semantics distinguishes one copy from two copies:

- multiplicity one gives `1`;
- multiplicity two gives `2`.

But both have support set `{c}`. Since Formation Stage VII accepts only a finite set, the two occurrence patterns map to the same core input.

Thus the support-forgetting map from finite multisets to `Pfin(C_L)` is non-injective, and occurrence-sensitive aggregation cannot factor through it in general.

### Exact scope statement

The current core can count

`|{c1,c2,...}|`

for distinct admitted tags, but it cannot represent a multiplicity function

`m:C_L -> N`

with `m(c)>1` while keeping the same operational tag `c`.

This is a **data-type limitation**, not an inconsistency.

## 4. Weakening analogy fails

Choosing `F subset C_L` is a choice of which admitted channels are aggregated. It is not an inference rule authorizing a resource to be discarded without consequence.

For `T(c)=1`,

`Comp({c}) != Comp(emptyset)`.

Therefore deletion is not semantically free in general.

If deletion happens to preserve an aggregate because a term is zero or cancellation occurs, the support-tagged/full descriptor still distinguishes the underlying channel families. Existing DSD results on non-injective aggregation already recognize this.

## 5. Contraction analogy fails

The equation

`{c} union {c} = {c}`

comes from ordinary set extensionality. It does not derive a rule that two independently available DSD resources may be merged into one.

Indeed, if two available resources have distinct operational tags `c1 != c2`, they remain distinct set elements and can contribute twice.

The only collapsed case is two supposed occurrences with exactly the same five-coordinate operational identity. The current Formation core simply has no occurrence coordinate by which to distinguish them.

## 6. Cross-layer consistency

### Axis-property layer
No contradiction was found. The axis layer preserves distinct tags even when the realized line is the same. Ordered typed property inputs may also repeat an argument position, but that is an extension-level relation/application issue rather than Stage-VII channel occurrence multiplicity.

### Static aggregation layer
No contradiction was found. It inherits the same set-indexed finite channel domain. Section 8.4 explicitly requires semantically distinct reuse of the same property record to be declared as bookkeeping rather than silently duplicated.

### Dynamics layer
No contradiction was found. The dynamic layer fixes inherited channel identity/support within a regular epoch and treats changes of support or channel identity as explicit transitions. It does not silently manufacture duplicate inherited channels.

## 7. Does this require a paper correction?

**No corrective revision is required.** Closure Clause VII already states the restriction explicitly.

A terminology clarification would nevertheless be useful:

> In the present system, channel multiplicity means multiplicity of distinct admitted operational tags. Stage-VII composition is set-indexed and does not encode repeated occurrence of one identical tag. Applications requiring occurrence-sensitive multiplicity need an additional occurrence index, finite-multiset extension, or other explicit downstream accounting.

This would prevent readers from interpreting Proposition 5.11 or Axis-Property Proposition 2.11 as claims about multiset occurrence multiplicity.

## 8. Potential future extension

If later physical or computational applications require one operational channel to participate multiple distinguishable times in a single aggregate, the cleanest options are:

1. an occurrence/event-indexed extension of channel identity;
2. a finite-multiset composition layer over fixed Stage-VI channels;
3. a weighted/counting downstream aggregate when provenance is intentionally discarded.

These are not equivalent extensions and should not be added to the core without a concrete application requirement.

## 9. Case classification

- Domain: mathematical/philosophical logic
- External node: Linear Logic
- DSD layers tested: Formation Stage VI–VII, Axis-Property tag multiplicity, Static Aggregation bookkeeping, dynamic support identity
- Main distinction: distinct-tag multiplicity vs same-tag occurrence multiplicity
- Mapping strength: **important non-correspondence / resource-sensitivity stress test**
- Falsification status: **not falsified**
- Paper contradiction: **none**
- Scope limitation found: **yes — no same-tag occurrence multiplicity in core `Pfin(C_L)` composition**
- Corrective revision required: **no**
- Optional terminology clarification: **yes**
- Cross-domain node status: **accepted as seventh provisional node**

## References

- Kwon Dominicus, *Formation Axiom System — Dimensional-Structural Describability*, 2026.
- Kwon Dominicus, *Axioms for the Property Structure of Realized Axes in Dimensional-Structural Describability*, 2026.
- Kwon Dominicus, *Channel-Indexed Static Aggregation in Dimensional-Structural Describability*, 2026.
- Kwon Dominicus, *Structural Reorganization Dynamics in Dimensional-Structural Describability*, 2026.
- Jean-Yves Girard, “Linear Logic,” *Theoretical Computer Science* 50 (1987), 1–101, DOI 10.1016/0304-3975(87)90045-4.
- Patrick Lincoln, John Mitchell, Andre Scedrov, Natarajan Shankar, “Decision Problems for Propositional Linear Logic,” *Annals of Pure and Applied Logic* 56 (1992), 239–311, DOI 10.1016/0168-0072(92)90075-B.
