# DSD General Audit Framework

## 1. Purpose

The DSD General Audit Framework is a reusable audit layer inside **DSD Analysis**.
It is intended to trace how a claim, judgment, procedure, model, decision, or output is formed from describable information, selections, exclusions, transitions, explicit bridges, and explicit criteria.

It is not a replacement for the validation standards of mathematics, science, law, software engineering, history, administration, or other fields.
Field-specific standards remain primary for field-specific truth, validity, legality, reproducibility, or performance judgments.

The stable common audit frame is kept separate from the paper-facing DSD interface profile in [`DSD_INTERFACE_PROFILE.md`](DSD_INTERFACE_PROFILE.md).
This separation allows predecessor DSD papers to evolve without forcing a complete rewrite of the common audit method.

## 2. Position in DSD Analysis

```text
DSD Analysis
├─ DSD Interface Profile
└─ General Audit Framework
   ├─ Domain Protocols
   └─ Individual Audit Records
```

Analysis and audit are related but distinct.

- **Analysis** decomposes and compares structures, states, relations, applicability, composition, transitions, and describability.
- **Audit** retraces the analysis and resulting claims under an explicit scope, interface lock, procedure, and verdict rule.

An analysis result is not automatically an audit pass.
An audit failure does not automatically imply that the audited object is false in every possible sense.

## 3. Core audit questions

Every audit should answer, as far as the available material permits:

1. What is describable within the present scope?
2. What remains undetermined, insufficiently specified, or outside scope?
3. What alternatives were available?
4. What was selected and what was excluded?
5. On what rule or evidence was each selection or exclusion based?
6. Is every transition from evidence/state to conclusion/state justified?
7. Are fact, inference, norm, and decision kept distinct?
8. Do alternative describable explanations remain compatible with the same outcome?
9. Does the strength of the conclusion exceed the strength of the evidence?
10. Can another reviewer reconstruct the audit from the record?
11. If DSD layers are used, which interfaces and source revisions were actually active?
12. Were any cross-layer selectors, bridges, or constitutive maps assumed without being declared?
13. If a reduced aggregate or summary is used, what information was lost and what justifies any reconstruction claim?
14. If identity changes across time or stages, is succession represented by an appropriate lineage or transition rule?

## 4. Eight-axis common frame

Let an audit record be summarized as

\[
\mathcal{A}=(D,R,S,E,T,C,N,O).
\]

### D — Describability
Record what can be stated from the available material, what is currently undetermined, and what is outside the audit scope.

### R — Resolution
Record the descriptive resolution at which a claim is made.
A coarse description must not be silently treated as a fine-grained causal or structural account.

### S — Selection
Record which candidates, sources, branches, hypotheses, rules, layers, or data were actually selected.

### E — Exclusion
Record what was excluded and why.
Exclusion is itself auditable.

### T — Transition
Record how one state, proposition, evidence set, or decision leads to the next.
A transition must not be inferred merely because two states are adjacent in the final narrative.
When DSD dynamics is used, distinguish regular value evolution from status/domain and formation-level transitions.

### C — Consistency
Check definitions, statuses, relations, interfaces, transitions, and claims for internal contradiction or incompatible commitments.

### N — Norm
Separate factual and inferential content from normative, legal, policy, ethical, procedural, or evaluative criteria.

### O — Outcome
Record the final result and the maximum conclusion that the current audit actually supports.

## 5. Required distinctions

### 5.1 Audit evidence status

Use at least these states:

- **Describable / established within scope**
- **Undetermined / insufficient**
- **Outside scope**

Do not convert an unknown state into a positive or negative conclusion merely to complete the audit.

These are statuses of the audit evidence, not necessarily statuses of the DSD object being analyzed.

### 5.2 DSD object status

When DSD formal layers materially affect the case, record object status separately according to the current interface profile.

Examples include:

- Formation: undefined assignment, defined zero, defined value, channel absence, admitted zero component term.
- Property: undeclared, profile unavailable, inapplicable, prerequisite unsatisfied, applicable but undefined, defined zero, defined nonzero or otherwise defined.
- Dynamics: regular value evolution, status/domain transition, optional geometric transition, channel/formation-level transition.

