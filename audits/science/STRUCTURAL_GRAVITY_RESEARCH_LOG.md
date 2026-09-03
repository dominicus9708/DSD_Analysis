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
