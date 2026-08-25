# K_R-004 / Global Case 042 — Identity, Same-As, and Naming Non-Identity

Status: **first-pass analysis completed**.

Final judgment: **strong structural support within the OWL semantic family; not counted as a new fully independent external family yet**.

## 1. Different names do not imply different individuals

OWL 2 does not adopt the unique-name assumption by default. Two syntactically different individual names may denote the same domain element, or they may denote different domain elements, unless other axioms constrain the interpretation.

For two names `a` and `b`, a base ontology can therefore admit both:

- `M_same`: `a^I = b^I`;
- `M_distinct`: `a^I != b^I`.

Hence the base ontology entails neither `SameIndividual(a b)` nor `DifferentIndividuals(a b)`.

## 2. Explicit equality and inequality add real semantic constraints

Under OWL 2 Direct Semantics:

- `SameIndividual(a b)` requires `a^I = b^I`;
- `DifferentIndividuals(a b)` requires `a^I != b^I`.

Therefore equality and inequality are not inferred from lexical difference alone; they are semantic constraints on denotation.

## 3. Identity supports substitution

The OWL 2 Structural Specification notes that individuals made equal by `SameIndividual` can be used as synonyms without changing ontology meaning.

Thus if `SameIndividual(a b)` and `P(a,c)` hold, then the same denotations make `P(b,c)` hold as well.

This is stronger than merely attaching the same human-readable label to two names.

## 4. Same display label does not imply identity

OWL 2 Direct Semantics ignores annotations when interpreting the logical ontology. Therefore two named individuals can carry equal annotation/display labels while remaining unconstrained with respect to logical identity.

Thus:

`same annotation label != SameIndividual`.

This is a particularly useful distinction between presentation-level coincidence and model-theoretic identity.

## 5. Structural constraints can force equality without an explicit SameIndividual axiom

The lack of a unique-name assumption does not mean identity can only be asserted manually.

For example, if a functional object property has one source connected to two differently named targets, the functionality condition can force those targets to denote the same individual. The OWL 2 Structural Specification gives exactly this kind of example.

Therefore the valid hierarchy is not:

`different names -> different objects`.

Instead, denotational identity is determined by the full semantic constraint system.

## 6. Finite witness

```text
BASE MODELS: 2
BASE entails SameIndividual(a,b): False
BASE entails DifferentIndividuals(a,b): False
SAME-AXIOM MODELS: 1
SAME ontology entails SameIndividual(a,b): True
DIFFERENT-AXIOM MODELS: 1
DIFFERENT ontology entails DifferentIndividuals(a,b): True
SAME substitution P(a,c)->P(b,c): True
SAME-LABEL annotation models retained: 2
SAME-LABEL entails identity: False
FUNCTIONAL+two-edges MODELS: 1
FUNCTIONAL+two-edges entails SameIndividual(a,b): True
```

The script is a finite semantic witness for the equality/inequality pattern and is not a complete OWL reasoner.

## 7. DSD comparison

The Formation Axiom System does not define operational identity by a display label. An admitted operational channel is the typed tuple

`c=(p,a,lambda,v,rho)`.

Restriction/realization witness history is retained separately by `Tr_L(c)` and is not inserted into channel identity.

For cross-model comparison, strict descriptive equivalence is defined through structure-preserving bijections over the complete formation descriptor. The synthetic finite witness also establishes strict non-equivalence without relying on literal channel names.

The structural recurrence is therefore:

`surface name/label coincidence or difference != sufficient structural identity criterion`.

A stronger identity/equivalence criterion must come from the formal structure being used.

## 8. Non-identity boundary

Do not identify:

- OWL denotational equality with DSD operational-channel equality;
- OWL `SameIndividual` with DSD strict formation isomorphism;
- OWL `DifferentIndividuals` with DSD non-isomorphism;
- OWL annotation labels with DSD material/channel tags.

OWL equality is equality of individual denotations in one interpretation. DSD operational identity is typed tuple identity inside a formation model, while strict formation isomorphism is a structure-preserving relation between full descriptors.

## 9. Falsification attempts

### Hypothesis A — different names must denote different objects

Rejected. OWL 2 has no default unique-name assumption.

### Hypothesis B — same display label implies identity

Rejected. Annotation labels have no Direct-Semantics identity force.

### Hypothesis C — `SameIndividual` is only cosmetic renaming

Rejected. It constrains denotations and enables substitution of equal individuals in logical assertions.

### Hypothesis D — identity can never be inferred without an explicit `SameIndividual`

Rejected. Other semantic constraints, such as functionality or cardinality, can force differently named individuals to co-denote.

### Hypothesis E — DSD and OWL use the same identity relation

Rejected. Their identity/equivalence relations have different objects, levels, and purposes.

## 10. Independence accounting

K_R-004 adds a distinct identity/naming mechanism to the earlier OWL cases, but it remains inside the same OWL 2 formal family. It is therefore recorded as another strong internal convergence result rather than a fourth independent external confirmation.

## 11. Final judgment

**Strong structural support.** K_R-004 shows that a mature formal knowledge-representation system explicitly separates names, labels, denotational equality, denotational inequality, and structure-implied identity.

This is compatible with the DSD discipline that structural identity/equivalence is not reconstructed from surface naming or reduced presentation alone.

No contradiction with the current Formation Axiom System or axis-property system was found.

## 12. Next case

K_R-005 / Global Case 043 should analyze **provenance and context-sensitive assertion attribution**. The main question should be whether identical proposition content from different sources/graphs/contexts can remain distinguishable when provenance is part of the information structure.