import streamlit as st
import pandas as pd
from View import View

class ManterServicoUI:
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir()

    def listar():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            dic = []
            for obj in servicos: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        descricao = st.text_input("Informe uma descrição")
        valor = st.text_input("Informe o valor")
        duracao = st.text_input("Informe a duração")
        if st.button("Inserir"):
            View.horario_inserir(descricao, valor, duracao)
            st.rerun()

    def atualizar():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Atualização de serviços", servicos)
            descricao = st.text_input("Informe o novo nome do cliente", op.descricao)
            valor = st.text_input("Informe o novo e-mail", op.valor)
            duracao = st.text_input("Informe o novo fone", op.duracao)
            if st.button("Atualizar"):
                View.servico_atualizar(op.id, descricao, valor, duracao)
                st.rerun()

    def excluir():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Exclusão de serviços", servicos)
            if st.button("Excluir"):
                View.servico_excluir(op.id)
                st.rerun()