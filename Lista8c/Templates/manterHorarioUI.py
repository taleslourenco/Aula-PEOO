import streamlit as st
import pandas as pd
from Lista8c.View import View

class ManterHorarioUI:
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()

    def listar():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in horarios: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        data = st.text_input("Informe a data da consulta")
        if st.button("Inserir"):
            View.horario_inserir(data)
            st.rerun()

    def atualizar():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Atualização de horários", horarios)
            data = st.text_input("Informe a nova data", op.data)
            if st.button("Atualizar"):
                View.horario_atualizar(op.id, data)
                st.rerun()

    def excluir():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Exclusão de horários", horarios)
            if st.button("Excluir"):
                View.horario_excluir(op.id)
                st.rerun()