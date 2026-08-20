import sqlite3
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE kv (key TEXT PRIMARY KEY, value TEXT)")
cursor.execute("INSERT INTO kv VALUES (?, ?)", ("greeting", "hello from sqlite"))
conn.commit()
print(cursor.execute("SELECT value FROM kv WHERE key = ?", ("greeting",)).fetchone()[0])
conn.close()
