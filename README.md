# DSD Analysis / DSD 분석론

This repository records the development and application of **DSD Analysis**.
The **DSD Audit** framework is now maintained as a distinct sibling module under [`DSD_Audit/`](DSD_Audit/).

이 저장소는 **DSD 분석론**의 전개와 분야별 적용을 기록합니다.
**DSD 감사**는 분석론과 구분하여 [`DSD_Audit/`](DSD_Audit/) 전용 폴더에서 별도 관리합니다.

## Repository role / 저장소의 역할

DSD Analysis selects only the DSD structures needed for the object being analyzed from the current Formation, General Property, Static Aggregation, Dynamics, and optional specialization interfaces.
Its purpose is to decompose and compare states, relations, applicability conditions, compositions, describability conditions, alternatives, and structural mappings without replacing the external field's own terminology or standards.

DSD 분석론은 Formation, General Property, Static Aggregation, Dynamics 및 선택적 특수화를 하나의 고정 패키지로 강제하지 않습니다.
분석 대상에 필요한 구조만 선택하여 상태·관계·적용·합성·기술가능성·대안·구조 대응을 분해하고 비교합니다.

## Separation from DSD Audit / DSD 감사와의 분리

Analysis and audit are related but distinct.

- **DSD Analysis / DSD 분석론**: decomposes, compares, and reinterprets structures.
- **DSD Audit / DSD 감사**: retraces an analysis, calculation, judgment, or record under explicit scope, interface, evidence, procedure, and verdict rules.

An analysis result is not automatically an audit pass.
Audit methodology, templates, protocols, future algorithmization, and new audit records are maintained under [`DSD_Audit/`](DSD_Audit/).

## Shared DSD interface / 공유 DSD 인터페이스

The current paper-facing DSD layer and status interface is maintained at:

- [`methodology/DSD_INTERFACE_PROFILE.md`](methodology/DSD_INTERFACE_PROFILE.md)

This interface is shared by DSD Analysis and DSD Audit.
Realized-axis geometry is treated as an optional specialization of the general Property interface rather than as a universal property core.

## Current structure / 현재 구조

```text
DSD_Analysis/
├─ README.md
├─ methodology/
│  └─ DSD_INTERFACE_PROFILE.md        # shared DSD interface
├─ DSD_Audit/                         # separated audit module
│  ├─ README.md
│  ├─ methodology/
│  │  ├─ GENERAL_AUDIT_FRAMEWORK.md
│  │  ├─ AUDIT_RECORDING_STANDARD.md
│  │  └─ AUDIT_ALGORITHMIZATION_ROADMAP.md
│  ├─ templates/
│  │  └─ AUDIT_CASE_TEMPLATE.md
│  ├─ protocols/
│  │  └─ README.md
│  └─ audits/
│     └─ README.md
├─ audits/                             # legacy/historical audit records
│  └─ science/
└─ ...                                 # analysis roadmaps and records
```

Older audit-methodology files may remain at previous repository paths for historical compatibility.
New audit work should use the `DSD_Audit/` structure.

## Current DSD layer model / 현재 DSD 층위 모델

The shared interface distinguishes:

1. **Formation** — staged structural admission, partial assignment, operational-channel formation, and finite composition after post-Stage-VI term data are supplied.
2. **General Property** — typed property profiles, applicability, contextual prerequisites, and partial property assignments over a fixed Stage-VI formation background.
3. **Static Aggregation** — analytic realization of admitted channels plus an optional, separate typed-property aggregation interface.
4. **Dynamics** — component-resolved trajectories, regular epochs, transition classes, and lineage.
5. **Optional specializations** — realized-axis geometry and other additional structures when explicitly supplied.

These are not a mandatory serial chain.
A case records only the layers it actually uses.

## Analysis operating rules / 분석 운영 규칙

- Preserve the external field's original terminology and validation standards.
- Do not infer structural identity from terminological similarity.
- Distinguish undefinedness, absence, inapplicability, and defined zero when the selected interface requires it.
- Do not infer a cross-layer bridge merely because names or coordinates resemble one another.
- Do not infer unique support, decomposition, or cause from aggregate equality without an applicable reconstruction basis.
- Preserve direct correspondence, partial correspondence, correspondence after explicit encoding, and non-correspondence.
- Record failed mappings and boundary cases rather than collecting only DSD-favorable examples.

## Structural gravity logging / 구조적 중력 로그

Structural-gravity results developed in the project conversation remain recorded as a research-line log rather than being promoted automatically into general DSD Analysis or DSD Audit methodology.

Legacy records currently remain under the historical `audits/science/` path.
When a structural-gravity case is newly re-audited, the new audit record should be created under `DSD_Audit/audits/science/` while preserving the legacy source path.

## Where to start / 활용 순서

### DSD Analysis / DSD 분석론

1. Read [`methodology/DSD_INTERFACE_PROFILE.md`](methodology/DSD_INTERFACE_PROFILE.md) when formal DSD layers matter.
2. Fix the analysis target and external-domain terminology.
3. Select only the DSD layers needed for the case.
4. Build structural correspondences without replacing external standards.
5. Preserve non-correspondence, alternatives, counterexamples, and boundary cases.

### DSD Audit / DSD 감사

Use the separated audit module:

1. [`DSD_Audit/README.md`](DSD_Audit/README.md)
2. [`DSD_Audit/methodology/GENERAL_AUDIT_FRAMEWORK.md`](DSD_Audit/methodology/GENERAL_AUDIT_FRAMEWORK.md)
3. [`DSD_Audit/methodology/AUDIT_RECORDING_STANDARD.md`](DSD_Audit/methodology/AUDIT_RECORDING_STANDARD.md)
4. [`DSD_Audit/templates/AUDIT_CASE_TEMPLATE.md`](DSD_Audit/templates/AUDIT_CASE_TEMPLATE.md)
5. [`DSD_Audit/methodology/AUDIT_ALGORITHMIZATION_ROADMAP.md`](DSD_Audit/methodology/AUDIT_ALGORITHMIZATION_ROADMAP.md) for future software-assisted auditing.

## Historical record policy / 과거 기록 보존 원칙

Separating DSD Audit from DSD Analysis does not retroactively rewrite older audit records.
Older paths, terminology, interface versions, and verdicts are preserved as historical states.
When a case is re-audited under the separated structure, create a new record or explicit migration record and cross-link the previous path.
