class Conta:

    def __init__(self, numero_conta, titular, cpf, saldo=0):  
        self.__numero = numero_conta
        self.__titular = titular
        self.__cpf = cpf
        self.__saldo = saldo

    @property    
    def numero(self):
        return self.__numero
        
    @property
    def titular(self):
        return self.__titular
        
    @property
    def saldo(self):
        return self.__saldo
        
    @property
    def cpf(self):
        return self.__cpf

    @numero.setter
    def numero(self, numero_conta):
        self.__numero = numero_conta

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    def debite(self, valor):
        self.__saldo -= valor

    def credite(self, valor):
        self.__saldo += valor