from repository.ContasRepository import ContaRepository 
from repository.TransacaoRepository import TransacaoRepository 
from services.Conta import Conta
import math

class Banco:
    
    def __init__(self, nome_banco, codigo_banco):
        if isinstance(nome_banco, str):
            self.__nome = nome_banco
        
        if isinstance(codigo_banco, int):
            self.__numero = codigo_banco

        self.__fichario = {}

        self.conta_repo = ContaRepository()
        self.transacao_repo = TransacaoRepository()
        
        self.__ultima_conta_criada = self.conta_repo.buscar_ultimo_id()


 
    
    # def le_extrato(self, numero_conta):
        

    
    def abre_conta(self, titular, cpf):

        if not cpf.isdigit():
            raise ValueError("O formato do cpf é inválido") 

        if not titular.isalpha():
            raise ValueError("O formato de nome é inválido")

        conta = self.conta_repo.buscar_por_cpf(cpf)
        if conta:
            raise ValueError("Cliente já existe")

       
        numero_da_conta = self.__ultima_conta_criada + 1
        conta = Conta(numero_da_conta, titular, cpf)

        self.conta_repo.inserir(conta)

        self.__ultima_conta_criada = numero_da_conta
        self.__fichario[cpf] = conta
        
        return self.__ultima_conta_criada
        
    

        
  
    def deposito(self, cpf, valor):
        conta = self.__fichario.get(cpf)
        if conta is None:
            conta = self.conta_repo.buscar_por_cpf(cpf)
            print("DEBUG: Buscou a conta pelo cpf")
            if conta is None:
                raise ValueError("Conta não encontrada")
            self.__fichario[cpf] = conta
        
        conta.credite(valor)
        try:
            self.transacao_repo.inserir(conta.numero, "DEPOSITO", valor)
            self.conta_repo.atualizar_saldo(conta)

        except Exception as erro:
            conta.debite(valor) 
            raise erro
        
            
    def saque(self, cpf, valor):
        conta = self.__fichario.get(cpf)
        if conta is None:
            conta = self.conta_repo.buscar_por_cpf(cpf)
            if conta is None:
                raise ValueError("Conta não encontrada")
            self.__fichario[cpf] = conta
            
        if conta.saldo < valor:
            raise ValueError("Saldo insuficiente")

        try:
            conta.debite(valor)
            self.transacao_repo.inserir(conta.numero, "SAQUE", valor)
            self.conta_repo.atualizar_saldo(conta)

        except Exception as erro:
            conta.credite(valor)
            raise erro

            
    
    def transferencia(self, cpf_origem, cpf_destino, valor):
        if cpf_origem == cpf_destino:
            raise ValueError("As contas de origem e destino não podem ser as mesmas.")

        conta_origem = self.__fichario.get(cpf_origem)
        if conta_origem is None:
            conta_origem = self.conta_repo.buscar_por_cpf(cpf_origem)
            if conta_origem is None:
                raise ValueError("Conta de origem não encontrada")
            self.__fichario[cpf_origem] = conta_origem

        conta_destino = self.__fichario.get(cpf_destino)
        if conta_destino is None:
            conta_destino = self.conta_repo.buscar_por_cpf(cpf_destino)
            if conta_destino is None:
                raise ValueError("Conta de destino não encontrada")
            self.__fichario[cpf_destino] = conta_destino

        if conta_origem.saldo < valor:
            raise ValueError("Saldo insuficiente")
            
        conta_origem.debite(valor)
        conta_destino.credite(valor)

        try:
            self.transacao_repo.inserir(conta_origem.numero, "TRANSFERENCIA ENVIADA", valor)
            self.transacao_repo.inserir(conta_destino.numero, "TRANSFERENCIA RECEBIDA", valor)
                
            self.conta_repo.atualizar_saldo(conta_origem)
            self.conta_repo.atualizar_saldo(conta_destino)
        
        except Exception as erro:
            conta_origem.credite(valor)
            conta_destino.debite(valor)

            raise erro
    

    def saldo(self, cpf):   
        conta = self.__fichario.get(cpf)
        if conta is None:
            conta = self.conta_repo.buscar_por_cpf(cpf)
            if conta is None:
                raise ValueError("Conta não encontrada")
            self.__fichario[cpf] = conta

        saldo = conta.saldo
        return saldo

 

    def encerra_conta(self, cpf): 
        conta = self.__fichario.get(cpf)
        if conta is None:
            conta = self.conta_repo.buscar_por_cpf(cpf)
            if conta is None:
                raise ValueError("Conta não encontrada")
            self.__fichario[cpf] = conta

        if conta.saldo != 0:
            raise ValueError("Não é possivel excluir uma conta com saldo positivo")
        self.conta_repo.deletar(cpf)
        
        if cpf in self.__fichario:
            del self.__fichario[cpf]
       
            

    
    
