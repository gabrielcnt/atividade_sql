import sqlite3

banco = sqlite3.connect('banco.db')

cursor = banco.cursor()

# 3 criar a tabela livros
cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL UNIQUE,
        autor TEXT,
        ano INTEGER,
        genero TEXT,
        disponivel INTEGER NOT NULL DEFAULT 1 CHECK (disponivel IN (0, 1)))
''')

# 4 inserir 5 livros
cursor.executemany('''
    INSERT OR IGNORE INTO livros (titulo, autor, ano, genero, disponivel)
        VALUES (?, ?, ?, ?, ?)
''',[
    ('1984', 'George Orwell', 1949, 'Distopia / Ficção política', 1), 
    ('Dom Casmurro', 'Machado de Assis', 1899, 'Romance psicológico / Romance brasileiro', 0),
    ('O Senhor dos Anéis: A Sociedade do Anel', 'J. R. R. Tolkien', 1954, 'Fantasia / Aventura', 1), 
    ('Orgulho e Preconceito', 'Jane Austen', 1813, 'Romance / Ficção clássica', 0), 
    ('A Revolução dos Bichos', 'George Orwell', 1945, 'Sátira política / Fábula', 1)
    ])

# 5 consultar livros disponiveis
livros_disponiveis = cursor.execute('''
    SELECT * FROM livros WHERE disponivel = 1
''')

resultados = livros_disponiveis.fetchall()
for livro in resultados:
    print(livro)

banco.commit()
banco.close()

