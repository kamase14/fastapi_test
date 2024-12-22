
def create_db(conn):
    cur = conn.cursor()
    cur.execute("""DROP TABLE IF EXISTS recipes""")
    cur.execute("""CREATE TABLE IF NOT EXISTS recipes ( id INTEGER PRIMARY KEY AUTOINCREMENT,
        title varchar(100)  NOT NULL,
        making_time varchar(100)  NOT NULL,
        serves varchar(100)  NOT NULL,
        ingredients varchar(300)  NOT NULL,
        cost integer NOT NULL,
        created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at datetime on_update CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        );""")
    cur.execute("""INSERT INTO recipes (
        id,
        title,
        making_time,
        serves,
        ingredients,
        cost,
        created_at,
        updated_at
        )
        VALUES (
        1,
        'チキンカレー',
        '45分',
        '4人',
        '玉ねぎ,肉,スパイス',
        1000,
        '2016-01-10 12:10:12',
        '2016-01-10 12:10:12'
        );""")
    cur.execute(
        """INSERT INTO recipes (
        id,
        title,
        making_time,
        serves,
        ingredients,
        cost,
        created_at,
        updated_at
        )
        VALUES (
        2,
        'オムライス',
        '30分',
        '2人',
        '玉ねぎ,卵,スパイス,醤油',
        700,
        '2016-01-11 13:10:12',
        '2016-01-11 13:10:12'
        );
    """)

    conn.commit()
    cur.execute('SELECT * from recipes')

    for row in cur:
        print(row)
