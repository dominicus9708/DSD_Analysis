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

```text
DSD Analysis
└─ General Audit Framework
   ├─ Domain Protocols
   └─ Individual Audit Records
```

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
   └─ README.md
```

Empty domain directories are intentionally not committed.
They should be created when the first real protocol or audit case is added.

빈 분야 디렉터리는 미리 만들지 않습니다.
실제 프로토콜이나 감사 사례가 처음 생길 때 해당 디렉터리를 추가합니다.

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

실제 감사를 시작할 때는 템플릿을 복사한 뒤, 결과를 먼저 정하지 말고 **감사 질문과 범위를 먼저 고정**합니다.
이후 원자료를 보존하고 선택·배제·전이·대안 기술가능성을 추적한 뒤 최종 판정을 기록합니다.

### To add a domain protocol / 분야별 프로토콜 추가

Read [`protocols/README.md`](protocols/README.md) and add only the requirements unique to that field.
The field's existing standard remains primary.

[`protocols/README.md`](protocols/README.md)를 기준으로 해당 분야에 필요한 추가 감사 규칙만 정의합니다.
분야 자체의 기존 검증 기준은 그대로 우선합니다.

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

이 8축은 기록·감사를 위한 공통 골격이며, 수학적 증명·과학 실험·법적 판단 기준·소프트웨어 테스트 등 분야별 외부 기준을 대신하지 않습니다.

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

Use the narrowest verdict that matches the audited layer.
Do not compress independent failure types into a generic pass/fail when the cause can be recorded more precisely.

판정은 가능한 한 좁고 구체적으로 기록합니다.
서로 다른 실패 원인을 단순한 PASS/FAIL 하나로 합치지 않습니다.

## Related documentation / 관련 문서

- [General Audit Framework](methodology/GENERAL_AUDIT_FRAMEWORK.md)
- [Audit Recording Standard](methodology/AUDIT_RECORDING_STANDARD.md)
- [Audit Case Template](templates/AUDIT_CASE_TEMPLATE.md)
- [Domain Protocol Guide](protocols/README.md)
- [Individual Audit Records Guide](audits/README.md)
