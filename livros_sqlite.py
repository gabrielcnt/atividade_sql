import sqlite3



def conectar_banco():
    
    return sqlite3.connect('livraria.db')


# 3 criar a tabela livros
def criar_tabela_livros():
    banco = conectar_banco()
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

# 4 inserir 5 livros
def inserir_livros():
    banco = conectar_banco()
    cursor = banco.cursor()

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
    banco.commit()
    banco.close()

# 5 consultar livros disponiveis
def consultar_livros_disponiveis():
    banco = conectar_banco()
    cursor = banco.cursor()
    livros_disponiveis = cursor.execute('''
        SELECT * FROM livros WHERE disponivel = 1
    ''')

    resultados = livros_disponiveis.fetchall()
    for livro in resultados:
        print(livro)

    banco.commit()
    banco.close()



# 6 atualizar disponibilidade
def atualizar_diponibilidade():
    banco = conectar_banco()
    cursor = banco.cursor()
    cursor.execute('''
        UPDATE livros
        SET disponivel = 1
        WHERE id = 4
    ''')

    banco.commit()
    banco.close()


# 7 ordernar livros por ano
def ordernar_livros_por_ano():
    banco = conectar_banco()
    cursor = banco.cursor()
    livros_ordernados_decrescente = cursor.execute('''
        SELECT * FROM livros
        ORDER BY ano DESC;
    ''')
    resultados = livros_ordernados_decrescente
    for livro in resultados:
        print(livro)
    banco.commit()
    banco.close()


# 8 deletar um livro antigo
def deletar_livro_antigo():
    banco = conectar_banco()
    cursor = banco.cursor()
    cursor.execute('''
        DELETE FROM livros
        WHERE ano < 1940;
    ''')

    banco.commit()
    banco.close()


# 9 criar tabela usuario
def criar_tabela_usuario():
    banco = conectar_banco()
    cursor = banco.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuario(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT)
    ''')

# 10 alterar tabela usuario
def alterar_tabela_usuario():
    banco = conectar_banco()
    cursor = banco.cursor()
    try:
        cursor.execute('''
            ALTER TABLE usuario
            ADD idade INTEGER
        ''')
    except sqlite3.OperationalError:
        pass

# 11 inserir 5 usuarios
def inserir_usuarios():
    banco = conectar_banco()
    cursor = banco.cursor()
    cursor.executemany('''
        INSERT OR IGNORE INTO usuario (nome, idade)
            VALUES (?, ?)
    ''', [
        ('Maira', 23),
        ('Gomelor', 36),
        ('Sinfane', 19),
        ('Katefy', 47),
        ('Crodoteica', 38)
    ])


    banco.commit()
    banco.close()



# 12 apagar tabela usuario
def apagar_tabela_usuario():
    banco = conectar_banco()
    cursor = banco.cursor()
    cursor.execute('''
        DROP TABLE usuario
    ''')



if __name__ == "__main__":
    criar_tabela_livros()
    inserir_livros()
    consultar_livros_disponiveis()
    atualizar_diponibilidade()
    ordernar_livros_por_ano()
    deletar_livro_antigo()
    criar_tabela_usuario()
    alterar_tabela_usuario()
    inserir_usuarios()
    apagar_tabela_usuario()