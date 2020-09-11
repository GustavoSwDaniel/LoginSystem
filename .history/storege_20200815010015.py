import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    user TEXT NOT NULL,
    password TEXT NOT NULL
);
""")

print('Tablea criada com sucesso.')
conn.close()