# Source Notes — K_R-001 / Global Case 039

## External primary sources

### W3C OWL 2 Direct Semantics (Second Edition)
URL: https://www.w3.org/TR/owl2-direct-semantics/

Relevant points:

- `ObjectPropertyAssertion(P a b)` is satisfied exactly when the interpretation pair for `a,b` belongs to the object-property extension of `P`.
- `NegativeObjectPropertyAssertion(P a b)` is satisfied exactly when that pair does **not** belong to the extension of `P`.
- Ontology entailment is universal over models: ontology `O` entails ontology `O1` only if every model of `O` is also a model of `O1`.

Consequently, if an ontology leaves `P(a,b)` unconstrained and has one model with the pair in `P` and another model without the pair, neither the positive nor negative assertion is entailed.

### W3C OWL 2 Primer (Second Edition)
URL: https://www.w3.org/TR/owl2-primer/

Relevant point:

OWL 2 explicitly follows an open-world assumption: a fact absent from an OWL document may simply be missing and can still be true. The Primer contrasts this with a closed-world database-style assumption.

### W3C OWL 2 Structural Specification and Functional-Style Syntax (Second Edition)
URL: https://www.w3.org/TR/owl2-syntax/

Relevant point:

OWL 2 provides explicit positive and negative object/data property assertions. An explicit negative assertion is therefore not represented merely by the absence of the corresponding positive assertion.

## DSD primary sources

### Formation Axiom System
Source: `DSD_Formation_Axiom_System_EN.pdf`

Relevant results:

- Corollary 5.3: undefined assignment is not a value and cannot be inferred to equal distinguished zero.
- Proposition 5.4: zero-padding is not assignment-faithful because an out-of-domain item and a defined-zero item can acquire the same totalized value while their domain statuses differ.
- Proposition 5.12: an absent channel is not a zero term.

### Axioms for the Property Structure of Realized Axes
Source: `DSD_Axioms for the Property Structure of Realized Axes_EN.pdf`

Relevant results:

- Definition 3.10 separates undeclared, unavailable input, undefined application, defined zero, defined nonzero, and defined value statuses.
- Proposition 3.11 states that undefined is not zero.

## Non-identity boundary

Do not identify OWL open-world non-entailment with DSD undefined assignment.

OWL non-entailment concerns truth across all admissible interpretations of a knowledge base. DSD undefined assignment concerns membership outside a partial assignment domain in a typed staged formation/property architecture.

The comparison is only the non-conflation pattern: lack of established positive information is not automatically an explicit negative/zero-valued state.