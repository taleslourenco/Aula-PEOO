import streamlit as st
import View

class ClienteUI:
    @staticmethod
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

    @staticmethod
    def Listar():
        clientes = View.cliente_listar()
        df = [{"ID": c.id, "Nome": c.nome, "Email": c.email, "Fone": c.fone} for c in clientes]
        st.dataframe(df)  
    
    @staticmethod
    def Inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")

        if st.button("Inserir"):
            View.cliente_inserir(nome, email, fone)

    @staticmethod
    def Atualizar():
        id = st.selectbox("Atualização de Clientes", View.cliente_listar())
        nome = st.text_input("Informe o novo nome")
        email = st.text_input("Informe o novo e-mail")
        fone = st.text_input("Informe o novo fone")

        if st.button("Atualizar"):
            View.cliente_atualizar(id, nome, email, fone)
    
    @staticmethod
    def Excluir():
        id = st.selectbox("Exclusão de Clientes", View.cliente_listar())
        if st.button("Excluir"):
            View.cliente_excluir(id)
