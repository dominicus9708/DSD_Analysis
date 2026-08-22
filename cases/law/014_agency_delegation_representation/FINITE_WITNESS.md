# LAW-003 Finite Witnesses

These are finite structural witnesses for the source distinctions recorded in `SOURCE_NOTES.md`. They are not substitutes for the source law and do not prove the legal rules.

## W1 — Same human, different capacity

Let the finite source carriers contain:

- human performer: `h`
- juridical person: `J`
- counterparty: `t`
- act kind: `contract`
- capacities: `self`, `director-representative`

Define two action tokens:

`tau_1 = (h, self, h, alpha_self, S_self, contract, t, k)`

`tau_2 = (h, director-representative, J, alpha_dir, S_dir, contract, t, k)`.

Then:

- underlying human coordinate is equal;
- capacity coordinate differs;
- represented-party coordinate differs;
- source-law attribution target may differ.

A Formation application maps these to distinct typed act-items `a_1`, `a_2`, preserving the shared human in their material records and the capacities in `rho_1 != rho_2`.

No contradiction arises from preserving one natural person while distinguishing two legally operative act tokens.

## W2 — Authorized ordinary agency

Let:

- principal: `P`
- agent: `A`
- third party: `T`
- authority scope: `sell <= 100`
- act: `sell 80`

Assume:

- `Authority(tau_80)=true`
- `WithinScope(tau_80)=true`
- `ForPrincipal(tau_80)=true`.

Source-side result under Civil Act Article 114:

`Attrib(tau_80, effective-for-principal)`.

Formation-side encoding:

`c_80=(p_cfg,a_80,lambda_effect,effective-for-principal,agent)`.

The legal conclusion is supplied by the external rule; Formation merely preserves the typed act, status value, and role.

## W3 — Same authority source, act outside scope

Keep the same principal, agent, third party, and authority source, but use:

`tau_150 = sell 150`.

Then:

- `AuthorityBase(tau_150)=true` in the sense that some agency relation exists;
- `WithinScope(tau_150)=false`.

### W3a — no protected reliance

If the Article 126 reliance condition is not satisfied, do not infer ordinary principal effect from Article 114.

Record the source status separately from act existence.

### W3b — protected reliance

If the Article 126 requirements are satisfied, the principal may bear responsibility despite the act being outside actual scope.

This finite pair proves the analysis must retain at least two coordinates:

`actual-scope status`

and

`legal responsibility/effect status`.

Collapsing them would make W3a and W3b indistinguishable.

## W4 — Unauthorized act before and after ratification

Let `tau_U` be an attempted contract made as agent without authority.

Pre-ratification state:

- `Unauthorized(tau_U)=true`
- `Ratified(P,tau_U)=false`
- `Attrib(tau_U, not-effective-against-principal)` under Article 130.

Post-ratification state:

- same historical attempted act token `tau_U`
- `Ratified(P,tau_U)=true`
- `Attrib(tau_U, effective-by-ratification)` subject to Article 133.

The source law therefore distinguishes:

1. existence of the attempted act;
2. authority status;
3. ratification status;
4. attribution/effect status.

The DSD comparison must not encode the pre-ratification attempted act as `channel absent`, because the source law regulates that act and gives the counterparty rights before ratification.

## W5 — Mandate without silently totalizing agency authority

Let:

`Mandate(P,A,task,k)=true`.

Do not add

`Authority(tau)=true`

unless the concrete source facts/rules separately establish the relevant agency authority.

This finite witness encodes the non-collapse discipline established by Article 680 together with Supreme Court 2023Da288772's separate treatment of the mandate-like underlying relation and lawful agency authority.

## W6 — Authority to conclude one contract does not totalize later authority

Let `A` have authority to conclude contract `x` for `P`.

After `x` is concluded, do not automatically create authority values for:

- rescission;
- termination;
- all later disposition;
- receipt of every later declaration.

Supreme Court 2008Da11276 expressly rejects that automatic totalization in the circumstances addressed by the decision.

This is a direct finite witness for the DSD analysis rule:

`defined authority for one typed act != defined authority for every related later act`.

## Minimal status table

| Witness | human | capacity | actual authority/scope | extra rule | principal effect/status |
|---|---|---|---|---|---|
| W2 | A | agent | yes / within | none | effective under ordinary agency rule |
| W3a | A | agent | base relation / outside | no protected reliance | ordinary route fails; no automatic reattribution |
| W3b | A | agent | base relation / outside | Article 126 conditions | principal responsibility may arise |
| W4-pre | A | purported agent | no authority | no ratification | not effective against principal under Article 130 |
| W4-post | A | purported agent | no authority at act time | ratification | effective by ratification subject to Article 133 |

## Witness conclusion

A model preserving only the human performer or only a binary `authorized/not-authorized` flag is insufficient to reconstruct these cases.

At minimum, the source structure requires separate coordinates for capacity, authority/scope, exceptional legal rule, and attribution/effect. Formation can preserve those distinctions under explicit application encoding and role tags, but it does not supply the legal rules that populate them.
