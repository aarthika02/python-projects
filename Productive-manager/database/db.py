import sqlite3

def init_db():
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()

    c.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              priority TEXT,
              deadline TEXT,
              status TEXT
            )
    """)

    conn.commit()
    conn.close()