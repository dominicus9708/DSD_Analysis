# K_R-002 / Global Case 040 — Class/Property Vocabulary versus Actual Property Assertion

Status: **first-pass analysis completed**.

Final judgment: **strong structural support within the OWL semantic family; not counted as a new fully independent external node yet**.

## 1. Core semantic separation

OWL 2 Direct Semantics interprets classes and object properties through different coordinates:

- a class is interpreted as a subset of the object domain;
- an object property is interpreted as a binary relation over the object domain;
- `ClassAssertion(C a)` constrains class membership;
- `ObjectPropertyAssertion(P a b)` constrains relation membership.

These conditions are not interchangeable.

## 2. Declaration does not instantiate a property relation

OWL 2 declarations are used to disambiguate the syntactic/type role of entities. Direct Semantics does not give declarations an additional satisfaction condition that would require a nonempty class or property extension.

Therefore declaring an object property `P` does not itself create any pair in the interpretation of `P`.

This provides a clean distinction between **property vocabulary/type availability** and **actual relational content**.

## 3. Domain and range are directional constraints

Direct Semantics defines:

`ObjectPropertyDomain(P C)`

as the condition that every pair `(x,y)` already in `P` has `x` in `C`.

Likewise,

`ObjectPropertyRange(P D)`

requires every existing `P` pair to have its second component in `D`.

Hence the valid direction is:

`P(a,b) + Domain(P,C) => C(a)`

and

`P(a,b) + Range(P,D) => D(b)`.

The converse does not generally hold. `C(a)` together with `Domain(P,C)` does not generate a `P` edge.

## 4. Functional property does not imply existence

`FunctionalObjectProperty(P)` says that if two `P` pairs share a first component, their second components must coincide. A model with no `P` pair vacuously satisfies this condition.

Thus functionality constrains multiplicity of existing relations but does not provide existence.

## 5. Finite witness

Two models were constructed over the same class and property constraints:

```text
M_empty: class=True domain=True range=True functional=True P(a,b)=False
M_edge: class=True domain=True range=True functional=True P(a,b)=True
ADMISSIBLE MODELS: 2
CONSTRAINT SET entails P(a,b): False
REVERSE DIRECTION with actual P(a,b): domain classifies a in C and range classifies b in D
```

Both models satisfy the same class membership, domain, range, and functional constraints. Only one contains the concrete relation.

Therefore:

`class membership + property type/constraints != actual property assertion`.

## 6. DSD comparison

The DSD axis-property system explicitly separates:

1. candidate property-kind universe;
2. globally declared property kinds;
3. configuration-level typed input carrier availability;
4. partial property assignment;
5. derived application domain;
6. undefined versus defined-zero/nonzero/value statuses.

It also states that property declarations are independent of configuration-level carrier availability and that a bare realized line does not determine its unary property values.

The structural recurrence is therefore strong:

`declared property kind != available application != defined assignment/value`.

OWL 2 expresses a different formal architecture, but likewise separates class/vocabulary declarations and implication-style constraints from actual assertion membership in a property relation.

## 7. Non-identity boundary

Do not identify:

- OWL class membership with DSD axis applicability;
- OWL declarations with DSD global property declarations as identical primitives;
- OWL object-property assertions with DSD property assignments;
- OWL property relations with DSD operational channels.

The semantic layers and purposes differ. Only the non-collapse pattern is compared.

## 8. Falsification attempts

### Hypothesis A — declaring `P` requires at least one `P` relation

Rejected. OWL declarations are typing/disambiguation devices and do not require nonempty property extensions.

### Hypothesis B — `C(a)` plus `Domain(P,C)` entails some `P(a,b)`

Rejected. A model with an empty `P` relation satisfies both conditions.

### Hypothesis C — adding range and functionality forces a relation

Rejected. Empty `P` still satisfies domain, range, and functionality.

### Hypothesis D — class and property layers are completely independent

Rejected as an overstatement. Once an actual property assertion exists, domain/range axioms can entail endpoint class membership. The correct result is directional separation, not total disconnection.

## 9. Independence accounting

K_R-002 is materially different from K_R-001: it tests the separation of semantic coordinates and the direction of implication-style property constraints rather than only open-world non-entailment.

However, both cases use the same OWL 2 Direct-Semantics framework. For conservative DSD Analysis bookkeeping, K_R-002 is therefore recorded as a **distinct strong structural result within the same external semantic family**, not yet as a second fully independent external confirmation.

Independent-node counting should be revisited after comparison with another knowledge-representation or classification formalism.

## 10. Final judgment

**Strong structural support.** OWL 2 gives a precise external example in which vocabulary/type declaration, class membership, relation constraints, and actual property assertion occupy distinct semantic roles. This aligns closely with the DSD axis-property discipline that declaration and application/value assignment are separate stages.

No contradiction with the current Formation Axiom System or axis-property system was found.

## 11. Next case

K_R-003 / Global Case 041 should analyze **existential restrictions and anonymous witnesses**: whether a formalism can require that some relation target exist without requiring a named or explicitly asserted filler. This provides the next step from 'constraint does not imply a relation' to 'a stronger constraint can imply existence while still not fixing identity'.