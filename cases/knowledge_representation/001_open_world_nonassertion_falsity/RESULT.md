# K_R-001 / Global Case 039 — Open-World Non-Assertion versus Falsity

Status: **first-pass analysis completed**.

Final judgment: **strong independent structural support**, with a strict semantic non-identity boundary.

## 1. External semantic result

OWL 2 Direct Semantics defines ontology entailment model-theoretically: `O` entails `O1` only when every model of `O` is also a model of `O1`.

For an object property `P` and named individuals `a,b`, the semantics distinguish:

- positive assertion: `(a,b)` belongs to the interpretation of `P`;
- negative assertion: `(a,b)` does not belong to the interpretation of `P`.

If the ontology contains neither assertion nor another axiom constraining this pair, two models can coexist:

- Model M0: `P(a,b)` is false;
- Model M1: `P(a,b)` is true.

Therefore silence about `P(a,b)` entails neither `P(a,b)` nor `not P(a,b)`.

This is the precise formal core of the open-world distinction relevant to this case.

## 2. Explicit negative information is stronger than silence

OWL 2 provides `NegativeObjectPropertyAssertion` as an explicit axiom form. Under Direct Semantics, every model satisfying such an axiom must exclude the specified pair from the object-property extension.

Hence:

`non-assertion != explicit negative assertion`.

The difference is semantic, not merely syntactic presentation.

## 3. Class membership does not automatically determine an unrelated property value

Suppose `ClassAssertion(C a)` is asserted, while no axiom constrains `P(a,b)`.

Both a model with `P(a,b)` and a model without `P(a,b)` remain compatible with the class assertion. Thus class membership alone does not provide an arbitrary concrete property assertion.

This is relevant to the DSD axis-property comparison because declaration or classification does not by itself imply assignment of every downstream property value.

## 4. Closed-world contrast

A system may add a rule such as:

`if P(a,b) is not derivable, treat P(a,b) as false`.

That rule can be useful in validation, databases, rule systems, or local-completeness settings, but it is an additional closed-world/completeness assumption. It is not a consequence of OWL 2 Direct Semantics.

The OWL 2 Primer explicitly contrasts OWL's open-world behavior with closed-world database practice.

## 5. Finite countermodel witness

The reproducibility script enumerates the two truth assignments for one unconstrained property pair.

Expected output:

```text
BASE MODELS: 2
BASE entails P(a,b): False
BASE entails not P(a,b): False
NEGATIVE-ASSERTION MODELS: 1
NEGATIVE ontology entails not P(a,b): True
POSITIVE-ASSERTION MODELS: 1
POSITIVE ontology entails P(a,b): True
CLASS-ONLY: C(a) leaves P(a,b) free across 2 P-variants
CLOSED-WORLD policy on absent P(a,b): false (extra rule, not OWL entailment)
```

This script is not an OWL 2 reasoner. It is a finite model-theoretic witness for the exact relation-membership condition used in the Direct Semantics.

## 6. DSD comparison

The Formation Axiom System distinguishes undefined assignment from defined zero and proves that zero-padding is not assignment-faithful. The axis-property system separately distinguishes undefined application from defined zero-valued application.

The structural recurrence is:

`not established / not assigned != explicit negative or defined zero`.

However, the semantics are different:

| OWL / knowledge representation | DSD | Boundary |
| --- | --- | --- |
| non-entailment of `P(a,b)` | undefined or non-formed status may occur | analogy only |
| explicit negative property assertion | defined negative proposition in the external formalism | not a DSD zero or undefined state |
| open set of admissible models | partial typed assignment/formation architecture | different semantic level |
| class membership without property assertion | declared/applicable structure without automatic value assignment | structural comparison only |

## 7. Why this is independent of DB-001

DB-001 concerned storage/query states such as row absence, SQL NULL, and defined zero.

K_R-001 instead concerns universal model-theoretic entailment in a formal knowledge-representation language. The obstruction is not caused by a nullable storage cell. It arises because multiple admissible interpretations remain possible.

Therefore K_R-001 should count as an **independent convergence node** relative to the database NULL family, while still avoiding any claim that OWL semantics and DSD partial assignment are identical.

## 8. Falsification attempts

### Hypothesis A — if `P(a,b)` is not asserted, then `not P(a,b)` follows

Rejected. A model in which `P(a,b)` holds remains admissible when the ontology does not constrain the pair.

### Hypothesis B — explicit negative assertion adds no information beyond silence

Rejected. `NegativeObjectPropertyAssertion(P a b)` removes all models in which the pair belongs to `P`.

### Hypothesis C — membership in class `C` automatically supplies a concrete value for property `P`

Rejected without an additional axiom that entails such a property assertion.

### Hypothesis D — closed-world inference contradicts the open-world result

Rejected as a contradiction claim. Closed-world reasoning adds a different semantic/completeness assumption; it changes the inference regime rather than refuting OWL 2 Direct Semantics.

## 9. Final judgment

**Strong independent structural support.** K_R-001 provides a non-database, model-theoretic external node showing that lack of established information must not generally be totalized into explicit falsity.

The result aligns with DSD's non-conflation discipline but does not prove DSD from OWL. The strongest defensible statement is independent convergence on the need to preserve the distinction between an unestablished status and a defined opposing/zero-valued status.

No contradiction with the Formation Axiom System or axis-property system was found.

## 10. Next case

K_R-002 / Global Case 040 should analyze **class membership / property vocabulary versus actual property assertion or value assignment**, using OWL 2 class/property semantics and restrictions while avoiding overlap with K_R-001's open-world non-entailment mechanism.