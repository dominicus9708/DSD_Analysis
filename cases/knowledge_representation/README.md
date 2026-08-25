# Knowledge Representation / Ontology / Classification

Status: **K_R-001–004 / Global Cases 039–042 first-pass analysis completed; K_R-005 next**.

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

## First-pass sequence

### K_R-001 / Global Case 039 — completed
**Open-World Non-Assertion versus Falsity**

Result: strong independent structural support. Absence of an assertion is not explicit falsity under OWL 2 model-theoretic entailment.

### K_R-002 / Global Case 040 — completed
**Class Membership versus Property Assertion**

Result: strong structural support within the same OWL semantic family. Declaration, class membership, domain/range/functionality constraints, and actual property assertion occupy distinct semantic roles. Not counted as a second fully independent external node yet.

### K_R-003 / Global Case 041 — completed
**Existential Restrictions and Anonymous Witnesses**

Result: strong structural support within the same OWL semantic family. An existential restriction forces existence of at least one suitable filler, while the filler need not be any particular named individual. Existence and named identity remain distinct.

### K_R-004 / Global Case 042 — completed
**Identity, Same-As, and Naming Non-Identity**

Result: strong structural support within the same OWL semantic family. Different names do not automatically imply distinct denotations; equal annotation labels do not imply identity; explicit equality/inequality and other semantic constraints determine identity relations.

### K_R-005 / Global Case 043 — next
**Provenance / Context-Sensitive Assertion Attribution**

Test whether equal proposition content from distinct sources/graphs/contexts remains structurally distinguishable when provenance matters.

## Anti-overcounting rule

Do not count multiple features of OWL or RDF as independent external confirmations merely because they are separate syntax forms. Group results by independent semantic mechanism and by independent external formalism.

## DSD boundary rule

Never identify:

- open-world unknown with DSD undefined;
- OWL class membership with DSD formation membership;
- RDF/OWL property assertion with a DSD channel;
- OWL existential restriction/filler with a DSD formation witness;
- `owl:sameAs` / `SameIndividual` with DSD operational identity or strict formation isomorphism.

The analysis is structural, not terminological.