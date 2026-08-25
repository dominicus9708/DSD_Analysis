from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass(frozen=True)
class CandidateState:
    name: str
    substrate: str
    mechanism: str
    observed: Tuple[int, ...]
    trust_status: str
    trust_value: Optional[int]


OBSERVATION = (1, 1, 1, 0, 1)

CANDIDATES = (
    CandidateState(
        "H_trust",
        "human",
        "trust-attitude",
        OBSERVATION,
        "defined",
        1,
    ),
    CandidateState(
        "H_strategic",
        "human",
        "sanction-avoidance",
        OBSERVATION,
        "defined",
        0,
    ),
    CandidateState(
        "A_policy",
        "AI",
        "fixed-cooperative-policy",
        OBSERVATION,
        "undefined",
        None,
    ),
    CandidateState(
        "A_internal_var",
        "AI",
        "learned-trust-like-variable",
        OBSERVATION,
        "defined",
        1,
    ),
)


def observation_class(observed: Tuple[int, ...]):
    return tuple(c for c in CANDIDATES if c.observed == observed)


def main() -> None:
    eq = observation_class(OBSERVATION)
    records = {(c.trust_status, c.trust_value) for c in eq}
    substrates = {c.substrate for c in eq}
    mechanisms = {c.mechanism for c in eq}

    print("HUMAN/AI TRUST ATTRIBUTION WITNESS")
    print("observation:", OBSERVATION)
    print("candidates:", [c.name for c in eq])
    print("substrates:", sorted(substrates))
    print("mechanisms:", sorted(mechanisms))
    print("trust_records:", sorted(records, key=str))
    print("observation_identifies_unique_mechanism:", len(mechanisms) == 1)
    print("observation_identifies_unique_trust_record:", len(records) == 1)

    assert len(eq) == 4
    assert len(mechanisms) > 1
    assert ("defined", 1) in records
    assert ("defined", 0) in records
    assert ("undefined", None) in records
    assert len(records) > 1

    print("witness_passed: True")


if __name__ == "__main__":
    main()
