# Comparison Model

## Layer A — variable component decomposition on fixed support

Fix a finite support `F` and, for each `c in F`, a subspace `U_c <= W_L`.

Define

`Sigma_F : product_{c in F} U_c -> W_L`,

`Sigma_F((u_c)) = sum_{c in F} u_c`.

The component decomposition is unique on the full product exactly when `Sigma_F` is injective, equivalently when the sum of the `U_c` is internal direct.

This is a standard sufficient/necessary characterization **for the chosen product of subspaces**. DSD does not supply the `U_c`; introducing them is an additional application structure.

## Layer B — fixed term values, variable selected support

Fix a finite candidate channel family `C_0 subset C_L` and the already supplied terms `T_L(c)`.

Define

`Phi_T : P(C_0) -> W_L`,

`Phi_T(F)=sum_{c in F} T_L(c)`.

Support recovery from the Stage-VII aggregate is possible exactly when `Phi_T` is injective.

Equivalently, there is no nonzero channel-indexed coefficient family

`epsilon_c in {-1,0,1}`

with

`sum_{c in C_0} epsilon_c T_L(c)=0`.

If the term map is injective, this is exactly dissociativity of the term image.

## Layer C — support-tagged varying records

For analytic records `(F,(y_c)_{c in F})`, aggregate values alone cannot in general distinguish

- `c notin F`, from
- `c in F` with `y_c=0`.

Thus even a numerically unique coordinate decomposition does not automatically reconstruct DSD support unless support is retained or a separate presence/nonzero rule is imposed.
