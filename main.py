import streamlit as st
from datetime import datetime

def calcular_senha_do_dia():
    hoje = datetime.now()
    senha_do_dia = hoje.day * hoje.month * int(str(hoje.year)[-2:]) * 3
    return senha_do_dia

senha = calcular_senha_do_dia()

# Define o tamanho do texto usando HTML
st.markdown(f"<h1 style='color: #FFF;'>Senha do Dia: {senha}</h1>", unsafe_allow_html=True)
st.markdown("[Builds Mobile](https://builds.unipluscdn.com/unimobile/)")
st.markdown("[Builds Uniplus](https://utilitarios.intelidata.inf.br/)")
st.markdown("[Wiki intelidata](https://centraldouniplus.intelidata.inf.br/)")


