# Platform Governance, Incentives, and Conflict Dynamics — Exploratory DSD Note

Status: exploratory extension of the free-speech structural analysis. This note does **not** infer malicious intent from profit motive alone.

## 1. Platform as private governance structure

A large social platform is not only a channel host. It sets and changes the practical capabilities available to users:

`Platform_t = (speech tools, reception tools, blocking, recommendation, visibility, reporting, sanctions, appeal, memory, recurrence handling, ranking, monetization, ...)`

Therefore:

`Platform_t != Platform_(t+1)`

when those affordances materially change, even if the user population and nominal legal environment stay the same.

Kate Klonick's “The New Governors” (Harvard Law Review 131, 2018) is an important external governance reference: major platforms should be studied as systems of private governance that actively curate online speech while remaining comparatively weakly accountable directly to users.

Source: https://harvardlawreview.org/print/vol-131/the-new-governors-the-people-rules-and-processes-governing-online-speech/

## 2. Social peace and private profit are different objective functions

A criminal-justice/state analogy can be useful only at the structural level: public institutions may be assigned functions such as dispute resolution, due process, victim protection, punishment under law, and interruption of private retaliatory cycles. A platform is not a state and need not inherit those legal duties merely because it governs a community.

The platform may instead optimize a mixed private objective:

`Objective_P = f(revenue, engagement, retention, advertiser demand, moderation cost, legal risk, reputation, user growth, safety, ...)`

The community may value a partly different objective:

`Objective_C = f(safety, fair participation, predictability, low harassment, correction, trust, exit, voice, ...)`

Thus:

`Objective_P != Objective_C`

is a possible structural condition, not an accusation of bad faith.

## 3. Advertising-driven incentive conflict

Beknazar-Yuzbashev, Jiménez-Durán, and Stalinski (AEA Papers and Proceedings 114, 2024) model a case in which an advertising-driven platform can profit from harmful content when that content is complementary to users' time spent on the platform. Their warning is directly relevant:

`engagement increase != welfare increase`

DOI: 10.1257/pandp.20241004
Source: https://www.aeaweb.org/articles?id=10.1257/pandp.20241004

This does not prove that every platform intentionally promotes conflict. It establishes a plausible incentive misalignment under some revenue structures.

## 4. Engagement-based distribution can alter conflict exposure

Luke Munn, “Angry by design: toxic communication and technical architectures” (Humanities and Social Sciences Communications, 2020), treats platforms as designed environments and argues that engagement-oriented architectures can privilege incendiary or antagonistic communication.

DOI: 10.1057/s41599-020-00550-7
Source: https://www.nature.com/articles/s41599-020-00550-7

A 2026 Nature registered report on feed ranking found engagement-based feeds amplified intergroup/moralized/emotional and toxic content relative to reverse-chronological feeds, with especially large increases in moral outrage and political content; an alternative ranking design reduced such exposure while maintaining comparable platform enjoyment.

Source: https://www.nature.com/articles/s41586-026-10536-1

DSD relevance:

`content existence != distribution probability != recommendation != amplification`

and

`moderation policy != ranking policy`.

A platform can leave content formally available while dramatically changing its practical visibility.

## 5. Moderation externality and conflict-cycle problem

Suppose a disruptive actor `D` creates conflict and participants `U_i` respond.

A simplified dynamic is:

`D_t -> reactions_t -> visibility_t -> engagement_t -> renewed D_(t+1)`

If ranking/monetization rewards the interaction volume regardless of whether it is constructive, then conflict can generate a positive feedback path.

This is not equivalent to saying the platform endorses `D`.

It means the platform may receive a private benefit from an interaction pattern whose social costs are borne partly by users, moderators, targets, and the wider community.

Candidate term:

**conflict externalization** — the platform captures some engagement benefit while some harassment, vigilance, retaliation, and community-fragmentation costs remain external to the platform's direct objective.

## 6. Why blocking alone may fail to terminate the cycle

Blocking can reduce personal exposure while reducing observability:

`Block: Exposure_U(D) ↓ ; Observability_U(D) ↓?`

If recurrence, ban evasion, identity switching, or migration across subcommunities is expected, users may rationally retain observation rather than fully block.

This can produce:

`official protection gap -> peer monitoring -> community memory -> warning practices`

but may then continue into:

`warning -> surveillance -> public shaming -> collective retaliation`.

Therefore:

`community memory != community punishment authority`.

External source family:
- Jhaver et al., “Online Harassment and Content Moderation: The Case of Blocklists,” ACM TOCHI 25, 2018. DOI: 10.1145/3185593.
- Chang & Danescu-Niculescu-Mizil, “Trajectories of Blocked Community Members: Redemption, Recidivism and Departure,” WWW 2019. DOI: 10.1145/3308558.3313638.
- Beadle & Vasek, “Peer Surveillance in Online Communities,” arXiv 2023. DOI: 10.48550/arXiv.2308.01304.

## 7. New platform-specific variables

Add to the structural audit:

- `RevenueModel(P)`
- `EngagementSensitivity(P)`
- `RankingObjective(P)`
- `ModerationCost(P)`
- `AdvertiserConstraint(P)`
- `LegalRisk(P)`
- `ReputationRisk(P)`
- `SanctionCapacity(P)`
- `AppealCapacity(P)`
- `RecurrenceHandling(P)`
- `IdentityContinuity(P)`
- `CommunityMemory(P)`
- `UserObservability(U,D,P)`
- `UserAvoidability(U,D,P)`

Do not collapse these into one scalar “platform power” score.

