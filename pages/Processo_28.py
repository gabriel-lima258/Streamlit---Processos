from pathlib import Path
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Processo dos 28",
    layout="wide"
)

# Caminho do Excel
pasta_datasets = Path(__file__).parent.parent / 'processos'
arquivo_excel = pasta_datasets / 'PLANILHA UNIFICADA.xlsx'
df_gifa = pd.read_excel(arquivo_excel, dtype={'CPF': str, 'ID': str})

nome_arquivo = arquivo_excel.name.replace('.xlsx', '')

st.markdown(f"# 📁 Processo - {nome_arquivo}")
st.markdown("---")

# Toggle para exibir ou ocultar filtros e seleção de colunas
col_filtro, col_adicionar = st.columns(2)
mostrar_filtros = col_filtro.toggle("🔎 Ativar filtros e colunas", value=False)

# Colunas disponíveis
colunas = list(df_gifa.columns)

# Variáveis padrão
colunas_selecionadas = colunas
df_resultado = df_gifa # mostra tudo por padrão

# Exibir filtros e seleção de colunas
if mostrar_filtros:

    st.markdown("---")
    st.markdown("### Filtros")

    # Seleção de colunas
    colunas_selecionadas = st.multiselect(
        '📌 Selecione as colunas a serem exibidas:',
        colunas,
        default=colunas
    )

    col1, col2 = st.columns(2)
    col_filtro = col1.selectbox('Coluna para filtrar:', colunas)
    valor_filtro = col2.selectbox('Valor para filtrar:', list(df_gifa[col_filtro].unique()))

    btn1, btn2 = st.columns(2)
    status_filtrar = btn1.button('Filtrar')
    status_limpar = btn2.button('Limpar')

    st.markdown("---")

    # Aplica filtros se necessário
    if status_filtrar:
        df_resultado = df_gifa.loc[df_gifa[col_filtro] == valor_filtro, colunas_selecionadas]
    elif status_limpar:
        df_resultado = df_gifa[colunas_selecionadas]
    else:
        df_resultado = df_gifa[colunas_selecionadas]
else:
    # Quando toggle está desligado, mostra todas as colunas
    df_resultado = df_gifa

# Exibe a tabela final
st.markdown("## 📊 Resultado")
st.dataframe(df_resultado, height=1000, column_config={
                 "DATA": st.column_config.DateColumn(
                     "DATA", 
                     format="DD/MM/YYYY",
                 ),
        
             })
