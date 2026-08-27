# Knowledge Representation, Ontology, and Classification — Manuscript Preparation

Canonical scope: `K_R-001–005`.

## Central question

How should open-world non-assertion, class/property declaration, instance assertion, identity, naming, provenance, and context be separated, and how can DSD audit false automatic transitions among them?

## Recommended angle

**Non-Assertion, Identity, and Provenance in Knowledge Representation: A DSD Structural Audit**.

## Core mechanisms

- non-assertion != false under an Open World semantics;
- class/property declaration != instance assertion;
- name equality != entity identity;
- `sameAs` meaning is determined by the external standard semantics;
- provenance/context != the asserted proposition itself.

## Proposed sections

1. OWL/RDF/PROV source semantics.
2. Cluster `K_R-001–005`.
3. DSD typed/partial correspondence.
4. Identity/naming negative controls.
5. Provenance/context-sensitive attribution.
6. Non-correspondence to DSD terminology.
7. Conclusion.

## Source freeze

Pin OWL 2 Direct Semantics (W3C Recommendation, 2012-12-11), PROV-O (W3C Recommendation, 2013-04-30), and exact relevant sections.

## Overclaim guards

Do not claim Open World is a DSD axiom, non-assertion is false, or naming identity is object identity.