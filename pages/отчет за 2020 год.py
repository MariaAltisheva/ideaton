import streamlit

st.title("Финансовый отчет компании ООО 'Гидрогазкомплект' за 2020 год")
st.write("""Данные предоставлены с сайта nalog.ru""")

streamlit.markdown("""
<embed src="https://bo.nalog.ru/download/bfo/pdf/1747362?period=2020" width="800" height="1200">""", unsafe_allow_html=True)
