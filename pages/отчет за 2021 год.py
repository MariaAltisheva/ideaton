import base64

import streamlit as st

st.title("Финансовый отчет компании ООО 'Гидрогазкомплект' за 2021 год")
st.write("""Данные предоставлены с сайта nalog.ru""")


def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)

show_pdf("2021.pdf")
