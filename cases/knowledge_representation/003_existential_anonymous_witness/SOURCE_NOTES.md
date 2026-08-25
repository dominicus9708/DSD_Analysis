# Source Notes — K_R-003 / Global Case 041

## W3C OWL 2 Direct Semantics

Primary source: https://www.w3.org/TR/owl2-direct-semantics/

Relevant semantics:

`ObjectSomeValuesFrom(OPE CE)` is interpreted as the class of all `x` for which there exists some `y` such that `(x,y)` belongs to the object-property interpretation of `OPE` and `y` belongs to the class interpretation of `CE`.

Therefore membership in an existential restriction requires existence of at least one suitable domain element, but the semantic clause itself does not require that this element be denoted by a particular named individual.

## W3C OWL 2 Primer

Primary explanatory source: https://www.w3.org/TR/2012/REC-owl2-primer-20121211/

The Primer's parent/child example explains that from an existential restriction one may know that an individual has at least one child even if the child's name is unknown.

## DSD Formation Axiom System

Source: `DSD_Formation_Axiom_System_EN.pdf`.

Definition 3.5 defines the formation-trace set `Tr_L(c)` as the set of restriction-realization witnesses that form candidate channel `c`.

Theorem 3.6 gives:

`c in C_L iff Tr_L(c) != empty`.

The operational identity of `c` remains the five-tuple `(p,a,lambda,v,rho)`; witness history is not inserted into channel identity.

This is only a structural comparison. An OWL existential filler is not a DSD trace witness.

## Boundary

The common pattern is limited to:

`existence of at least one witness/filler != identification of a particular witness/filler`.

The two theories implement this pattern at different semantic layers.