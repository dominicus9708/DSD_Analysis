# DSD Analysis Case Template

## 1. Case identity

- Global case number:
- Purpose ID:
- External domain:
- Topic:
- Primary purpose: falsification / coherence / predefinition / reinterpretation
- Secondary purpose tags:
- Date:
- Status: preparation / active / completed / revised

## 2. Source lock

### External source structure

Record the source discipline in its own terminology before mapping to DSD.

- Original problem:
- Formal objects:
- Domain/codomain or typing conditions:
- Native treatment of undefinedness, inapplicability, absence, zero, and equality:
- External claims actually used:

### DSD source structure

- Paper role ID:
- Paper title:
- Exact section/definition/axiom/theorem/closure clause:
- Claim actually used:
- Additional interpretation supplied by this case, if any:

## 3. DSD scope selection

Use only the required layer.

- Formation Axiom System: used / not used
- Axis-Property System: used / not used
- Static Aggregation: used / not used
- Dynamics: used / not used

## 4. Structural correspondence table

| External structure | DSD structure | Mapping strength | Preserved | Not preserved |
|---|---|---|---|---|
| | | direct / partial / after encoding / no mapping | | |

## 5. Finite witness, countermodel, or boundary construction

Construct the smallest explicit example that distinguishes the relevant states when possible.

- Carrier/input set:
- Primitive domains:
- Defined values:
- Undefined/inapplicable/absent cases:
- Derived data:
- Tested collision or contradiction:
- What would count as failure:

## 6. Purpose-specific questions

### Falsification

- Is there a legal DSD model that falsifies the target claim?
- Is the failure internal, or is the candidate already outside the signature/type system?

### Coherence

- Can the DSD clauses be jointly reconstructed in the external formal setting?
- Are extra assumptions required?
- What is standard mathematical infrastructure versus DSD-specific structure?

### Predefinition

- Does a prior definition/type/sort/function signature already remove alternatives?
- Does weakening the prior assumption change the conclusion?

### Reinterpretation

- Does the DSD decomposition clarify a real source-domain ambiguity or failure?
- Is the result more than renaming an existing distinction?

Use only the subsection relevant to the case.

## 7. Result discipline

Record separately:

- Mapping judgment:
- Main result class: compatible / conditionally compatible / non-corresponding / boundary / contradiction found
- Problem-solving contribution:
- Counterexample or boundary:
- What DSD adds:
- What DSD does not add:
- Whether the case is independent enough to count as a cross-domain node:

## 8. Reproducibility

Follow `methodology/reproducibility_contract.md`.

- Source references:
- DSD references:
- Script/notebook, if any:
- Exact input:
- Exact command:
- Expected output:
- Search/enumeration bounds, if any:

## 9. Cross-domain tags

Add only after the case is completed.

Examples:

- undefined-vs-zero
- applicability-before-value
- absence-vs-zero
- formation-before-composition
- result-equality-vs-structure-equality
- signature-predefinition
- primitive-vs-definitional-closure
