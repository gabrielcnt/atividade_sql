import sqlite3

banco = sqlite3.connect('banco.db')

cursor = banco.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL UNIQUE,
        autor TEXT,
        ano INTEGER,
        genero TEXT,
        disponivel INTEGER NOT NULL DEFAULT 1 CHECK (disponivel IN (0, 1)))
''')
