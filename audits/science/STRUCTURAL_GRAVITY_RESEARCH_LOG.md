# Structural Gravity Research Log / 구조적 중력 연구 로그

> 운영 규칙: 이 파일은 구조적 중력 연구 중 실제로 새 성과, 교정, 반례, 조건부 정리, 핵심 미결정점이 생길 때마다 날짜순으로 누적한다. 일반 DSD 분석론 규칙을 작성하는 곳이 아니다. 같은 시점에 Notion의 `구조적 중력 연구 로그`도 동기화한다.

## Log format / 기록 형식

Each entry records:

- date
- experiment / stage number
- new result
- verdict: confirmed / conditional / rejected / unresolved
- consequence for the current chain
- next audit target

---

## 2026-09-03 — Experiments 19–20: exterior selection vs propagation

### Result

Factor the distance-dependent exterior map as

\[
\Pi_r=U_r\circ E.
\]

- \(E\): selects what can physically enter the exterior sector.
- \(U_r\): propagates/reorganizes exterior information with distance/time.

Thus

\[
\boxed{\text{absent from exterior at the start}\neq\text{present at boundary but later erased}}
\]

For a fixed coarse-source fiber, if the exterior discrepancy is \(\Delta_\Pi(r)\) and a response bridge has sensitivity \(L_r\), then

\[
L_r\Delta_\Pi(r)\to0
\]

is sufficient for structural-distortion differences to vanish asymptotically.
Rank reduction alone is insufficient.

### Verdict

- exterior selection / propagation separation: **CONFIRMED**
- rank reduction alone implies erasure: **REJECTED**
- \(c_{\rm info}\) determines decay rate: **REJECTED**
- detail-sector relaxation: **CONDITIONAL**

---

## 2026-09-03 — Experiments 21–22: distance exponent vs source exponent

### Result

Spherical symmetry alone does not imply inverse-square decay.
With an additional shell-wise conserved coarse flux,

\[
4\pi r^2J_q(r)=Q_q
\]

gives

\[
J_q\propto r^{-2}.
\]

For strongly independent sources, if a coarse source is additive and mildly regular,

\[
Q_0(M_1+M_2)=Q_0(M_1)+Q_0(M_2)
\]

implies the conditional theorem candidate

\[
Q_0(M)=\alpha M.
\]

Distance exponent 2 and source exponent 1 are therefore separate questions with separate assumptions.

### Verdict

- conserved 3D spreading \(\Rightarrow r^{-2}\): **CONDITIONAL**
- independent-source additivity \(\Rightarrow M^1\): **CONDITIONAL**
- \(J=-\lambda_X\nabla X\): **UNRESOLVED CONSTITUTIVE BRIDGE**

---

## 2026-09-03 — Experiments 23–26: internal structure as correction sector

### Result

Typed properties, relations, distortion scales, and describability differences are separated from the source-independent far-field normalization.
The current clean schematic form is

\[
a_X(r;S)=\frac{\chi_*}{4\pi}\frac{M_{\rm coarse}}{r^2}[1+\delta F(S,r)],
\]

with the conditional target

\[
\delta F(S,r)\to0.
\]

Using a source's own

\[
L/M
\]

as the universal coupling can cancel the same source mass in the downstream response, so it is not a valid universal far-field normalization candidate.

### Verdict

- internal relation/property/describability as structural-correction input: **CONDITIONAL**
- source-specific \(L/M\) as universal coupling: **REJECTED**
- source-independent \(\chi_*\): **UNRESOLVED**

---

## 2026-09-03 — Experiments 25–26 correction: sector-resolved describability

### Result

Structural-gravity describability is tracked sector by sector:

\[
\mathfrak D_G=(D_B,D_L,D_M,D_X,D_{\nabla X},D_R,D_P,\ldots).
\]

Boundedness, length, mass, distortion, relations, and properties have different data types and roles, so they are not reduced in advance to one scalar \(\Delta_D\).

### Verdict

- one universal scalar describability gap as the default representation: **REJECTED**
- sector-resolved typed describability: **CONFIRMED**

---

## 2026-09-03 — Experiment 27: mass describability as internal partition preservation

### Result

Use two bounded components \(B_1,B_2\) and two density sectors \(H,L\):

