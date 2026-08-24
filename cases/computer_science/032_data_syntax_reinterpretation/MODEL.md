# CS-004 / Global Case 032 — Model and Finite Witnesses

Status: first-pass model complete.

## Source-native state model

For an external value `v`, distinguish:

- `I(v)`: upstream input/value admissibility;
- `C`: downstream parser or sink context;
- `Bind(C,v)`: the mechanism by which `v` is inserted/bound into `C`;
- `Role(C,Bind,v)`: the syntactic/semantic role actually assigned by the downstream interpreter;
- `Eff(C,Bind,v)`: downstream operation/effect.

The rejected shortcut is:

`I(v) => Role(C,Bind,v) = data` for arbitrary `C` and `Bind`.

The source systems instead require context-sensitive binding/encoding or structured APIs.

## Finite witness A — SQL value binding

Let the benign string be:

`v = "O'Reilly"`.

Two pipelines use the same host-language string:

1. parameterized query: SQL syntax is fixed, `v` is supplied through a parameter slot;
2. string-built query: `v` is inserted into SQL source text and the quote character participates in SQL parsing unless handled correctly.

The point is not an attack payload. It is that the same valid application string has different parser status depending on the binding mechanism.

Therefore:

`same host value != same SQL syntactic role`.

## Finite witness B — browser text versus markup

Let:

`v = "<b>A</b>"`.

Two sinks receive the same JavaScript string:

1. `textContent`: the value is inserted as text;
2. `innerHTML`: the value is parsed as HTML markup.

The visible text may contain the same letter `A`, but the DOM structure and parser role differ.

Therefore:

`same string != same browser structural interpretation`.

## Finite witness C — process argument versus shell language

Let a filename contain ordinary shell-significant formatting such as whitespace:

`v = "report 2026.txt"`.

Two interfaces differ:

1. an argument-vector API keeps `v` as one process argument;
2. a shell command string requires shell quoting so the shell parser preserves that one-argument role.

Therefore:

`same string != same tokenization/command-language role`.

## Cross-witness invariant

The common failure is not that `v` is intrinsically undefined, malformed, or malicious.

The relevant structure is:

`value -> interpretation context -> binding/encoding relation -> parsed role -> effect`.

A context can preserve the upstream data role, transform it into another typed representation, or allow it to participate in syntax. That distinction is supplied by the external interpreter/API.