import streamlit as st
import base64

st.title("Финансовый отчет компании ООО 'Гидрогазкомплект' за 2020 год")
st.write("""Данные предоставлены с сайта nalog.ru""")

st.info("Если отчет не отображается, то посмотреть/скачать его можно по "
                "[ссылке](https://bo.nalog.ru/download/bfo/pdf/1747362?period=2020).")

def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)

show_pdf("2020.PDF")
