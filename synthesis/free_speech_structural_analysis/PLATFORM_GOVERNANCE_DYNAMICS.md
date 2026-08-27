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
