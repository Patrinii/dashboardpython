import streamlit as st
import pandas as pd
import plotly.express as px

# Dados
data = {
    "Código": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Nome": ["Amostra 1", "Amostra 2", "Amostra 3", "Amostra 4", "Amostra 5", "Amostra 6", "Amostra 7", "Amostra 8", "Amostra 9", "Amostra 10"],
    "Latitude": [-19.6697480, -19.6696909, -19.6701963, -19.6698424, -19.6698787, -19.6696603, -19.6763258, -19.6761095, -19.6761095, -19.6761095],
    "Longitude": [-43.2089288, -43.2088443, -43.2084782, -43.2097184, -43.2097365, -43.2096912, -43.2048361, -43.2050275, -43.2050275, -43.2050275],
    "pH": [6.61, 6.63, 6.54, 6.46, 6.32, 6.36, 6.20, 6.10, 6.16, 6.09],
    "Condutividade": [157.1, 93.1, 156.5, 154.1, 157.0, 89.3, 37.6, 68.9, 68.7, 68.7],
    "NaCl": [72.6, 42.7, 72.3, 71.3, 72.8, 41.2, 17.22, 31.7, 31.6, 31.6],
    "Turbidez": [5.33, 1000, 7.53, 50.8, 50.8, 1000, 29.0, 1000, 1000, 1000],
    "Acidez": [45, None, 10, 15, 10, None, 5, None, None, None],
    "Alcalinidade Total": [57.5, None, 47.5, 50, 85, None, 10, None, None, None]
}

df = pd.DataFrame(data)

# Configuração do Streamlit
st.title("Dashboard de Qualidade da Água")

# Gráfico 1: Mapa Geográfico
st.subheader("Mapa Geográfico")
mapa = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_name="Nome",
                         zoom=10, height=400, title="Localização das Amostras")
mapa.update_layout(mapbox_style="open-street-map")
st.plotly_chart(mapa)

# Gráfico 2: Comparação Geral
st.subheader("Comparação Geral: pH, Turbidez, Condutividade, NaCl, Acidez e Alcalinidade")
dados_combinados = df.melt(id_vars=["Nome"], value_vars=["pH", "Turbidez", "Condutividade", "NaCl", "Acidez", "Alcalinidade Total"])
grafico_comparacao_geral = px.bar(
    dados_combinados, x="Nome", y="value", color="variable",
    title="Comparação Geral de Parâmetros",
    labels={"value": "Valor", "variable": "Parâmetro", "Nome": "Amostra"}
)
st.plotly_chart(grafico_comparacao_geral)

# Gráfico 3: Comparação de pH e Acidez
st.subheader("Relação entre pH e Acidez")
grafico_ph_acidez = px.scatter(
    df, x="pH", y="Acidez", color="Nome",
    title="Comparação de pH e Acidez",
    labels={"pH": "pH", "Acidez": "Acidez (mg/L)"}
)
st.plotly_chart(grafico_ph_acidez)

# Gráfico 4: Comparação de Turbidez, Acidez e Alcalinidade Total
st.subheader("Comparação entre Turbidez, Acidez e Alcalinidade Total")
dados_turbidez = df.melt(id_vars=["Nome"], value_vars=["Turbidez", "Acidez", "Alcalinidade Total"])
grafico_turbidez = px.bar(
    dados_turbidez, x="Nome", y="value", color="variable",
    title="Turbidez, Acidez e Alcalinidade Total",
    labels={"value": "Valor", "variable": "Parâmetro", "Nome": "Amostra"}
)
st.plotly_chart(grafico_turbidez)