\[
\mathbf M=
\begin{pmatrix}
M_{1H}&M_{1L}\\
M_{2H}&M_{2L}
\end{pmatrix}.
\]

The bounded-component marginal

\[
R_B(\mathbf M)=\left(\sum_jM_{1j},\sum_jM_{2j}\right)
\]

and density marginal

\[
R_\rho(\mathbf M)=\left(\sum_iM_{iH},\sum_iM_{iL}\right)
\]

preserve different information.
Even both marginals together may fail to reconstruct the full bounded×density intersection structure.
Hence

\[
\boxed{\text{mass-total preservation}\neq\text{mass-structure preservation}}.
\]

For a mass exterior map

\[
E_M:\mathcal M_{\rm int}\to\mathcal M_{\rm ext}
\]

and distortion exterior map

\[
E_X:\mathcal M_{\rm int}\to\mathcal X_{\rm ext},
\]

distortion is fully determined by the mass descriptor only if

\[
E_X=F\circ E_M.
\]

For linear specializations, the exact factorization criterion is

\[
\boxed{\ker E_M\subseteq\ker E_X}.
\]

### Verdict

- bounded-component mass structure = density mass structure: **REJECTED**
- both marginals = complete internal mass structure: **REJECTED**
- mass describability = distortion describability: **REJECTED**
- kernel-inclusion factorization criterion: **CONFIRMED**

### Next target

Apply the same fiber/kernel sufficiency audit to

\[
E_B,E_L,E_M,E_R,E_P,E_X
\]

to determine which sectors are sufficient upstream descriptors of the structural-distortion response.

---

## 2026-09-03 — Experiment 28: density profile vs cumulative source

### Setup

Hold one spherical bounded source fixed with total mass \(M\), outer radius \(R\), and a core boundary at \(R/2\). Vary only the fraction \(f_c\) of total mass inside the core.
With mean density

\[
\bar\rho=\frac{3M}{4\pi R^3},
\]

the piecewise-uniform control family is

\[
\frac{\rho_f(r)}{\bar\rho}=
\begin{cases}
8f_c,&0\le r\le R/2,\\
\dfrac{8(1-f_c)}7,&R/2<r\le R.
\end{cases}
\]

Three controls were used:

- uniform: \(f_c=1/8\);
- core-heavy: \(f_c=1/2\);
- envelope-heavy: \(f_c=1/20\).

All have identical \(M\) and \(R\).

### Result 1 — local density and enclosed source can have opposite ordering

At \(r=3R/4\), the local-density ordering is

\[
\rho_{\rm envelope}>\rho_{\rm uniform}>\rho_{\rm core},
\]

while the enclosed-mass ordering is

\[
M_{\rm core}(<r)>M_{\rm uniform}(<r)>M_{\rm envelope}(<r).
\]

Numerically,

\[
\rho/\bar\rho=(1.0857,1,0.5714)
\]

for envelope-heavy, uniform, core-heavy respectively, whereas

\[
M(<3R/4)/M=(0.3723,0.4219,0.6696).
\]

Therefore

\[
\boxed{\text{local density}\neq\text{enclosed source}}
\]

is strengthened by an explicit same-\(M\), same-\(R\) rank-inversion witness.

### Result 2 — full radial density and full cumulative mass are equivalent under spherical regularity

For a spherically symmetric regular density,

\[
M(<r)=4\pi\int_0^r\rho(s)s^2\,ds
\]

and, for \(r>0\),

\[
\rho(r)=\frac{1}{4\pi r^2}\frac{dM(<r)}{dr}.
\]

Thus local scalar values \(\rho(r_0)\) and \(M(<r_0)\) are not interchangeable, but the **complete radial profiles** \(\rho(r)\) and \(M(<r)\) contain the same information under the stated spherical/regular assumptions.

### Result 3 — density describability is a hierarchy, not a new independent scalar by default

In 3D the source-description chain can be written schematically as

\[
\rho(\mathbf x)
\xrightarrow{\text{angular coarse map}}
\bar\rho(r)
\leftrightarrow
M(<r)
\longrightarrow
M.
\]

The first arrow can lose angular structure; the middle equivalence holds only in the spherical radial specialization; the final total-mass map loses all zero-total redistribution modes.

