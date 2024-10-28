import streamlit as st

class IndexUI:
    def main():
        st.sidebar.title("Menu")
        opcao = st.sidebar.selectbox("Selecione uma opção", ["Cadastro de Clientes", "Cadastro de Horários", "Cadastro de Serviços", "Abrir Agenda do Dia"])
        if opcao == "Cadastro de Clientes":
            st.page_link("ManterClienteUI.py")
        if opcao == "Cadastro de Horários":
            st.page_link("ManterHorarioUI.py")
        if opcao == "Cadastro de Serviços":
            st.page_link("ManterServicoUI.py")
        
IndexUI.main()
    