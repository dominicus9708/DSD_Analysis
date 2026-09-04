# Structural Gravity Audit — Axis Support, Spectral Support, Admissibility Limits, and Stasis

Date: 2026-09-05
Status: DSD Analysis + DSD Audit continuation

## Experiment 469 — `Axis support` splits into local, spectral, and admissibility notions

The old label `axis support` should not be mapped to one primitive scalar without a specialization.
At least three downstream notions must be distinguished:

1. **local constitutive support**: pointwise/local positivity or capacity of restoration/stiffness data;
2. **global spectral support**: positivity of the full linearized coupled operator;
3. **admissibility support/capacity**: remaining inside the declared geometric/constitutive domain.

A useful derived state is therefore not one number but schematically
\[
\mathfrak S_{\rm sup}
=(m_{\rm spec},\,m_{\rm adm},\,\text{local support data},\ldots),
\]
where every margin requires its own declared normalization/metric.

---

## Experiment 470 — Global spectral support

For a self-adjoint variational specialization with full Hessian \(\mathcal H\), define
\[
\boxed{
m_{\rm spec}
=
\inf_{\|v\|=1}\langle v,\mathcal H v\rangle
=
\lambda_{\min}(\mathcal H)
}
\]
when the lowest eigenvalue exists.

Then

- \(m_{\rm spec}>0\): linearly supported/stable;
- \(m_{\rm spec}=0\): marginal spectral support;
- \(m_{\rm spec}<0\): an unstable direction exists.

This is a derived diagnostic, not the old static support property value itself.

---

## Experiment 471 — Positive local sectors do not guarantee global support

For a two-sector Hessian
\[
\mathcal H=
\begin{pmatrix}
k_1&g\\
g&k_2
\end{pmatrix},
\qquad k_1,k_2>0,
\]
full positivity additionally requires
\[
k_1k_2-g^2>0.
\]
Thus each isolated/local sector may be positive while coupling destabilizes the full system.

### Verdict

\[
\boxed{\text{local positive support data}\not\Rightarrow\text{global support}}
\]

---

## Experiment 472 — A locally negative region need not imply global spectral failure