### Result 4 — near/far distortion factorization condition

The three profiles are explicit witnesses in the same total-mass fiber:

\[
T[\rho_A]=T[\rho_B]=M.
\]

A near-field distortion map may distinguish them if it depends on local density, enclosed mass, or other retained profile structure.
A mass-only far-field universality requires

\[
\boxed{\ker T\subseteq\ker E_X^{\infty}}.
\]

Thus every zero-total density redistribution must become invisible to the far-field distortion descriptor if total mass alone is to suffice.

### Verdict

- local density = enclosed mass at the same radius: **REJECTED**
- full spherical radial \(\rho(r)\) and full \(M(<r)\) as independent source sectors: **REJECTED; they are mutually reconstructible under regularity**
- general 3D density and radial cumulative mass as equivalent: **REJECTED because angular information may be lost**
- density redistribution can matter near the source while total mass remains fixed: **LOGICALLY CONFIRMED / PHYSICAL BRIDGE UNRESOLVED**
- total mass alone determines far-field distortion: **UNRESOLVED; requires kernel inclusion above**

### Consequence

Do not duplicate density and cumulative mass as independent inputs when the full spherical radial profile is already retained. Keep them separate only at pointwise/reduced-descriptor level, or when non-spherical/partial exterior descriptions lose information.

---

## 2026-09-03 — Experiment 29: density descriptor sufficiency ladder

### Result 1 — analytic rank reversal in the control family

Let \(x=r/R\), and compare each core fraction \(f_c\) with the uniform case \(f_c=1/8\).
For the cumulative mass fraction \(m_f(x)=M_f(<r)/M\),

\[
m_f(x)-x^3=
\begin{cases}
(8f_c-1)x^3,&x\le1/2,\\
\dfrac{(8f_c-1)(1-x^3)}7,&1/2<x<1.
\end{cases}
\]

Hence the sign of the cumulative-mass deviation is fixed throughout the interior.
The core-heavy profile stays above uniform and the envelope-heavy profile stays below uniform for all \(0<r<R\).

By contrast, the local-density deviation is

\[
\frac{\rho_f-\bar\rho}{\bar\rho}=
\begin{cases}
8f_c-1,&r<R/2,\\
-\dfrac{8f_c-1}{7},&r>R/2,
\end{cases}
\]

so its sign reverses across the core boundary.

Therefore a local-density-sensitive response and an enclosed-mass-sensitive response can predict qualitatively different radial ordering even before any standard gravity law is inserted.

### Result 2 — global density-shape descriptor

A normalized second radial mass moment is

\[
\mu_2
=\frac1{MR^2}\int r^2\,dm
=\frac{93-72f_c}{140}.
\]

For the three controls,

\[
\mu_2=(0.6000,\;0.4071,\;0.6386)
\]

for uniform, core-heavy, and envelope-heavy respectively.
Thus same total mass and radius do not determine the radial mass-shape descriptor.

### Result 3 — minimal descriptor ladder

Within the spherical radial specialization, a useful information ladder is

\[
\rho(r)\leftrightarrow M(<r)
\succ (M,I_2)
\succ M,
\]

where

\[
I_2=\int r^2\,dm.
\]

The full radial profile is most informative; a finite moment set is lossy; total mass is the coarsest descriptor.

For a candidate distortion map \(E_X\), test the weakest sufficient source descriptor in order:

1. total mass \(T\): \(\ker T\subseteq\ker E_X\);
2. total + moment \((T,I_2)\): \(\ker(T,I_2)\subseteq\ker E_X\);
3. full cumulative/radial profile \(C\): \(\ker C\subseteq\ker E_X\).

### Verdict

- density and cumulative source are always separate upstream inputs: **REJECTED**
- pointwise/reduced density and cumulative descriptors can disagree qualitatively: **CONFIRMED**
- total mass and radius determine radial density structure: **REJECTED**
- a density-descriptor sufficiency ladder can be audited without inserting Newtonian gravity: **CONFIRMED**

### Consequence

The next structural-gravity step should not ask whether `density matters` in the abstract. It should determine the **minimum exterior density/mass descriptor through which the distortion map factors**: total only, finite radial moments, or full radial profile.
