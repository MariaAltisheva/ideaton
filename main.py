import io
from io import StringIO

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from urllib.request import urlopen
import json
from PIL import Image


# Настройка заголовка и текста
st.title("Идеатон X-Mas Hacks")
st.write("""Оптимизация финансов компании""")
st.write("""Проект разработан командой участников: Алтышева Мария, Наумов Константин, Шилкин Александр""")

# Настройка боковой панели
st.sidebar.title("Python-forever")

