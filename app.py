import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('heart.csv')

# Substituir códigos por rótulos legíveis
df['sex'] = df['sex'].map({0: 'Feminino', 1: 'Masculino'})
df['cp'] = df['cp'].map({
    0: 'Angina típica',
    1: 'Angina atípica',
    2: 'Dor não anginosa',
    3: 'Assintomático'
})
df['fbs'] = df['fbs'].map({0: '≤ 120 mg/dl', 1: '> 120 mg/dl'})
df['restecg'] = df['restecg'].map({
    0: 'Normal',
    1: 'Anomalia de ST-T',
    2: 'Hipertrofia ventricular esquerda'
})
df['exang'] = df['exang'].map({0: 'Não', 1: 'Sim'})
df['slope'] = df['slope'].map({
    0: 'Ascendente',
    1: 'Plano',
    2: 'Descendente'
})
df['thal'] = df['thal'].map({
    0: 'Desconhecido',
    1: 'Normal',
    2: 'Defeito fixo',
    3: 'Defeito reversível'
})
df['target'] = df['target'].map({0: 'Não possui doença', 1: 'Possui doença'})

st.title('Dashboard - Doença Cardíaca (Heart Disease)')

# Gráfico de barras
st.subheader("Distribuição por Gênero")
fig1 = px.histogram(df, x='sex', color='target', barmode='group', labels={'sex': 'Sexo', 'target': 'Doença Cardíaca'})
st.plotly_chart(fig1)

# Gráfico de dispersão
st.subheader("Idade vs Colesterol")
fig2 = px.scatter(df, x='age', y='chol', color='target', labels={'chol': 'Colesterol', 'target': 'Doença Cardíaca'})
st.plotly_chart(fig2)

# Filtro interativo
st.subheader("Filtrar por idade mínima")
idade = st.slider('Escolha a idade mínima', int(df['age'].min()), int(df['age'].max()), 30)
df_filtrado = df[df['age'] >= idade]
st.write(df_filtrado)
