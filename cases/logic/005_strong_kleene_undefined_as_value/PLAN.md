# Case 005 — Strong Kleene Three-Valued Logic

## Question

Test whether DSD `undefined` can be identified with the third semantic value of Strong Kleene logic without changing the DSD formal structure.

## DSD targets

1. Formation Stage-V partial assignment and Corollary 5.3.
2. Stage-VI consequence of assignment-domain exclusion.
3. Axis-property undefined application versus defined zero/value.

## External comparison node

Strong Kleene K3 uses a three-element semantic truth-value carrier. In Fitting's presentation the values are false, true, and bottom/unknown, with conjunction and disjunction determined by the truth ordering.

## Tests

1. **Type test:** compare DSD domain-exclusion undefinedness with a K3 semantic value.
2. **Lifted-encoding test:** encode a partial map faithfully into an enlarged disjoint codomain and determine what this does and does not prove.
3. **Semantic-operation test:** determine whether K3 truth operations can be transferred to DSD assignment status without new axioms.
4. **Channel test:** determine what happens if an external sentinel is fed back into Stage V as if it were an ordinary assignment value.
5. **Scope test:** determine whether the paper's phrase `undefined assignment is not a value` is formally correct or overbroad.

## Falsification criterion

A formal contradiction would require the current DSD definitions to both exclude undefined inputs from the assignment domain and simultaneously require them to carry an ordinary value of the original value space. No such contradiction is assumed in advance.
