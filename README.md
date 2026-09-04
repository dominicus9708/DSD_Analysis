# DSD Analysis / DSD 분석론

This repository records the development, application, and audit methodology of **DSD Analysis**.

이 저장소는 **DSD 분석론**의 전개, 분야별 적용, 검증·감사 방법론을 기록합니다.

## Repository role / 저장소의 역할

DSD Analysis does not force all DSD layers into one fixed package.
It selects only the structures needed for the audited or analyzed object from the current Formation, General Property, Static Aggregation, Dynamics, and optional specialization interfaces.
Its purpose is to decompose problems into distinguishable states, relations, applicability conditions, compositions, selections, exclusions, transitions, bridges, and describability conditions, then compare those structures with external disciplines without replacing the external discipline's own terminology or standards.

DSD 분석론은 최신 DSD의 Formation, General Property, Static Aggregation, Dynamics 및 선택적 특수화를 하나의 고정 패키지로 강제하지 않습니다.
분석 대상에 필요한 층위만 명시적으로 선택하고, 상태·관계·적용·합성·선택·배제·전이·브리지·기술가능성을 분해한 뒤 외부 분야와 비교합니다.
외부 분야의 기존 용어와 검증 기준을 DSD 용어로 대체하지 않는 것을 원칙으로 합니다.

The current paper-facing interface is fixed in [`methodology/DSD_INTERFACE_PROFILE.md`](methodology/DSD_INTERFACE_PROFILE.md).
Realized-axis geometry is treated as an optional specialization of the general Property interface rather than as a universal property core.

현재 논문 기준 DSD 층위와 상태·브리지·집계·lineage 규칙은 [`methodology/DSD_INTERFACE_PROFILE.md`](methodology/DSD_INTERFACE_PROFILE.md)에서 관리합니다.
실현축 기하는 일반 Property 코어의 보편 전제가 아니라 선택적 특수화로 다룹니다.

## General audit framework / 일반 감사체계

The **DSD General Audit Framework** is maintained inside this repository rather than as a separate repository.
It formalizes a reusable audit path from source preservation through describability, selection/exclusion, transitions, contradiction checks, verdict discipline, and reproducibility.

**DSD 일반 감사체계**는 별도 저장소가 아니라 이 분석론 저장소 내부의 공통 방법론 모듈로 관리합니다.
원자료 보존부터 기술가능성, 선택·배제, 전이, 모순 검사, 판정 강도, 재현·추적까지 반복 가능한 감사 경로를 제공합니다.

Analysis and audit are distinct layers:

- **Analysis / 분석**: decompose and compare the structure of the object.
- **Audit / 감사**: retrace the analysis and its conclusions under an explicit scope, procedure, interface lock, and verdict rule.

## Current structure / 현재 구조

