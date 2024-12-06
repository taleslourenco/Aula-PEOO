import streamlit as st
import pandas as pd
from views import View
import time

class AbrirContaUI:
    def main():
        st.header("Abrir Conta no Sistema")
        AbrirContaUI.inserir()

    def inserir():
        perfis = View.perfil_listar()
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")
        perfil = st.selectbox("Informe o perfil do cliente", perfis, index = None)

        if st.button("Inserir"):
            View.cliente_inserir(nome, email, fone, senha, perfil.id)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()