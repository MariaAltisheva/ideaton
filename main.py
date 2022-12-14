import io
from io import StringIO

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from urllib.request import urlopen
import json
from PIL import Image
import base64

# Настройка заголовка и текста
st.title("Идеатон X-Mas Hacks")
st.write("""Оптимизация финансов компании""")
st.write("""Проект разработан командой участников:""")
st.write("""Алтышева Мария""")
st.write("""Наумов Константин""")
st.write("""Шилкин Александр""")

# Настройка боковой панели
st.sidebar.title("Python-forever")

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('theme_15.png')

