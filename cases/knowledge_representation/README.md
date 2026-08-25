# Knowledge Representation / Ontology / Classification

Status: **first-pass analysis started**.

Starting global case: **039**.

## Naming convention

Field-case identifiers use the form `K_R-###`.

The previous preparation-only `KR-###` spelling is superseded by `K_R-###` from Global Case 039 onward.

## Field objective

Test whether formal knowledge-representation and classification systems independently distinguish layers such as:

- object/entity existence;
- class membership;
- vocabulary/property existence;
- property applicability or relation eligibility;
- assertion presence;
- known falsity/negation;
- unknown or non-asserted status;
- identity/equivalence;
- provenance/context.

The purpose is not to rename these mechanisms as DSD. Each external formalism must retain its own semantics.

## Planned first-pass sequence

### K_R-001 / Global Case 039
**Open-World Non-Assertion versus Falsity**

Test whether absence of an assertion in an OWL-style knowledge base is semantically equivalent to falsity. Compare only the structural non-conflation role with DSD `undefined != defined false/zero`.

### K_R-002 / Global Case 040
**Class Membership versus Property Assertion**

Test whether class membership or vocabulary declaration forces every relevant property assertion/value for an instance.

### K_R-003 / Global Case 041
**Existential Restrictions and Anonymous Witnesses**

Test whether an existential requirement can be satisfied without a named/explicitly identified filler, and how that differs from a concrete asserted relation.

### K_R-004 / Global Case 042
**Identity, Same-As, and Naming Non-Identity**

Test whether same labels/names/identifiers imply object identity, and how explicit identity relations change inference.

### K_R-005 / Global Case 043
**Provenance / Context-Sensitive Assertion Attribution**

Test whether equal proposition content from distinct sources/graphs/contexts remains structurally distinguishable when provenance matters.

## Anti-overcounting rule

Do not count multiple features of OWL or RDF as independent external confirmations merely because they are separate syntax forms. Group results by independent semantic mechanism and by independent external formalism.

## DSD boundary rule

Never identify:

- open-world unknown with DSD undefined;
- OWL class membership with DSD formation membership;
- RDF/OWL property assertion with a DSD channel;
- OWL existential restriction with a DSD formation witness;
- `owl:sameAs` with DSD object identity without explicit comparison.

The analysis is structural, not terminological.