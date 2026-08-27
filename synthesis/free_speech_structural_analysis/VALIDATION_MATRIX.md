# Validation Matrix — DSD Free-Speech Structural Analysis

Status: pre-case audit design. No formal case ID assigned.

Purpose: prevent the framework from becoming a conclusion-fitting device. Positive cases, negative controls, counterexamples, and undetermined cases must be designed before selecting politically salient real-world examples.

## 1. Variable families

### Actor state
- age
- developmental capacity
- legal status
- role / office
- formal authority
- knowledge / expertise
- economic resources
- livelihood dependence
- alternative channels
- amplification capacity
- accountability

### Relation state
- dependency
- authority direction
- sanction power
- exit cost
- targeting
- prior refusal
- consent to receive
- employment relation
- representation claim
- financial/professional conflict relation

### Channel state
- publicness
- accessibility
- persistence
- searchability
- replicability
- amplification
- occupancy
- algorithmic targeting
- avoidability
- physical obstruction / captive condition

### Receiver and interpretation state
- audience role
- uptake
- background knowledge
- credibility assignment
- interpretation
- attribution
- uncertainty
- correctability

### Effect state
- capability loss
- irreversibility
- material harm
- social cost
- legal effect
- correction path
- appeal path
- exit path

## 2. Minimum counterexample set

| Type | Example | Automatic transition that must fail |
|---|---|---|
| Same words, different office | ordinary citizen vs mayor praises same company | `same words -> same social act` |
| Later information | speaker later identified as mayor | `new context -> bribery established` |
| Refusal | proselytizing/selling invitation followed by explicit refusal | `initial speech right -> continuing targeted-contact right` |
| Public offense | avoidable offensive sign in public | `offense -> general censorship` |
| Captive/targeted | following and repeating after refusal | `public place -> forced audience right` |
| Economic asymmetry | large corporation vs livelihood-dependent street seller | `same restriction -> same capability loss` |
| Representation | organized civic group statement | `visibility -> public mandate` |
| Silence | most citizens inattentive/unmeasured | `silence -> assent/delegation` |
| Expertise | expert technical judgment | `expertise -> political representation` |
| Child protection | general educational exposure vs targeted self-serving adult influence | `same content -> same influence structure` |
| Education | low-education speaker | `less education -> less basic speech standing` |
| Translation | freedom/liberty both translated as 자유 | `same translation -> same concept` |
| Listener autonomy | individual blocks own feed | `self-block -> censorship` |
| Group reaction | many individually lawful mocking responses aggregate | `each small response -> no aggregate structural effect` |

## 3. Protection-versus-oppression direction audit

For any intervention `L`, record capability changes separately:

`L -> {ΔC_protected, ΔC_speaker, ΔC_listener, ΔC_third_party}`

Questions:
1. Who is the stated protected party?
2. Who is the actual beneficiary?
3. Which active capabilities are reduced?
4. Does the intervener gain independent power or material advantage?
5. Is a less restrictive intervention available?
6. Can the constrained party contest or appeal?
7. Is the restriction reversible?
8. Is the asserted risk defined or merely presumed?
9. What external legal/ethical/institutional bridge authorizes the transition?
10. Does the same rule apply symmetrically where relevant, or is asymmetry explicitly justified?

## 4. Justification-burden heuristic

Not a legal formula and not a numerical law:

`power asymmetry ↑ + irreversibility ↑ + capability loss ↑ => audit burden ↑`

This determines how much external justification must be documented, not the final legal outcome.

## 5. Outcome classes

- `STRUCTURALLY PERMITTED CANDIDATE`: exercise of one's own capability without an unbridged reduction of another's independent capability.
- `PROTECTION CANDIDATE`: specified risk reduction while preserving the protected party's active capabilities as far as possible.
- `INFRINGEMENT CANDIDATE`: another person's valid capability is reduced without a separately supplied bridge.
- `OPPRESSION CANDIDATE`: asymmetry + repetition/institutionality + capability loss + weakened exit/rebuttal/appeal.
- `EXTRA-BRIDGE REQUIRED`: structure is described but normative conclusion requires external law/ethics/institution rules.
- `UNDETERMINED`: required input/property/evidence is undefined.

These are **not** substitutes for legal findings such as lawful/unlawful, guilty/not guilty, protected/unprotected speech.

## 6. Prospective validation plan

