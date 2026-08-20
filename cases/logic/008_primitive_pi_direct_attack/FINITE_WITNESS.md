# Case 008 — Finite Witnesses

## Witness A — Nontrivial PI realization always exists after a nonempty selection

Fix any valid Stage-VI formation record and one describable configuration `p` with any selected inherited-channel set

`S := C^ax_A,p ⊆ C_L(p)`.

No finiteness assumption on `S` is needed for this elementary existence argument.

Choose the one-dimensional ambient carrier

`E^amb_A,p := F`.

As a vector space over itself, `F` has exactly one one-dimensional subspace, namely `F` itself. Hence

`Gr_1(F) = {F}`.

Define

`AxLine_A,p(c) := F`

for every `c ∈ S`.

Then

`Dom(AxLine_A,p)=S=C^ax_A,p`,

so PI holds.

### Consequence

Neither the number of selected channels nor finite dimensionality causes an obstruction, because PI does not require injectivity. Arbitrarily many selected channels may realize the same line.

## Witness B — Zero-dimensional ambient carrier obstruction

Let

`C^ax_A,p = {c}`

for one selected inherited channel, but choose

`E^amb_A,p = {0}`.

Then

`Gr_1(E^amb_A,p)=∅`.

No total map exists from the nonempty set `{c}` to the empty codomain. Therefore PI cannot hold.

Thus every full axis-property model satisfies the derived implication

`C^ax_A,p != ∅  =>  dim(E^amb_A,p) >= 1`.

This is not a contradiction. It is an admissibility consequence of PI. A layered primitive presentation may choose the zero-dimensional carrier and then simply fail PI.

## Witness C — Branching/multiline realization excluded before PI

Fix one selected channel

`C^ax_A,p={c}`

and choose

`E^amb_A,p=F^2`.

Let

`ell_x = span{(1,0)}`,
`ell_y = span{(0,1)}`,

with `ell_x != ell_y`.

Consider the candidate branching realization

`R(c)={ell_x,ell_y}`.

Nothing in the inherited Stage-VI formation record forbids this external relation because Stage VI contains no axis-line coordinate.

However it cannot be represented by the present core type

`AxLine_A,p : C^ax_A,p ⇀ Gr_1(E^amb_A,p)`

because a function may assign at most one output to `c`.

Therefore the branching candidate is not a countermodel to PI inside the current language. It is excluded earlier by Definition 2.7.

### Exact logical diagnosis

The statement

`each selected channel has at most one realized line`

comes from the **function type**.

The statement

`each selected channel has at least one realized line`

comes from **PI totality**.

Together they yield exactly one line per selected channel.

## Witness D — Eligibility is not established by PI

Take two inherited admitted channels `c1,c2 ∈ C_L(p)` with otherwise arbitrary formation coordinates.

The extension may choose

`C^ax_A,p={c1}`

or

`C^ax_A,p={c2}`

or both or neither, provided the remaining extension data are supplied coherently.

PI only requires total `AxLine` data for whichever channels were selected. It does not derive the selection from quantity-kind, role, value, or formation trace.

Hence

`admitted channel -> axis channel`

is not a theorem of PI or of the Formation system.
