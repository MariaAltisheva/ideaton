import streamlit as st

st.title("Финансовый отчет компании ООО 'Гидрогазкомплект' за 2021 год")
st.write("""Данные предоставлены с сайта nalog.ru""")

st.markdown("""
<embed src="./data/2021.pdf" width="800" height="1200">""", unsafe_allow_html=True)
