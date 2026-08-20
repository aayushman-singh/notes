#!/usr/bin/env sh
set -eu
python3 -c "import os; os.makedirs('/record', exist_ok=True); open('/record/postgresql_everything_demo.py', 'w').write('import sqlite3\nconn = sqlite3.connect(\":memory:\")\ncursor = conn.cursor()\ncursor.execute(\"CREATE TABLE kv (key TEXT PRIMARY KEY, value TEXT)\")\ncursor.execute(\"INSERT INTO kv VALUES (?, ?)\", (\"greeting\", \"hello from sqlite\"))\nconn.commit()\nprint(cursor.execute(\"SELECT value FROM kv WHERE key = ?\", (\"greeting\",)).fetchone()[0])\nconn.close()\n')"
