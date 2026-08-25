import sqlite3


def main():
    con = sqlite3.connect(":memory:")
    con.execute("PRAGMA foreign_keys = ON")
    con.executescript("""
    CREATE TABLE grp(
      gid TEXT PRIMARY KEY,
      label TEXT NOT NULL
    );
    CREATE TABLE parent(
      id INTEGER PRIMARY KEY
    );
    CREATE TABLE rel(
      id INTEGER PRIMARY KEY,
      gid TEXT NOT NULL REFERENCES grp(gid),
      target_id INTEGER REFERENCES parent(id),
      weight REAL
    );

    INSERT INTO grp(gid,label) VALUES
      ('A','no relation row'),
      ('B','relation row, no target, no weight'),
      ('C','valid target, missing weight'),
      ('D','valid target, defined zero'),
      ('E','two valid targets, +5 and -5 cancellation'),
      ('F','valid target, defined 7');

    INSERT INTO parent(id) VALUES (30),(40),(50),(51),(60);

    INSERT INTO rel(id,gid,target_id,weight) VALUES
      (2,'B',NULL,NULL),
      (3,'C',30,NULL),
      (4,'D',40,0),
      (5,'E',50,5),
      (6,'E',51,-5),
      (7,'F',60,7);
    """)

    rows = con.execute("""
    SELECT g.gid,
           COUNT(*) AS joined_rows,
           COUNT(r.id) AS relation_rows,
           COUNT(r.target_id) AS target_refs,
           COUNT(r.weight) AS defined_weights,
           SUM(r.weight) AS sum_weight,
           SUM(COALESCE(r.weight,0)) AS sum_coalesced_weight,
           COALESCE(SUM(r.weight),0) AS coalesced_sum_weight
    FROM grp AS g
    LEFT JOIN rel AS r ON r.gid = g.gid
    GROUP BY g.gid
    ORDER BY g.gid
    """).fetchall()

    print("GROUP AGGREGATES")
    for row in rows:
        print(row)

    empty = con.execute("""
    SELECT COUNT(*) AS rows,
           COUNT(weight) AS defined_weights,
           SUM(weight) AS sum_weight,
           COALESCE(SUM(weight),0) AS coalesced_sum_weight
    FROM rel
    WHERE 1 = 0
    """).fetchone()
    print("EMPTY RELATION AGGREGATE")
    print(empty)

    collisions = {}
    for row in rows:
        gid = row[0]
        coalesced_sum_weight = row[-1]
        collisions.setdefault(coalesced_sum_weight, []).append(gid)

    print("COALESCED-SUM COLLISIONS")
    for value in sorted(collisions):
        gids = collisions[value]
        if len(gids) > 1:
            print((value, tuple(gids)))


if __name__ == "__main__":
    main()
