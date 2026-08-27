# DSD General Audit Framework

## 1. Purpose

The DSD General Audit Framework is a reusable audit layer inside **DSD Analysis**.
It is intended to trace how a claim, judgment, procedure, model, decision, or output is formed from describable information, selections, exclusions, transitions, and explicit criteria.

It is not a replacement for the validation standards of mathematics, science, law, software engineering, history, administration, or other fields.
Field-specific standards remain primary for field-specific truth, validity, legality, reproducibility, or performance judgments.

## 2. Position in DSD Analysis

```text
DSD Analysis
└─ General Audit Framework
   ├─ Domain Protocols
   └─ Individual Audit Records
```

Analysis and audit are related but distinct.

- **Analysis** decomposes and compares structures, states, relations, applicability, composition, and describability.
- **Audit** retraces the analysis and resulting claims under an explicit scope, procedure, and verdict rule.

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
Record which candidates, sources, branches, hypotheses, rules, or data were actually selected.

### E — Exclusion
Record what was excluded and why.
Exclusion is itself auditable.

### T — Transition
Record how one state, proposition, evidence set, or decision leads to the next.
A transition must not be inferred merely because two states are adjacent in the final narrative.

### C — Consistency
Check definitions, states, relations, transitions, and claims for internal contradiction or incompatible commitments.

### N — Norm
Separate factual and inferential content from normative, legal, policy, ethical, procedural, or evaluative criteria.

### O — Outcome
Record the final result and the maximum conclusion that the current audit actually supports.

## 5. Required distinctions

### 5.1 Descriptive status

Use at least these states:

- **Describable / established within scope**
- **Undetermined / insufficient**
- **Outside scope**

Do not convert an unknown state into a positive or negative conclusion merely to complete the audit.

### 5.2 Proposition layer

Keep these layers distinct:

- **Fact** — source material, observation, record, or established statement used as evidence.
- **Inference** — a conclusion derived from facts or other premises.
- **Norm** — a rule, criterion, value, law, policy, or evaluative standard.
- **Decision** — the selected action, judgment, classification, or conclusion.

### 5.3 Mapping strength

When DSD structures are compared with an external field, record one of:

- Direct correspondence
- Partial correspondence
- Correspondence after explicit additional encoding
- Non-correspondence

Do not treat terminological similarity as structural identity.

## 6. Universal audit procedure

1. Fix the audit object and audit question.
2. Fix scope, time, resolution, and exclusions.
3. Preserve the original source, rule, claim, data, or procedure before reinterpretation.
4. Separate describable, undetermined, and out-of-scope information.
5. Reconstruct available alternatives where feasible.
6. Record selections and exclusions, including their criteria.
7. Trace transitions between evidence, states, inferences, and decisions.
8. Separate fact, inference, norm, and decision.
9. Search for alternative describable explanations, minimal witnesses, counterexamples, and boundary cases.
10. Check definition, transition, structural, and claim-level contradictions.
11. Restrict the verdict to the strongest conclusion actually supported.
12. Record enough material for independent reconstruction or reproduction.

## 7. Core prohibitions

The framework adopts the following audit safeguards:

- **Not described does not mean false.**
- **Not observed does not automatically mean nonexistent.**
- **Possible does not mean established.**
- The same outcome must not be reverse-engineered into a unique cause without excluding alternatives.
- Present knowledge must not be projected backward onto an earlier decision-maker unless that knowledge was available at the relevant time.
- A normative conclusion must not be presented as if it followed from facts alone when an additional norm is required.
- Cases must not be selectively excluded after the outcome is known merely to preserve a preferred DSD interpretation.

## 8. Default verdict vocabulary

Use the narrowest suitable verdict.

| Verdict | Meaning |
|---|---|
| Confirmed | The relevant structure and formation path are sufficiently traceable within the stated scope. |
| Conditionally confirmed | Confirmation depends on explicit assumptions, environment, resolution, or scope. |
| Partially confirmed | Only part of the audited structure or process is established. |
| Undetermined | Available describable information is insufficient for a determinate verdict. |
| Insufficient basis | Required evidence or specification for the claimed conclusion is absent. |
| Exclusion error | A materially relevant alternative, source, or branch was unjustifiably removed. |
| Transition error | A move from evidence/state to conclusion/state is not justified by the stated rule. |
| Norm conflation | Fact/inference and normative criteria are not kept distinct. |
| Contradiction | Definitions, states, transitions, or claims are mutually incompatible. |
| Overclaim | The conclusion is stronger than the audited evidence permits. |

Multiple verdicts may be recorded when they refer to different layers.

## 9. Domain extension rule

The common frame should remain stable, while domain protocols add the field's own requirements.

Examples:

- Mathematics: definitions, axioms, proof steps, counterexamples, finite computation vs. general proof.
- Science: hypotheses, models, observation, uncertainty, alternative hypotheses, reproducibility.
- Law: evidence, procedure, authority, burden, historical information state, norms.
- Software: specification, implementation, execution environment, branch/state transitions, reproducibility.
- AI: inputs, tools, references, outputs, evaluation data, observable vs. unobservable process claims.
- History/media: primary sources, later interpretation, omission, quotation, temporal information state, competing interpretations.

## 10. Minimum audit record

Every individual audit should contain at least:

```text
OBJECT
QUESTION
SCOPE
SOURCE
DESCRIPTIVE_STATUS
SELECTION
EXCLUSION
TRANSITIONS
ALTERNATIVES
WITNESS_OR_COUNTEREXAMPLE
CONTRADICTION_AUDIT
VERDICT
LIMITS
REPRODUCIBILITY
```

Use `templates/AUDIT_CASE_TEMPLATE.md` for actual cases.
