# COH-001 / Global Case 011 — Formation Partiality, Typing, and Closure Coherence

## 1. Classification

- Primary purpose: coherence and consistency comparison
- External domain: mathematical logic / model-theoretic and set-theoretic formalization
- Status: prepared, not yet judged
- DSD primary source: Formation Axiom System

## 2. Core question

Can the Formation Axiom System's principal distinctions be jointly reconstructed in standard typed set-theoretic terms without adding a hidden contradiction or silently changing the meaning of its partial maps, closure clauses, or structure-preserving comparisons?

## 3. Subquestions

1. Is Stage-V partial assignment faithfully represented as a genuine partial function rather than a total function with a default value?
2. Are expression/configuration sorts and restriction/realization relations jointly type-consistent?
3. Do Primitive Axioms I–III and V constrain primitive data while Clauses IV, VI, VII act as definitional closure relative to supplied post-Stage-VI term data?
4. Does the unique relative closure claim add any hidden primitive constraint?
5. Are forward maps, embeddings, and strict equivalence coherently ordered as different preservation strengths?
6. Which results are ordinary consequences of function typing, induced substructures, or set-theoretic construction, and which are genuine DSD-specific constraints?

## 4. Decision classes

For each subquestion, record one of:

- compatible
- conditionally compatible
- non-corresponding but not contradictory
- design/signature boundary
- internal contradiction or countermodel found

## 5. Anti-bias rule

Cases 001–010 may supply earlier witnesses and known failure modes, but their conclusions are not treated as premises. In particular, `not falsified` from prior cases does not count as evidence that COH-001 must return `compatible`.

## 6. Minimum evidence

The case is not complete until it contains:

- locked DSD source clauses;
- locked external formal claims actually used;
- an explicit correspondence/non-correspondence table;
- at least one nonempty finite full-formation witness;
- a check of primitive-versus-derived dependency;
- a result section separating ordinary mathematical infrastructure from DSD-specific content.

## 7. Reproducibility

A small deterministic Python witness checker is included only as a sanity check for one finite model. It does not prove the general coherence result. General claims require mathematical argument in `RESULT.md`.