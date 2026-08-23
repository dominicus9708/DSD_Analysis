# LAW-008 Reproducibility

## Required source set

Primary/official sources used in the first pass:

1. Vienna Convention on the Law of Treaties (1969), Articles 30, 31, 53.
   - https://legal.un.org/ilc/texts/instruments/english/conventions/1_1_1969.pdf
2. Charter of the United Nations, Article 103.
   - https://www.un.org/en/about-us/un-charter/full-text
3. International Law Commission, Conclusions of the Study Group on Fragmentation of International Law (2006).
   - https://legal.un.org/ilc/texts/instruments/english/draft_articles/1_9_2006.pdf
4. Project DSD Formation source:
   - `DSD_Formation_Axiom_System_EN.pdf`

## Reproduction protocol

### Step 1 — Source-side relation inventory

For each witness, record:

- the two or more rules/norms/instruments;
- subject matter;
- parties or legal subject;
- time;
- validity/in-force status;
- applicability;
- source-supplied relation rule;
- source-supplied consequence.

### Step 2 — Attempt universal compression

Try to encode each witness using only:

`CONFLICT={YES,NO}`

or a slightly richer context-free enum:

`{NO_CONFLICT,R1_WINS,R2_WINS,BOTH_INVALID}`.

Record which distinctions are lost.

Expected failures:

- harmonized co-application;
- special rule without general-rule extinction;
- Article 103 priority without automatic global invalidity;
- Article 53 invalidity;
- VCLT Article 30 party-sensitive relations.

### Step 3 — Typed reconstruction

Use:

`tau=(subject,actor,act_or_issue,role,context,time,parties,jurisdiction,regime)`

and retain separate rule identities `r1`, `r2`.

Record:

`Valid(r,t)`;
`Applies(r,tau)`;
`Out(r,tau)`;
`Rel(r1,r2,tau)`.

### Step 4 — DSD audit

Verify that the DSD mapping does not identify:

- priority loss with channel absence;
- exception with zero;
- invalidity with undefined assignment;
- unresolved source conflict with missing DSD data.

### Step 5 — Generalization judgment

A successful first-pass reproduction should reach:

- no single context-free conflict consequence preserves all witnesses;
- no direct contradiction with Formation after explicit typing;
- no claim that DSD supplies the legal conflict resolver.

## No Python requirement

This case is symbolic/source-structural. No numerical simulation is required for the first-pass result.
