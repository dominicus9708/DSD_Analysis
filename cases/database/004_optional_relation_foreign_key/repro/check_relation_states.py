import sqlite3


def main() -> None:
    con = sqlite3.connect(":memory:")
    con.execute("PRAGMA foreign_keys = ON")

    con.executescript(
        """
        CREATE TABLE entity(
            id INTEGER PRIMARY KEY,
            label TEXT NOT NULL
        );
        CREATE TABLE target(
            id INTEGER PRIMARY KEY,
            label TEXT NOT NULL
        );
        CREATE TABLE relation(
            source_id INTEGER PRIMARY KEY REFERENCES entity(id),
            target_id INTEGER REFERENCES target(id),
            weight REAL
        );
        """
    )

    con.executemany(
        "INSERT INTO entity(id,label) VALUES (?,?)",
        [(1, "E1"), (2, "E2"), (3, "E3"), (4, "E4"), (5, "E5"), (6, "E6")],
    )
    con.executemany(
        "INSERT INTO target(id,label) VALUES (?,?)",
        [(30, "T30"), (40, "T40"), (50, "T50")],
    )
    con.executemany(
        "INSERT INTO relation(source_id,target_id,weight) VALUES (?,?,?)",
        [(2, None, None), (3, 30, None), (4, 40, 0.0), (5, 50, 7.0)],
    )

    rows = con.execute(
        """
        SELECT e.id, r.source_id, r.target_id, t.id AS target_exists, r.weight,
        CASE
          WHEN r.source_id IS NULL THEN 'NO_RELATION_ROW'
          WHEN r.target_id IS NULL THEN 'RELATION_ROW_NO_TARGET'
          WHEN t.id IS NOT NULL AND r.weight IS NULL THEN 'TARGET_RELATION_VALUE_MISSING'
          WHEN t.id IS NOT NULL AND r.weight = 0 THEN 'TARGET_RELATION_DEFINED_ZERO'
          ELSE 'TARGET_RELATION_DEFINED_VALUE'
        END AS status
        FROM entity e
        LEFT JOIN relation r ON r.source_id = e.id
        LEFT JOIN target t ON t.id = r.target_id
        WHERE e.id <= 5
        ORDER BY e.id
        """
    ).fetchall()

    print("RELATION STATES")
    for row in rows:
        print(row)

    try:
        con.execute(
            "INSERT INTO relation(source_id,target_id,weight) VALUES (?,?,?)",
            (6, 999, 1.0),
        )
    except sqlite3.IntegrityError as exc:
        print("INVALID TARGET:", str(exc))

    con2 = sqlite3.connect(":memory:")
    con2.execute("PRAGMA foreign_keys = ON")
    con2.executescript(
        """
        CREATE TABLE target(id INTEGER PRIMARY KEY);
        CREATE TABLE rel_setnull(
            id INTEGER PRIMARY KEY,
            target_id INTEGER REFERENCES target(id) ON DELETE SET NULL,
            weight REAL
        );
        CREATE TABLE rel_cascade(
            id INTEGER PRIMARY KEY,
            target_id INTEGER REFERENCES target(id) ON DELETE CASCADE,
            weight REAL
        );
        INSERT INTO target VALUES (1);
        INSERT INTO rel_setnull VALUES (10, 1, 7.0);
        INSERT INTO rel_cascade VALUES (20, 1, 7.0);
        DELETE FROM target WHERE id = 1;
        """
    )

    print("SET NULL AFTER PARENT DELETE:", con2.execute("SELECT * FROM rel_setnull").fetchall())
    print("CASCADE AFTER PARENT DELETE:", con2.execute("SELECT * FROM rel_cascade").fetchall())


if __name__ == "__main__":
    main()
