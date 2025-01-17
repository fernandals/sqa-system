import streamlit as st
from utils.data_handler import DataHandler

st.set_page_config(
    page_title="Avaliação de Qualidade de Fala",
    page_icon=":loud_sound:",
    initial_sidebar_state="collapsed",
)

data_handler = DataHandler()

st.write("# 🗣️ Teste de Síntese de Fala")

st.write(f"ID do participante: {data_handler.participant_id}")
st.write(f"Amostras balanceadas: {data_handler.balanced_model_list[:5]}") 
