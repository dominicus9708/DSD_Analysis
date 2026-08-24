# DSD Source Notes

## Formation Axiom System

The current Stage-VII domain is `P_fin(C_L)` and, after Stage VI, supplied term data determine

`Comp_L(F)=sum_{c in F} T_L(c)`.

The uniqueness result for Clause VII is a **forward closure uniqueness** statement: after the Stage-VI record and post-Stage-VI term map are supplied, the Stage-VII composition operator is fixed.

It is not an inverse theorem recovering `F` from `Comp_L(F)`.

## Channel-Indexed Static Aggregation

The static paper realizes the same finite composition analytically and states:

- support-tagged channel records retain `F` explicitly;
- zero-padding is rejected because channel absence must remain distinct from selected zero contribution;
- for fixed finite support `F`, the sum map is
  `S_F: W_L^F -> W_L`, `S_F(y)=sum_c y_c`;
- when `W_L != {0}` and `|F|>=2`, `ker S_F` is nontrivial on the full product space;
- for an admissible record class `A_F`, `S_F|A_F` is injective iff `(A_F-A_F) intersect ker S_F={0}`;
- the combined channel/property criterion is the analogous difference-set/kernel criterion;
- across varying supports, aggregate equality alone does not reconstruct support.

These source statements already separate forward aggregation from inverse reconstruction.

## Axis-property system

The axis-property paper remains pre-aggregation. Its complete descriptor retains typed property records and does not imply that later reduced aggregation reconstructs them.

## Dynamics

Not needed for the principal proof. Its component-versus-reduced-readout distinction is consistent with the static reconstruction boundary but is not used to establish MATH-005.
