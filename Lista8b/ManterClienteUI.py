import streamlit as st
import View
import pandas as pd

class ClienteUI:
    def main():
        st.header("Cadastro Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Inserir", "Listar", "Atualizar", "Excluir"])
        with tab1:
            ClienteUI.Inserir()
        with tab2:
            ClienteUI.Listar()
        with tab3:
            ClienteUI.Atualizar()
        with tab4:
            ClienteUI.Excluir()

    def Listar():
        data = {
        'ID': [1, 2, 3],
        'Nome': ['Alice', 'Bob', 'Charlie'],
        'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com'],
        'Fone': ['(11) 99999-0001', '(11) 88888-0002', '(11) 77777-0003']}
        df = pd.DataFrame(data)
        st.table(df)

    def Inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")

        if st.button("Inserir"):
            View.cliente_inserir(nome, email, fone)

    def Atualizar():
        id = st.selectbox("Atualização de Clientes", View.cliente_listar())
        nome = st.text_input("Informe o novo nome")
        email = st.text_input("Informe o novo e-mail")
        fone = st.text_input("Informe o novo fone")

        if st.button("Atualizar"):
            View.cliente_atualizar(id, nome, email, fone)
    
    def Excluir():
        id = st.selectbox("Exclusão de Clientes", View.cliente_listar())
        if st.button("Excluir"):
            View.cliente_excluir(id)