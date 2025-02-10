import streamlit as st
import random

st.set_page_config(
    page_title="Avaliação de Qualidade de Fala",
    page_icon=":loud_sound:",
    initial_sidebar_state="collapsed",
)

handler = st.session_state.data_handler

st.title("🎧 Avaliação da Qualidade de Áudio")

st.text(f"ID do participante: {handler.participant_id}")

st.markdown(
    """
    Neste teste, você avaliará a **qualidade perceptiva** de áudios sintetizados usando a métrica **Mean Opinion Score (MOS)**, amplamente utilizada para medir a naturalidade e inteligibilidade de sistemas de conversão de texto em fala (TTS).  

    #### 📝 Como funciona?  
    1️⃣ **Ouça o áudio por completo** antes de fazer sua avaliação.  
    2️⃣ Selecione a opção que melhor representa sua percepção da qualidade do áudio.  

    As opções de avaliação seguem a escala MOS:  

    ⭐ **1 - Péssima qualidade**: Áudio com distorções ou difícil de entender.  
    ⭐ **2 - Baixa qualidade**: Áudio com falhas perceptíveis.  
    ⭐ **3 - Qualidade razoável**: Áudio compreensível, mas com imperfeições notáveis.  
    ⭐ **4 - Boa qualidade**: Áudio natural e claro, com pequenas falhas.  
    ⭐ **5 - Excelente qualidade**: Áudio muito próximo à voz humana real, sem distorções.  
    """
)

st.header("Avaliação das Amostras")

# selecionando 20 amostras aleatoriamente
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
        'test_type': 'mos',
        'response': None  # será preenchido com base na avaliação
    }

    audio_path = f"../datasets/{handler.balanced_model_list[i]}/{file['audio_id']}.wav"
    st.audio(audio_path, format="audio/wav")

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

    responses.append(response_data)

    st.write("---")

st.write("Após preencher todas as respostas, clique abaixo para salvar e ir para o próximo teste.")

l, m, r = st.columns(3)
if m.button("Próximo Teste", use_container_width=True):
    handler.save_response(responses)

    st.switch_page("pages/similarity.py")

