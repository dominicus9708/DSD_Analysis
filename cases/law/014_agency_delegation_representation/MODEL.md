# LAW-003 Model — Role-Sensitive Legal Acts and Attribution

## 1. Scope

This model is an application-level comparison model. It does not redefine Korean private law in DSD vocabulary and does not claim that DSD derives agency, mandate, representation, apparent agency, or ratification.

The source-law structure is fixed first from `SOURCE_NOTES.md`.

## 2. Source-side typed carriers

Let:

- `U` be natural human actors;
- `P` be principals or represented persons/entities;
- `T` be counterparties/third parties;
- `R_cap` be legally relevant capacities, including at least `self`, `agent`, `director-representative`, and `mandatary` where the source relation supports them;
- `A_src` be authority-source records;
- `S` be authority scopes;
- `X` be legal act kinds;
- `K` be institutional/legal contexts;
- `E` be source-law effect/attribution statuses.

A source-side action token is

`tau = (u, r, p, alpha, s, x, t, k)`

with

- `u in U` — human performer;
- `r in R_cap` — capacity in which the act is presented;
- `p in P` — represented/principal coordinate where applicable;
- `alpha in A_src` — source of authority or relevant representative status;
- `s in S` — authority scope;
- `x in X` — act performed;
- `t in T` — counterparty where applicable;
- `k in K` — legal/institutional context.

The underlying human `u` is deliberately **not** the whole legally operative action token.

## 3. External predicates and relations

The application supplies source-law predicates rather than deriving them from DSD:

- `Mandate(p,u,task,k)` — an Article-680-type mandate relation where established;
- `Authority(tau)` — actual agency/representative authority exists for the relevant act;
- `WithinScope(tau)` — the act lies within the legally relevant scope;
- `ForPrincipal(tau)` — the source rule's manifestation/representation condition is satisfied where required;
- `ProtectedReliance(tau)` — the source rule's good-faith/justifiable-reliance condition is satisfied;
- `Ratified(p,tau)` — the principal has ratified the unauthorized act;
- `Attrib(tau,e)` — source law assigns effect/attribution status `e in E`.

These are application-level legal relations.

## 4. Ordinary agency rule skeleton

For the ordinary Article 114 route, define a source-law condition

`OrdinaryAgency(tau) := Authority(tau) and WithinScope(tau) and ForPrincipal(tau)`.

The source rule permits

`OrdinaryAgency(tau) -> Attrib(tau, effective-for-principal)`.

The implication is a source-law rule, not a DSD theorem.

## 5. Unauthorized and exceptional routes

### 5.1 Unauthorized agency

For an attempted contract made as another's agent without authority:

`Unauthorized(tau) := not Authority(tau)`.

Article 130 supplies the source status

`Unauthorized(tau) and not Ratified(p,tau) -> Attrib(tau, not-effective-against-principal)`.

The attempted contract token still exists as a legally regulated event. Therefore the model does not encode unauthorized agency as `no event existed`.

### 5.2 Ratification

Article 133 supplies an additional rule:

`Unauthorized(tau) and Ratified(p,tau) -> Attrib(tau, effective-by-ratification)`

with the statutory retroactivity condition and third-party-right limitation kept as source-law metadata.

### 5.3 Excess of authority / apparent agency

Article 126 supplies a separate route:

`not WithinScope(tau) and ProtectedReliance(tau) -> Attrib(tau, principal-responsible-by-apparent-agency)`.

Thus

`not WithinScope(tau)`

does **not** universally entail

`no legal effect or responsibility can reach p`.

### 5.4 Terminated authority

Articles 128-129 separate actual termination from third-party protection. Therefore

`AuthorityTerminated(tau)`

and

`EffectAssertableAgainstProtectedThirdParty(tau)`

are distinct source-side statuses.

## 6. Mandate is not silently identified with agency authority

The model keeps

`Mandate(p,u,task,k)`

separate from

`Authority(tau)`.

This is supported by the statutory distinction between Article 680 and the agency provisions, and by Supreme Court 2023Da288772, which separately analyzes the underlying mandate-like relationship and whether lawful agency authority was granted, including its existence, content, scope, and termination.

No implication

`Mandate -> Authority`

is inserted unless an additional source-law rule establishes it for the concrete case.

## 7. Juridical-person representation

For a juridical person `Pj` and director `d`, Civil Act Article 59 supplies a source-side organ/representative route.

Use

`tau_dir = (d, director-representative, Pj, alpha_dir, s_dir, x, t, k)`.

Article 62 separately permits, under its conditions, appointment of another person for a specific act:

`tau_agent = (u2, agent, Pj, alpha_specific, s_specific, x2, t2, k)`.

