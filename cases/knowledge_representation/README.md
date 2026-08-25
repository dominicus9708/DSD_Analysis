# Knowledge Representation / Ontology / Classification

Status: **K_R-001–005 / Global Cases 039–043 first-pass analysis completed; field synthesis completed**.

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

Result: strong structural support within the same OWL semantic family. Declaration, class membership, domain/range/functionality constraints, and actual property assertion occupy distinct semantic roles.

### K_R-003 / Global Case 041 — completed
**Existential Restrictions and Anonymous Witnesses**

Result: strong structural support within the same OWL semantic family. An existential restriction forces existence of at least one suitable filler, while the filler need not be any particular named individual.

### K_R-004 / Global Case 042 — completed
**Identity, Same-As, and Naming Non-Identity**

Result: strong structural support within the same OWL semantic family. Different names do not automatically imply distinct denotations; equal display labels do not imply identity; explicit or structure-implied semantic constraints determine identity.

### K_R-005 / Global Case 043 — completed
**Provenance / Context-Sensitive Assertion Attribution**

Result: strong structural support from a second independent external formal family. RDF Dataset preserves graph occurrence/content coordinates without automatically assigning provenance semantics to graph names, while W3C PROV explicitly represents attribution, roles, and derivation. Equal proposition content can therefore coexist with distinct provenance-sensitive records.

## Independent-family accounting

The five cases are grouped conservatively into two external formal families:

1. **OWL 2 semantic family** — K_R-001–004.
2. **RDF Dataset + W3C PROV provenance family** — K_R-005.

Separate OWL features are not counted as separate independent external confirmations merely because their syntax differs.

At the broader DSD Analysis level, K_R-005 reinforces the previously observed support/provenance-retention family rather than creating a wholly new global structural pattern.

## Anti-overcounting rule

Do not count multiple features of OWL, RDF, or PROV as independent external confirmations merely because they are separate syntax forms. Group results by independent semantic mechanism and independent external formalism.

## DSD boundary rule

Never identify:

- open-world unknown with DSD undefined;
- OWL class membership with DSD formation membership;
- RDF/OWL property assertion with a DSD channel;
- OWL existential restriction/filler with a DSD formation witness;
- `owl:sameAs` / `SameIndividual` with DSD operational identity or strict formation isomorphism;
- RDF graph names or PROV attribution with DSD formation-provenance labels, support tags, or formation traces.

The analysis is structural, not terminological.

## Closure

The K_R-001–005 first-pass sequence is closed. See `SYNTHESIS.md` for the field-level summary and handoff to the next DSD Analysis field.