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
3. Lock the audit question and scope before evaluating the result.
4. Preserve original source claims before DSD reinterpretation.
5. Record both selected and excluded alternatives.
6. End with the external-domain verdict, DSD structural verdict, limits, and reproducibility information.

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

Do not erase a previous reasonable verdict merely because new evidence appears later.
Instead, preserve the earlier record and add a revision entry showing:

- what new information appeared
- which earlier assumption or scope changed
- how the verdict changed
- whether the earlier verdict was unreasonable at the time or merely superseded by new information

This prevents hindsight information from being silently projected into the earlier audit state.