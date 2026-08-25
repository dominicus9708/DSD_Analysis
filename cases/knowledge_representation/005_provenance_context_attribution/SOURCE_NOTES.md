# Source Notes — K_R-005 / Global Case 043

## RDF 1.1 Concepts and Abstract Syntax

W3C RDF 1.1 defines an RDF dataset as exactly one default graph plus zero or more named graphs. Each named graph is a pair of a graph name (IRI or blank node) and an RDF graph, and graph names are unique within a dataset.

Critical boundary: despite the term “named graph,” RDF 1.1 does not require the graph name to denote the graph and does not standardize a source/provenance interpretation for that name. The graph name is syntactically paired with the graph; applications need additional conventions or vocabulary to say what the name means.

The RDF 1.1 Primer gives a provenance-like example in which graph names are assumed to represent data sources, but explicitly notes that RDF itself provides no standard way to convey that assumption.

Primary sources:

- https://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/
- https://www.w3.org/TR/rdf11-primer/
- https://www.w3.org/TR/rdf11-datasets/ (Working Group Note on alternative dataset semantics; not a single normative provenance semantics)

## W3C PROV-DM / PROV-O

PROV-DM is a data model for provenance involving entities, activities, and agents, including responsibility/attribution and derivation relations.

PROV-O defines `prov:wasAttributedTo` as attribution of an entity to an agent. `prov:qualifiedAttribution` allows the attribution relation to carry additional information, such as a role. `prov:wasDerivedFrom` relates a derived entity to an entity from which it was derived.

Primary sources:

- https://www.w3.org/TR/prov-o/
- W3C PROV publications and PROV-DM family: https://www.w3.org/groups/wg/prov/publications/

## Important non-overclaiming boundary

RDF named graphs alone do not make a graph name a provenance source. In K_R-005, the bridge from a graph occurrence to a provenance entity/agent is explicit application data expressed using PROV. The analysis therefore uses a two-layer construction:

1. RDF Dataset preserves graph occurrence/name and graph content as distinct dataset coordinates.
2. PROV explicitly represents attribution/role/derivation for the entity chosen to represent that occurrence or information resource.

This prevents the analysis from silently treating an RDF graph name as semantically equivalent to a PROV source.