import streamlit as st

gifa = st.Page(
    page='pages/GIFA.py',
    title='GIFA',
    icon='🗂️',
    default=True
)

projeto_28 = st.Page(
    page='pages/Processo_28.py',
    title='Processo 28',
    icon='🗂️'
)

home = st.Page(
    page='pages/home.py',
    title='ChatGPT',
    icon='🤖'
)

pg = st.navigation({
    "ChatBot": [home],
    "Processos": [gifa, projeto_28]
}, position='sidebar')

pg.run()