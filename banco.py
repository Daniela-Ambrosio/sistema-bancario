from ficha_bancaria import *
import math

class Banco:
    
    def __init__(self, nome_banco, codigo_banco):
        self.__nome = nome_banco
        self.__numero = codigo_banco
        self.__ultima_conta_criada = 0
        self.__fichario = {}
        
    def abre_conta(self, nome_cliente, cpf_cliente):

        self.__ultima_conta_criada += 1
        ficha = FichaBancaria(self.__ultima_conta_criada, nome_cliente, cpf_cliente)
        self.__fichario[cpf_cliente] = ficha

        return self.__ultima_conta_criada
  
    def deposito(self, cpf_cliente, valor):
        
        if cpf_cliente in self.__fichario:
            self.__fichario[cpf_cliente].credite(valor)
            return True
        else:
            return False
            
    def saque(self, cpf_cliente, valor):
        
        if cpf_cliente in self.__fichario:
            conta = self.__fichario[cpf_cliente]
            
            if conta.get_saldo >= valor:
                conta.debite(valor)
                return True        
            else:
                return False
        else:  
            return False
    
    def transferencia(self, cpf_origem, cpf_destino, valor):
        
        if cpf_origem in self.__fichario and cpf_destino in self.__fichario: 
            conta_origem = self.__fichario[cpf_origem]
            conta_destino = self.__fichario[cpf_destino]
            
            if conta_origem.get_saldo >= valor:
                conta_origem.debite(valor)
                conta_destino.credite(valor)
                return True
            else:
                return False
        else:
            return False

    def saldo(self, cpf_cliente):       
    
        if cpf_cliente in self.__fichario:
            conta = self.__fichario[cpf_cliente]
            saldo = conta.get_saldo
            return saldo
        else:
            return False
 
    def encerra_conta(self, cpf_cliente):
        
        if cpf_cliente in self.__fichario and self.saldo(cpf_cliente) == 0:
            del self.__fichario[cpf_cliente]
            return True
        else:
            return False
            
    
    
