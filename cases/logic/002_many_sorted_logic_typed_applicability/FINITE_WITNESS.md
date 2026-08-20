# Case 002 — Finite Witness

## 1. External many-sorted witness
Let the sort set contain two distinct sorts

`S = {A, B}`

with nonempty carriers

`M_A = {a0}`,
`M_B = {b0}`.

Let the Boolean/value carrier be

`Bool = {0,1}`

with `0` interpreted as false.

Declare one unary predicate/property symbol

`P : A -> Bool`

and define

`P(a0) = 0`.

Then:

- `P(a0)` is a well-sorted application with a defined false/zero result;
- `P(b0)` is not a well-sorted application because `b0` has sort `B`, not sort `A`.

The second case is not another occurrence of the value `0` in the typed system.

## 2. Default-value type erasure
Define an application-state set

`R = {Defined(v) : v in Bool} union {IllTyped}`.

For a fallback value `d in Bool`, define the raw-value encoding

`E_d(Defined(v)) = v`,
`E_d(IllTyped) = d`.

### Theorem 2.1 — Ordinary fallback collapse
For every fallback value `d` that is itself an ordinary member of the value carrier, `E_d` is not injective.

### Proof
Both `Defined(d)` and `IllTyped` are distinct application states, while

`E_d(Defined(d)) = d = E_d(IllTyped)`.

Therefore the raw output value alone cannot reconstruct whether the original state was a valid application with value `d` or an ill-typed attempted application. QED.

The witness above is the special case `d=0`.

## 3. Faithful alternatives
Two simple encodings preserve the distinction.

### 3.1 Status mask
Encode

`Defined(v) -> (v, 1)`,
`IllTyped -> (0, 0)`.

The second coordinate reconstructs application status.

### 3.2 Disjoint error/status symbol
Extend the codomain to

`Bool disjoint_union {ILL}`

and encode

`Defined(v) -> v`,
`IllTyped -> ILL`.

Because `ILL` is not an ordinary Boolean value, no defined Boolean result collides with ill-typedness.

Therefore the mathematical claim is not that a typed structure cannot be flattened. It can be flattened if the type/status information is explicitly preserved. What fails is **type erasure followed by replacement with an ordinary legitimate value without status metadata**.

## 4. DSD instantiation
Fix one axis-applicable DSD configuration `p` and a declared zero-bearing property kind `varpi` with profile

`sigma_L(varpi) = (tag)`

and value carrier

`Z_{L,varpi} = {0,1}`.

Let the tag carrier contain a tagged axis `t0`, and let the line carrier contain a realized line `ell0`.

Supply a partial property assignment with

`t0 in D_{A,p,varpi}`

and

`Xi_{A,p,varpi}(t0) = 0`.

The two situations are now:

1. `t0` — correct sort, inside the application domain, defined zero;
2. `ell0` considered as a line-sort input — wrong sort for the profile `(tag)`.

By Definition 3.3, the property assignment has typed source `X_{A,p,varpi}=X_{A,p}(tag)`. Therefore the line-sort object is outside the typed source. It is not assigned the value zero by the DSD map.

By Definition 3.10, `undefined application` is evaluated only for `x` inside the available typed product but outside the partial assignment domain. Hence the wrong-sort line is not an `undefined application` either.

It is also not `unavailable input`: the required tag carrier is available in this witness. The attempted line input simply does not match the declared profile.

## 5. Correct status partition for this case
The DSD status boundary relevant to Case 002 is therefore:

- **ill-typed / outside profile product**: no property application status is evaluated;
- **carrier unavailable**: the property kind is declared, but at least one carrier required by the profile is unavailable at `p`;
- **undefined application**: full typed product is available, input is well typed, but input is outside the partial assignment domain;
- **defined zero**: well-typed input lies in the domain and receives zero;
- **defined nonzero/value**: well-typed input lies in the domain and receives another defined value.

This is a strictly finer analysis than the original roadmap shorthand.

## 6. Boundary test: many-sorted logic does not establish every DSD layer
Case 002 independently supports the first boundary: sort/type correctness must be established before ordinary value evaluation.

It does not independently establish:

- configuration-relative carrier unavailability;
- partial undefinedness on well-typed inputs;
- candidate-versus-declared property kinds.

Partial undefinedness was tested separately in Case 001. Carrier availability and declaration status remain future analysis targets.

## 7. Falsification attempt
A contradiction would arise if the Axis-Property definitions forced an out-of-profile object such as `ell0` to receive an ordinary value of `Z_{L,varpi}`, or classified it as a defined-zero application merely because a fallback representation uses zero.

They do not. The source of `Xi_{A,p,varpi}` is the typed profile product itself, and Closure Clause 4.2 preserves that typing.

Therefore this finite witness produces no counterexample to the tested DSD typing structure.
