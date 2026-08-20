# Case 006 — Public Announcement Logic and observer/update boundaries

## Goal

Stress-test whether DSD Formation silently imports external knowledge into configuration describability, and whether an epistemic information update can be identified with a DSD formation update without extra structure.

## External node

Public Announcement Logic (PAL) and Dynamic Epistemic Logic.

## DSD targets

- Primitive Axiom III and Definitional Closure Clause IV.
- The regime-relative character of `Desexpr_L` and `Descfg_L`.
- Full candidate-configuration retention and Remark 6.9 on induced subsets.

## Falsification questions

1. Does factual truth or external analyst knowledge force `Descfg_L(p)` without the declared DSD witness?
2. Can a public-announcement model restriction be identified with an internal DSD reduction while preserving the full formation semantics?
3. Does Formation already contain enough structure to represent epistemic accessibility and information update, or would such a mapping require extra encoding?

## Planned finite tests

- A two-world one-agent PAL model where a fact is true at the actual world but not known before announcement, and becomes known after a truthful public announcement.
- A DSD finite witness with a sound realization and all configuration-admission predicates true but `Desexpr_L(h)=false`, so the configuration remains non-describable despite the full external construction being known to the metatheory.
- A paired-regime witness in which only the regime-level describability primitive changes, making the same underlying material/configuration data describable in one regime but not the other.
- A deletion stress test showing that PAL-style restriction of alternatives is not automatically a formation submodel operation because DSD witness closure can be destroyed.

## Success / failure criteria

A DSD defect would be found if external truth alone forced a later DSD status, or if the paper claimed PAL-like update behavior without enough structure to define it. If instead DSD requires its own explicit witness data and PAL requires extra accessibility/update structure, the correct classification is partial methodological correspondence plus a scope boundary, not identity.
