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

    A sua participação neste teste é de extrema importância para o avanço das pesquisas na área de conversão de texto em fala (TTS). Ao compartilhar suas avaliações sobre os áudios sintetizados, você ajudou a melhorar a qualidade, a naturalidade e a inteligibilidade dos sistemas de síntese de fala. 🚀

    **O que acontece a seguir?**  
    Seus dados serão analisados para ajudar na melhoria dos modelos de TTS, contribuindo diretamente para o desenvolvimento de tecnologias de fala mais precisas e naturais. A sua opinião está fazendo a diferença

    Fique atento às novidades e, caso deseje, acompanhe os próximos passos dessa pesquisa! 📚
    """
)

st.write("Se você tiver mais perguntas ou quiser saber mais sobre a pesquisa, não hesite em nos contatar!")

st.write("---")

st.button("Sair", on_click=lambda: st.stop())