```text
DSD_Analysis/
├─ README.md
├─ methodology/
│  ├─ DSD_INTERFACE_PROFILE.md
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

## Current DSD layer model / 현재 DSD 층위 모델

The current common interface distinguishes:

1. **Formation** — staged structural admission, partial assignment, operational-channel formation, and finite composition after post-Stage-VI term data are supplied.
2. **General Property** — typed property profiles, applicability, contextual prerequisites, and partial property assignments over a fixed Stage-VI formation background.
3. **Static Aggregation** — analytic realization of admitted channels plus an optional, separate typed-property aggregation interface.
4. **Dynamics** — component-resolved trajectories, regular epochs, transition classes, and lineage.
5. **Optional specializations** — realized-axis geometry and other additional structures when explicitly supplied.

These are not a mandatory serial chain.
A case records only the layers it actually uses.

## Required interface lock / 필수 인터페이스 잠금

When DSD formal structure materially affects an analysis or audit, record:

```text
DSD_INTERFACE_PROFILE_DATE:
FORMATION_LAYER: used / not used
PROPERTY_CORE: used / not used
STATIC_AGGREGATION_LAYER: used / not used
DYNAMICS_LAYER: used / not used
REALIZED_AXIS_SPECIALIZATION: supplied / not supplied
OTHER_SPECIALIZATION:
SOURCE_VERSIONS:
```

This prevents a later paper revision from being silently projected backward onto an older audit.

## Status discipline / 상태 규율

Audit evidence status and DSD object status are separate.

- **Evidence**: established within scope / undetermined or insufficient / out of scope.
- **Formation**: undefined assignment, defined zero, defined value, channel absence, admitted zero term, and other formation statuses required by the selected layer.
- **Property**: undeclared, profile unavailable, inapplicable, prerequisite unsatisfied, applicable but undefined, defined zero, defined nonzero or otherwise defined.

Do not convert undefinedness or absence into numerical zero merely to simplify a record.

## Bridge, aggregation, and lineage discipline / 브리지·집계·lineage 규율

- A multi-input property datum has no automatic unary channel owner.
- Static property-to-analytic mappings require an explicit bridge.
- Property-to-dynamic-operator mappings require a separate constitutive dynamic bridge.
- Aggregate equality does not automatically imply equal support or decomposition; reconstruction claims require injectivity or another explicit theorem/condition.
- Formation-level identity changes are not ordinary value evolution of one unchanged channel; successor claims require the appropriate lineage record.

## Structural gravity logging / 구조적 중력 로그

Structural-gravity results developed in the project conversation are recorded as a running research log rather than promoted into general DSD Analysis methodology merely because they were useful in one research line.

구조적 중력 채팅에서 새 성과·교정·반례·조건부 정리·핵심 미결정점이 생기면 [`audits/science/STRUCTURAL_GRAVITY_RESEARCH_LOG.md`](audits/science/STRUCTURAL_GRAVITY_RESEARCH_LOG.md)에 날짜순으로 누적합니다.
같은 시점에 Notion의 `구조적 중력` 하위 `구조적 중력 연구 로그`에도 동기화합니다.

상세 감사가 필요한 경우에는 별도의 감사 기록 파일을 추가하되, 일반 방법론으로 승격하는 것은 별도 판단이 있을 때만 진행합니다.

## Where to start / 활용 순서

### To understand the method / 방법론 확인

Read:

1. [`methodology/DSD_INTERFACE_PROFILE.md`](methodology/DSD_INTERFACE_PROFILE.md)
2. [`methodology/GENERAL_AUDIT_FRAMEWORK.md`](methodology/GENERAL_AUDIT_FRAMEWORK.md)
3. [`methodology/AUDIT_RECORDING_STANDARD.md`](methodology/AUDIT_RECORDING_STANDARD.md)

### To start an actual audit / 실제 감사 시작

1. Copy [`templates/AUDIT_CASE_TEMPLATE.md`](templates/AUDIT_CASE_TEMPLATE.md).
2. Lock the DSD interface profile and exact source revisions used by the case.
3. Lock the audit question, scope, time, resolution, and external standard before judging the result.
4. Preserve original claims and sources before DSD reinterpretation.
5. Separate audit evidence status from DSD object status.
6. Record selections **and exclusions**.
7. Record every material cross-layer selector or bridge.
8. Trace transitions, lineage requirements, alternative describabilities, and aggregation/reconstruction assumptions.
9. End with the external-domain verdict, DSD structural audit verdict, limitations, and reproducibility information.

## Common eight-axis audit frame / 공통 8축

The stable general audit layer summarizes each case with:

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
- The same outcome does not prove a unique cause, support, or decomposition. / 같은 결과가 하나의 원인·support·구조분해만을 증명하지 않습니다.
- Present knowledge must not be projected backward without historical availability. / 현재의 정보를 당시에도 알았던 것으로 소급하지 않습니다.
- Facts, inferences, norms, and decisions must be separated. / 사실·추론·규범·결정을 분리합니다.
- Finite computation must not be silently upgraded into a general proof. / 유한 계산을 일반 증명으로 승격하지 않습니다.
- Favorable cases must not be selectively retained while failures are discarded. / 유리한 사례만 남기고 실패 사례를 버리지 않습니다.
- Optional specialization data must not be promoted into universal DSD requirements. / 선택적 특수화 구조를 보편 DSD 전제로 승격하지 않습니다.

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

- [DSD Interface Profile](methodology/DSD_INTERFACE_PROFILE.md)
- [General Audit Framework](methodology/GENERAL_AUDIT_FRAMEWORK.md)
- [Audit Recording Standard](methodology/AUDIT_RECORDING_STANDARD.md)
- [Structural Gravity Research Log](audits/science/STRUCTURAL_GRAVITY_RESEARCH_LOG.md)
- [Structural Gravity Sector-Resolved Audit](audits/science/2026-09-03_structural-gravity-sector-describability-audit.md)
- [Mass–Distortion Factorization Control](audits/science/2026-09-03_mass-distortion-factorization-control.md)
- [Audit Case Template](templates/AUDIT_CASE_TEMPLATE.md)
- [Domain Protocol Guide](protocols/README.md)
- [Individual Audit Records Guide](audits/README.md)
