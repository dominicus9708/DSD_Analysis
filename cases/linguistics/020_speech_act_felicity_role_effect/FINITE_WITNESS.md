# LING-007 / Global Case 020 — Finite Witness

## Witness A — same locution, different institutional felicity

Fix one meeting context `C` and one surface utterance token type

`u = "I declare the meeting open."`

Let the speakers be

- `s_chair`: authorized chair for this meeting;
- `s_guest`: visitor with no declaration authority.

Let

- `Loc(s,u,C)` mean the meaningful locution is successfully produced;
- `Role(s)` record the institutionally relevant role;
- `Auth(s,DECL_OPEN,C)` be an **external application-supplied** authority relation;
- `Proc(u,C)` mean the accepted declaration procedure is correctly applicable;
- `IllocOpen(s,u,C)` mean the intended illocutionary declaration succeeds.

Set

`Loc(s_chair,u,C) = true`

`Loc(s_guest,u,C) = true`

`Role(s_chair) = chair`

`Role(s_guest) = guest`

`Auth(s_chair,DECL_OPEN,C) = true`

`Auth(s_guest,DECL_OPEN,C) = false`

`Proc(u,C) = true`

and define, only for this witness,

`IllocOpen(s,u,C) := Loc(s,u,C) and Auth(s,DECL_OPEN,C) and Proc(u,C)`.

Then

`IllocOpen(s_chair,u,C) = true`

but

`IllocOpen(s_guest,u,C) = false`.

Therefore

`same surface words + same locution != same successful illocution`.

The guest case is a model of an attempted institutional declaration that misfires because a felicity prerequisite is absent. The utterance exists and is meaningful; the intended institutional speech act does not thereby succeed.

## Witness B — illocutionary success versus downstream perlocutionary effect

Let `React(audience)` be a contingent audience reaction, for example immediate applause or compliance with a subsequent request.

Take the authorized chair case above and set

`IllocOpen(s_chair,u,C) = true`

while

`React(audience) = false`.

This is structurally coherent because perlocutionary consequences are not identical to the illocutionary act itself.

Hence

`successful illocution != guaranteed downstream reaction`.

A DSD application must not encode absence of a desired audience response as retroactive nonexistence of the successful declaration unless the external institution explicitly defines such a dependency.

## Witness C — misfire versus abuse

Let `p = "I promise to repay you tomorrow."`

Take a speaker who successfully performs the promise under the relevant conventional/communicative conditions but privately intends not to repay.

Record

`PromiseAct = formed`

`Sincerity = false`.

In Austin's classification this can be an **abuse** rather than a **misfire**: the promise act is performed, but a felicity condition concerning sincerity is violated.

Therefore

`act absent / failed to form != act formed but defective`.

This mirrors a status-preservation requirement but is not identified with any one Formation status without an explicit bridge.

## DSD encoding boundary

### Formation-only encoding
Formation can preserve a role coordinate in channel identity:

`c = (p,a,lambda,v,rho)`.

A formation application can therefore distinguish a chair-tagged utterance channel from a guest-tagged utterance channel.

But no Formation theorem gives

`rho = chair -> Auth(s,DECL_OPEN,C)`.

That implication is external institutional data.

### Optional Axis-Property encoding
If an application wants a typed authority network after selecting the relevant formation channels into an axis-property extension, it may declare an authority-like tag-sensitive property/relation, for example a profile over tagged inputs.

However:
- the property kind must be explicitly declared;
- its input profile must be specified;
- a value carrier must be supplied;
- the application domain and values must be assigned;
- the interpretation `authority` remains external.

Thus Axis-Property is **available but not mandatory** for the finite witness.

## Structural conclusions from the witness

1. `utterance exists` does not entail `intended institutional act succeeds`.
2. `role label exists` does not entail `authority relation holds`.
3. `successful illocution` does not entail `desired perlocutionary effect`.
4. `misfire` is not the same status as `abuse`.
5. equal surface language does not determine equal speech-act structure.