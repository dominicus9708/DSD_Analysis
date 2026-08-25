# Reproducibility — K_R-005 / Global Case 043

The Python witness is intentionally small and dependency-free. It is not a complete RDF, SPARQL, PROV, or OWL reasoner.

It instantiates the structural distinction tested in this case:

- two graph occurrences may carry exactly the same RDF triple content;
- their graph names, attributed agents, and qualified roles may differ;
- a projection that retains only triple content collapses the two records;
- the full provenance-sensitive records remain distinct.

Run from the repository root:

```bash
python cases/knowledge_representation/005_provenance_context_attribution/repro/check_provenance_projection.py
```

Compare stdout with:

`cases/knowledge_representation/005_provenance_context_attribution/repro/expected_output.txt`

The script does not claim that RDF graph names automatically denote provenance sources. Source attribution is represented as explicit additional record data, corresponding to the use of a provenance model such as W3C PROV.