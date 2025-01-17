import streamlit as st

st.set_page_config(
    page_title="Avaliação de Qualidade de Fala",
    page_icon=":loud_sound:",
    initial_sidebar_state="collapsed",
)

st.write("# 🗣️ Teste de Síntese de Fala: Avaliação Subjetiva")

st.markdown(
    """
    ### 🎧 Sua opinião é essencial!

    Estamos testando modelos de **conversão de texto em fala (TTS)** e sua avaliação subjetiva é fundamental para medir a qualidade das vozes geradas. Ouça os áudios atentamente e forneça sua opinião sincera. Sua contribuição ajudará a melhorar a naturalidade e inteligibilidade dos modelos! 🚀

    Este teste faz parte de uma pesquisa na área de aprendizado profundo em fala na **Universidade Federal do Rio Grande do Norte (UFRN)** e contribuirá para avanços no campo. 🎓
"""
)

# blank header as divider
st.write("###")

l, m, r = st.columns(3)
if m.button("Iniciar Teste ▶️", use_container_width=True):
    st.switch_page("pages/test.py")
