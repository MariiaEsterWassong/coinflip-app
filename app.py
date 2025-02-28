import streamlit as st
import numpy as np
import pandas as pd

st.header('Tossing a Coin')

# 1️⃣ Ползунок для выбора количества бросков (от 1 до 1000, по умолчанию 10)
number_of_trials = st.slider('Number of trials?', 1, 1000, 10)

# 2️⃣ Кнопка запуска симуляции
start_button = st.button('Run')

if start_button:
    st.write(f'Running the experiment with {number_of_trials} trials...')

st.write('It is not a functional application yet. Under construction.')
