# Case 009 — Finite Witnesses

## Witness A — PII catches missing bilinear data
Take one configuration `p`, one selected channel `c`, and `E_amb=R`. Let PI hold with `AxLine(c)=R`.

Declare one unary tag property `varpi_bil` with `varpi_bil in Pi_bil_A`. Define its assignment on the unique tagged axis, so `Dom(Xi_A,p,varpi_bil)` is nonempty. Set `K_bil_A=empty`.

All nonbilinear typing can be satisfied, but PII fails. This reproduces the paper's intended obstruction: a defined bilinear-dependent application cannot coexist with missing bilinear data in a full model.

## Witness B — declared but unused bilinear kind
Use the same axis data and declare `varpi_bil in Pi_bil_A`, but let its available assignment have empty domain.

Set `K_bil_A=empty`, with all closure declarations inactive.

Then PII does not trigger.

This is consistent with partial-map semantics: a global declaration does not force local bilinear data when there is no defined local application.

## Witness C — zero-form completion
Let any finite-dimensional `E_amb` be supplied and suppose one PII antecedent is true. Put `p in K_bil_A` and define

`b(x,y)=0` for all `x,y in E_amb`.

This is a symmetric bilinear form. Therefore PII is satisfiable regardless of the number of selected channels, realized-axis rank, or degeneracy.

Consequences:
- PII does not require nondegeneracy;
- PII does not require positive definiteness;
- PII does not impose a cardinality/dimension obstruction beyond the already supplied vector-space type.

## Witness D — semantic-value mismatch that still satisfies PII
Let `E_amb=R^2` with Euclidean bilinear form `b(x,y)=x dot y` and two realized lines

`l1=span(e1)`, `l2=span(e1+e2)`.

They are not orthogonal because `b(e1,e1+e2)=1`.

Declare a binary tag property `varpi_bil in Pi_bil_A` with Boolean value carrier and define

`Xi(t1,t2)=1`.

PII is satisfied because `p in K_bil_A` and a symmetric bilinear form is supplied. Yet nothing in PII forces the Boolean value 1 to equal, encode, or agree with the bilinear relation determined by `b`.

This is not an internal contradiction because the paper explicitly states that property labels gain mathematical content only from their typed assignments and any additional compatibility law. It shows that PII is an availability-compatibility axiom, not a semantic-value compatibility theorem.

## Witness E — normal-profile dependency is typing-gated before PII
Suppose a bilinear-dependent kind has profile `(normal,tag)`. If `p notin K_bil_A`, the normal carrier is unavailable, so the full profile product is unavailable and no property assignment on that product is supplied.

Thus a defined normal-input application cannot be used to infer `p in K_bil_A`; the input cannot exist before that membership is already present.

This is not circular because `K_bil_A` is primitive P3 data and P4 derives the normal carrier from it. It does mean the first PII antecedent is nontrivial mainly for bilinear-dependent kinds whose profiles are available without the bilinear layer.

## Witness F — formal-closure asymmetry
Let `ClDecl(p)=1` and `FormalBilDep(p)=1`, even if the active requirement family is empty. Then PII triggers and requires `p in K_bil_A`.

By contrast, a merely declared bilinear property kind with empty assignment domain does not trigger PII.

The asymmetry is coherent: the formal-closure bit is itself a local declaration that the active closure record depends on bilinear data, whereas a global property-kind declaration need not be locally applied.