## 8. Platform-governance non-equivalences

`private rulemaking != public law`

`recommendation != speech permission`

`de-recommendation != deletion`

`blocking != sanction`

`report != guilt finding`

`sanction != rehabilitation`

`engagement != social value`

`profit motive != malicious intent`

`platform inaction != neutral effect`

The final line is especially important: failure to intervene can still have structural effects when ranking, visibility, or monetization systems continue operating.

## 9. Candidate audit principle

> Where a platform simultaneously controls speech distribution, user-protection affordances, sanction procedures, and monetization, the audit must preserve the possibility that governance and revenue objectives diverge. Claims of deliberate exploitation require evidence; structural incentive conflict does not.

This distinction is necessary to avoid two symmetric errors:

1. `profit motive -> intentional harm` (invalid without evidence), and
2. `absence of proven bad intent -> no structural responsibility` (also invalid).

## 10. Resource, operational capacity, authority, and responsibility

Institutional scale should not be collapsed into a single claim of capacity.

`Resource(P) != OperationalCapacity(P,t) != Authority(P,t) != Responsibility(P,t)`

Possible capacity inputs include:
- staffing and capital;
- moderation tooling;
- case volume;
- language and regional coverage;
- required response latency;
- evidentiary complexity;
- false-positive/false-negative tolerance;
- availability of human review.

Accordingly:

`non-performance != incapacity`

while also:

`large resource base != unlimited case-handling capacity`.

A claim that an institution lacked capacity is itself a describable and auditable claim. The framework does not accept or reject it merely because the institution is large or wealthy.

Technical ability must also remain separate from legitimate authority and duty:

`can act != may act != must act`.

## 11. Procedural legitimacy profile

Outcome counts such as removals or bans are insufficient to describe governance quality.

Use a provisional procedure profile:

`G_P = (RuleNotice, ReasonGiving, Evidence, Consistency, Appeal, Review, Correction, Restoration)`.

Questions include:
- Was the applicable rule knowable?
- Was the user told what decision occurred?
- Was a reason supplied?
- Can relevant evidence be reviewed?
- Are comparable cases treated consistently?
- Can the decision be challenged?
- Is review meaningfully independent from the first decision?
- Can an erroneous decision be corrected?
- Can lost access/status be restored?

External anchors:
- Judit Bayer, “Procedural rights as safeguard for human rights in platform regulation,” *Policy & Internet* (2022), DOI 10.1002/poi3.298.
- Nicolas Suzor, Tess Van Geelen, Sarah Myers West, “Evaluating the legitimacy of platform governance,” *International Communication Gazette* (2018), DOI 10.1177/1748048518757142.
- Rory Van Loo, “Federal Rules of Platform Procedure” (2020).
- Catalina Goanta & Pietro Ortolani, “Unpacking Content Moderation: the Rise of Social Media Platforms as Online Civil Courts,” DOI 10.2139/ssrn.3969360.

These sources are used for procedural comparison, not as proof that private platforms are legally equivalent to courts or states.

## 12. Distinguish distribution and sanction states

A binary `moderated/not moderated` variable loses too much structure.

Preserve at least:

`Allow != Recommend != Amplify != Monetize != Deprioritize != Remove != Sanction`.

Examples of invalid automatic transitions:
- `not removed -> neutrally distributed`;
- `de-recommended -> deleted`;
- `monetized -> endorsed`;
- `reported -> guilty`.

This permits analysis of lawful-but-downranked, visible-but-demonetized, removed-but-appealable, or allowed-but-interaction-limited states without forcing them into one category.

## 13. Conflict termination and recurrence

The objective of content moderation may differ from the objective of conflict termination.

`ContentModerated != ConflictResolved`.

Track at least:
- `ConflictPersistence(t)`;
- `Recurrence(t+1)`;
- `BanEvasion`;
- `IdentitySwitching`;
- `CommunityMigration`;
- `PeerMonitoringBurden`.

Sanction purposes must also be typed:

`Punishment != Incapacitation != Deterrence != Rehabilitation != Restoration`.

A temporary block may succeed at immediate incapacitation while failing at deterrence or rehabilitation. A removal may reduce exposure while leaving retaliation and recurrence unchanged.

Therefore success metrics should be matched to the declared intervention purpose instead of using removal counts alone.

## 14. Feasible alternatives and proportionality audit

Before treating deletion or permanent exclusion as the only available intervention, record:

`FeasibleAlternative(P,t)`.

Candidate alternatives may include:
- de-recommendation;
- amplification reduction;
- interaction restriction;
- user-controlled filtering;
- warning or friction;
- temporary suspension;
- rate limitation;
- human review;
- appeal;
- restoration after correction.

An alternative matters only if it was actually technically and institutionally feasible at the relevant time. The framework therefore avoids the hindsight error `conceivable alternative -> feasible alternative`.

The audit question is not “why did the platform fail to choose my preferred policy?” but:

> Given the defined risk, authority, operational capacity, and available alternatives, what capability changes did each feasible intervention produce or avoid?

## 15. Core publication-control rule

The main argument should remain actor-neutral and motive-light.

Exclude from core claims unless externally established:
- hidden malicious intent;
- unsupported accusations against a named company or institution;
- assumptions about internal resource allocation not publicly evidenced;
- claims outside DSD's descriptive or external-source authority.

Permit named entities in externally sourced examples where the source is necessary to establish an actual policy, experiment, decision, or historical change.

The controlling pair remains:

`profit motive != malicious intent`

and

`absence of proven malicious intent != absence of structural effect or responsibility`.