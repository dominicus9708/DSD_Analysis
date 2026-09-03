# DSD Analysis / DSD 분석론

This repository records the development, application, and audit methodology of **DSD Analysis**.

이 저장소는 **DSD 분석론**의 전개, 분야별 적용, 검증·감사 방법론을 기록합니다.

## Repository role / 저장소의 역할

DSD Analysis uses structures from the Formation Axiom System and the Axis-Property Axiom System selectively rather than forcing them as one fixed package.
Its purpose is to decompose problems into distinguishable states, relations, applicability conditions, compositions, selections, exclusions, and describability conditions, then compare those structures with external disciplines without replacing the external discipline's own terminology or standards.

DSD 분석론은 형성공리계와 축 속성공리계를 항상 하나의 고정된 패키지로 강제하지 않고, 분석 대상에 필요한 구조를 선택적으로 사용합니다.
대상의 상태·관계·적용·합성·선택·배제·기술가능성을 분해한 뒤 외부 분야와 비교하되, 외부 분야의 기존 용어와 검증 기준을 DSD 용어로 대체하지 않는 것을 원칙으로 합니다.

## General audit framework / 일반 감사체계

The **DSD General Audit Framework** is maintained inside this repository rather than as a separate repository.
It formalizes a reusable audit path from source preservation through describability, selection/exclusion, transitions, contradiction checks, verdict discipline, and reproducibility.

**DSD 일반 감사체계**는 별도 저장소가 아니라 이 분석론 저장소 내부의 공통 방법론 모듈로 관리합니다.
원자료 보존부터 기술가능성, 선택·배제, 전이, 모순 검사, 판정 강도, 재현·추적까지 반복 가능한 감사 경로를 제공합니다.

Analysis and audit are distinct layers:

- **Analysis / 분석**: decompose and compare the structure of the object.
- **Audit / 감사**: retrace the analysis and its conclusions under an explicit scope, procedure, and verdict rule.

## Current structure / 현재 구조

```text
DSD_Analysis/
├─ README.md
├─ methodology/
│  ├─ GENERAL_AUDIT_FRAMEWORK.md
│  └─ AUDIT_RECORDING_STANDARD.md
├─ templates/
│  └─ AUDIT_CASE_TEMPLATE.md
├─ protocols/
│  └─ README.md
└─ audits/
   ├─ science/
   │  ├─ STRUCTURAL_GRAVITY_RESEARCH_LOG.md
   │  ├─ 2026-09-03_structural-gravity-sector-describability-audit.md
   │  └─ 2026-09-03_mass-distortion-factorization-control.md
   └─ README.md
```

## Structural gravity logging / 구조적 중력 로그

Structural-gravity results developed in the project conversation are recorded as a running research log rather than promoted into general DSD Analysis methodology merely because they were useful in one research line.

구조적 중력 채팅에서 새 성과·교정·반례·조건부 정리·핵심 미결정점이 생기면 [`audits/science/STRUCTURAL_GRAVITY_RESEARCH_LOG.md`](audits/science/STRUCTURAL_GRAVITY_RESEARCH_LOG.md)에 날짜순으로 누적합니다.
같은 시점에 Notion의 `구조적 중력` 하위 `구조적 중력 연구 로그`에도 동기화합니다.

상세 감사가 필요한 경우에는 별도의 감사 기록 파일을 추가하되, 일반 방법론으로 승격하는 것은 별도 판단이 있을 때만 진행합니다.

## Where to start / 활용 순서

### To understand the method / 방법론 확인

Read:

1. [`methodology/GENERAL_AUDIT_FRAMEWORK.md`](methodology/GENERAL_AUDIT_FRAMEWORK.md)
2. [`methodology/AUDIT_RECORDING_STANDARD.md`](methodology/AUDIT_RECORDING_STANDARD.md)

### To start an actual audit / 실제 감사 시작

1. Copy [`templates/AUDIT_CASE_TEMPLATE.md`](templates/AUDIT_CASE_TEMPLATE.md).
2. Create the appropriate domain directory under `audits/` if it does not exist.
3. Lock the audit question, scope, time, resolution, and external standard before judging the result.
4. Preserve original claims and sources before DSD reinterpretation.
5. Record selections **and exclusions**.
6. Trace transitions and alternative describabilities.
7. End with the external-domain verdict, DSD structural audit verdict, limitations, and reproducibility information.

## Common eight-axis audit frame / 공통 8축

The general audit layer summarizes each case with:

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

These axes are a recording and audit frame, not a substitute for domain-specific mathematics, experiment, legal doctrine, software testing, or other external standards.

## Core safeguards / 핵심 감사 원칙

- Not described does not mean false. / 기술되지 않았다고 해서 거짓은 아닙니다.
- Not observed does not automatically mean nonexistent. / 관찰되지 않았다고 해서 자동으로 부재가 되는 것은 아닙니다.
- Possible does not mean established. / 가능하다는 것과 확립되었다는 것은 다릅니다.
- The same outcome does not prove a unique cause or structure. / 같은 결과가 하나의 원인이나 구조만을 증명하지 않습니다.
- Present knowledge must not be projected backward without historical availability. / 현재의 정보를 당시에도 알았던 것으로 소급하지 않습니다.
- Facts, inferences, norms, and decisions must be separated. / 사실·추론·규범·결정을 분리합니다.
- Finite computation must not be silently upgraded into a general proof. / 유한 계산을 일반 증명으로 승격하지 않습니다.
- Favorable cases must not be selectively retained while failures are discarded. / 유리한 사례만 남기고 실패 사례를 버리지 않습니다.

## Default verdict vocabulary / 기본 판정

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

## Related documentation / 관련 문서

- [General Audit Framework](methodology/GENERAL_AUDIT_FRAMEWORK.md)
- [Audit Recording Standard](methodology/AUDIT_RECORDING_STANDARD.md)
- [Structural Gravity Research Log](audits/science/STRUCTURAL_GRAVITY_RESEARCH_LOG.md)
- [Structural Gravity Sector-Resolved Audit](audits/science/2026-09-03_structural-gravity-sector-describability-audit.md)
- [Mass–Distortion Factorization Control](audits/science/2026-09-03_mass-distortion-factorization-control.md)
- [Audit Case Template](templates/AUDIT_CASE_TEMPLATE.md)
- [Domain Protocol Guide](protocols/README.md)
- [Individual Audit Records Guide](audits/README.md)