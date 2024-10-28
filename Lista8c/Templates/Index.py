import streamlit as st

class IndexUI:
    def main():
        st.sidebar.title("Menu")
        opcao = st.sidebar.selectbox("Selecione uma opção", ["Cadastro de Clientes", "Cadastro de Horários", "Cadastro de Serviços", "Abrir Agenda do Dia"])
        if opcao("Cadastro de Clientes"):
            ManterClienteUI.ManterClienteUI.main()
        
        
IndexUI.main()