# Case 010 — Source Audit Notes

## Formation Axiom System

The integrated attack uses the fixed Formation Stage-VI record as the inherited base.

Relevant source facts:

- Formation Stage VI admits an operational channel only from a describable configuration, an actual Stage-V assignment, and a declared role.
- The operational tag retains the tuple `(p,a,lambda,v,rho)`.
- Formation Theorem 7.1 gives an explicit one-point full model and shows the full Formation model class is nonempty relative to the background set theory.
- The Stage-VI interface is fixed before Formation Stage VII finite composition.

For a nontrivial Case-010 base, the Theorem-7.1 one-point construction may be duplicated only in its role coordinate: two admitted roles `rho1 != rho2` over the same `p,a,lambda,v` produce two distinct Stage-VI channel tags. This uses the already established Formation rule that role differences can create distinct channels.

## Axis-Property System — inherited interface

Definition 2.5 requires

`K_ax_A subset K_des_L`

and for each axis-applicable configuration

`C_ax_A,p subset C_L(p)`.

Thus selected axis channels are inherited admitted Formation channels rather than new operational channels.

Remark 2.6 explicitly says Formation does not determine which admitted channels are axes; axis selection is primitive extension data.

Definition 2.7 supplies the ambient vector space and the primitive partial map

`AxLine_A,p : C_ax_A,p ⇀ Gr_1(E_amb_A,p)`.

Remark 3.4 states that extension-level property assignments do not alter Formation assignments `q_L,lambda`, do not alter `Gamma_L,lambda`, and do not create new operational channels in `L`.

## Layer ordering

Definition 4.5 gives the staged dependency structure:

- P0: fixed inherited Formation Stage-VI record;
- P1: primitive axis applicability, selection, ambient carrier, partial `AxLine`;
- P2: primitive property declarations;
- P3: primitive bilinear-domain data and symmetric bilinear forms;
- P4: derived tagged axes, distinct lines, span/rank, subspace and normal carriers;
- P5: dependent primitive partial property assignments;
- P6: derived domains, statuses, line-factor maps, property-record sets;
- P7: dependent primitive representation/closure declarations and witness data;
- P8: derived closure-dependency readout, representations, requirements, closure statuses, cyclic/nondegeneracy profiles, complete descriptor.

The source explicitly says P5 and P7 are primitive dependent layers whose types are fixed by earlier completed coordinates.

## PI and PII

PI requires the already functional `AxLine` map to be total on the selected inherited-channel set.

PII requires `p in K_bil_A` when either:

- a bilinear-dependent property kind has an available profile product and a nonempty local assignment domain; or
- active formal closure declares `FormalBilDep_A(p)=1`.

The bilinear layer supplies a symmetric bilinear form whenever `p in K_bil_A`.

## Completion

Definition 9.1 defines a layered primitive presentation as a typed/coherent premodel containing all independently chosen primitive coordinates.

Definition 9.2 says explicit completion inserts only functionally determined derived coordinates.

Definition 9.4 defines a full axis-property model as a layered primitive presentation satisfying PI–PII and equipped exactly with the derived coordinates inserted by explicit completion.

Theorem 9.5 states that every such primitive presentation has exactly one explicit completion and that primitive reduction and completion are inverse in the stated sense.

The proof proceeds by functional determination: total `AxLine` gives tagged-axis data; primitive bilinear forms give normal/radical data; partial assignments give domains/statuses and, when fiber constancy holds, unique line-factor maps; supplied representation/closure data determine their evaluations and status readouts.

## Model existence and Stage-VI factorization

Theorem 11.1 states that every Stage-VI Formation record induced by a full Formation model admits at least one Axis-Property extension. The proof takes `K_ax_A=empty`, `Pi_A=empty`, and all option tags zero, so PI and PII are vacuous.

This establishes base-extension nonemptiness but does not force any nontrivial axis interpretation.

Proposition 10.8 states that the Axis-Property structures in Sections 2–10 factor through the Formation Stage-VI truncation and do not depend on post-Stage-VI term spaces, component-term maps, finite-composition domains, or composite operators.

## Important reading discipline

The source does **not** define a full model by requiring every optional closure profile to be `satisfied`.

Formal closure status and nondegeneracy status are derived coordinates that may be `failed`. The full-model definition requires the primitive presentation, PI–PII, typing/coherence, and exact explicit completion; a derived negative status is still a legitimate recorded result.
