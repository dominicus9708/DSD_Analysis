# Source Notes — K_R-004 / Global Case 042

## External primary sources

### W3C OWL 2 Direct Semantics (Second Edition)
URL: https://www.w3.org/TR/owl2-direct-semantics/

Relevant semantics:

- `SameIndividual(a1 ... an)` is satisfied when all named individuals have equal interpretations.
- `DifferentIndividuals(a1 ... an)` is satisfied when each pair of distinct listed names has unequal interpretations.
- ontology entailment requires the conclusion to hold in every model.
- annotations have no semantic meaning in OWL 2 Direct Semantics.

### W3C OWL 2 Structural Specification and Functional-Style Syntax (Second Edition)
URL: https://www.w3.org/TR/owl2-syntax/

Relevant points:

- OWL 2 does not make the unique-name assumption.
- `SameIndividual` makes names interchangeable with respect to ontology meaning.
- `DifferentIndividuals` can explicitly axiomatize distinctness for selected individual names.
- functionality/cardinality constraints can indirectly force differently named individuals to be equal.

### W3C OWL 2 Primer
URL: https://www.w3.org/TR/owl2-primer/

Relevant point:

Different names are not automatically different individuals; explicit identity or difference information may be needed.

## DSD primary source

### Formation Axiom System
Source: `DSD_Formation_Axiom_System_EN.pdf`

Relevant results:

- An operational channel is the typed tuple `c=(p,a,lambda,v,rho)`.
- restriction and realization histories are retained but are not additional channel-identity coordinates.
- Definition 3.5 / Theorem 3.6 preserve formation-trace information without inserting witness history into operational identity.
- strict descriptive equivalence is defined using structure-preserving bijections over the full formation descriptor.
- the synthetic finite witness contains a strict non-equivalence argument that does not rely on literal channel names.

## Boundary

Do not identify OWL denotational equality with DSD channel identity or strict formation isomorphism. The comparison concerns the insufficiency of surface naming or reduced presentation as a standalone structural identity criterion.