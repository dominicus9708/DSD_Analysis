import sqlite3


def main() -> None:
    con = sqlite3.connect(":memory:")
    cur = con.cursor()

    cur.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, x INTEGER, s TEXT)")
    cur.executemany(
        "INSERT INTO t(id, x, s) VALUES (?, ?, ?)",
        [
            (1, 0, ""),
            (2, None, None),
        ],
    )

    checks = [
        ("rows", "SELECT COUNT(*) FROM t"),
        ("nonnull_x", "SELECT COUNT(x) FROM t"),
        ("sum_x", "SELECT SUM(x) FROM t"),
        ("nonnull_coalesced_x", "SELECT COUNT(COALESCE(x,0)) FROM t"),
        ("sum_empty_relation", "SELECT SUM(x) FROM t WHERE id > 100"),
        ("count_empty_relation", "SELECT COUNT(*) FROM t WHERE id > 100"),
        ("missing_id_rows", "SELECT COUNT(*) FROM t WHERE id = 3"),
        ("null_rows", "SELECT COUNT(*) FROM t WHERE x IS NULL"),
        ("zero_rows", "SELECT COUNT(*) FROM t WHERE x = 0"),
        ("empty_string_rows", "SELECT COUNT(*) FROM t WHERE s = ''"),
        ("null_string_rows", "SELECT COUNT(*) FROM t WHERE s IS NULL"),
    ]

    for label, sql in checks:
        value = cur.execute(sql).fetchone()[0]
        print(f"{label}: {value!r}")


if __name__ == "__main__":
    main()
