# Source Notes — K_R-002 / Global Case 040

## W3C OWL 2 Direct Semantics

Primary URL: https://www.w3.org/TR/owl2-direct-semantics/

Relevant semantics:

- OWL 2 declarations are used for syntactic/type disambiguation and are not given an additional Direct-Semantics satisfaction clause.
- A class is interpreted as a subset of the object domain.
- An object property is interpreted as a subset of the Cartesian square of the object domain.
- `ClassAssertion(C a)` requires the interpretation of `a` to belong to the class extension of `C`.
- `ObjectPropertyAssertion(P a b)` requires the pair `(a,b)` to belong to the object-property extension of `P`.
- `ObjectPropertyDomain(P C)` means every existing `P` pair has its first component in `C`.
- `ObjectPropertyRange(P D)` means every existing `P` pair has its second component in `D`.
- `FunctionalObjectProperty(P)` means that two `P` pairs with the same first component must have the same second component. It does not require any pair to exist.

These clauses make the directionality explicit: domain/range/classification constraints can classify endpoints of an existing relation, but do not reverse into an existence assertion for a relation.

## W3C OWL 2 Structural Specification

Primary URL: https://www.w3.org/TR/owl2-syntax/

Relevant point:

Declarations type IRIs as classes, object properties, data properties, etc. The typing constraints disambiguate entity kinds. This is distinct from an object-property assertion that connects two individuals.

## DSD source comparison

Source: `DSD_Axioms for the Property Structure of Realized Axes_EN.pdf`.

Relevant structure:

- Definition 3.1: global declared property kinds `Pi_A` are selected independently of configuration-level carrier availability.
- Definition 3.2: typed input carriers are interpreted per configuration and can be unavailable.
- Definition 3.3: when a kind is declared and the profile carrier is available, the property layer still supplies a partial assignment map; its application domain is separate.
- Definition 3.10: undeclared, unavailable input, undefined application, defined zero, defined nonzero/value are distinct statuses.
- Proposition 5.3: a bare realized line does not determine unary property values.

## Non-identity boundary

OWL declarations, class membership, property relations, and DSD property declarations/assignments belong to different formal systems. The comparison is the separation of declaration/classification/constraint from actual assigned relational content, not an identification of primitives.