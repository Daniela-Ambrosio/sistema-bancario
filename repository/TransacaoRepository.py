import sqlite3
from database.connection import get_connection
from datetime import datetime

class TransacaoRepository:
    def inserir(self, numero_conta, operacao, valor):
        try:
            conexao = get_connection()
            cursor = conexao.cursor()

            data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cursor.execute('''
                INSERT INTO transacoes (numero_conta, operacao, valor, data_hora) 
                VALUES (?, ?, ?, ?)
            ''', (numero_conta, operacao, valor, data_hora))

            conexao.commit()

        except sqlite3.Error as erro:
            conexao.rollback()

            print(erro)
            raise Exception("Falha no banco de dados")

        finally:
            conexao.close()


