# COH-001 Source Notes

Status: **DSD source lock and external formal-source lock completed for the first analysis pass**.

## DSD primary source

Kwon Dominicus, *Formation Axiom System: Dimensional-Structural Describability*.

Stable role ID: `Kwon2026DSDFormation`.

DOI: https://doi.org/10.5281/zenodo.18466754

The analysis uses the current 2026-08-06 English formation manuscript supplied in the project as the authoritative DSD text for this case.

## DSD clauses targeted

### Formal setting

- Section 2.1 — static typed set-theoretic status and ZFC background
- Definition 2.1 — primitive and derived vocabulary
- Definition 2.2 — primitive formation core and full model
- Definition 2.4 / Proposition 2.5 — stage truncations and formation reductions

### Primitive and closure layers

- Primitive Axiom I — expression describability implies expression admission
- Primitive Axiom II — sound restricted expression and identity restriction
- Primitive Axiom III — sound configuration realization
- Definitional Closure Clause IV — configuration describability criterion
- Primitive Axiom V — quantity-specific regime-global partial assignment
- Definitional Closure Clause VI — component-channel formation
- Definitional Closure Clause VII — finite composition relative to supplied term data
- Theorem 3.3 — unique relative closure expansion and primitive-reduct characterization

### Dependency/minimality checks

- Proposition 4.6 — typing-induced clause dependencies
- Theorem 4.7 — residual clausewise independence
- Propositions 5.2–5.13 — separation of undefined, defined zero, channel absence, and zero term

### Structure-preserving comparison

- Definition 6.2 — forward formation map
- Definition 6.4 — formation embedding and submodel
- Definition 6.10 and following — strict base-fixed formation isomorphism / strict descriptive equivalence

### Existence

- Section 7 — model existence and finite constructions

## External formal sources actually used

### E1. Partial functions and definedness

William M. Farmer, “Reasoning about Partial Functions with the Aid of a Computer,” *Erkenntnis* 43(3), 279–294 (1995), DOI 10.1007/BF01135375.

- Bibliographic/abstract record: https://philpapers.org/rec/FARRAP
- McMaster record: https://experts.mcmaster.ca/scholarly-works/1710278

Use in COH-001: partial functions are legitimate mathematical/logical objects whose definedness must be tracked rather than silently replaced by a default value. The source is used only to establish that partial-function reasoning is standard external infrastructure; it is not used to identify Farmer’s semantics with DSD Stage V.

### E2. Many-sorted structures and preservation strengths

Stanford Encyclopedia of Philosophy, “Many-Sorted Logic.”

https://plato.stanford.edu/entries/logic-many-sorted/

Use in COH-001: many-sorted structures admit sort-respecting homomorphisms; embeddings add injectivity and relation reflection; isomorphisms are bijective embeddings. Reducts and expansions are also standard notions. This supplies the comparison baseline for DSD’s typed carriers and its forward-map / embedding / strict-isomorphism hierarchy.

### E3. Model-unique extension versus stronger definitional claims

“Extensions in graph normal form,” *Logic Journal of the IGPL* 30(1), 101–126.

https://academic.oup.com/jigpal/article/30/1/101/5954216

Use in COH-001: the paper explicitly distinguishes a definitional extension from the weaker model-unique-extension property in which every old model has a unique expansion. This is important because DSD Theorem 3.3 states a model-class unique relative expansion and explicitly declines a proof-theoretic conservativity claim.

### E4. Definitional/Morita equivalence boundary

Thomas William Barrett and Hans Halvorson, “Morita Equivalence,” *The Review of Symbolic Logic* 9(3), 556–582 (2016), DOI 10.1017/S1755020316000186.

https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S1755020316000186

Use in COH-001: definitional, Morita, and categorical equivalence are distinct theory-level comparison notions. DSD’s strict base-fixed formation isomorphism is therefore not to be relabeled as any of them merely because it is an equivalence relation on full descriptors.

## External claims locked for this case

1. A partial function can be represented without assigning a default value outside its domain of definition.
2. Many-sorted structures support typed homomorphism, embedding, isomorphism, reduct, and expansion notions.
3. Unique expansion at the model level is weaker in status than a full formal-theory definitional-extension claim unless the latter’s syntactic conditions are supplied.
4. Ordinary homomorphism/embedding/isomorphism terminology concerns different preservation/reflection strengths; an application may impose additional reflection clauses.
5. Arbitrary subsets are automatically induced substructures for a purely relational internal signature, while internal function symbols would require closure of the retained subset. COH-001 therefore treats the Formation manuscript’s relational material-signature restriction as a deliberate signature boundary, not as a theorem about arbitrary signatures.

## Non-identification rules

- Farmer-style partial-function formalisms are not DSD Stage V by definition.
- Many-sorted logic is not the Formation Axiom System.
- Model-unique expansion does not by itself justify calling DSD a syntactic definitional extension.
- DSD strict formation isomorphism is not identified with definitional, Morita, categorical, or empirical equivalence.

## Current scope exclusion

The following are not primary sources for COH-001:

- Axis-Property Axiom System
- Channel-Indexed Static Aggregation
- Structural Reorganization Dynamics

They remain downstream interfaces and are not imported into the formation-coherence judgment.