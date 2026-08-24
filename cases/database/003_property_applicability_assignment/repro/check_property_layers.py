import sqlite3


def main() -> None:
    con = sqlite3.connect(":memory:")
    cur = con.cursor()

    cur.executescript(
        """
        CREATE TABLE wide_entity (
          id INTEGER PRIMARY KEY,
          kind TEXT NOT NULL,
          score REAL NULL
        );

        INSERT INTO wide_entity VALUES
          (1, 'A', 0),
          (2, 'A', NULL),
          (3, 'B', NULL),
          (4, 'A', 7);

        CREATE TABLE property_kind (
          name TEXT PRIMARY KEY
        );
        INSERT INTO property_kind VALUES ('score');

        CREATE TABLE property_applicability (
          entity_id INTEGER NOT NULL,
          property_name TEXT NOT NULL,
          PRIMARY KEY(entity_id, property_name),
          FOREIGN KEY(entity_id) REFERENCES wide_entity(id),
          FOREIGN KEY(property_name) REFERENCES property_kind(name)
        );

        INSERT INTO property_applicability VALUES
          (1, 'score'),
          (2, 'score'),
          (4, 'score');

        CREATE TABLE property_assignment (
          entity_id INTEGER NOT NULL,
          property_name TEXT NOT NULL,
          value REAL NOT NULL,
          PRIMARY KEY(entity_id, property_name),
          FOREIGN KEY(entity_id, property_name)
            REFERENCES property_applicability(entity_id, property_name)
        );

        INSERT INTO property_assignment VALUES
          (1, 'score', 0),
          (4, 'score', 7);
        """
    )

    wide = cur.execute(
        "SELECT id, kind, score FROM wide_entity ORDER BY id"
    ).fetchall()

    layered = cur.execute(
        """
        SELECT e.id,
               e.kind,
               CASE WHEN a.entity_id IS NULL THEN 0 ELSE 1 END AS applicable,
               CASE WHEN v.entity_id IS NULL THEN 0 ELSE 1 END AS assigned,
               v.value
        FROM wide_entity AS e
        LEFT JOIN property_applicability AS a
          ON a.entity_id = e.id AND a.property_name = 'score'
        LEFT JOIN property_assignment AS v
          ON v.entity_id = e.id AND v.property_name = 'score'
        ORDER BY e.id
        """
    ).fetchall()

    counts = cur.execute(
        """
        SELECT
          (SELECT COUNT(*) FROM property_kind) AS declared_kinds,
          (SELECT COUNT(*) FROM property_applicability
             WHERE property_name = 'score') AS applicable_entities,
          (SELECT COUNT(*) FROM property_assignment
             WHERE property_name = 'score') AS assigned_entities,
          (SELECT COUNT(*) FROM property_assignment
             WHERE property_name = 'score' AND value = 0) AS defined_zero_entities
        """
    ).fetchone()

    print("Wide nullable projection:")
    for row in wide:
        print(row)

    print("\nLayered status projection:")
    for row in layered:
        print(row)

    print("\nCounts (declared kinds, applicable, assigned, defined zero):")
    print(counts)

    assert wide[1][2] is None and wide[2][2] is None
    assert layered[1] == (2, 'A', 1, 0, None)
    assert layered[2] == (3, 'B', 0, 0, None)
    assert layered[0] == (1, 'A', 1, 1, 0.0)
    assert counts == (1, 3, 2, 1)


if __name__ == "__main__":
    main()
