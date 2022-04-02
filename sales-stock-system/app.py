import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import pyfiglet
from dashboard.config import set_streamlit, set_page_style
from dbutils.CRUDfuncs import dbtest

title = pyfiglet.figlet_format('loja')
PAGES = {
    "CONSULTAR": 'consulta',
    "CADASTRAR": 'cadastro',
    "ATUALIZAR": 'atualização',
    "DELETAR": 'deleção'
}

def main():
    # Streamlit Config
    set_streamlit()
    set_page_style()
    st.text(title)
    st.sidebar.title('Navegação')
    selection = st.sidebar.radio("Selecionar", list(PAGES.keys()))
    with st.spinner(f"Carregando paǵina ..."):
        st.write(f'Tela de {PAGES[selection]}')

if __name__ == "__main__":
    main()
    dbtest()