Do not merge evidence uncertainty with object undefinedness or absence.

### 5.3 Proposition layer

Keep these layers distinct:

- **Fact** — source material, observation, record, or established statement used as evidence.
- **Inference** — a conclusion derived from facts or other premises.
- **Norm** — a rule, criterion, value, law, policy, or evaluative standard.
- **Decision** — the selected action, judgment, classification, or conclusion.

### 5.4 Mapping strength

When DSD structures are compared with an external field, record one of:

- Direct correspondence
- Partial correspondence
- Correspondence after explicit additional encoding
- Non-correspondence

Do not treat terminological similarity as structural identity.

## 6. DSD interface lock

When the DSD formal structure is material to the result, lock the interface before evaluating the case.

```text
DSD_INTERFACE_PROFILE_DATE:
FORMATION_LAYER: used / not used
PROPERTY_CORE: used / not used
STATIC_AGGREGATION_LAYER: used / not used
DYNAMICS_LAYER: used / not used
REALIZED_AXIS_SPECIALIZATION: supplied / not supplied
OTHER_SPECIALIZATION:
SOURCE_VERSIONS:
```

Do not force all DSD layers into one mandatory serial chain.
The current profile treats the general Property layer as a Stage-VI-based static extension, static aggregation as a separate analytic interface, dynamics as independently selectable over the fixed Stage-VI background, and realized-axis geometry as an optional specialization.

## 7. Bridge and allocation audit

A cross-layer role must not be inferred from names or coincident coordinates alone.
When relevant, record:

```text
BRIDGE_NAME:
BRIDGE_SOURCE_LAYER:
BRIDGE_DOMAIN:
BRIDGE_CODOMAIN:
BRIDGE_ASSUMPTIONS:
BRIDGE_JUSTIFICATION:
IMPLICIT_BRIDGE_CHECK:
```

Audit at least the following cases when they occur:

1. allocation of multi-input property data to one formation channel;
2. static typed-property mapping into an analytic output carrier;
3. constitutive mapping from property data to dynamic coefficients or operators;
4. representation-specific encodings later treated as if they were core property structure.

## 8. Aggregation, compression, and reconstruction audit

A reduced output can erase support, decomposition, typed-input correlation, or negative status information.
Aggregate equality does not establish structural equality without an injectivity or reconstruction result for the chosen admissible data class.

When a summary, scalarization, finite sum, or other reduced readout is used, record:

```text
OUTPUT_EQUALITY_CHECK:
SUPPORT_EQUALITY_CHECK:
DECOMPOSITION_RETENTION_CHECK:
INJECTIVITY_ESTABLISHED:
COLLISION_WITNESS:
KERNEL_OR_INFORMATION_LOSS_CHECK:
RECONSTRUCTION_CLAIM:
```

## 9. Transition and lineage audit

If the case includes time, stages, regime changes, or identity change, classify the transition before judging it.

Suggested DSD transition classes when the current dynamics interface is used:

```text
DOWNSTREAM_VALUE_EVOLUTION
PROPERTY_ASSIGNMENT_EVOLUTION
PROPERTY_STATUS_OR_DOMAIN_TRANSITION
OPTIONAL_GEOMETRIC_SPECIALIZATION_TRANSITION
CHANNEL_OR_FORMATION_LEVEL_TRANSITION
```

If a coordinate belonging to Stage-VI channel identity changes, do not describe it as one unchanged inherited channel with a silently varying identity coordinate.
If successor identity is claimed across a formation-level transition, record the lineage relation or equivalent explicit succession rule.

## 10. Universal audit procedure

