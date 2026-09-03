# Mass–Distortion Exterior-Map Factorization Control
# 질량–구조왜곡 외부 맵 인수분해 통제감사

```text
AUDIT_ID: DSD-AUDIT-20260903-PHYSICS-002
STATUS: COMPLETED_SYNTHETIC_CONTROL
DOMAIN: structural gravity / physics
DATE: 2026-09-03
RELATED_METHOD: methodology/SECTOR_RESOLVED_DESCRIBABILITY_PROTOCOL.md
PARENT_AUDIT: DSD-AUDIT-20260903-PHYSICS-001
```

## 1. Audit question / 감사 질문

With total bounded mass held fixed, vary

1. bounded-component mass structure;
2. density-partition mass structure;
3. their intersection structure;

and test whether mass describability and structural-distortion describability must share the same exterior coarse map.

## 2. Internal mass structure / 내부 질량구조

Use two bounded components \(B_1,B_2\) and two density sectors \(H,L\).
Normalize total mass to \(M=1\).

The component-resolved mass structure is

\[
\mathbf M=\begin{pmatrix}
M_{1H}&M_{1L}\\
M_{2H}&M_{2L}
\end{pmatrix}.
\]

Define four synthetic states:

\[
\mathbf M_0=
\begin{pmatrix}
0.45&0.05\\
0.05&0.45
\end{pmatrix},
\]

\[
\mathbf M_\rho=
\begin{pmatrix}
0.40&0.10\\
0.30&0.20
\end{pmatrix},
\]

\[
\mathbf M_B=
\begin{pmatrix}
0.40&0.30\\
0.10&0.20
\end{pmatrix},
\]

\[
\mathbf M_\times=
\begin{pmatrix}
0.25&0.25\\
0.25&0.25
\end{pmatrix}.
\]

All four have total mass 1.

## 3. Marginal maps / 주변합 맵

Define the bounded-component marginal

\[
R_B(\mathbf M)=
\left(
\sum_jM_{1j},
\sum_jM_{2j}
\right),
\]

the density marginal

\[
R_\rho(\mathbf M)=
\left(
\sum_iM_{iH},
\sum_iM_{iL}
\right),
\]

and the total map

\[
T(\mathbf M)=\sum_{ij}M_{ij}.
\]

The four states give:

| State | \(R_B\) | \(R_\rho\) | \(T\) |
|---|---|---|---:|
| \(M_0\) | (0.5, 0.5) | (0.5, 0.5) | 1 |
| \(M_\rho\) | (0.5, 0.5) | (0.7, 0.3) | 1 |
| \(M_B\) | (0.7, 0.3) | (0.5, 0.5) | 1 |
| \(M_\times\) | (0.5, 0.5) | (0.5, 0.5) | 1 |

## 4. Immediate result / 즉시 결과

The bounded and density marginals are not interchangeable.

\[
R_B(\mathbf M_0)=R_B(\mathbf M_\rho)
\]

while

\[
R_\rho(\mathbf M_0)\neq R_\rho(\mathbf M_\rho).
\]

Conversely,

\[
R_\rho(\mathbf M_0)=R_\rho(\mathbf M_B)
\]

while

\[
R_B(\mathbf M_0)\neq R_B(\mathbf M_B).
\]

Therefore

\[
\boxed{\text{bounded-component mass structure}\not\equiv\text{density mass structure}}.
\]

Neither marginal replaces the other.

## 5. Even both marginals do not reconstruct the full intersection structure / 두 주변합만으로도 교차구조 복원 불가

The baseline and cross state satisfy

\[
R_B(\mathbf M_0)=R_B(\mathbf M_\times),
\]

\[
R_\rho(\mathbf M_0)=R_\rho(\mathbf M_\times),
\]

and

\[
T(\mathbf M_0)=T(\mathbf M_\times),
\]

but

\[
\mathbf M_0\neq\mathbf M_\times.
\]

Their difference is

\[
\delta\mathbf M_\times
=\mathbf M_\times-\mathbf M_0
=
0.20
\begin{pmatrix}
-1&1\\
1&-1
\end{pmatrix}.
\]

This change has zero row sums, zero column sums, and zero total.

Thus

\[
\delta\mathbf M_\times\in
\ker R_B\cap\ker R_\rho\cap\ker T,
\]

while

\[
\delta\mathbf M_\times\neq0.
\]

Hence both marginals together can still lose intersection/correlation structure.

## 6. Mass-describability hierarchy / 질량 기술가능성 계층

A useful partial order is

\[
\mathbf M_{B\rho}
\succ
(R_B,R_\rho)
\succ
\{R_B\text{ or }R_\rho\}
\succ
T.
\]

This is not a single scalar-resolution ladder in every case, because \(R_B\) and \(R_\rho\) are generally incomparable.

Mass describability is therefore better represented as a lattice/partial-order of retained structures than as one ratio.

## 7. Synthetic distortion probes / 합성 왜곡 탐침

The following maps are NOT proposed gravitational laws.
They are synthetic control maps used only to test logical necessity.

### Density-sensitive probe

\[
E_X^{(\rho)}(\mathbf M)
=2M_H+M_L,
\]

where

\[
M_H=\sum_iM_{iH},\qquad M_L=\sum_iM_{iL}.
\]

Then

