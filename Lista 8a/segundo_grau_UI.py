import streamlit as st
from segundo_grau import Bhaskara

class segundograuUI:
    def main():
        st.header("Equação do II Grau | Fórmula de Bhaskara")
        a = st.text_input("Valor de A")
        b = st.text_input("Valor de B")
        c = st.text_input("Valor de C")
        
        if st.button("Calcular"):
            b = Bhaskara(float(a), float(b), float(c))
            st.write(b)
            st.write(f"Delta = {b.calc_delta}")
            st.write(f"Raizes (x1, x2) = {b.calc_raizes}")
        
