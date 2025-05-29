import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np

# Configuração da página
st.set_page_config(page_title="Painel da Merenda Escolar", layout="wide")
st.title("🍽️ Painel de Otimização da Merenda Escolar")
st.markdown("Envie o arquivo CSV com os dados de presença e consumo de alimentos.")

# Upload do CSV
arquivo = st.file_uploader("📂 Envie o arquivo CSV com os dados da merenda", type=["csv"])

if arquivo:
    df = pd.read_csv(arquivo)

    # Verifica se as colunas obrigatórias existem
    colunas_necessarias = ["Dia", "Ano", "Alunos Presentes", "Alimento Preparado (kg)", "Alimento Consumido (kg)"]
    if not all(col in df.columns for col in colunas_necessarias):
        st.error("⚠️ O arquivo CSV deve conter as colunas: " + ", ".join(colunas_necessarias))
    else:
        # Cálculos
        df["Desperdício (kg)"] = df["Alimento Preparado (kg)"] - df["Alimento Consumido (kg)"]

        # MODELO DE IA - REGRESSÃO LINEAR
        X = df[["Alunos Presentes"]]
        y = df["Alimento Consumido (kg)"]
        modelo = LinearRegression()
        modelo.fit(X, y)
        df["Preparo Ideal (kg)"] = modelo.predict(X)

        # Sidebar
        st.sidebar.header("🔧 Filtros")
        ano_selecionado = st.sidebar.selectbox("Selecione o ano:", sorted(df["Ano"].unique()))
        df_ano = df[df["Ano"] == ano_selecionado]

        dias_disponiveis = df_ano["Dia"].tolist()
        dias_selecionados = st.sidebar.slider("Selecionar intervalo de dias:", min(dias_disponiveis), max(dias_disponiveis), (min(dias_disponiveis), max(dias_disponiveis)))
        df_filtrado = df_ano[(df_ano["Dia"] >= dias_selecionados[0]) & (df_ano["Dia"] <= dias_selecionados[1])]

        # Previsão interativa
        st.sidebar.markdown("## Previsão Inteligente")
        alunos_input = st.sidebar.number_input("Número de alunos presentes hoje:", min_value=0, max_value=1000, value=400)
        previsao = modelo.predict(np.array([[alunos_input]]))[0]
        st.sidebar.success(f"Preparo ideal: **{previsao:.2f} kg**")

        # Mostrar equação
        st.sidebar.markdown("---")
        st.sidebar.markdown("### 📈 Equação preditiva")
        st.sidebar.code(f"Consumo = {modelo.coef_[0]:.3f} * Alunos + {modelo.intercept_:.2f}")

        # Gráfico 1
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=df_filtrado["Dia"], y=df_filtrado["Alunos Presentes"], name="Alunos Presentes", mode='lines+markers'))
        fig1.add_trace(go.Scatter(x=df_filtrado["Dia"], y=df_filtrado["Alimento Consumido (kg)"], name="Consumido", mode='lines+markers'))
        fig1.add_trace(go.Scatter(x=df_filtrado["Dia"], y=df_filtrado["Alimento Preparado (kg)"], name="Preparado", mode='lines+markers'))
        fig1.update_layout(title="Presença, Consumo e Preparo")

        # Gráfico 2
        fig2 = px.bar(df_filtrado, x="Dia", y="Desperdício (kg)", color="Desperdício (kg)",
                      title="Desperdício por Dia", color_continuous_scale="RdYlGn_r")

        # Gráfico 3
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=df_filtrado["Dia"], y=df_filtrado["Preparo Ideal (kg)"], name="Preparo Ideal", mode='lines+markers'))
        fig3.add_trace(go.Scatter(x=df_filtrado["Dia"], y=df_filtrado["Alimento Preparado (kg)"], name="Preparado Real", mode='lines+markers'))
        fig3.update_layout(title="Preparo Ideal vs Real")

        # Layout dos gráficos
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig1, use_container_width=True)
        with col2:
            st.plotly_chart(fig2, use_container_width=True)

        st.plotly_chart(fig3, use_container_width=True)

        # Tabela
        with st.expander("📊 Ver dados detalhados"):
             st.dataframe(df_filtrado.style.format({
        "Alimento Preparado (kg)": "{:.2f}",
        "Alimento Consumido (kg)": "{:.2f}",
        "Desperdício (kg)": "{:.2f}",
        "Preparo Ideal (kg)": "{:.2f}",
    }))
    
else:
    st.info("📌 Por favor, envie um arquivo CSV para iniciar a análise.")

# Rodapé
st.markdown("""
    <style>
    .rodape {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: #fff;
        font-weight:500;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    </style>

    <div class="rodape">
        Desenvolvido por Guilherme Soares
    </div>
""", unsafe_allow_html=True)