1. Fix the audit object and audit question.
2. Fix scope, time, resolution, exclusions, and external standard.
3. If DSD formal layers are used, lock the interface profile and exact source revisions.
4. Preserve the original source, rule, claim, data, or procedure before reinterpretation.
5. Separate audit evidence status from DSD object status.
6. Reconstruct available alternatives where feasible.
7. Record selections and exclusions, including their criteria.
8. Record every material selector, bridge, allocation rule, or constitutive map.
9. Trace transitions between evidence, states, inferences, decisions, and identity-bearing components.
10. Separate fact, inference, norm, and decision.
11. Search for alternative describable explanations, minimal witnesses, counterexamples, boundary cases, and aggregate collisions.
12. Check definition, transition, structural, interface, and claim-level contradictions.
13. Check whether any reconstruction from compressed outputs has an injectivity basis.
14. Restrict the verdict to the strongest conclusion actually supported.
15. Record enough material for independent reconstruction or reproduction.

## 11. Core prohibitions

The framework adopts the following audit safeguards:

- **Not described does not mean false.**
- **Not observed does not automatically mean nonexistent.**
- **Possible does not mean established.**
- Undefinedness, absence, and numerical zero must not be silently identified.
- The same outcome must not be reverse-engineered into a unique cause, support, or decomposition without excluding alternatives or proving injectivity.
- Present knowledge must not be projected backward onto an earlier decision-maker unless that knowledge was available at the relevant time.
- A normative conclusion must not be presented as if it followed from facts alone when an additional norm is required.
- Cases must not be selectively excluded after the outcome is known merely to preserve a preferred DSD interpretation.
- Optional specialization data must not be promoted into universal DSD requirements.
- A property label or representation name must not be treated as a dynamic coefficient or structural law without an explicit bridge.
- A formation-level identity change must not be hidden inside ordinary value evolution.

## 12. Default verdict vocabulary

Use the narrowest suitable verdict.

| Verdict | Meaning |
|---|---|
| Confirmed | The relevant structure and formation path are sufficiently traceable within the stated scope. |
| Conditionally confirmed | Confirmation depends on explicit assumptions, environment, resolution, interface, or scope. |
| Partially confirmed | Only part of the audited structure or process is established. |
| Undetermined | Available describable information is insufficient for a determinate verdict. |
| Insufficient basis | Required evidence or specification for the claimed conclusion is absent. |
| Exclusion error | A materially relevant alternative, source, or branch was unjustifiably removed. |
| Transition error | A move from evidence/state to conclusion/state is not justified by the stated rule. |
| Norm conflation | Fact/inference and normative criteria are not kept distinct. |
| Contradiction | Definitions, states, interfaces, transitions, or claims are mutually incompatible. |
| Overclaim | The conclusion is stronger than the audited evidence permits. |

Multiple verdicts may be recorded when they refer to different layers.

## 13. Domain extension rule

The common frame should remain stable, while domain protocols add the field's own requirements.

Examples:

- Mathematics: definitions, axioms, proof steps, counterexamples, finite computation vs. general proof.
- Science: hypotheses, models, observation, uncertainty, alternative hypotheses, reproducibility.
- Law: evidence, procedure, authority, burden, historical information state, norms.
- Software: specification, implementation, execution environment, branch/state transitions, reproducibility.
- AI: inputs, tools, references, outputs, evaluation data, observable vs. unobservable process claims.
- History/media: primary sources, later interpretation, omission, quotation, temporal information state, competing interpretations.

Domain protocols should additionally state which DSD interface layers are actually used and which bridge, aggregation, reconstruction, or lineage checks are mandatory for that domain.

## 14. Minimum audit record

Every individual audit should contain at least:

```text
OBJECT
QUESTION
SCOPE
SOURCE
DSD_INTERFACE_LOCK
EVIDENCE_STATUS
OBJECT_STATUS
SELECTION
EXCLUSION
BRIDGES_OR_ALLOCATION_RULES
TRANSITIONS
LINEAGE_IF_REQUIRED
ALTERNATIVES
AGGREGATION_OR_RECONSTRUCTION_CHECK
WITNESS_OR_COUNTEREXAMPLE
CONTRADICTION_AUDIT
VERDICT
LIMITS
REPRODUCIBILITY
```

Use `templates/AUDIT_CASE_TEMPLATE.md` for actual cases.
