# DSD General Audit Framework / DSD 일반 감사체계

## 1. Purpose / 목적

The DSD General Audit Framework is the stable common audit layer used by **DSD Audit**.
It retraces how a claim, calculation, judgment, procedure, model, decision, or output is formed from describable information, selections, exclusions, transitions, bridges, aggregation assumptions, and explicit criteria.

DSD 일반 감사체계는 **DSD 감사**의 안정적인 공통 감사층입니다.
주장·계산·판단·절차·모형·결정·출력이 어떤 기술가능한 정보, 선택·배제, 전이, bridge, 집계 가정, 명시적 기준을 거쳐 형성되었는지 재추적합니다.

It does not replace field-specific standards of mathematics, science, law, software engineering, history, administration, or other domains.

## 2. Position / 위치

```text
DSD Analysis  <->  DSD Audit
                     |
                     +-- General Audit Framework
                     +-- Domain Protocols
                     +-- Individual Audit Records
```

- **Analysis** decomposes and compares structures.
- **Audit** retraces the path and supported claim under explicit rules.

An analysis result is not automatically an audit pass.
An audit failure does not automatically mean the audited object is false in every possible sense.

## 3. Shared DSD interface lock / 공유 DSD 인터페이스 잠금

When DSD formal layers materially affect the case, use the shared profile:

- [`../../methodology/DSD_INTERFACE_PROFILE.md`](../../methodology/DSD_INTERFACE_PROFILE.md)

Record the exact interface date and source revisions actually used.

## 4. Eight-axis common frame / 공통 8축

\[
\mathcal{A}=(D,R,S,E,T,C,N,O)
\]

- **D — Describability / 기술가능성**
- **R — Resolution / 해상도**
- **S — Selection / 선택**
- **E — Exclusion / 배제**
- **T — Transition / 전이**
- **C — Consistency / 정합성**
- **N — Norm / 규범·판정 기준**
- **O — Outcome / 결과**

These axes are an audit-recording frame, not a substitute for domain truth or validity standards.

## 5. Required distinctions / 필수 구분

### 5.1 Audit evidence status / 감사 증거 상태

```text
ESTABLISHED_WITHIN_SCOPE
UNDETERMINED_OR_INSUFFICIENT
OUT_OF_SCOPE
```

### 5.2 DSD object status / DSD 객체 상태

When a DSD layer is used, preserve the object-status distinctions required by the shared interface profile.
Do not collapse undefinedness, absence, inapplicability, or prerequisite failure into numerical zero merely to simplify the record.

### 5.3 Proposition layers / 명제 층위

- Fact
- Inference
- Norm
- Decision

### 5.4 Mapping strength / 대응 강도

- Direct correspondence
- Partial correspondence
- Correspondence after explicit additional encoding
- Non-correspondence

## 6. Universal audit procedure / 보편 감사 절차

1. Fix object and audit question.
2. Fix scope, time, descriptive resolution, exclusions, and external standard.
3. Lock DSD interface and source revisions when relevant.
4. Preserve original source claims and procedures.
5. Separate evidence status from DSD object status.
6. Reconstruct available alternatives.
7. Record selections and exclusions with criteria.
8. Record material selectors and bridges.
9. Trace transitions and lineage requirements.
10. Audit aggregation, information loss, injectivity, and reconstruction claims where used.
11. Separate fact, inference, norm, and decision.
12. Search for witnesses, counterexamples, and boundary cases.
13. Check definition, transition, structural, and claim-level contradictions.
14. Restrict the verdict to the maximum supported claim.
15. Preserve enough material for independent reconstruction or reproduction.

## 7. Core safeguards / 핵심 금지 규칙

- Not described does not mean false.
- Not observed does not automatically mean nonexistent.
- Possible does not mean established.
- The same output does not prove a unique cause, support, or decomposition.
- Present knowledge must not be projected backward without historical availability.
- Facts and norms must not be silently conflated.
- Finite computation must not be upgraded into a general proof without a separate argument.
- Favorable cases must not be retained by post-hoc exclusion of failures.
- Optional DSD specializations must not be promoted into universal DSD requirements.

## 8. Default verdict vocabulary / 기본 판정

```text
CONFIRMED
CONDITIONALLY_CONFIRMED
PARTIALLY_CONFIRMED
UNDETERMINED
INSUFFICIENT_BASIS
EXCLUSION_ERROR
TRANSITION_ERROR
NORM_CONFLATION
CONTRADICTION
OVERCLAIM
```

## 9. Domain extension rule / 분야별 확장

The common frame remains stable while domain protocols add field-specific requirements.
External-domain judgment and DSD structural audit judgment must remain separately recorded.

## 10. Minimum audit record / 최소 감사 기록

```text
OBJECT
QUESTION
SCOPE
INTERFACE_LOCK
SOURCE
EVIDENCE_STATUS
OBJECT_STATUS
SELECTION
EXCLUSION
BRIDGES
TRANSITIONS
LINEAGE
ALTERNATIVES
AGGREGATION_RECONSTRUCTION
WITNESS_OR_COUNTEREXAMPLE
CONTRADICTION_AUDIT
VERDICT
LIMITS
REPRODUCIBILITY
REVISION_MIGRATION
```

Use `../templates/AUDIT_CASE_TEMPLATE.md` for actual cases.
