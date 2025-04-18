import streamlit as st
import random

st.set_page_config(
    page_title="Avaliação de Qualidade de Fala",
    page_icon=":loud_sound:",
    initial_sidebar_state="collapsed",
)

handler = st.session_state.data_handler

st.title("🎙️ Avaliação de Similaridade de Locutor")

st.text(f"ID do participante: {handler.participant_id}")

st.markdown(
    """
    Neste teste, você avaliará o **grau de similaridade** entre a voz de um locutor original (natural) e a voz gerada por um sistema de síntese de fala.  

    #### 📝 Como funciona?  
    1️⃣ **Ouça os dois áudios por completo** antes de fazer sua avaliação.  
    2️⃣ Compare as características vocais, como tom, ritmo e clareza.  
    3️⃣ Selecione a opção que melhor representa sua percepção de similaridade.  

    As opções de avaliação seguem a escala abaixo:  

    ⭐ **1 - Nada semelhante**: As vozes são completamente diferentes.  
    ⭐ **2 - Pouco semelhante**: Algumas características são parecidas, mas há diferenças marcantes.  
    ⭐ **3 - Moderadamente semelhante**: A voz tem semelhanças, porém ainda notam-se diferenças.  
    ⭐ **4 - Muito semelhante**: As vozes são bem parecidas.  
    ⭐ **5 - Quase idêntico**: A voz sintética é praticamente igual à original.  
    """
)

st.header("Comparação de Amostras")

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
        'test_type': 'similarity',
        'response': None  # será preenchido com base na avaliação
    }

    nat_audio_path = f"dataset/ground_truth/{file['audio_id']}.wav"
    sin_audio_path = f"dataset/{handler.balanced_model_list[i]}/{file['audio_id']}.wav"

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

    responses.append(response_data)

    st.write("---")

st.write("Após preencher todas as respostas, clique abaixo para salvar e ir para o próximo teste.")

l, m, r = st.columns(3)
if m.button("Próximo Teste", use_container_width=True):
    handler.save_response(responses)
    st.switch_page("pages/intelligibility.py")
