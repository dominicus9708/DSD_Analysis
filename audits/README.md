# Individual Audit Records / 개별 감사 기록

This directory stores completed or ongoing audit cases that apply the common DSD audit method to a specific object.

이 디렉터리는 DSD 일반 감사체계를 실제 대상에 적용한 개별 감사 기록을 보관합니다.

## Recommended layout / 권장 구조

```text
audits/
├─ mathematics/
├─ science/
├─ law/
├─ software/
├─ ai/
├─ history_media/
├─ administration_organization/
└─ README.md
```

Create a domain directory only when the first case exists.

## Current records / 현재 기록

- [`science/STRUCTURAL_GRAVITY_RESEARCH_LOG.md`](science/STRUCTURAL_GRAVITY_RESEARCH_LOG.md) — running project-conversation log for structural-gravity achievements, corrections, counterexamples, conditional theorems, and unresolved bottlenecks. Synchronized with the Notion `구조적 중력 연구 로그` page.
- [`science/2026-09-03_structural-gravity-sector-describability-audit.md`](science/2026-09-03_structural-gravity-sector-describability-audit.md) — structural gravity sector-resolved describability, exterior-interface, scaling, and normalization audit (`DSD-AUDIT-20260903-PHYSICS-001`).
- [`science/2026-09-03_mass-distortion-factorization-control.md`](science/2026-09-03_mass-distortion-factorization-control.md) — minimal bounded/density mass-partition control and mass→distortion exterior-map factorization criterion (`DSD-AUDIT-20260903-PHYSICS-002`).

## File naming / 파일명

Recommended:

```text
YYYY-MM-DD_short-audit-title.md
```

For audits with a formal ID, place the ID near the top of the file:

```text
DSD-AUDIT-YYYYMMDD-DOMAIN-NNN
```

## Starting a new audit / 새 감사 시작

1. Copy `templates/AUDIT_CASE_TEMPLATE.md`.
2. Place the copy under the appropriate domain directory in `audits/`.
3. Lock the audit question, scope, time, resolution, and external standard before evaluating the result.
4. If DSD formal layers materially affect the audit, lock the current interface profile from `methodology/DSD_INTERFACE_PROFILE.md` and record the exact predecessor-source revisions used.
5. Preserve original source claims before DSD reinterpretation.
6. Keep audit evidence status separate from Formation/Property/Dynamics object status.
7. Record both selected and excluded alternatives.
8. Record every material selector, bridge, allocation rule, aggregation/reconstruction assumption, and lineage requirement.
9. End with the external-domain verdict, DSD structural verdict, limits, and reproducibility information.

## Interface and source lock / 인터페이스·출처 잠금

For a new DSD-dependent audit, record at minimum:

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

Do not assume that the newest DSD paper revision was the basis of an older audit.
The interface lock records the actual state under which the audit was performed.

## Historical-record policy / 과거 기록 보존 원칙

Older audit records may contain terminology or interfaces that were correct for the DSD revision used at that time, including earlier realized-axis or axis-property terminology.
Do **not** rewrite those records merely to make them look current.

If an older case is re-evaluated under the current General Property / Static Aggregation / Dynamics interfaces:

1. preserve the original record and verdict;
2. append a revision or migration section;
3. state the old and new interface profiles separately;
4. identify which conclusions survive unchanged, which require reinterpretation, and which become unsupported;
5. do not back-project the current generalized Property core into the historical audit as if it had already been used.

Recommended migration fields:

```text
METHODOLOGY_VERSION:
PREVIOUS_DSD_INTERFACE_PROFILE:
CURRENT_DSD_INTERFACE_PROFILE:
MIGRATION_STATUS:
LEGACY_TERMINOLOGY:
MIGRATION_NOTES:
VERDICT_CHANGED:
REASON:
```

## Audit status / 감사 상태

Use clear textual status near the top of a case when useful:

```text
STATUS: PLANNED
STATUS: IN_PROGRESS
STATUS: BLOCKED_BY_MISSING_EVIDENCE
STATUS: COMPLETED
STATUS: REVISED
```

`BLOCKED_BY_MISSING_EVIDENCE` is not a negative verdict. It means the audit cannot yet decide the relevant question from the available material.

## Revision policy / 개정 원칙

Do not erase a previous reasonable verdict merely because new evidence or a new DSD interface appears later.
Instead, preserve the earlier record and add a revision entry showing:

- what new information or interface appeared
- which earlier assumption or scope changed
- how the verdict changed
- whether the earlier verdict was unreasonable at the time or merely superseded by new information
- whether terminology changed because a former specialization became a non-universal optional module

This prevents hindsight information and later DSD generalizations from being silently projected into the earlier audit state.
