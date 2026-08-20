# Case 008 — Source Notes

## Axis-property paper: exact PI interface

The fixed inherited background is the Stage-VI channel-complete formation record. For each describable configuration `p`, the inherited admitted channels are `C_L(p)`.

Definition 2.5 introduces primitive extension data:

- `K^ax_A ⊆ K^des_L`;
- for `p ∈ K^ax_A`, `C^ax_A,p ⊆ C_L(p)`.

Remark 2.6 explicitly states that the Formation Axiom System determines admitted operational channels but does not designate which admitted channels are axes. Selection is therefore primitive extension data. Any eligibility rule based on quantity-kind, role, or formation trace requires an additional predicate.

Definition 2.7 then supplies a finite-dimensional vector space `E^amb_A,p` over the scalar field and a partial function

`AxLine_A,p : C^ax_A,p ⇀ Gr_1(E^amb_A,p)`.

Thus **single-valuedness is already part of the type before PI is imposed**.

Primitive Axiom PI states

`Dom(AxLine_A,p) = C^ax_A,p`.

Accordingly PI adds totality on the selected set; at-most-one line per selected channel follows from the pre-axiom function type.

## Relevant existence statements

Countermodel 9.6 intentionally supplies one selected channel and an empty `AxLine` domain. It satisfies PII and the coherence clauses while failing PI. This establishes independence, not inconsistency.

Theorem 11.1 gives a trivial extension over every Stage-VI formation record by taking `K^ax_A = ∅`.

Theorem 11.4 assumes an explicit finite-dimensional vector space and an explicit line in `Gr_1(E_p)` for every selected channel. Under the remaining typing/coherence hypotheses, the supplied data determine a finitely specified realization.

Construction 11.5 uses `E_p = F^r`, explicit nonzero vectors, and `AxLine(c_s)=span{u_s}`.

## Scope statements

The paper states that the ambient realization carrier is configuration-relative representational data and is not automatically an ordinary physical ambient space.

Section 14.2 does not claim a physical law or dynamical realization.

Section 14.5 explicitly leaves additional comparison/branching layers undeveloped.

## Internal analytical consequence

Because both channel selection and line assignment are primitive extension data, inherited Stage-VI channel structure alone cannot force a geometric contradiction with PI unless an additional bridge constrains which channels must be selected or which lines they may realize.
