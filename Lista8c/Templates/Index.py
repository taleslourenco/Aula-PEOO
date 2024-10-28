import streamlit as st
import ManterClienteUI, ManterHorarioUI, ManterServicoUI

class IndexUI:
    def main():
        st.sidebar.title("Menu")
        opcao = st.sidebar.selectbox("Selecione uma opção", ["Cadastro de Clientes", "Cadastro de Horários", "Cadastro de Serviços", "Abrir Agenda do Dia"])
        if st.selectbox("Cadastro de Clientes", opcao):
            ManterClienteUI.ManterClienteUI.main()
        if st.selectbox("Cadastro de Horários", opcao):
            ManterHorarioUI.ManterHorarioUI.main()
        if st.selectbox("Cadastro de Serviços", opcao):
            ManterServicoUI.ManterServicoUI.main()
        
IndexUI.main()
    