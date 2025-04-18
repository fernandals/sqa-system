import streamlit as st
import random

st.set_page_config(
    page_title="Avaliação de Qualidade de Fala",
    page_icon=":loud_sound:",
    initial_sidebar_state="collapsed",
)

handler = st.session_state.data_handler

st.title("🗣️ Avaliação de Inteligibilidade de Áudio")

st.text(f"ID do participante: {handler.participant_id}")

st.markdown(
    """
    Neste teste, você avaliará a **inteligibilidade** de áudios sintetizados, ou seja, quão bem podemos compreender o conteúdo falado.  

    #### 📝 Como funciona?  
    1️⃣ **Ouça o áudio por completo** antes de fazer sua avaliação.  
    2️⃣ **Digite a transcrição** do que você conseguiu entender no campo de texto.  
    3️⃣ Sua transcrição será comparada ao texto original para medir a precisão do áudio.  

    Esse teste ajuda a verificar se o áudio sintetizado é claro e compreensível.  
    """
)

st.header("Transcrição das Amostras")

# Selecionando 20 amostras aleatoriamente
if "selected_samples" not in st.session_state:
    st.session_state.selected_samples = random.sample(handler.audio_files, min(20, len(handler.audio_files)))

selected_samples = st.session_state.selected_samples  

responses = []

for i, file in enumerate(selected_samples):
    st.subheader(f"Amostra {i+1}")

    response_data = {
        'participant_id': handler.participant_id,
        'model_id': handler.balanced_model_list[i],
        'audio_id': file['audio_id'],
        'test_type': 'intelligibility',
        'response': None  # será preenchido com a transcrição do usuário
    }

    sin_audio_path = f"dataset/{handler.balanced_model_list[i]}/{file['audio_id']}.wav"

    st.audio(sin_audio_path, format="audio/wav")

    st.write("**Ouça atentamente o áudio e digite o texto que você conseguiu compreender.**")

    transcription = st.text_area(f"Transcrição do áudio sintético (Amostra {i+1})", key=f"trans_{i}")

    response_data['response'] = transcription

    responses.append(response_data)

    st.write("---")

st.write("Após preencher todas as respostas, clique abaixo para salvar e encerrar o teste.")

l, m, r = st.columns(3)
if m.button("Finalizar Teste", use_container_width=True):
    handler.save_response(responses)
    st.switch_page("pages/end.py")