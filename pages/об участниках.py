import streamlit as st

from main import add_bg_from_local

st.title("Об участниках проекта")
st.write("Алтышева Мария - преподаватель программирования на Python, аспирант университета Росноу")
st.write("моб. +7(916)151-72-84")
st.write()

st.write("Константин Наумов - преподаватель информатики, магистр университета")
st.write("моб. ")
st.write()

st.write("Шилкин Александр - студент программы 'Код будущего' университета Синергия")
st.write("моб. +7(977)148-58-94")

add_bg_from_local('theme_15.png')
