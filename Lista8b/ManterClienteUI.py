import streamlit as st
import View
import CRUD

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
        clientes = View.cliente_listar()
        ids = [c.id for c in clientes]

    
        id = st.selectbox("Selecione o ID do cliente", ids, key="atualizar_cliente_id")
        cliente = CRUD.listar_id(id)

        nome = st.text_input("Nome", cliente.nome, key="atualizar_nome")
        email = st.text_input("Email", cliente.email, key="atualizar_email")
        fone = st.text_input("Telefone", cliente.fone, key="atualizar_fone")

        if st.button("Atualizar", key="btn_atualizar"):
         View.cliente_atualizar(nome, email, fone)
    
    @staticmethod
    def Excluir():
        id = st.selectbox("Exclusão de Clientes", View.cliente_listar())
        if st.button("Excluir"):
            View.cliente_excluir(id)
