import streamlit as st
from Templates.manterClienteUI import ManterClienteUI 
from Templates.manterHorarioUI import ManterHorarioUI
from Templates.manterServicoUI import ManterServicoUI

class IndexUI:
    def main():
        st.sidebar.title("Menu")
        opcao = st.sidebar.selectbox("Selecione uma opção", ["Cadastro de Clientes", "Cadastro de Horários", "Cadastro de Serviços"])
        if opcao == "Cadastro de Clientes":
            ManterClienteUI.main()
        if opcao == "Cadastro de Horários":
            ManterHorarioUI.main()
        if opcao == "Cadastro de Serviços":
            ManterServicoUI.main()
        
IndexUI.main()