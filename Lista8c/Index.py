import streamlit as st
from Lista8c.Templates.manterClienteUI import ManterClienteUI 
from Lista8c.Templates.manterHorarioUI import ManterHorarioUI
from Lista8c.Templates.manterServicoUI import ManterServicoUI

class IndexUI:
    def main():
        st.sidebar.title("Menu")
        opcao = st.sidebar.selectbox("Selecione uma opção", ["Cadastro de Clientes", "Cadastro de Horários", "Cadastro de Serviços", "Abrir Agenda do Dia"])
        if opcao("Cadastro de Clientes"):
            ManterClienteUI.ManterClienteUI.main()
        if opcao("Cadastro de Horários"):
            ManterHorarioUI.ManterHorarioUI.main()
        if opcao("Cadastro de Serviços"):
            ManterServicoUI.ManterServicoUI.main()
        
IndexUI.main()