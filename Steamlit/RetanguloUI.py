import streamlit as st
from Retangulo import Retangulo

class RetanguloUI:
    def main():
        st.header("Calcular Retangulo")
        b = st.text_input("Base")
        h = st.text_input("Altura")
        if st.button("Calcular"):
            r = Retangulo(float(b), float(h))
            st.write(r)
            st.write(f"Área = {r.calc_area()}")
            st.write(f"Diagonal = {r.calc_diagonal()}")