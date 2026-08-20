# Finite Witness — Institutional Language and Authority

## Objects
Let two institutional actors have the same role label `manager`:

- `m1`: manager with an active delegated approval authority for purchase class A;
- `m2`: manager whose delegation for class A has expired.

Let both utter the same meaningful institutional sentence:

`u = "Approved."`

Let the target request `r` belong to class A.

## External institutional data
Define:

- `Role(mi)=manager` for both actors;
- `Delegated(m1,A,C)=1`;
- `Delegated(m2,A,C)=0`;
- `Jurisdiction(mi,r,C)=1` for both;
- `Procedure(u,r,C)=1` for both.

Define institutional effectiveness only as an application-level witness:

`Eff(mi,u,r,C) := Loc(mi,u,C) AND Delegated(mi,A,C) AND Jurisdiction(mi,r,C) AND Procedure(u,r,C)`.

Then:

- `Loc(m1,u,C)=Loc(m2,u,C)=1`;
- `Role(m1)=Role(m2)=manager`;
- `Eff(m1,u,r,C)=1`;
- `Eff(m2,u,r,C)=0`.

Therefore:

`same role + same utterance + same target` does not imply `same institutional effect`.

## Context witness
If the same utterance is made by `m1` about request `rB` outside the delegated class A, then:

`Delegated(m1,A,C)=1` but `Jurisdiction(m1,rB,C)=0`,

so institutional effect still fails.

Thus authority is not a scalar attached once and for all to a person or role; its applicability may be relation-, target-, context-, and procedure-sensitive.

## DSD lesson
Formation can preserve the role-tagged event/channel. Axis-Property can optionally encode relations such as delegated-authority or jurisdiction on typed profiles. The final `Eff` rule remains an external institutional bridge.
