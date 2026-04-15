import sqlite3

def init_db():
    conexao = sqlite3.connect("sistema_bancario.db")
    cursor = conexao.cursor()

    with open("database/schema.sql") as f:
        cursor.executescript(f.read())

    conexao.commit()
    conexao.close()
