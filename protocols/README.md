# Domain Audit Protocols / 분야별 감사 프로토콜

This directory contains domain-specific extensions of the DSD General Audit Framework.

이 디렉터리는 DSD 일반 감사체계에 각 분야의 기존 검증 기준을 추가하는 곳입니다.

## Operating rule / 운영 원칙

The DSD common frame is used to trace structure, describability, selection, exclusion, transition, consistency, norms, and outcome.
It does **not** replace the external validation standard of the audited field.

DSD 공통 프레임은 구조·기술가능성·선택·배제·전이·정합성·규범·결과를 추적하기 위해 사용합니다.
해당 분야의 외부 검증 기준을 DSD 용어로 대체하지 않습니다.

## Required sections for every domain protocol / 분야별 프로토콜 필수 항목

Each protocol should define:

1. External standards used by the field.
2. Which of the eight common DSD axes apply without modification.
3. Additional fields required by the domain.
4. DSD analogies or reductions that must **not** be made.
5. Minimal witness, counterexample, or boundary-case format.
6. Domain-specific verdict vocabulary.
7. Relationship between the external-field verdict and the DSD structural audit verdict.

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

### Science / 과학

- hypothesis, model, observation, and experiment separation
- measurement uncertainty and descriptive resolution
- alternative hypotheses
- reproducibility, repetition, and external data

### Law and institutions / 법·제도

- information available at the relevant historical time
- separation of fact, evidence, inference, norm, and judgment
- procedural authority and burden/standard of proof
- competing describable possibilities

### Software and algorithms / 소프트웨어·알고리즘

- specification, implementation, environment, and output separation
- input domain and exception handling
- branch/state transitions
- versions, dependencies, deterministic or seeded reproduction

### AI / AI

- input, prompt, tools, references, evaluation data, and output separation
- observable process claims vs. unobservable internal-state claims
- sample and benchmark selection
- hallucination, omission, bias, and reproducibility checks

### History, documents, media / 역사·문헌·언론

- primary vs. secondary sources
- historical information state vs. later knowledge
- quotation, omission, and selection bias
- competing interpretations and irreducible uncertainty

### Administration, organization, policy / 행정·조직·정책

- authority and information flow
- available options and exclusion criteria
- factual claims vs. policy goals and norms
- outcome evaluation and hindsight bias

## Result format / 결과 형식

Every domain audit should end with three separate summaries:

1. **External-domain verdict** — what the field's own standard says.
2. **DSD structural audit verdict** — what the DSD audit finds about describability and formation structure.
3. **Correspondence and limits** — direct, partial, encoded, or non-correspondence, including unresolved limits.

Do not combine these into a single success percentage or validation rate.
