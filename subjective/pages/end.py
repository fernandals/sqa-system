import streamlit as st

st.set_page_config(
    page_title="Avaliação de Qualidade de Fala",
    page_icon=":loud_sound:",
    initial_sidebar_state="collapsed",
)

st.title("🎉 Obrigado pela Sua Participação!")

st.markdown(
    """
    **Sua contribuição foi fundamental!** 🙏

    A sua participação neste teste é de extrema importância para o avanço das pesquisas na área de conversão de texto-fala (TTS). Ao compartilhar suas avaliações sobre os áudios sintetizados, você ajudou a melhorar a qualidade, a naturalidade e a inteligibilidade dos sistemas de síntese de fala. 🚀

    **O que acontece a seguir?**  
    Seus dados serão analisados para ajudar na melhoria dos modelos de TTS, contribuindo diretamente para o desenvolvimento de tecnologias de fala mais precisas e naturais. A sua opinião está fazendo a diferença

    Fique atento às novidades e, caso deseje, acompanhe os próximos passos dessa pesquisa! 📚
    """
)

st.write("Se você tiver mais perguntas ou quiser saber mais sobre a pesquisa, não hesite em nos contatar!")

st.write("---")

# Coleta de dados adicionais (Idade e Ocupação)
st.markdown(
    """
    **Antes de finalizar, gostaríamos de saber um pouco mais sobre você.**  
    Essas informações serão usadas para análise de métricas da pesquisa e são completamente confidenciais. 
    Por favor, preencha os campos abaixo:
    """
)

col1, col2 = st.columns(2)

with col1:
    age = st.text_input("Qual a sua idade?", key="age")
    specialist = st.checkbox("Trabalha na área de processamento de fala?", key="specialist")

with col2:
    occupation = st.text_input("Qual a sua ocupação?", key="occupation")

    st.button(
        "Submeter",
        on_click=st.session_state.data_handler.save_participant_info,
        args=(st.session_state.data_handler.participant_id, age, occupation),
        use_container_width=True
    )

st.write("---")

l, m, r = st.columns(3)
m.button("Sair", on_click=lambda: st.stop(), use_container_width=True)
