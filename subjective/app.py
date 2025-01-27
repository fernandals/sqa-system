import sys
import os

import streamlit as st

# utils path correction
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)

from utils.data_handler import DataHandler

st.set_page_config(
    page_title="Avaliação de Qualidade de Fala",
    page_icon=":loud_sound:",
    initial_sidebar_state="collapsed",
)

st.title("🗣️ Teste de Síntese de Fala: Avaliação Subjetiva")

st.markdown(
    """
    ### 🎧 Sua opinião é essencial!

    Estamos testando modelos de **conversão de texto em fala (TTS)** e sua avaliação subjetiva é fundamental para medir a qualidade das vozes geradas. Durante o experimento, você participará de **três testes diferentes**:

    1️⃣ **Qualidade**: Você avaliará a **qualidade** dos áudios sintéticos.  
    2️⃣ **Similaridade**: Você comparará a voz do áudio sintético com a do locutor original para medir o quão semelhantes elas são.  
    3️⃣ **Inteligibilidade**: Você ouvirá um áudio sintético e deverá transcrever o que foi dito, ajudando a medir a clareza da fala gerada.  

    Sua opinião sincera é essencial para aperfeiçoarmos a naturalidade e inteligibilidade dos modelos! 🚀  

    Este teste faz parte de uma pesquisa na área de aprendizado profundo em fala na **Universidade Federal do Rio Grande do Norte (UFRN)** e contribuirá para avanços no campo. 🎓  
    """
)

# blank header as divider
st.text("")

l, m, r = st.columns(3)
if m.button("Iniciar Teste ▶️", use_container_width=True):
    if "data_handler" not in st.session_state:
        st.session_state.data_handler = DataHandler()

    st.switch_page("pages/quality.py")
