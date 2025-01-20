import streamlit as st
import random
from utils.data_handler import DataHandler

st.set_page_config(
    page_title="Avaliação de Qualidade de Fala",
    page_icon=":loud_sound:",
    initial_sidebar_state="collapsed",
)

# logica de seleção
data_handler = DataHandler()

test_types = ["MOS", "Inteligibilidade", "Proximidade do Locutor"]


st.write("# 🗣️ Teste de Síntese de Fala")

st.write(f"ID do participante: {data_handler.participant_id}")
st.write("### Avaliação das Amostras")

responses = [] 

for i, file in enumerate(data_handler.audio_files):
    st.write(f"#### Amostra {i+1}")
    
    test_choice = random.choice(test_types)

    response_data = {
        'participant_id': data_handler.participant_id,
        'audio_id': file['audio_id'],
        'test_type': test_choice,
        'response': None  # This will be filled based on the test type
    }

    if test_choice == "Proximidade do Locutor":
        nat_audio_path = f"datasets/ground_truth/{file['audio_id']}.wav"
        sin_audio_path = f"datasets/{data_handler.balanced_model_list[i]}/{file['audio_id']}.wav"

        col1, col2 = st.columns(2)

        with col1:
            st.audio(nat_audio_path, format="audio/wav")
            st.caption("Áudio Natural")            

        with col2:
            st.audio(sin_audio_path, format="audio/wav")
            st.caption("Áudio Sintético")

        similarity_options = [
            (1, "Nada semelhante"),
            (2, "Pouco semelhante"),
            (3, "Moderadamente semelhante"),
            (4, "Muito semelhante"),
            (5, "Quase idêntico")
        ]

        st.write("**Qual o grau de similaridade entre a voz do áudio sintético e a voz do áudio natural?** (Escala de 1 a 5)")

        selected_similarity = st.selectbox(
            f"Proximidade entre o áudio natural e sintético (Amostra {i+1})",
            options=[f"{num} - {desc}" for num, desc in similarity_options],
            key=f"sim_{i}"
        )

        selected_similarity_value = int(selected_similarity.split(" - ")[0])
        response_data['response'] = selected_similarity_value

    else:
        audio_path = f"datasets/{data_handler.balanced_model_list[i]}/{file["audio_id"]}.wav"
        st.audio(audio_path, format="audio/wav")

        if test_choice == "MOS":
            st.write("**Avalie a qualidade do áudio sintético em uma escala de 1 a 5** (MOS - Mean Opinion Score).")

            mos_options = [
                (1, "Péssima qualidade"),
                (2, "Baixa qualidade"),
                (3, "Qualidade razoável"),
                (4, "Boa qualidade"),
                (5, "Excelente qualidade")
            ]

            selected_mos = st.selectbox(
                f"Avalie a qualidade do áudio sintético (Amostra {i+1})",
                options=[f"{num} - {desc}" for num, desc in mos_options],
                key=f"mos_{i}"
            )    

            selected_mos_value = int(selected_mos.split(" - ")[0])
            response_data['response'] = selected_mos_value

        elif test_choice == "Inteligibilidade":
            st.write("**Ouça atentamente o áudio e digite o texto que você conseguiu compreender. Sua transcrição ajudará a avaliar a clareza e a precisão do áudio sintetizado.**")
            transcription = st.text_area(f"Transcrição do áudio sintético (Amostra {i+1})", key=f"trans_{i}")

            response_data['response'] = transcription

    responses.append(response_data)

    st.write("---")

st.write("Após preencher todas as respostas, clique abaixo para enviar.")

l, m, r = st.columns(3)
if m.button("Enviar Respostas", use_container_width=True):
    data_handler.save_response()


