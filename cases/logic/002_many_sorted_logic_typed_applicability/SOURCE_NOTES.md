# Case 002 — Source Notes

## External source discipline first

### 1. Many-sorted typing
In ordinary many-sorted first-order practice, variables and constants carry sorts/types and a function application is well typed only when each argument has the sort required by the function symbol's declared type.

For a function symbol

`f : (S1, ..., Sn) -> T`,

an application `f(t1,...,tn)` is a term of sort `T` only when each `ti` has sort `Si`.

The CVC3 manual states this explicitly as the usual rule of first-order many-sorted logic and rejects ill-typed terms rather than assigning them a Boolean value.

The SMT-LIB language likewise works with declared sort and function symbols and speaks of semantics for well-sorted terms.

### 2. Consequence for wrong-sort applications
Suppose a predicate/property expects an input of sort `A` and returns Boolean values. If `a:A`, evaluating `P(a)` may yield false. If `b:B` with `B != A`, then `P(b)` is not another false case merely because `false` is available in the codomain. It fails the typing condition before ordinary truth-value evaluation.

This is the external structure Case 002 uses.

### 3. What this source does not supply
Ordinary many-sorted logic by itself does not automatically provide all of the DSD status layers.

In particular, this case does not infer from many-sorted logic that:

- a required sort-carrier may be configuration-relative and unavailable;
- a well-typed property application may be partial and undefined on some otherwise admissible input;
- a property kind may exist in a candidate universe but remain undeclared in one extension.

Those are additional DSD distinctions and need their own mathematical justification or comparison nodes.

### 4. Correction to the earlier lightweight roadmap mapping
The earlier roadmap loosely compared a wrong-sort expression with DSD `unavailable input`. This is not precise.

The corrected correspondence is:

- many-sorted wrong-sort input -> outside the DSD typed input product for that property profile;
- DSD `unavailable input` -> at least one required profile carrier is not available at the configuration;
- DSD `undefined application` -> full typed input carrier exists, but the chosen typed input lies outside the partial assignment domain;
- DSD `defined zero` -> typed input lies in the assignment domain and receives the designated zero.

Therefore Case 002 must not claim direct correspondence between ordinary many-sorted ill-typing and DSD carrier unavailability.

## DSD source structure
The current Axis-Property paper defines a shared signature with sort universe

`S_L = {tag, line, sub, normal}`

and a finite typed profile map

`sigma_L(varpi) = (s1,...,sm)`.

At an axis-applicable configuration `p`, each sort label is interpreted by a carrier. The full input carrier for a property kind is the corresponding product of those carriers and is available only when every required factor carrier is available.

A declared property kind with available full input carrier receives a partial assignment

`Xi_{A,p,varpi} : X_{A,p,varpi} ⇀ Z_{L,varpi}`.

Definition 3.10 then separates unavailable input, undefined application, defined zero, defined nonzero, and defined value. Closure Clause 4.2 requires property assignments to remain typed and states that no input outside the partial assignment domain is silently assigned zero.

## References
- Kwon Dominicus, *Axioms for the Property Structure of Realized Axes in Dimensional-Structural Describability*, 2026, Definitions 2.1, 3.2, 3.3, 3.10 and Closure Clause 4.2.
- Clark Barrett, Pascal Fontaine, Cesare Tinelli, *The SMT-LIB Standard: Version 2.7*.
- CVC3 User Manual, section on Type Checking.
