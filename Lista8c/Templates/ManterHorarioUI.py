import streamlit as st
import pandas as pd
from View import View

class ManterHorarioUI:
    def main():
        st.header("Cadastro de Horarios")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()

    def listar():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horario cadastrado")
        else:
            dic = []
            for obj in horarios: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        data = st.text_input("Informe a data da consulta")
        confirmado = st.button("Confirmar")
        id_cliente = st.text_input("Informe o ID do cliente")
        id_servico = st.text_input("Informe o ID do serviço")
        if st.button("Inserir"):
            View.horario_inserir(data, confirmado, id_cliente, id_servico)
            st.rerun()

    def atualizar():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Atualização de horarios", horarios)
            data = st.text_input("Informe o novo nome do cliente", op.nome)
            confirmado = st.button("Confirmado")
            id_cliente = st.text_input("Informe o novo e-mail", op.email)
            id_servico = st.text_input("Informe o novo fone", op.fone)
            if st.button("Atualizar"):
                View.horario_atualizar(op.id, data, confirmado, id_cliente, id_servico)
                st.rerun()

    def excluir():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horario cadastrado")
        else:
            op = st.selectbox("Exclusão de horarios", horarios)
            if st.button("Excluir"):
                View.horario_excluir(op.id)
                st.rerun()