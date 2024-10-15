import streamlit as st
import pandas as pd
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
            st.write(f"Delta = {b.calc_delta()}")
            st.write(f"Raizes (x1, x2) = {b.calc_raizes()}")

            xmin = 5
            xmax = 15
            n = 150
            d = (xmax - xmin)/n  # 0.5
            px = []
            py = []
            x = xmin
            while x < xmax:
                y = x**2 - 5*x + 6
                px.append(x)
                py.append(y)
                x = x + d
            x = xmax
            y = x**2 - 5*x + 6
            px.append(x)
            py.append(y)

            dic = { "x" : px, "y" : py }
            chart_data = pd.DataFrame(dic)
            st.line_chart(chart_data, x = "x", y = "y") 
       

        
