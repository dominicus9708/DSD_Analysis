import sqlite3


def rows(cur, sql):
    return cur.execute(sql).fetchall()


def main():
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.executescript(
        """
        CREATE TABLE l(id INTEGER PRIMARY KEY, label TEXT NOT NULL);
        CREATE TABLE r(id INTEGER PRIMARY KEY, val INTEGER);
        INSERT INTO l VALUES (1,'A'),(2,'B'),(3,'C');
        INSERT INTO r VALUES (1,10),(3,NULL);
        """
    )

    q_inner = """
        SELECT l.id, r.id, r.val
        FROM l INNER JOIN r ON l.id = r.id
        ORDER BY l.id
    """
    q_left = """
        SELECT l.id, r.id, r.val
        FROM l LEFT JOIN r ON l.id = r.id
        ORDER BY l.id
    """
    q_left_where = """
        SELECT l.id, r.id, r.val
        FROM l LEFT JOIN r ON l.id = r.id
        WHERE r.val > 5
        ORDER BY l.id
    """
    q_left_on_filter = """
        SELECT l.id, r.id, r.val
        FROM l LEFT JOIN r ON l.id = r.id AND r.val > 20
        ORDER BY l.id
    """
    q_projected = """
        SELECT l.id, r.val
        FROM l LEFT JOIN r ON l.id = r.id
        ORDER BY l.id
    """

    inner = rows(cur, q_inner)
    left = rows(cur, q_left)
    left_where = rows(cur, q_left_where)
    left_on_filter = rows(cur, q_left_on_filter)
    projected = rows(cur, q_projected)

    print(f"INNER JOIN: {inner}")
    print(f"LEFT JOIN: {left}")
    print(f"LEFT JOIN + WHERE r.val > 5: {left_where}")
    print(f"LEFT JOIN + ON r.val > 20: {left_on_filter}")
    print(f"Projected LEFT JOIN: {projected}")

    assert inner == [(1, 1, 10), (3, 3, None)]
    assert left == [(1, 1, 10), (2, None, None), (3, 3, None)]
    assert left_where == [(1, 1, 10)]
    assert left_on_filter == [(1, None, None), (2, None, None), (3, None, None)]
    assert projected == [(1, 10), (2, None), (3, None)]

    # id=2 is unmatched; id=3 matched a real right row whose val is NULL.
    assert left[1][1] is None
    assert left[2][1] == 3
    assert projected[1][1] is None and projected[2][1] is None

    con.close()


if __name__ == "__main__":
    main()
