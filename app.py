import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração de página
st.set_page_config(layout="wide")

# Criando os dados manualmente
data = {
    "Bairro": ["Centro", "Ocupação Valinhos", "Vila Rodrigues"],
    "Escolas Próximas": [14, 4, 11],
    "Tempo a Pé Escolas (min)": [8.6, 29.25, 8.18],
    "Tempo de Carro Escolas (min)": [4.5, 6.25, 1.81],
    "Distância Média Escolas (m)": [1050, 2200, 628],
    "Hospitais": [5, 4, 4],
    "Tempo a Pé Hospitais (min)": [12, 86, 21.25],
    "Tempo de Carro Hospitais (min)": [4.6, 14.5, 8],
    "Distância Média Hospitais (m)": [840, 6200, 1537],
    "Praças Públicas": [5, 1, 3],
    "Tempo a Pé Lazer (min)": [7, 57, 11],
    "Tempo de Carro Lazer (min)": [2.6, 8, 3.33],
    "Distância Média Lazer (m)": [524.6, 4100, 780],
    "Valor Médio Aluguel (R$)": [1500, 800, 1200],
    "Número de Ônibus": [12, 4, 6],
    "Tempo Médio Espera Ônibus (min)": [10, 25, 15]
}

# Convertendo para DataFrame
df = pd.DataFrame(data)

# Criando um índice de facilidade de acesso (média ponderada)
df["Índice de Acesso"] = (
    df["Escolas Próximas"] * 0.3 +
    df["Hospitais"] * 0.3 +
    df["Praças Públicas"] * 0.2 -
    (df["Tempo a Pé Escolas (min)"] + df["Tempo a Pé Hospitais (min)"] + df["Tempo a Pé Lazer (min)"]) * 0.05 -
    (df["Distância Média Escolas (m)"] + df["Distância Média Hospitais (m)"] + df["Distância Média Lazer (m)"]) * 0.0005
)

# Aplicando estilo escuro
st.markdown("""
    <style>
        body {
            background-color: black;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Título do App
st.title("Comparação de Acesso aos Serviços por Bairro")

# Filtro para escolher a métrica de comparação
opcoes = ["Distância Média", "Tempo a Pé", "Tempo de Carro"]
escolha = st.radio("Escolha o tipo de comparação:", opcoes, horizontal=True)

# Função para criar gráficos
def criar_grafico(colunas, titulo):
    df_plot = df.melt(id_vars=["Bairro"], value_vars=colunas, var_name="Métrica", value_name="Valor")
    fig = px.bar(df_plot, x="Bairro", y="Valor", color="Métrica", barmode="group", title=titulo)
    st.plotly_chart(fig, use_container_width=True)

# Gráficos de comparação
if escolha == "Distância Média":
    criar_grafico(["Distância Média Escolas (m)", "Distância Média Hospitais (m)", "Distância Média Lazer (m)"], "Distância Média até Serviços")
elif escolha == "Tempo a Pé":
    criar_grafico(["Tempo a Pé Escolas (min)", "Tempo a Pé Hospitais (min)", "Tempo a Pé Lazer (min)"], "Tempo a Pé até Serviços")
elif escolha == "Tempo de Carro":
    criar_grafico(["Tempo de Carro Escolas (min)", "Tempo de Carro Hospitais (min)", "Tempo de Carro Lazer (min)"], "Tempo de Carro até Serviços")

# Exibir Índice de Acesso
st.subheader("Índice de Facilidade de Acesso por Bairro")
st.dataframe(df[["Bairro", "Índice de Acesso"]])

# Gráfico do índice de acesso
fig_indice = px.bar(df, x="Bairro", y="Índice de Acesso", title="Índice de Facilidade de Acesso")
st.plotly_chart(fig_indice, use_container_width=True)

# Gráfico de comparação do valor médio do aluguel
st.subheader("Comparação do Valor Médio dos Aluguéis por Bairro")
fig_aluguel = px.bar(df, x="Bairro", y="Valor Médio Aluguel (R$)", title="Valor Médio do Aluguel")
st.plotly_chart(fig_aluguel, use_container_width=True)

# Gráfico comparando o número de ônibus e tempo médio de espera
st.subheader("Comparação do Número de Ônibus e Tempo Médio de Espera")
df_onibus = df.melt(id_vars=["Bairro"], value_vars=["Número de Ônibus", "Tempo Médio Espera Ônibus (min)"], var_name="Métrica", value_name="Valor")
fig_onibus = px.bar(df_onibus, x="Bairro", y="Valor", color="Métrica", barmode="group", title="Número de Ônibus e Tempo de Espera")
st.plotly_chart(fig_onibus, use_container_width=True)