1. Build 8–12 synthetic controls with intentionally varied speaker/receiver/channel profiles.
2. Include cases where the same words must yield different structural descriptions because role or relation changed.
3. Include cases where different words should remain equivalent under the relevant audit rule.
4. Include at least two cases expected to remain `UNDETERMINED`.
5. Include at least two cases where the framework should reject a censorship conclusion despite offense.
6. Include at least two cases where the framework should reject an unlimited-speech conclusion because the receiver is made captive or targeted after refusal.
7. Include child/age cases where protection and participation must coexist rather than one eliminating the other.
8. Include economic-asymmetry cases where equal formal rules produce unequal capability losses.
9. Include representation cases where high visibility must not infer population mandate.
10. After synthetic controls are frozen, apply blind/prospective mapping to real legal, organizational, platform, advertising, educational, and public-sphere cases.

## 7. Failure criteria

The draft framework should be revised or rejected if it systematically:
- classifies almost every disagreement as infringement/oppression;
- classifies almost every speech act as protected freedom regardless of targeting/captivity;
- cannot distinguish self-blocking from censorship;
- infers intention from outcome;
- infers representation from visibility;
- converts expertise into political authority;
- treats age as sufficient to erase child participation rights;
- treats education as speech eligibility;
- treats dictionary translation as conceptual identity;
- retroactively rewrites prior states after later information;
- produces a normative verdict when its required bridge is missing.

## 8. Evidence accounting

Raw case count is not independent evidence count. Cases sharing the same theory, source family, jurisdiction, or structural mechanism should be clustered before synthesis.

Mode C/prospective results, synthetic controls, external theory convergence, legal comparisons, and lexical audits answer different questions and must not be merged into one success percentage.

## 9. Publication gate

Before any formal paper claim:
- freeze case registry with domain-local IDs only;
- freeze source versions and DOI metadata;
- build BibTeX and claim-source matrix;
- record failed mappings and negative controls;
- separate source-derived claims, DSD reinterpretation, and normative bridges;
- conduct prior-art/novelty audit before calling the integrated protocol new.

## 10. Platform-governance extension

### Capacity and institutional claims
Track separately:
- `resources`;
- `operational_capacity`;
- `case_volume`;
- `language_coverage`;
- `latency_requirement`;
- `decision_complexity`;
- `error_tolerance`;
- `authority_scope`;
- `responsibility_scope`.

The following automatic transitions must fail without evidence or bridge:
- `high capital -> unlimited moderation capacity`;
- `non-performance -> incapacity`;
- `technical ability -> legitimate authority`;
- `authority -> mandatory duty`.

### Procedure
Track:
- `rule_notice`;
- `reason_giving`;
- `evidence_visibility`;
- `decision_consistency`;
- `appeal_capacity`;
- `review_independence`;
- `correction_path`;
- `restoration_path`.

The following transitions must fail:
- `report -> guilt`;
- `removal -> fair procedure`;
- `sanction -> conflict resolved`.

### Distribution and sanction state
Keep separate:
- `allow`;
- `recommend`;
- `amplify`;
- `monetize`;
- `deprioritize`;
- `remove`;
- `sanction`.

Reject:
- `not removed -> neutrally distributed`;
- `de-recommended -> censored`;
- `monetized -> endorsed`.

### Dynamics
Track where evidence allows:
- `conflict_persistence(t)`;
- `recurrence(t+1)`;
- `ban_evasion`;
- `identity_switching`;
- `community_memory`;
- `peer_monitoring_burden`.

Removal count alone must not serve as a general conflict-resolution success metric.

### Feasible alternatives
For each intervention, record `FeasibleAlternative(P,t)` and distinguish a merely conceivable alternative from one actually available given technology, authority, timing, and institutional process.

Candidate alternatives include de-recommendation, amplification reduction, interaction restriction, warning, temporary suspension, human review, appeal, and restoration.

## 11. Additional platform-specific failure criteria

Revise the framework if it:
- infers operational capacity or legal/moral duty from company size alone;
- treats absence of proven bad intent as proof of zero structural effect;
- treats institutional inaction as system suspension;
- collapses recommendation, amplification, monetization, removal, and sanction into one moderation value;
- treats a user report as a finding of fact or guilt;
- fails to record recurrence, correction, or appeal after sanction;
- ignores feasible less-restrictive alternatives;
- fills hidden corporate or institutional intent without evidence;
- assumes a private platform is legally equivalent to a state merely because it performs governance-like functions.