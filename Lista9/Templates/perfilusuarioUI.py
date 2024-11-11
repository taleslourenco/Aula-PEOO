import streamlit as st
from views import View
import time


class perfilusuarioUI:
    def main():
        st.header("Gerenciar Perfil")
        perfilusuarioUI.perfil()

    def perfil():
        clientes = View.cliente_listar()
        if len(clientes) == 0: 
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Atualização de cliente", clientes)
            nome = st.text_input("Informe o novo nome do cliente", op.nome)
            email = st.text_input("Informe o novo e-mail", op.email)
            fone = st.text_input("Informe o novo fone", op.fone)
            senha = st.text_input("Informe a nova senha", op.senha, type="password")
            confsenha = st.text_input("Confirme a nova senha", type="password")
            if st.button("Atualizar"):
                View.cliente_atualizar(op.id, nome, email, fone, senha, confsenha)
                st.success("Cliente atualizado com sucesso")
                time.sleep(2)
                st.rerun()