On a one-dimensional bounded interval with Dirichlet boundaries, consider
\[
Q[u]=\int_0^L\left(|u'|^2-\alpha |u|^2\right)dx.
\]
The lowest mode has margin
\[
\boxed{m_{\rm spec}=\frac{\pi^2}{L^2}-\alpha}.
\]
Hence a negative local zero-order term \(-\alpha\) can coexist with positive global support whenever
\[
\alpha<\pi^2/L^2.
\]

### Verdict

Local sign and global spectral support are different questions.

---

## Experiment 473 — Admissibility/capacity failure can occur without a zero mode

Take
\[
E(q;f)=\frac12kq^2-fq,
\qquad |q|\le q_{\max},
\qquad k>0.
\]
The unconstrained equilibrium is
\[
q_*=f/k.
\]
The Hessian is always
\[
E''=k>0,
\]
but the admissible equilibrium ceases to exist when
\[
|f|>kq_{\max}.
\]

Thus support can be lost by reaching a declared domain/capacity boundary while the spectral Hessian remains strictly positive.

### Verdict

\[
\boxed{\text{admissibility support loss}\not\Rightarrow m_{\rm spec}=0}
\]

---

## Experiment 474 — Spectral support can fail without an admissibility boundary

Take
\[
E(q;\lambda)
=\frac12(k-\lambda)q^2+\frac14bq^4,
\qquad b>0,
\qquad q\in\mathbb R.
\]
At the symmetric branch \(q=0\),
\[
E''(0)=k-\lambda.
\]
The spectral margin crosses zero at
\[
\lambda=k
\]
although the admissible state space has no boundary there.

### Verdict

\[
\boxed{m_{\rm spec}=0\not\Rightarrow\text{admissibility/domain transition}}
\]

The two support-loss mechanisms are logically independent.

---

## Experiment 475 — Derived load-support capacity

For a supplied load/control parameter \(\lambda\), define the stable admissible support capacity
\[
\boxed{
\lambda_{\rm sup}
:=
\sup\{\lambda:\exists q_\lambda\in\mathcal A,
\ \nabla E(q_\lambda;\lambda)=0,
\ m_{\rm spec}(q_\lambda;\lambda)>0\}
}
\]
with the exact endpoint convention declared by the specialization.

The endpoint can arise through:

- a spectral zero mode;
- an admissibility/domain boundary;
- a discontinuous constitutive/status transition;
- loss of existence of an equilibrium branch.

Thus `support limit` is naturally a derived branch property, not necessarily one universal primitive force value.

---

## Experiment 476 — The bounded-source self-field threshold is a concrete spectral-support example

The previously derived spherical transformed self-field problem is
\[
-w''=\lambda d(s)w,
\qquad
w(0)=0,
\qquad
w'(1)=0,
\]
with
\[
\lambda=\frac{3\epsilon}{2}.
\]
Let \(\lambda_1[d]\) be the first weighted eigenvalue. Define
\[
\boxed{
m_U(\epsilon)
=\lambda_1[d]-\frac{3\epsilon}{2}.
}
\]
Then
\[
m_U>0
\]
is the subcritical side and
\[
\boxed{m_U=0}
\]
occurs exactly at
\[
\epsilon_c[d]=\frac23\lambda_1[d].
\]

### Verdict

The earlier bounded-source self-field criticality can be reclassified as a **global progression-sector spectral-support boundary** within that conditional self-field branch.

---

## Experiment 477 — Axis coupling and self-field support unify in one block operator

For progression-sector perturbation \(u\) and axis perturbation \(a\), write
\[
\mathcal H_{\rm full}
=
\begin{pmatrix}
L_U&\beta_A C\\
\beta_A C^*&\mathcal H_A
\end{pmatrix}.
\]
The full support margin is
\[
\boxed{m_{\rm full}=\lambda_{\min}(\mathcal H_{\rm full})}.
\]
Even while
\[
m_U>0,
\qquad
m_A>0,
\]
the full margin can reach zero through coupling.
Equivalently, when \(\mathcal H_A>0\),
\[
L_{U,\rm eff}
=L_U-\beta_A^2C\mathcal H_A^{-1}C^*.
\]

### Verdict

The previous `coupled threshold before pure U threshold` result is exactly a full-system support-loss event.

---

## Experiment 478 — Prestress changes support through \(\mathcal H_A\), not by direct synonymy

Using the preceding tension audit,
\[
\mathcal H_A
=
\mathsf R_A
+\mathsf K_A^{\rm material}
+\mathsf K_A^{\rm geo}(\Sigma_0)
+\mathsf C_A.
\]
Prestress can therefore shift the full support margin by hardening or softening the axis block.
No universal sign follows from the word `tension`.

---

## Experiment 479 — Property-level `support` and derived support margin must remain distinct

A typed static record \(z_{\rm sup}\) may enter a constitutive bridge that changes:

- admissible perturbation classes;
- boundary conditions;
- restoration/stiffness/coupling coefficients;
- constitutive domain limits.

But the downstream diagnostic
\[
m_{\rm spec}=\lambda_{\min}(\mathcal H)
\]
is not definitionally equal to \(z_{\rm sup}\).

Otherwise the argument `support property exists -> system is supported -> support is verified` becomes circular.

---

## Experiment 480 — Support status should be multi-axis rather than a single scalar in the general case

Two states can have identical \(m_{\rm spec}\) but different distance to an admissibility boundary, and identical admissibility status but different spectral margins.
Therefore a complete support diagnosis should preserve at least the distinction
\[
\boxed{
\text{spectral margin}
\quad\text{vs}\quad
\text{admissibility/capacity margin}
}
\]
rather than prematurely compress them to one number.

---

## Experiment 481 — A conditional spectral route to `stasis-like` critical slowing

For a soft mode amplitude \(z\) with effective inertia \(\mu_{\rm eff}>0\),
\[
\mu_{\rm eff}\ddot z+m_{\rm spec}z=0.
\]
For \(m_{\rm spec}>0\),
\[
\omega_{\min}^2=\frac{m_{\rm spec}}{\mu_{\rm eff}}.
\]
Hence as
\[
m_{\rm spec}\to0^+,
\]
the period diverges.

In an overdamped specialization
\[
\gamma\dot z+m_{\rm spec}z=0,
\]
the relaxation time is
\[
\boxed{\tau_{\rm relax}=\gamma/m_{\rm spec}\to\infty}.
\]

### Verdict

A system near a support-zero mode can appear increasingly slow under suitable dynamics. This supplies a precise **conditional critical-slowing interpretation** for one form of the earlier `stasis` intuition.

---

## Experiment 482 — Marginal support is not itself stasis

At exactly
\[
m_{\rm spec}=0,
\]
the conservative soft-mode equation becomes
\[
\mu_{\rm eff}\ddot z=0,
\]
with generic solution
\[
z(t)=z_0+v_0t.
\]
Thus a marginal mode may drift rather than remain static.

### Verdict

\[
\boxed{m_{\rm spec}=0\not\Rightarrow\dot z=0}
\]

Marginality and stasis must remain separate concepts.

---

## Experiment 483 — Stasis can occur far from support loss

A model may have positive support margin but very small mobility, very large inertia, pinning, or an externally constrained evolution law. Then rates can be small while
\[
m_{\rm spec}>0.
\]

### Verdict

\[
\boxed{\text{kinetic arrest/stasis}\not\Rightarrow\text{marginal support}}
\]

---

## Experiment 484 — Refined stasis taxonomy

Retain the earlier distinctions:

- **kinematic stasis**: small observed rate;
- **dynamic equilibrium**: net drive vanishes;
- **kinetic arrest**: drive exists but mobility/evolution is suppressed;
- **critical slowing**: a support eigenvalue approaches zero and the response time diverges under a chosen dynamic law;
- **marginal support**: \(m_{\rm spec}=0\).

These may overlap but are not synonymous.

---

## Experiment 485 — Refined axis-support taxonomy

The migrated `axis support` vocabulary is best split as follows:

1. **support-like typed property** — predecessor static input candidate;
2. **local constitutive support** — positivity/capacity of selected local operators;
3. **global spectral support** — \(m_{\rm spec}>0\);
4. **admissibility support** — state remains in the declared domain;
5. **support capacity** — supremal external/control load admitting a stable admissible branch;
6. **support-loss event** — spectral, admissibility, or hybrid transition identified by the changed data.

---

## Experiment 486 — Consolidated chain

The strongest surviving chain is
\[
\boxed{
\text{typed support candidate}
\to
\text{constitutive/domain bridge}
\to
\mathcal H_{\rm full},\mathcal A_{\rm adm}
\to
(m_{\rm spec},m_{\rm adm})
\to
\text{support capacity/loss classification}
}
\]

The earlier bounded-source self-field threshold is one concrete spectral-support instance; axis coupling and prestress can move the full-system threshold; admissibility failure can occur independently; and `stasis` is at most a derived dynamical regime, not a primitive synonym for support.

## Final verdict

`Axis support` should be migrated, but as a **family of support diagnostics/constraints** rather than one primitive mechanical coefficient.

The most useful current structural-gravity quantity is the full spectral support margin
\[
m_{\rm full}=\lambda_{\min}(\mathcal H_{\rm full}),
\]
augmented separately by an admissibility/capacity margin when the model has hard geometric or constitutive boundaries.

## Next audit target

Audit the remaining `axis inertia` more deeply against:

1. kinetic metric versus physical mass;
2. spatially distributed inertia and characteristic speed \(c_A^2\sim K_A/M_A\);
3. whether axis inertia can alter the propagation cone without altering the static support threshold;
4. how inertia interacts with critical slowing, overshoot, and finite-time support crossing.
