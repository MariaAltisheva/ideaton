import streamlit as st


st.title("Финансовый отчет компании ООО 'Гидрогазкомплект' за 2019 год")
st.write("""Данные предоставлены с сайта nalog.ru""")



st.markdown("""
<embed src="https://bo.nalog.ru/download/bfo/pdf/1747362?period=2019" width="800" height="1200">""", unsafe_allow_html=True)
