# K_R-003 / Global Case 041 — Existential Restriction and Anonymous Witness

Status: **first-pass analysis completed**.

Final judgment: **strong structural support within the OWL semantic family; distinct from K_R-001/002 but not counted as a new fully independent external family yet**.

## 1. Core semantic result

OWL 2 Direct Semantics interprets

`ObjectSomeValuesFrom(P C)`

as the set of individuals `x` for which there exists at least one domain element `y` with both:

- `(x,y)` in the interpretation of `P`;
- `y` in the interpretation of `C`.

Thus if `a` is asserted to belong to `ObjectSomeValuesFrom(P C)`, every model must contain at least one suitable `P`-successor in `C`.

This is stronger than the underconstrained situation in K_R-001/002: existence is now forced.

## 2. Existence does not fix a named filler

Consider a named individual `b`. Two models can satisfy the same existential assertion:

- one model uses an unnamed domain element `w` as the `P`-successor in `C`;
- another model uses the named individual `b`.

Therefore the ontology entails that **some** suitable filler exists, but does not in general entail `P(a,b)` or `C(b)`.

Formally:

`a in ObjectSomeValuesFrom(P C)`

does not imply, for an arbitrary named `b`,

`P(a,b)`.

## 3. Finite witness

```text
M_UNNAMED satisfies existential: True
M_UNNAMED P(a,b): False
M_UNNAMED C(b): False
M_NAMED_B satisfies existential: True
M_NAMED_B P(a,b): True
M_NAMED_B C(b): True
EXISTENTIAL entails existence of some P-successor in C: True
EXISTENTIAL entails P(a,b): False
EXISTENTIAL entails C(b): False
```

This finite witness instantiates the Direct-Semantics existential clause. It is not a complete OWL reasoner.

## 4. Relation to K_R-001 and K_R-002

K_R-001: silence did not determine truth or falsity.

K_R-002: declarations/classification/constraints did not by themselves generate a property edge.

K_R-003: a stronger existential restriction **does** force a suitable property edge to some filler, but leaves the filler identity/name underdetermined.

The three cases therefore form a useful progression:

`no existential requirement -> relation may be absent`

`existential requirement -> at least one relation must exist`

`existential requirement alone -> no particular named filler is fixed`.

## 5. DSD comparison

The DSD Formation Axiom System defines a formation trace `Tr_L(c)` collecting restriction-realization witnesses for candidate channel `c` and proves:

`c in C_L iff Tr_L(c) != empty`.

At the same time the operational channel identity remains the five-tuple `(p,a,lambda,v,rho)`; the witness history is recorded separately rather than inserted into channel identity.

The structural recurrence is therefore:

`existence of at least one admissible witness != identity/history of a particular witness`.

This is a strong comparison point with the OWL existential case, where existence of a filler is forced while its naming/identity need not be determined by the existential condition.

## 6. Non-identity boundary

Do not identify:

- an OWL existential filler with a DSD formation-trace witness;
- an OWL object-property edge with a DSD operational channel;
- OWL class-expression membership with DSD channel admission;
- lack of a named OWL filler with DSD undefined assignment.

OWL fillers are domain elements satisfying a model-theoretic existential class condition. DSD trace witnesses are explicit restriction-realization records inside the staged formation system.

## 7. Falsification attempts

### Hypothesis A — existential restriction does not require any actual successor

Rejected. The Direct Semantics contains an existential quantifier over a relation successor in the filler class.

### Hypothesis B — existential restriction identifies a unique named filler

Rejected. Different models may satisfy the existential with different domain elements, including unnamed ones.

### Hypothesis C — if `b` is a named individual in the ontology, the existential must choose `b`

Rejected. A model can satisfy the existential with an unnamed element while leaving `P(a,b)` false.

### Hypothesis D — existential witness identity is irrelevant in every downstream theory

Rejected as an overstatement. Additional axioms such as `ObjectHasValue`, nominals, cardinality/identity constraints, or explicit property assertions can constrain or identify fillers. The result concerns the existential restriction by itself.

## 8. Independence accounting

K_R-003 is semantically distinct from K_R-001 and K_R-002, but all three are still drawn from OWL 2 Direct Semantics.

For conservative DSD Analysis bookkeeping, K_R-003 is recorded as another **strong structural result within the same external formal family**, not as a third independent external confirmation.

## 9. Final judgment

**Strong structural support.** K_R-003 shows that a formal semantic system can separate a positive existence requirement from the identity or name of the particular witness that satisfies it.

This aligns well with the DSD practice of distinguishing witness existence from operational identity/history, while preserving the non-identity of the two formalisms.

No contradiction with the Formation Axiom System or axis-property system was found.

## 10. Next case

K_R-004 / Global Case 042 should analyze **identity, same-as, and naming non-identity**: whether different names must denote different objects, whether equal labels imply identity, and what explicit identity axioms contribute.