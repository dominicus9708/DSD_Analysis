# DSD Analysis Case Template

## 1. Case identity
- Case ID:
- Domain:
- Topic:
- Date:
- Status: preparation / active / completed / revised

## 2. External source structure
Record the source discipline in its own terminology before mapping to DSD.

- Original problem:
- Formal objects:
- Domain/codomain or typing conditions:
- Native treatment of undefinedness, inapplicability, absence, zero, and equality:
- Source claims actually used:

## 3. DSD scope selection
Use only the layer required by the case.

- Formation Axiom System: used / not used
- Axis-Property System: used / not used
- Static Aggregation: used / not used
- Dynamics: used / not used

## 4. Structural correspondence table
For each proposed correspondence, record both similarity and mismatch.

| External structure | DSD structure | Mapping strength | Preserved | Not preserved |
|---|---|---|---|---|
| | | direct / partial / after encoding / no mapping | | |

## 5. Finite witness or counterexample
Construct the smallest explicit example that can distinguish the relevant states.

- Carrier/input set:
- Partial domain:
- Defined values:
- Undefined inputs:
- Totalized representation, if tested:
- Collision created by totalization:

## 6. Comparison questions
1. Does the native system distinguish undefinedness from an ordinary value?
2. Does a default-value totalization preserve the original domain information?
3. Can a defined zero be distinguished from an undefined input after totalization?
4. Does any downstream structure depend on that distinction?
5. Is extra status/domain metadata sufficient to reconstruct the distinction?
6. Is the DSD mapping direct, partial, encoding-dependent, or invalid?

## 7. Result discipline
Record separately:

- Mapping judgment:
- Problem-solving contribution:
- Counterexample or boundary:
- What DSD adds:
- What DSD does not add:
- Whether the case is independent enough to count as a cross-domain node:

## 8. Reproducibility
- Source references:
- DSD references:
- Script/notebook, if any:
- Exact finite input:
- Expected output:

## 9. Cross-domain tags
Add only after the case is completed.

- undefined-vs-zero
- applicability-before-value
- absence-vs-zero
- formation-before-composition
- result-equality-vs-structure-equality
