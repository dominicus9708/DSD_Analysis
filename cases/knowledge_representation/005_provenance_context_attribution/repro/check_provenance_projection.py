from dataclasses import dataclass
from typing import FrozenSet, Tuple

Triple = Tuple[str, str, str]


@dataclass(frozen=True)
class GraphOccurrence:
    graph_name: str
    triples: FrozenSet[Triple]
    attributed_agent: str
    role: str


def main() -> None:
    triple = ("ex:subject", "ex:predicate", "ex:object")

    graph_a = GraphOccurrence(
        graph_name="ex:graphA",
        triples=frozenset({triple}),
        attributed_agent="ex:alice",
        role="ex:publisher",
    )
    graph_b = GraphOccurrence(
        graph_name="ex:graphB",
        triples=frozenset({triple}),
        attributed_agent="ex:bob",
        role="ex:reviewer",
    )

    print("GRAPH CONTENTS EQUAL:", graph_a.triples == graph_b.triples)
    print("GRAPH NAMES EQUAL:", graph_a.graph_name == graph_b.graph_name)
    print("ATTRIBUTED AGENTS EQUAL:", graph_a.attributed_agent == graph_b.attributed_agent)
    print("QUALIFIED ROLES EQUAL:", graph_a.role == graph_b.role)
    print("FULL RECORDS EQUAL:", graph_a == graph_b)

    content_projection = {graph_a.triples, graph_b.triples}
    full_records = {graph_a, graph_b}

    print("CONTENT-ONLY DISTINCT COUNT:", len(content_projection))
    print("FULL PROVENANCE-RECORD DISTINCT COUNT:", len(full_records))
    print(
        "CONTENT PROJECTION LOSES PROVENANCE:",
        len(content_projection) < len(full_records),
    )


if __name__ == "__main__":
    main()
