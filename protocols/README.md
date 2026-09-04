# Domain Audit Protocols / 분야별 감사 프로토콜

This directory contains domain-specific extensions of the DSD General Audit Framework.

이 디렉터리는 DSD 일반 감사체계에 각 분야의 기존 검증 기준을 추가하는 곳입니다.

## Operating rule / 운영 원칙

The DSD common frame is used to trace structure, describability, selection, exclusion, transition, consistency, norms, outcome, and explicit interface/bridge assumptions.
It does **not** replace the external validation standard of the audited field.

DSD 공통 프레임은 구조·기술가능성·선택·배제·전이·정합성·규범·결과와 명시된 인터페이스·브리지 전제를 추적하기 위해 사용합니다.
해당 분야의 외부 검증 기준을 DSD 용어로 대체하지 않습니다.

Before a domain protocol applies DSD formal structure, it should state which layers from [`../methodology/DSD_INTERFACE_PROFILE.md`](../methodology/DSD_INTERFACE_PROFILE.md) are active.
Formation, General Property, Static Aggregation, Dynamics, and optional realized-axis or other specializations are not forced into one mandatory package.

분야별 프로토콜에서 DSD 형식구조를 사용할 때는 어떤 층위를 실제로 사용하는지 먼저 고정합니다.
일반 Property 코어와 realized-axis 등 선택적 특수화를 구분하며, 특수화 구조를 보편 DSD 전제로 승격하지 않습니다.

## Required sections for every domain protocol / 분야별 프로토콜 필수 항목

Each protocol should define:

1. External standards used by the field.
2. Which DSD interface layers are used, and which exact source revisions are the reference set.
3. Which of the eight common DSD audit axes apply without modification.
4. Additional evidence-status or object-status fields required by the domain.
5. Required selectors, bridges, constitutive maps, or allocation rules.
6. Aggregation, compression, support-retention, injectivity, or reconstruction checks required by the domain.
7. Transition and lineage checks required by the domain.
8. DSD analogies or reductions that must **not** be made.
9. Minimal witness, counterexample, collision, or boundary-case format.
10. Domain-specific verdict vocabulary.
11. Relationship between the external-field verdict and the DSD structural audit verdict.

## Planned protocol groups / 기본 분류

```text
protocols/
├─ mathematics/
├─ science/
├─ law/
├─ software/
├─ ai/
├─ history_media/
├─ administration_organization/
└─ README.md
```

Directories may be created when the first real audit in that domain is added.
Empty directories are intentionally not committed.

## Minimum domain additions / 분야별 최소 추가 항목

### Mathematics / 수학

- exact definitions, domain, axioms, and theorem statement
- proof-step justification
- counterexamples and boundary cases
- distinction between finite computation and general proof
- exact status of assumptions imported from DSD or another formal system
- explicit bridge if a DSD structural category is mapped to a mathematical object

### Science / 과학

- hypothesis, model, observation, and experiment separation
- measurement uncertainty and descriptive resolution
- alternative hypotheses
- reproducibility, repetition, and external data
- constitutive bridge and coefficient provenance when property data are used dynamically
- distinction between reduced readout agreement and component-resolved state agreement

### Law and institutions / 법·제도

- information available at the relevant historical time
- separation of fact, evidence, inference, norm, and judgment
- procedural authority and burden/standard of proof
- competing describable possibilities
- explicit distinction between unavailable evidence and a negative fact

### Software and algorithms / 소프트웨어·알고리즘

- specification, implementation, environment, and output separation
- input domain and exception handling
- branch/state transitions
- versions, dependencies, deterministic or seeded reproduction
- audit evidence status separated from program/DSD object status
- selector, bridge, aggregation, and reconstruction assumptions made machine-readable where feasible
- lineage or stable identifier rules for stateful or versioned objects

### AI / AI

- input, prompt, tools, references, evaluation data, and output separation
- observable process claims vs. unobservable internal-state claims
- sample and benchmark selection
- hallucination, omission, bias, and reproducibility checks
- model/tool/version lock
- explicit distinction between missing information, unavailable capability, and negative output

### History, documents, media / 역사·문헌·언론

- primary vs. secondary sources
- historical information state vs. later knowledge
- quotation, omission, and selection bias
- competing interpretations and irreducible uncertainty
- explicit record of source availability and provenance

### Administration, organization, policy / 행정·조직·정책

- authority and information flow
- available options and exclusion criteria
- factual claims vs. policy goals and norms
- outcome evaluation and hindsight bias
- explicit decision and responsibility transitions

## DSD-specific fields that protocols may require / DSD 전용 선택 필드

Use only when relevant:

```text
DSD_INTERFACE_PROFILE_DATE
FORMATION_LAYER
PROPERTY_CORE
STATIC_AGGREGATION_LAYER
DYNAMICS_LAYER
REALIZED_AXIS_SPECIALIZATION
OBJECT_STATUS
BRIDGE_DECLARATIONS
AGGREGATION_RECONSTRUCTION_CHECK
TRANSITION_CLASS
LINEAGE_REQUIRED
LINEAGE_SUPPLIED
```

## Result format / 결과 형식

Every domain audit should end with three separate summaries:

1. **External-domain verdict** — what the field's own standard says.
2. **DSD structural audit verdict** — what the DSD audit finds about describability, interface use, status discipline, and formation/transition structure.
3. **Correspondence and limits** — direct, partial, encoded, or non-correspondence, including unresolved limits.

Do not combine these into a single success percentage or validation rate.
