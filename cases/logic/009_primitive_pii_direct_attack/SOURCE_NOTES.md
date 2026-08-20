# Case 009 — Source Notes

## Primitive declaration structure
The current paper declares a global subfamily `Pi_bil_A subset Pi_A` of property kinds whose interpretation requires the supplied symmetric bilinear datum.

For each axis-applicable configuration `p`, the primitive bilinear layer independently supplies `K_bil_A subset K_ax_A` and, for every `p in K_bil_A`, a symmetric bilinear form

`b_A,p : E_amb_A,p x E_amb_A,p -> F`.

The normal input carrier is available exactly when `p in K_bil_A`.

## Primitive PII
For every `p in K_ax_A`, PII requires `p in K_bil_A` if either:

1. there exists `varpi in Pi_bil_A` such that the profile product is available and `Dom(Xi_A,p,varpi)` is nonempty; or
2. formal closure is active and its primitive `FormalBilDep_A(p)` bit is 1.

Cyclic-triadic and subspace declarations are omitted from PII because their typing already requires `p in K_bil_A`.

## Important source boundaries
- A property kind may be globally declared bilinear-dependent while having no defined local applications at a particular configuration.
- Property assignments are partial maps; empty application domain is a genuine absence of defined applications, not zero-valued data.
- Remark 3.12 states that a property name alone has no mathematical content and that additional compatibility laws may be required.
- Countermodel 9.7 explicitly demonstrates a PII failure: a bilinear-dependent property application is defined while `K_bil_A` is empty.
- The bilinear form is required to be symmetric but is not required by PII to be nondegenerate or positive definite.

## Layer order
P3 supplies primitive bilinear-domain data; P4 derives normal carriers; P5 supplies partial property assignments on available profile products; P7 supplies closure declarations and the formal bilinear-dependency bit. PII is therefore a final cross-layer admissibility condition, not a construction algorithm that creates the earlier P3 data retroactively.
