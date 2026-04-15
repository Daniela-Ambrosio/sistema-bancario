import streamlit as st
from services.Banco import Banco
from database.init_DB import init_db

@st.cache_resource
def inicializar_banco():
    init_db()

inicializar_banco()

st.set_page_config(
    page_title="Sistema Bancário",
    
    )

st.title("Bem-vindo ao Banco do Brejo")

if 'Banco' not in st.session_state:
    st.session_state['Banco'] = Banco("Banco do Brejo", 999)

bc = st.session_state['Banco']

#barra lateral =========================================
menu = st.selectbox(
    "Menu",
    ["Início", "Abrir Conta", "Encerrar Conta", "Depositar", "Sacar", "Transferência", "Extrato de Transações", "Ver Saldo"]
)


#Menu ================================
if menu == "Início":
    st.info("Selecione uma opção no menu acima.")

elif menu == "Abrir Conta":
    st.header("Nova Conta")
    cpf_cliente = st.text_input("Digite seu CPF (Somente números ex: 1234678910)")
    titular = st.text_input("Digite seu nome completo")
    
    try:
        if st.button("Criar Conta"):
            numero_da_conta = bc.abre_conta(titular, cpf_cliente)
    
            st.success(f"O número da sua conta é: {numero_da_conta}")

    except ValueError as erro_formato_dos_campos:
        st.error(erro_formato_dos_campos)
    
    except Exception as erro:
        st.error(erro)

elif menu == "Encerrar Conta":
    st.header("Encerrar essa conta")
    cpf_cliente = st.text_input("Digite seu CPF (Somente números)")

    try:
        if st.button("Encerrar Conta"):
            bc.encerra_conta(cpf_cliente)
            st.success("Conta encerrada com sucesso")

    except ValueError as erro_saldo_positivo:
        st.error(erro_saldo_positivo)

    except Exception as erro:
        st.error(erro)



elif menu == "Depositar":
    st.header("Fazer Depósito")
    cpf_cliente = st.text_input("Digite seu CPF")
    valor = st.number_input("Valor do depósito", min_value=0)
    
    try:
        if st.button("Confirmar Depósito"):
            bc.deposito(cpf_cliente, valor)
            st.success("Depósito realizado com sucesso!")

    except ValueError as erro_conta_não_encontrada:
        st.error(erro_conta_não_encontrada)
        
    except Exception as erro: 
        st.error(erro)

elif menu == "Transferência":
    st.header("Fazer transferência")
    cpf_origem = st.text_input("CPF da conta de origem")
    cpf_destino = st.text_input("CPF da conta de destino")
    valor = st.number_input("Valor da transferência", min_value=0)

    try:
        if st.button("Confirmar transferência"):
            bc.transferencia(cpf_origem, cpf_destino, valor)
            st.success("Transferência realizada com sucesso!")
        
    except Exception as erro:
        st.error(erro)

elif menu == "Sacar":
    st.header("Fazer Saque")
    cpf_cliente = st.text_input("CPF da conta")
    valor = st.number_input("Valor do saque", min_value=0)
    
    try:
        if st.button("Confirmar Saque"):
            bc.saque(cpf_cliente, valor)
            st.success("Saque realizado com sucesso!")

    except ValueError as erro:
        st.error(erro)

    except Exception as erro:
        st.error(erro)
       

elif menu == "Ver Saldo":
    st.header("Consultar Saldo")
    cpf_cliente = st.text_input("Digite seu CPF contendo apenas números. (ex: 12345678910)")

    try:
        if st.button("Ver Saldo"):
            saldo = bc.saldo(cpf_cliente)
            st.metric(label="Seu Saldo Atual", value=f"R$ {saldo:.2f}")
            
    except ValueError as erro_conta_não_encontrada:
        st.error(erro_conta_não_encontrada)

        
# elif menu == "Extrato de Transações":
#     st.header( "Consultar Extrato")
#     numero_da_conta = st.text_input("Digite o número da sua conta") 
    
#     try:
#         if st.button("Ver Extrato"):
#             bc.le_extrato(numero_da_conta)

#     except Exception as erro:
#         st.error(erro)