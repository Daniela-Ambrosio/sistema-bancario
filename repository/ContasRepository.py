import sqlite3
from database.connection import get_connection
from services.Conta import Conta

class ContaRepository:

#retorna 0 caso não tenha nenhuma conta ainda
    def buscar_ultimo_id(self):
        try:
            conexao = get_connection()
            cursor = conexao.cursor()
            cursor.execute("SELECT MAX(CAST(numero_conta AS INTEGER)) FROM contas")
            resultado = cursor.fetchone()[0] 

            if resultado is not None:
                return resultado  
            else:
                return 0

        except sqlite3.Error as erro:
            print(erro)
            raise erro

        finally:
            conexao.close()

#retorna None caso não tenha nenhuma conta com esse cpf
    def buscar_por_cpf(self, cpf):
        try:
            conexao = get_connection()
            cursor = conexao.cursor()

            cursor.execute(
                "SELECT numero_conta, titular, cpf, saldo FROM contas WHERE cpf = ?",
                (cpf,)
            )

            tupla = cursor.fetchone()
            if tupla:
                conta = Conta(tupla[0], tupla[1], tupla[2], tupla[3])
                return conta
            else:
                return None
                
        except sqlite3.Error as erro:
            print(erro)
            raise Exception("Erro no banco de dados")

        finally:
            conexao.close()

    def inserir(self, conta):
        try:
            conexao = get_connection()
            cursor = conexao.cursor()
            
            cursor.execute( '''
                INSERT INTO contas (numero_conta, titular, cpf, saldo) 
                    VALUES (?, ?, ?, ?)
                ''', (conta.numero , conta.titular, conta.cpf, conta.saldo))
            
            conexao.commit()
            conexao.close()

        except sqlite3.Error as erro:
            print(erro)
            raise Exception("Erro ao tentar salvar no banco de dados")

        finally:
            conexao.close()
        

    def atualizar_saldo(self, conta):
        conexao = get_connection()
        cursor = conexao.cursor()

        cursor.execute( '''
            UPDATE contas 
            SET saldo = ? 
            WHERE numero_conta = ?''',
            (conta.saldo, conta.numero)
        )

        conexao.commit()
        conexao.close()

    def deletar(self, cpf):
        try:
            conexao = get_connection()
            cursor = conexao.cursor()

            cursor.execute("DELETE FROM contas WHERE cpf = ?", (cpf,))
            conexao.commit()

            linhas_apagadas = cursor.rowcount 
            
            conexao.commit()
            
            if linhas_apagadas == 0:
                raise ValueError("Conta não encontrada no banco de dados para exclusão.")
        
        except sqlite3.Error as erro:
            print(erro)
            raise Exception("Erro ao deletar conta do banco de dados")

        finally:
            conexao.close()

#só deve entregar o extrato descriptografado usando a chave simétrica 
    # def le_extrato(cpf):
    #     try:
    #         conexao = get_connection()
    #         cursor = conexao.cursor()

    #         conta = buscar_por_cpf(cpf)

    #         cursor.execute('''
    #                 SELECT descricao_criptografada
    #                 FROM transacoes 
    #                 WHERE numero_conta = ?
    #             ''', (conta.numero))

    #         lista_do_banco = cursor.fetchall()
    #         extrato_formatado = f"-----EXTRATO DA CONTA {numero_conta} ----- \n"

    #         if not linhas_do_banco:
    #             return extrato_formatado + "Nenhuma transação encontrada."
                
    #         for linha in linhas_do_banco:
    #             extrato_criptografado = linha[0]
                    
    #             extrato_formatado += f"- {extrato_criptografado}\n"
        
    #         return extrato_formatado

    #     except sqlite3.Error as erro:
    #         print(erro)
    #         raise Exception("Erro ao ler extrato no banco de dados")

    #     finally:
    #         conexao.close()