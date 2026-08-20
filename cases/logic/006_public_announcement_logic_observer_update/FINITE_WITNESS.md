# Case 006 — Finite witnesses

## Witness A — truth without knowledge, then public announcement

Take one agent `i` and a two-world epistemic model

- `W = {w0,w1}`;
- actual world `w0`;
- `R_i = W x W`;
- atomic proposition `s` is true only at `w0`.

Then at the actual world,

`M,w0 |= s`

but

`M,w0 !|= K_i s`,

because `w1` is accessible and `s` is false there.

After the truthful public announcement of `s`, restrict the model to the `s`-worlds. The updated model has

- `W'={w0}`;
- `R'_i={(w0,w0)}`;
- the valuation at `w0` unchanged.

Hence

`M|s,w0 |= K_i s`.

The factual truth of `s` at the actual world was already present before the announcement; what changed was the epistemic alternative structure.

## Witness B — external metatheoretic knowledge does not force DSD describability

Take a finite DSD formation core with one material item `a`, one expression `h`, and one candidate configuration `p`.

Set

- `mat_L(h)=act_L(p)={a}`;
- matching anchors;
- `Admexpr_L(h)=true`;
- `Res_L(h,h)=true`;
- `Realize_L(h,p)=true`;
- all three configuration admission/coherence predicates at `p` true;
- but `Desexpr_L(h)=false`.

Primitive Axioms I–III are satisfied: Axiom I permits admitted but non-describable expressions, Axiom II gives the sound identity restriction, and Axiom III gives sound realization.

However the Clause-IV witness formula fails because its `Desexpr_L(h)` conjunct is false. Therefore

`Psi_L(p)=false`

and

`Descfg_L(p)=false`.

An external analyst can know every set, relation, and truth assignment used to construct this finite model, yet that metatheoretic knowledge is not a formal premise that can override Clause IV.

Thus

`external truth/knowledge of the model != DSD configuration describability`.

## Witness C — same underlying structure, different regime-level describability input

Construct a second regime `L+` over the same fixed base and same material/configuration data as Witness B, but change the expression-status data so that

- `Desexpr_{L+}(h)=true`,
- all other witness conditions remain true.

Then

`Psi_{L+}(p)=true`

and

`Descfg_{L+}(p)=true`.

This is a valid paired-regime contrast, but it is not yet a Public Announcement update theorem. The Formation core does not define an agent accessibility relation or an announcement operator that derives `L+` from `L`.

Therefore an epistemic reading requires an additional bridge specifying how information states alter regime primitives.

## Witness D — naive PAL-style deletion is not automatically a DSD submodel operation

Start with a DSD formation model containing a describable configuration `p` whose only Clause-IV witness uses an expression `h`.

Now form an induced subset that retains `p` but removes `h` from the expression carrier.

In the restricted structure, the old witness no longer exists, so `Psi(p)` can change from true to false. Therefore the induced subset is not automatically a formation submodel.

This mirrors the paper's Remark 6.9.

Hence a PAL operation of "remove incompatible alternatives" cannot simply be identified with arbitrary deletion of DSD candidate records. A DSD update layer would need explicit witness-closure rules, or would need to permit a declared formation-level transition.
