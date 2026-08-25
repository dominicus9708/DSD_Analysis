# K_R-005 / Global Case 043 — Provenance and Context-Sensitive Assertion Attribution

Status: first-pass analysis completed.

## Question

Can two records carry the same RDF proposition content while remaining structurally distinct because graph occurrence, source, attribution, role, or derivation metadata differ?

## External formalisms

- RDF 1.1 Dataset / Named Graph data model.
- W3C PROV-DM and PROV-O provenance model.

## Pressure tests

1. Equal triple content does not imply equal named-graph occurrence.
2. A graph name does not automatically mean source/provenance in RDF 1.1.
3. Explicit PROV attribution can distinguish two entities carrying equal content.
4. Qualified attribution can retain role/context beyond the bare agent relation.
5. Projecting full records to proposition content can be non-injective when provenance matters.

## DSD comparison target

Compare only the structural pattern

`equal reduced/content projection != equal support/provenance record`

with DSD support-tagged record retention and aggregate-level non-reconstruction.

Do not identify RDF graph names, PROV entities, agents, or attribution relations with DSD channels, formation labels, support tags, or formation traces.

## Independence rule

Because this case uses the RDF Dataset data model and the W3C PROV provenance model rather than OWL 2 Direct Semantics as the primary mechanism, evaluate it as a candidate second independent external convergence family. Do not count mere RDF syntax variation as a separate node.