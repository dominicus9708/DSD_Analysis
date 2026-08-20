# Case 010 — Adversarial Integrated Witness

This witness is intentionally constructed to make the combined system look as fragile as possible while remaining inside the declared signatures and typing rules.

## 1. Formation Stage-VI base

Use one describable configuration `p`, one material item `a`, one quantity kind `lambda`, and one defined zero assignment

`q_L,lambda(a)=0`.

Take two distinct roles

`rho1 != rho2`

and declare both role relations at `(p,a,lambda)`.

Stage VI therefore contains two distinct admitted operational channels

`c1=(p,a,lambda,0,rho1)`,

`c2=(p,a,lambda,0,rho2)`.

They agree in configuration, material item, quantity kind, and value, but remain distinct because the role coordinate differs.

For a full Formation completion one may take the zero vector space as the Stage-VII term space and assign both component terms the zero vector. Nothing in the Axis-Property construction below depends on that Stage-VII choice.

## 2. P1 — collapse two distinct tags onto one realized line

Let

`K_ax_A={p}`,

`C_ax_A,p={c1,c2}`,

`E_amb_A,p=R^2`.

Set

`ell=span(e1)`

and define

`AxLine_A,p(c1)=ell`,

`AxLine_A,p(c2)=ell`.

PI holds because `AxLine` is total on the selected set.

The P4 completion therefore contains two distinct tagged-axis records

`t1=(c1,ell)`,

`t2=(c2,ell)`,

but only one distinct realized line, so the realized-axis rank is 1 rather than 2.

This directly stresses the distinction between operational tag multiplicity and realized-line rank.

## 3. P2–P6 — tag-sensitive and bilinear-dependent properties coexist

Declare two property kinds in the shared candidate signature:

- `alpha`: unary profile `(tag)`, value carrier `{0,1}`, not bilinear-dependent;
- `beta`: binary profile `(tag,tag)`, value carrier `{0,1}`, declared bilinear-dependent.

Let

`Pi_A={alpha,beta}`,

`Pi_bil_A={beta}`.

### P3 bilinear data

Put

`K_bil_A={p}`

and use the degenerate zero symmetric bilinear form

`b_p(x,y)=0`

for every `x,y in R^2`.

### P5 property assignments

Supply

`Xi_alpha(t1)=0`,

`Xi_alpha(t2)=1`.

The two tagged inputs lie in one line-projection fiber but receive different values. Therefore `alpha` is tag-sensitive rather than line-invariant, and P6 does not generate a line-factor map for it.

Also supply one defined bilinear-dependent binary application, for example

`Xi_beta(t1,t2)=1`.

Because the profile is available, the local domain is nonempty, and `p in K_bil_A`, the first PII trigger is satisfied.

Nothing in PII requires the arbitrary Boolean value of `beta` to be computed from the zero form; that would require an additional application-level compatibility law.

## 4. P7–P8 — deliberately failed formal closure

Activate formal closure:

`ClDecl_A(p)=1`,

`FormalBilDep_A(p)=1`.

Let the obligation carrier be

`O_A,p={tau}`.

Choose the requirement generator so that for the actual tagged-axis/property-record families it returns

`Req_A,p={tau}`.

Supply a witness carrier `Y_A,p={y}` but leave the primitive witness map undefined at `tau`.

Then the derived formal closure status is

`ClStat_A(p)=failed`.

PII still holds because the active formal closure is declared bilinear-dependent and `p in K_bil_A` with a supplied symmetric bilinear form.

The failed closure status is therefore a recorded derived result, not a failure of full-model completion.

## 5. P7–P8 — deliberately failed nondegeneracy

Activate the subspace declaration

`SubDecl_A(p)=1`

and choose the axis-generated subspace

`S=ell`.

Because the supplied bilinear form is identically zero,

`Rad_A,p(S)=S != {0}`.

Hence the derived nondegeneracy coordinate is

`NonDeg_A,p=failed`.

Again this does not violate PI or PII and is not excluded by the definition of full axis-property model.

Set the triadic and optional representation declarations inactive to avoid adding irrelevant coordinates.

## 6. Resulting completed descriptor

The same completed model simultaneously contains:

- two distinct inherited operational tags;
- one realized line and realized-axis rank 1;
- a defined-zero property value on one tag;
- a different nonzero value on the other tag despite the same line;
- a bilinear-dependent defined property application;
- a degenerate zero symmetric bilinear form;
- `ClStat=failed`;
- `NonDeg=failed`;
- a complete P8 descriptor.

No coordinate forces a contradiction with another.

## 7. What this witness establishes

This witness does **not** prove the entire combined theory consistent.

It does show that several intuitively dangerous combinations are jointly admissible under the published definitions:

`distinct tags + same line + tag-sensitive values + degenerate bilinear data + failed closure + failed nondegeneracy`.

The completion machinery records these distinctions rather than silently upgrading them into success conditions.

## 8. Stage-VII variation test

Keep the entire Formation Stage-VI record above fixed and vary only post-Stage-VI Formation data such as the component-term map or finite composite operator.

Under the Stage-VI factorization proposition, the Axis-Property primitive presentation and its explicit completion remain unchanged.

Therefore no integrated contradiction can be produced solely by changing Formation Stage VII while the Stage-VI interface is held fixed.

This is also a scope boundary: if a future axis property is intended to depend on Formation component terms or composite-description values, that dependence requires an explicit additional bridge because the present Axis-Property core intentionally does not read those coordinates.
