class FichaBancaria:

    def __init__(self, numero, nome, cpf):  
        self.__numero = numero
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = 0

    @property    
    def get_numero(self):
        return self.__numero
        
    @property
    def get_nome(self):
        return self.__nome
        
    @property
    def get_saldo(self):
        return self.__saldo
        
    @property
    def get_cpf(self):
        return self.__cpf

    def set_numero(self, numero_conta):
        self.__numero = numero_conta

    def set_nome(self, nome):
        self.__nome = nome

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def debite(self, valor):
        self.__saldo -= valor

    def credite(self, valor):
        self.__saldo += valor