# K_R-005 / Global Case 043 — Provenance and Context-Sensitive Assertion Attribution

Status: **first-pass analysis completed**.

Final judgment: **strong structural support; accepted as a second independent external formal family within the knowledge-representation field, while not counted as a wholly new global structural pattern beyond the already established support/provenance-retention family**.

## 1. RDF Dataset separates graph occurrence from graph content

RDF 1.1 defines a dataset as one default graph plus zero or more named graphs. A named graph is a pair of a graph name and an RDF graph.

Therefore two graph occurrences may carry equal RDF graph content while occupying different named-graph coordinates in a dataset.

This already distinguishes:

`graph content`

from

`named graph occurrence / dataset position`.

However, RDF 1.1 does **not** require the graph name to denote the graph, its source, its publisher, or any provenance entity. The graph name is syntactically paired with the graph, but the intended meaning of that name requires additional conventions or vocabulary.

## 2. Named graph is not automatically provenance

A tempting overstatement would be:

`different graph name => different source/provenance`.

RDF 1.1 does not license this conclusion by itself. The RDF Primer gives source-oriented named-graph examples but explicitly notes that RDF provides no standard way to convey the assumption that graph names represent data sources.

Thus K_R-005 must use an explicit provenance layer rather than silently reading provenance semantics into graph names.

## 3. PROV explicitly represents attribution and provenance relations

W3C PROV-DM and PROV-O supply a separate provenance data model.

PROV-O defines `prov:wasAttributedTo` as attribution of an entity to an agent. A qualified attribution can retain additional information, including a role. PROV also provides derivation relations such as `prov:wasDerivedFrom`.

Consequently, an application may explicitly represent two information entities or graph-occurrence entities that carry equal proposition content but differ in attribution, role, derivation, generation history, or other provenance coordinates.

The provenance distinction is additional structured information, not a change to the proposition content itself.

## 4. Finite witness

The finite witness constructs two graph-occurrence records containing the same RDF triple but different graph names, attributed agents, and qualified roles.

```text
GRAPH CONTENTS EQUAL: True
GRAPH NAMES EQUAL: False
ATTRIBUTED AGENTS EQUAL: False
QUALIFIED ROLES EQUAL: False
FULL RECORDS EQUAL: False
CONTENT-ONLY DISTINCT COUNT: 1
FULL PROVENANCE-RECORD DISTINCT COUNT: 2
CONTENT PROJECTION LOSES PROVENANCE: True
```

The content projection has one distinct value because the triple sets are equal. The full provenance-sensitive record set has two distinct values.

Hence the projection

`full record -> proposition/graph content`

is non-injective in this witness.

## 5. Core structural result

The strongest result is:

`equal proposition content != equal provenance-sensitive information record`.

More explicitly:

`same triples`

need not imply

`same graph occurrence`,

`same attribution`,

`same responsible agent`,

`same role`,

or

`same derivation history`.

Conversely, different graph names alone do not establish any of those provenance differences unless an additional semantic convention or provenance relation is supplied.

## 6. DSD comparison

The current DSD static aggregation layer explicitly separates support-tagged channel/property records from their reduced aggregates. It proves that equal aggregate values do not by themselves reconstruct the underlying support-tagged records, and kernel criteria specify what additional reconstruction conditions would be needed.

The structural recurrence in K_R-005 is therefore:

`content/reduced projection equality != support/provenance-record equality`.

This is especially close to the DSD rule that reduced output does not reconstruct channel support or complete typed property structure.

Formation provenance and DSD support tags remain different objects from RDF graph names or PROV attribution records. The comparison is only the shared non-injectivity / record-retention pattern.

## 7. Non-identity boundary

Do not identify:

- an RDF graph name with a DSD formation-provenance label;
- an RDF named graph with a DSD operational channel or support-tagged record;
- a PROV Entity with a DSD configuration, channel, or property record;
- `prov:wasAttributedTo` with `Tr_L`, channel support, or any DSD formation relation;
- equal RDF triples with equal DSD aggregate values as the same mathematical operation.

The external standards and DSD use different objects, semantics, and purposes.

## 8. Falsification attempts

### Hypothesis A — equal triple content means the full information records are identical

Rejected. Two named graph/provenance records can contain the same triple set while retaining different names, agents, roles, or derivation records.

### Hypothesis B — a different RDF graph name automatically means a different source

Rejected. RDF 1.1 does not standardize that interpretation of graph names.

### Hypothesis C — named graphs alone are a complete provenance formalism

Rejected. RDF Dataset preserves graph partition/name coordinates, but provenance meaning requires explicit additional conventions or a provenance model such as PROV.

### Hypothesis D — provenance attribution changes the truth conditions of the proposition content

Rejected as a general claim. PROV describes responsibility, generation, derivation, and attribution of entities; retaining that metadata does not by itself rewrite the RDF proposition being carried.

### Hypothesis E — collapsing full records to proposition content is lossless

Rejected whenever provenance is part of the required information structure. The finite witness is explicitly non-injective under content-only projection.

## 9. Independence accounting

K_R-001–004 were all tested primarily inside OWL 2 Direct Semantics.

K_R-005 instead uses:

- the RDF Dataset / Named Graph data model for graph occurrence and content separation;
- W3C PROV-DM / PROV-O for explicit provenance attribution and qualification.

Although PROV-O is serialized as an OWL ontology, the operative mechanism here is the independent W3C provenance data model together with RDF dataset structure, not the OWL open-world, class, existential, or identity mechanisms tested in K_R-001–004.

Therefore K_R-005 is accepted as a **second independent external formal family within this knowledge-representation field**.

At the broader DSD Analysis level, however, it is not counted as a wholly new structural pattern because database analysis and DSD static aggregation already established the more general family:

`reduced/content equality != support/provenance equality`.

K_R-005 strengthens that family by showing the same separation in a dedicated standards-based provenance architecture.

## 10. Final judgment

**Strong structural support.** RDF Dataset and W3C PROV demonstrate that proposition content, graph occurrence, responsible agent, role, and provenance lineage can occupy distinct information coordinates. A content-only projection can erase those distinctions.

This is compatible with the DSD discipline of retaining support/provenance-bearing records separately from reduced aggregates or readouts.

No contradiction with the current Formation Axiom System, axis-property system, or channel-indexed static aggregation layer was found.

## 11. Field-level consequence

K_R-001–005 now provide two conservatively distinct external formal families:

1. **OWL 2 semantic family** — non-assertion/falsity, declaration/assertion, existential witness, and naming/identity separation.
2. **RDF Dataset + W3C PROV family** — content occurrence and explicit provenance/attribution separation.

The first-pass knowledge-representation sequence can therefore be closed and synthesized before moving to the next major DSD Analysis field.