\[
E_X^{(\rho)}(M_0)=1.5,
\quad
E_X^{(\rho)}(M_\rho)=1.7,
\quad
E_X^{(\rho)}(M_B)=1.5,
\quad
E_X^{(\rho)}(M_\times)=1.5.
\]

This probe distinguishes a density redistribution invisible to \(R_B\).

### Bounded-component-sensitive probe

\[
E_X^{(B)}(\mathbf M)
=1.2M_{B_1}+0.8M_{B_2}.
\]

Then

\[
E_X^{(B)}(M_0)=1.0,
\quad
E_X^{(B)}(M_\rho)=1.0,
\quad
E_X^{(B)}(M_B)=1.08,
\quad
E_X^{(B)}(M_\times)=1.0.
\]

This probe distinguishes a bounded-component redistribution invisible to \(R_\rho\).

### Intersection-sensitive probe

\[
E_X^{(\times)}(\mathbf M)
=2(M_{1H}+M_{2L})+(M_{1L}+M_{2H}).
\]

Then

\[
E_X^{(\times)}(M_0)=1.9,
\]

\[
E_X^{(\times)}(M_\times)=1.5.
\]

Therefore a distortion map can distinguish internal intersection structure even when total, bounded marginal, and density marginal are all identical.

## 8. General factorization criterion / 일반 인수분해 기준

Let

\[
E_M:\mathcal M_{\rm int}\to\mathcal M_{\rm ext}
\]

be a mass exterior map and

\[
E_X:\mathcal M_{\rm int}\to\mathcal X_{\rm ext}
\]

be a distortion exterior map built from the same internal source structure.

There exists a map \(F\) such that

\[
E_X=F\circ E_M
\]

if and only if \(E_X\) is constant on every fiber of \(E_M\):

\[
E_M(M_1)=E_M(M_2)
\Rightarrow
E_X(M_1)=E_X(M_2).
\]

For linear maps between vector spaces, this reduces to

\[
\boxed{\ker E_M\subseteq\ker E_X}.
\]

### Interpretation

Every internal mass redistribution hidden by \(E_M\) must also be invisible to \(E_X\) if distortion is to be fully determined by mass describability alone.

If there exists

\[
\delta M\in\ker E_M
\]

with

\[
E_X(\delta M)\neq0,
\]

then distortion describability does not factor through that mass descriptor.

## 9. Hidden-to-mass but visible-to-distortion dimension / 질량에는 숨고 왜곡에는 보이는 모드

In a linear finite-dimensional specialization, define

\[
d_{M\to X}
=
\dim\ker E_M
-
\dim(\ker E_M\cap\ker E_X).
\]

If

\[
d_{M\to X}>0,
\]

there exist independent internal redistribution modes that are invisible to the chosen mass exterior descriptor but remain visible to the distortion descriptor.

This is a structural diagnostic, not a gravitational-strength coefficient.

## 10. Near-field vs far-field consequence / 근거리와 원거리

A far-field mass-only response requires the stronger condition

\[
\ker T\subseteq\ker E_X^{(\infty)}.
\]

That is, every internal mass redistribution preserving total mass must become invisible to the far-field distortion descriptor.

Near the source, the condition may fail:

\[
\ker T\not\subseteq\ker E_X^{(\rm near)}.
\]

This provides a clean structural form for the coexistence of

- near-field sensitivity to density/bounded/intersection structure;
- far-field universality controlled only by total coarse source.

The far-field inclusion is a condition to be derived or tested, not assumed as a DSD theorem.

## 11. Verdict / 판정

```text
VERDICT:
CONFIRMED_AS_LOGICAL_SEPARATION / CONDITIONAL_PHYSICAL_APPLICATION

MAXIMUM_SUPPORTED_CLAIM:
Bounded-component mass structure, density mass structure, their intersection structure, and total mass are distinct descriptive layers. Mass describability and distortion describability need not share the same exterior map. Distortion can be determined from a chosen mass descriptor only when it is constant on that mass descriptor's fibers; in the linear case, ker(E_M) must be contained in ker(E_X).

UNSUPPORTED:
- any specific physical distortion weighting used in the synthetic probes
- the claim that actual gravity must detect density, bounded-component, or intersection modes
- the claim that the far-field distortion map automatically factors through total mass
```

## 12. Eight-axis summary / 8축 요약

| Axis | Summary |
|---|---|
| D | mass describability resolved into full intersection, bounded marginal, density marginal, and total layers |
| R | observer resolution not used; maps are physical-description controls |
| S | 2x2 minimal synthetic states selected to isolate orthogonal redistribution modes |
| E | no measured G or standard gravity law used |
| T | mass-structure equality to distortion equality rejected unless factorization criterion holds |
| C | explicit countermodels demonstrate non-equivalence of the maps |
| N | not applicable |
| O | mass/distortion map independence is logically possible; physical bridge remains open |

## 13. Next step / 다음 단계

Generalize the factorization audit from mass to the full sector family:

\[
E_B,E_L,E_M,E_R,E_P,E_X.
\]

Determine which sectors are upstream sufficient descriptors for others by testing fiber constancy / kernel inclusion.

For structural gravity, prioritize whether the distortion map factors through

1. total mass only;
2. mass + density marginal;
3. mass + bounded-component marginal;
4. the full bounded-density intersection structure.

This creates a falsifiable hierarchy of candidate exterior descriptions before any absolute coupling normalization is introduced.
