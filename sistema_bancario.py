from banco import Banco

bc = Banco("Banco do Brejo", 999)
cpfs_cadastrados = []
menu = """
Bem-vindo ao Banco do Brejo!
Escolha uma operação:
[a] Abrir conta
[i] Encerrar conta
[d] Depósito
[s] Saque
[t] Transferência
[e] Extrato  
[q] Sair
"""

while True:
    
    opcao = input(menu)
    
    if opcao == "a":
        cpf_cliente = int(input("Digite seu cpf: "))
        nome_cliente = input("Digite seu nome completo:")
        
        numero_da_conta = bc.abre_conta(nome_cliente, cpf_cliente)
        cpfs_cadastrados.append(cpf_cliente)

        print(f"O número da sua conta é: {numero_da_conta}")
    

    elif opcao == "i":
        cpf_cliente = int(input("Digite o seu cpf: "))

        encerra = bc.encerra_conta(cpf_cliente)
        
        if encerra:
            print("Conta encerrada com sucesso")
        else:
            print("Conta não registrada ou saldo positivo, por favor tente novamente")
        

    elif opcao == "d":
        cpf_cliente = int(input("Digite seu cpf: "))
        valor = float(input("Digite o valor que você deseja depositar: R$ "))
        
        deposito = bc.deposito(cpf_cliente, valor)

        if deposito:
            print("Depósito realizado com sucesso!")
        else:
            print("Erro ao tentar realizar o depósito, por favor verifique o valor digitado")


    elif opcao == "s":
        cpf_cliente = int(input("Digite seu cpf: "))
        valor = float(input("Digite o valor que deseja sacar: R$ "))
        
        saque = bc.saque(cpf_cliente, valor)

        if saque:
            print("Saque realizado com sucesso!")
        else:
            print('Saldo insuficiente ou conta não encontrada no sistema, por favor tente novamente')
    

    elif opcao == "t":
        cpf_origem = int(input("Digite o cpf da conta de origem: "))
        cpf_destino = int(input("Digite o cpf da conta de destino: "))
        valor = float(input("Digite o valor que deseja transferir: R$ "))
        
        transferencia = bc.transferencia(cpf_origem, cpf_destino, valor)

        if transferencia:
            print("Transferência realizada com sucesso!")
        else:
            print('Saldo da conta de origem insuficiente ou conta não encontrada no sistema, por favor tente novamente')


    elif opcao == "e":  #saldo
        cpf_cliente = int(input("Digite o seu cpf: "))

        saldo = bc.saldo(cpf_cliente)

        if saldo is False:
            print("Conta não cadastrada")
        else:
            print(f"R$ {saldo}")


    elif opcao == "q":
        break


    elif opcao == "":
        print("Não entendi sua escolha, por favor tente novamente")
   


