# LAW-006 Finite Witnesses — Normative Status Is Not One Global Value

## W1 — Physical possibility does not imply permission

Let `tau1` be an action that an actor is physically capable of performing but that a governing legal rule forbids.

Then:

`Possible(tau1) = true`

while

`Forbidden(r,tau1) = true`.

Therefore:

`Possible(tau) -> Permitted(tau)`

is not a universal rule.

The ILO Forced Labour Convention supplies a concrete witness family: illegal exaction of forced labour must be punishable, even though such exaction is physically possible and historically occurs.

## W2 — A protected liberty can coexist with rule-conditioned restriction

Let `tau2` be an exercise of expression under a rights regime.

The base regime recognizes a right/liberty, but a separate restriction rule may become applicable only under specified legal and necessity conditions.

Thus:

`RightOrPermission(base,tau2)`

need not imply

`Unrestricted(tau2)`.

This witness defeats a one-bit model in which a right means unconditional permission under every context.

## W3 — Obligation to seek permission while permission remains unresolved

Let `tau_apply` be the act of applying for a required public permission and `tau_perform` the regulated performance.

Under the UNIDROIT public-permission structure:

`Obligatory(r_apply,tau_apply) = true`

while the permission status of `tau_perform` can still be pending:

`GrantStatus(tau_perform) = PENDING`.

Therefore:

`obligation concerning permission`

is not identical to

`permission already granted`.

The same transaction simultaneously contains different normative coordinates.

## W4 — Exception can change rule scope rather than flip an opposite value

Let `tau4` be emergency work satisfying the conditions of an ILO Convention No. 29 exclusion.

A naive model might encode:

`Forbidden(tau4) = true`

and then overwrite it with

`Permitted(tau4) = true`.

A source-faithful model instead permits:

`ExcludedFromForcedLabourDefinition(r,tau4) = true`.

Then the Convention's forced-labour prohibition need not attach to `tau4` in the first place.

Thus:

`exception`

need not equal

`opposite deontic value`.

## W5 — Derogation is not unlimited cancellation

Let a base treaty obligation apply at `t0`.

At `t1`, a qualifying emergency and formal conditions allow a temporary derogation from some obligations, subject to strict necessity and other safeguards.

The model retains:

`BaseObligation(r,t0)`;

`DerogationAuthority(d,t1)`;

`ModifiedScope(r,d,t1)`;

and, for non-derogable rights or residual limits,

`ResidualConstraint(r2,t1)`.

Therefore:

`derogation`

is not identical to

`all relevant obligations become false`.

## W6 — Exemption from duty does not imply duty to do the opposite

Let `O(a)` be a duty to perform action `a` under a base rule and let an exemption remove that duty for subject `u`.

Then a minimal result is:

`not O_u(a)`.

It does not follow without another rule that:

`O_u(not a)`

or even that the source recognizes a strong affirmative permission for `not a`.

This witness prevents the collapse:

`exempt from obligation -> obligatory opposite`.

## W7 — Prosecutorial/defence functional witness

Suppose the attribution/prosecution function `P` argues:

`Applies(r,tau) and Forbidden(r,tau)`.

The defence function `D` can defeat that route by establishing:

`not Applies(r,tau)`

or

`Exception(e,r,tau)`.

The defence does **not** thereby have to prove a universal proposition:

`Permitted_under_all_rules(tau)`.

The judgment function `J` must preserve the distinction between:

- failure of the asserted prohibition rule to apply;
- affirmative permission under another rule;
- an exemption from a duty;
- a conflicting norm requiring separate priority resolution.

This extends LAW-002's non-totalization result into normative-rule applicability.

## W8 — Norm conflict cannot be repaired by encoding choice

Let:

`Obligatory(r1,tau) = true`

and

`Forbidden(r2,tau) = true`.

If the source regime supplies no priority rule, a DSD application may record the conflict but cannot legitimately replace it with either:

`PERMITTED`

or

`PROHIBITED`

as a unique global value.

The resolution must come from a source-side priority, hierarchy, exception, temporal, jurisdictional, or conflict rule.

## Finite-witness conclusion

These witnesses jointly falsify the universal map:

`N : Action -> {OBLIGATORY, PERMITTED, PROHIBITED, EXEMPT}`

when interpreted as a total, mutually-exclusive, context-free classification.

The source-faithful carrier must preserve at least rule, actor, context, role, time, and applicability information before deriving a normative consequence.
