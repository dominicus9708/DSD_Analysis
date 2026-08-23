# LAW-006 Structural Model — Rule-Indexed Normative Status

## 1. Why one global deontic value is insufficient

Let `A` be action tokens and suppose one tries to define

`N : A -> {OBLIGATORY, PERMITTED, PROHIBITED, EXEMPT}`.

The selected source families already defeat this as a universal model.

Reasons:

- an obligatory act may also be permitted in standard deontic systems;
- an exception may mean the prohibition never applies to that token;
- an exemption may remove a duty without imposing the opposite duty;
- one actor may be obligated to seek permission while another authority has discretion to grant or refuse it;
- the same physical act can have different legal statuses under different purposes, times, actors, and rule regimes.

## 2. Typed normative-action instance

Use a rule-sensitive token:

`tau = (u, a, r, k, t, p, j)`

where:

- `u` = actor/subject;
- `a` = action or omission;
- `r` = role/capacity;
- `k` = context/condition;
- `t` = time;
- `p` = purpose or legally relevant use;
- `j` = jurisdiction/institutional regime.

The underlying physical action can remain common provenance while normative evaluation attaches to `tau`.

## 3. Normative rules as indexed relations

Let `R` be the set of source rules.

For a rule `r in R`, define a partial applicability relation:

`Applies(r, tau)`.

Only after applicability is established may the source rule supply one or more normative consequences.

Instead of a single value, use a package:

`Sigma(r, tau) = (O, P_s, P_w, F, E, W, C)`

where the coordinates are optional/source-dependent:

- `O`: obligation/requirement status;
- `P_s`: strong/affirmative permission if the source recognizes it;
- `P_w`: weak permission/non-prohibition if the source logic recognizes it;
- `F`: prohibition/forbidden status;
- `E`: exception/exclusion from rule scope;
- `W`: waiver/exemption/non-obligation status;
- `C`: conditions, limits, remedies, or consequence rules.

No universal claim is made that every source has all coordinates.

## 4. Minimal source-faithful relations

The model keeps at least these relations separate:

`Possible(tau)` — physically/causally executable.

`Applies(r,tau)` — rule applies.

`Obligatory(r,tau)` — source requires the action/omission.

`Permitted(r,tau)` — source affirmatively or weakly permits, according to that source's semantics.

`Forbidden(r,tau)` — source prohibits.

`Excluded(r,tau)` — token is outside a regulated category by an exception/exclusion rule.

`Exempted(r,tau)` — subject is relieved from a duty or burden by an exemption/waiver.

These predicates are not assumed to be mutually exclusive unless the source logic says so.

## 5. Rule-scope before opposite-value assignment

For an ILO-style exclusion, a faithful structure is:

`CandidateCategory(tau)`

`+ ExceptionCondition(tau)`

`-> not Applies(ProhibitionRule, tau)`

or another source-defined scope result.

It is not automatically:

`Forbidden(tau) = true`

then

`Permitted(tau) = true`.

This distinction matters because exception can alter the domain of the prohibition rather than reverse a previously formed status.

## 6. Permission-gated obligation example

UNIDROIT public-permission structure can be typed as:

`Obligatory(R_apply, tau_apply)`

while

`PermissionGranted(R_public, tau_perform)`

is still unresolved.

Therefore:

`O(seek_permission)`

can coexist with

`undefined/grant_pending(permission_to_perform)`.

This directly falsifies any model that uses one global deontic value for the whole transaction.

## 7. Derogation and exemption

A derogation/exception relation is modeled as a separate rule:

`Dg : (base_rule, subject, context, time) ⇀ modified_rule_scope`.

This allows:

- ordinary obligation under the base regime;
- temporary authorized deviation under specified conditions;
- non-derogable residual constraints.

The derogation relation is not the same object as the underlying obligation or prohibition.

## 8. Norm conflict

If two source rules yield:

`Obligatory(r1,tau)`

and

`Forbidden(r2,tau)`

DSD Analysis must not silently resolve the conflict.

Resolution requires an external priority, hierarchy, exception, lex-specialis, temporal, jurisdictional, or other source rule.

Until then the faithful representation is a conflict-bearing descriptor, not a repaired single value.

## 9. DSD Formation bridge

A legal/normative application may form channels over typed normative instances, for example:

`c_tau = (p_cfg, a_tau, lambda_norm, v_tau, rho_tau)`.

The application can use distinct channels/status coordinates for:

- applicability;
- obligation;
- permission;
- prohibition;
- exception/exemption;
- consequence.

However:

`legal permission != Formation admission`

`legal obligation != Formation realization`

`legal prohibition != channel absence`

`legal exemption != defined zero`.

The bridge is structural only.

## 10. Other DSD layers

Axis-Property: not required without independently justified realized-axis semantics.

Static Aggregation: not required; normative statuses are not additive weights.

Dynamics: optional only for norm creation, repeal, expiration, derogation, waiver, revocation, or other temporal transition analysis.

## 11. Surviving universal candidate

The strongest candidate that survives counterpressure is:

**Normative status is rule- and context-indexed. Physical possibility, rule applicability, obligation, permission, prohibition, exception/exemption, and consequence must not be collapsed unless the source system supplies the rule or logic that licenses that identification.**
