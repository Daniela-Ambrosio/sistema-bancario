import streamlit as st
from banco import Banco

st.set_page_config(page_title="Sistema Bancário")

st.title("Banco do Brejo")

if 'banco' not in st.session_state:
    st.session_state['banco'] = Banco("Banco do Brejo", 999)

bc = st.session_state['banco']

#barra lateral =========================================
menu = st.sidebar.selectbox(
    "Menu Principal",
    ["Início", "Abrir Conta", "Encerrar Conta", "Depositar", "Sacar", "Transferência", "Extrato"]
)


#Menu ================================
if menu == "Início":
    st.write("Bem-vindo ao Banco do Brejo.")
    st.info("Selecione uma opção no menu ao lado.")

elif menu == "Abrir Conta":
    st.header("Nova Conta")
    cpf_cliente = st.number_input("Digite seu CPF (Somente números)", min_value=0, format="%d")
    nome_cliente = st.text_input("Digite seu nome completo")
    
    if st.button("Criar Conta"):
        numero_da_conta = bc.abre_conta(nome_cliente, int(cpf_cliente))
        st.success(f"O número da sua conta é: {numero_da_conta}")

elif menu == "Encerrar Conta":
    st.header("Encerrar essa conta")
    cpf_cliente = st.number_input("Digite seu CPF (Somente números)", min_value=0, format="%d")

    if st.button("Encerrar Conta"):
        encerra = bc.encerra_conta(cpf_cliente)

        if encerra:
            st.success("Conta encerrada com sucesso")
        else:
            st.error("Conta não registrada ou saldo positivo, por favor tente novamente")


elif menu == "Depositar":
    st.header("Fazer Depósito")
    cpf_cliente = st.number_input("CPF da conta", min_value=0, format="%d")
    valor = st.number_input("Valor do depósito", min_value=0.01)
    
    if st.button("Confirmar Depósito"):
        deposito = bc.deposito(cpf_cliente, valor)
        
        if deposito:
            st.success("Depósito realizado com sucesso!")
        else:
            st.error("Erro ao tentar realizar o depósito, por favor verifique o CPF digitado")

elif menu == "Transferência":
    st.header("Fazer transferência")
    cpf_origem = st.number_input("CPF da conta de origem", min_value=0, format="%d")
    cpf_destino = st.number_input("CPF da conta de destino", min_value=0, format="%d")
    valor = st.number_input("Valor da transferência", min_value=0.01)

    if st.button("Confirmar transferência"):
        transferencia = bc.transferencia(cpf_origem, cpf_destino, valor)

        if transferencia:
            st.success("Transferência realizada com sucesso!")
        else:
            st.error('Saldo da conta de origem insuficiente ou conta não encontrada no sistema, por favor tente novamente')

elif menu == "Sacar":
    st.header("Fazer Saque")
    cpf_cliente = st.number_input("CPF da conta", min_value=0, format="%d")
    valor = st.number_input("Valor do saque", min_value=0.01)
    
    if st.button("Confirmar Saque"):
        saque = bc.saque(cpf_cliente, valor)
        if saque:
            st.success("Saque realizado com sucesso!")
        else:
            st.error("Saldo insuficiente ou conta não encontrada no sistema, por favor tente novamente")
       
elif menu == "Extrato":
    st.header( "Consultar Saldo")
    cpf_cliente = st.number_input("Digite seu CPF", min_value=0, format="%d")
    
    if st.button("Ver Saldo"):
        saldo = bc.saldo(cpf_cliente)
        if saldo is False:
            st.error("CPF não encontrado.")
        else:
            st.metric("Seu Saldo", f"R$ {saldo:.2f}")