The two routes share the represented entity but not necessarily capacity, authority source, or scope.

## 8. Personal capacity versus representative capacity

For the same human `u`, define two tokens

`tau_self = (u, self, u, alpha_self, s_self, x, t, k)`

and

`tau_rep = (u, director-representative, Pj, alpha_dir, s_dir, x, t, k)`.

They share the natural person coordinate but not the legally operative capacity/represented-party coordinates.

Supreme Court 2008Da11276 supplies a concrete procedural boundary: the individual who had been representative director and the company were not the same party for ordinary party-name correction.

Hence the source side supports

`same human != same legally operative party/capacity`.

## 9. DSD application bridge

The safest Formation-level mapping does **not** use the natural person alone as the DSD material item if a legal-status value is to be assigned.

Let the application map each legally described action token `tau` to a typed material/action item

`a_tau`.

Retain the underlying person `u` in the material record/annotation of `a_tau`.

Use a Formation channel

`c_tau = (p_cfg, a_tau, lambda_legal, v_tau, rho_tau)`

where:

- `p_cfg` identifies the legal/institutional configuration;
- `a_tau` is the role/context-sensitive action token carrier;
- `lambda_legal` is an application-supplied legal-status quantity-kind;
- `v_tau` is an externally determined legal status code, not a DSD-derived legal conclusion;
- `rho_tau` preserves the legally operative capacity (`self`, `agent`, `director-representative`, etc.).

This bridge is explicit extra encoding.

## 10. Why the material item should not be the human alone

Primitive Axiom V uses one regime-global partial assignment per quantity-kind. If the same material item were simply the human `u`, then assigning one legal-status value to that human and later expecting a different value solely because the person acts under another legal capacity could create an artificial conflict with the global assignment discipline.

The source law does not say that `the human as such` has contradictory legal status. It says that different **acts in different capacities, scopes, contexts, or authority relations** can receive different legal effects.

Therefore the faithful carrier is the typed act-instance `a_tau`, while the common human is retained as shared provenance/annotation.

This is a type correction, not an evasion of a source-law identity.

## 11. Role coordinate

Formation Definitional Closure Clause VI includes the role relation in admitted channel formation, and the operational channel retains `rho` in its identity.

Accordingly, two source-side act tokens with the same human performer can map to distinct role-bearing channels without forcing the human beings themselves to be different objects.

This gives a direct structural correspondence for the capacity distinction.

## 12. Legal effect is not channel presence

A crucial non-identification is:

`channel admitted/described != source-law act effective for principal`.

An unauthorized agency act is still a legally describable event. Therefore it should not be represented simply by channel absence.

Instead, the source-law effect status is an externally supplied value/relation attached to the described action token. This preserves distinctions such as:

- attempted unauthorized contract exists;
- effect against principal is absent/pending under Article 130;
- later ratification changes the legal status under Article 133;
- apparent-agency rules may impose responsibility through another route.

## 13. Axis-Property boundary

The legal sources require role-sensitive relations, but they do not independently supply the `realized axis line` structure required by the axis-property system.

Therefore LAW-003 does not promote legal roles into realized axes merely to use tag-sensitive property machinery.

Judgment for this case:

- Formation role identity: meaningful and sufficient for the main role/capacity separation after explicit application encoding;
- Axis-Property system: not required; no meaningful direct mapping is asserted without an additional realized-axis interpretation.

## 14. Static/temporal boundary

Ratification and termination introduce time/order-sensitive legal change. The Formation Axiom System used here is static.

LAW-003 therefore compares fixed source-law states such as pre-ratification and post-ratification descriptors. It does not claim that Formation alone derives the transition or the statutory retroactivity rule.

A temporal lineage model would require an additional dynamic or application-level transition layer.

## 15. Comparison classes

| Source distinction | DSD comparison | Class |
|---|---|---|
| same human, different legal capacity | distinct `rho` on typed act-instance channels | direct structural correspondence after application encoding |
| mandate relation vs agency authority | separate source relations; no automatic DSD identification | direct structural correspondence / non-collapse |
| authority scope vs legal effect | separate value/relation coordinates | partial correspondence after extra encoding |
| unauthorized act vs nonexistent act | described act retained while effect status differs | strong structural correspondence |
| ratification | separate post-state/transition supplied by source law | complementary different layer |
| apparent agency | explicit exception route rather than ordinary authority | apparent conflict resolved by rule/regime separation |
| director representation vs personal capacity | shared human provenance, distinct role/represented-party token | direct structural correspondence |
| Axis-Property tag-sensitive properties | not invoked without realized-axis semantics | no meaningful mapping required |
