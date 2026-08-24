# Source Notes

## DSD source findings

### Static aggregation — fixed-support kernel

For fixed finite channel support `F`, Section 11 defines

`S_F : W_L^F -> W_L`, `S_F(y_F)=sum_{c in F} y_c`.

It proves:

- if `W_L != {0}` and `|F| >= 2`, then `ker S_F != {0}`;
- for any admissible record class `A_F subset W_L^F`, the restriction `S_F|A_F` is injective iff `(A_F-A_F) intersect ker S_F = {0}`;
- support-tagged records retain `F` explicitly so channel absence is not identified with a selected channel whose coordinate is zero;
- across varying supports, aggregate equality alone does not reconstruct support.

### Formation system

Formation Stage VII uses finite channel sets and explicitly permits composite-level coincidence below strict descriptive equivalence. Aggregate equality therefore cannot be promoted to full structural identity.

### Axis-property system

Reduced scalar or finite-coordinate summaries are not complete classifiers unless an additional reconstruction theorem is supplied.

## Standard mathematics comparison

### Congruence and quotient algebra

In universal algebra, a congruence is an equivalence relation compatible with the algebraic operations. A quotient algebra is well-defined only when the equivalence is a congruence. The kernel relation of an algebra homomorphism is a congruence.

Reference used: Peter Selinger, *Functionality, Polymorphism, and Concurrency*, basic universal algebra discussion of compatible relations and congruences, hosted by nLab.

### Quotient by kernel

For a linear map `T: V -> W`, vectors differing by an element of `ker T` have the same image, and the induced map `V/ker T -> im T` is an isomorphism.

Reference used: Stanford linear algebra notes, section on kernel/range and the homomorphism theorem.

## Source boundary

The standard results above are comparison mathematics. They do not alter the DSD source carrier. Any global linearization across varying DSD supports is an extra encoding and must be audited for loss of the absence-versus-zero distinction.