import streamlit as st
import pandas as pd
from views import View
import time

class AlterarDadosUI:
    def main():
        st.header("Abrir Conta no Sistema")
        AlterarDadosUI.inserir()

    def atualizar():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Atualizar"):
            View.cliente_atualizar(nome, email, fone, senha)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()