import pandas as pd
import locale
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go



url = './bd-lojas/loja_1.csv'
url2 = './bd-lojas/loja_2.csv'
url3 = './bd-lojas/loja_3.csv'
url4 = './bd-lojas/loja_4.csv'
#url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
#url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
#url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
#url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

loja = pd.read_csv(url)
loja2 = pd.read_csv(url2)
loja3 = pd.read_csv(url3)
loja4 = pd.read_csv(url4)
# Análise do faturamento por loja  - Calcular a coluna Preço
 #Loja 01 --------------------------------------------------------------------------

loja.head()
faturamento_loja1 = loja['Preço'].sum()
format_faturamento_loja1 = f"R$ {faturamento_loja1:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


#Loja 02 --------------------------------------------------------------------------
loja2.head()
faturamento_loja2 = loja2['Preço'].sum()
format_faturamento_loja2 = f"R$ {faturamento_loja2:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


#Loja 03 --------------------------------------------------------------------------
loja3.head()
faturamento_loja3 = loja3['Preço'].sum()
format_faturamento_loja3 = f"R$ {faturamento_loja3:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

#Loja 04 --------------------------------------------------------------------------
loja4.head()
faturamento_loja4 = loja4['Preço'].sum()
format_faturamento_loja4 = f"R$ {faturamento_loja4:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

#-----------------------------------------------------------------------------------------------------------------

# vendas por categoria
venda_por_categoria_loja1 = loja['Categoria do Produto'].value_counts()

venda_por_categoria_loja2 = loja2['Categoria do Produto'].value_counts()

venda_por_categoria_loja3 = loja3['Categoria do Produto'].value_counts()

venda_por_categoria_loja4 = loja4['Categoria do Produto'].value_counts()


# média de avaliação por lojas

media_avaliacao_loja1 = loja['Avaliação da compra'].mean()
media_avaliacao_loja1 = round(media_avaliacao_loja1, 2)

media_avaliacao_loja2 = loja2['Avaliação da compra'].mean()
media_avaliacao_loja2 = round(media_avaliacao_loja2, 2)

media_avaliacao_loja3 = loja3['Avaliação da compra'].mean()
media_avaliacao_loja3 = round(media_avaliacao_loja3, 2) 

media_avaliacao_loja4 = loja4['Avaliação da compra'].mean()         
media_avaliacao_loja4 = round(media_avaliacao_loja4, 2)

# produtos mais vendidos e menos vendidos
produtos_mais_vendidos_loja1 = loja['Produto'].value_counts().head(5)
produtos_mais_vendidos_loja1 = produtos_mais_vendidos_loja1.reset_index()
produtos_mais_vendidos_loja1.columns = ['Produto', 'Quantidade']

produto_menos_vendidos_loja1 = loja['Produto'].value_counts().tail(5)
produto_menos_vendidos_loja1 = produto_menos_vendidos_loja1.reset_index()   
produto_menos_vendidos_loja1.columns = ['Produto', 'Quantidade']


produtos_mais_vendidos_loja2 = loja2['Produto'].value_counts().head(5)
produtos_mais_vendidos_loja2 = produtos_mais_vendidos_loja2.reset_index()
produtos_mais_vendidos_loja2.columns = ['Produto', 'Quantidade']

produto_menos_vendidos_loja2 = loja2['Produto'].value_counts().tail(5)
produto_menos_vendidos_loja2 = produto_menos_vendidos_loja2.reset_index()
produto_menos_vendidos_loja2.columns = ['Produto', 'Quantidade']

produtos_mais_vendidos_loja3 = loja3['Produto'].value_counts().head(5)
produtos_mais_vendidos_loja3 = produtos_mais_vendidos_loja3.reset_index()
produtos_mais_vendidos_loja3.columns = ['Produto', 'Quantidade']

produto_menos_vendidos_loja3 = loja3['Produto'].value_counts().tail(5)
produto_menos_vendidos_loja3 = produto_menos_vendidos_loja3.reset_index()
produto_menos_vendidos_loja3.columns = ['Produto', 'Quantidade']

produtos_mais_vendidos_loja4 = loja4['Produto'].value_counts().head(5)  
produtos_mais_vendidos_loja4 = produtos_mais_vendidos_loja4.reset_index()
produtos_mais_vendidos_loja4.columns = ['Produto', 'Quantidade']

prpoduto_menos_vendidos_loja4 = loja4['Produto'].value_counts().tail(5)
prpoduto_menos_vendidos_loja4 = prpoduto_menos_vendidos_loja4.reset_index()
prpoduto_menos_vendidos_loja4.columns = ['Produto', 'Quantidade']


# frete médio por loja 
frete_medio_loja1 = loja['Frete'].mean()
frete_medio_loja1 = round(frete_medio_loja1, 2)

frete_medio_loja2 = loja2['Frete'].mean()
frete_medio_loja2 = round(frete_medio_loja2, 2)


frete_medio_loja3 = loja3['Frete'].mean()
frete_medio_loja3 = round(frete_medio_loja3, 2)


frete_medio_loja4 = loja4['Frete'].mean()
frete_medio_loja4 = round(frete_medio_loja4, 2)


st.set_page_config(page_title="Análise de Vendas", page_icon=":bar_chart:", layout="wide")
st.title("Análise de Dados da Loja do Sr João")
st.write("##")
st.subheader("Relatório Final")
st.subheader("Contexto")
st.write("O sr João possui uma rede de 4 Lojas chamada Alura Store no qual vende diversos produtos. Neste caso, o sr João deseja vender uma de suas lojas para iniciar um novo empreendimento. Meu trabalho aqui é auxiliar-lo a entender qual das lojas é mais apropriada para realizar o desejo do Sr João.")

fig = px.line(
    x=["Loja 1", "Loja 2", "Loja 3", "Loja 4"],
    y=[faturamento_loja1, faturamento_loja2, faturamento_loja3, faturamento_loja4],
    labels={"x": "", "y": "Faturamento R$"},
    title="Faturamento por Loja",
    markers=True,
)
fig.update_traces(marker=dict(size=10, line=dict(width=2, color="DarkSlateGrey")))
fig.update_layout(
    title_font=dict(size=20, color="white"),
    xaxis_title_font=dict(size=16, color="white"),
    yaxis_title_font=dict(size=16, color="white"),
    legend_title_font=dict(size=16, color="black"),
    font=dict(size=14, color="black"),
)
st.plotly_chart(fig, use_container_width=True)

col1, col2, col3, col4 = st.columns(4)
col1.metric(" Loja 1", format_faturamento_loja1)
col1.metric(" Avaliação", media_avaliacao_loja1)
col1.metric(" Frete Médio", frete_medio_loja1)
col1.metric("Quantidade de Vendas", loja['Produto'].count())

col2.metric(" Loja 2", format_faturamento_loja2)
col2.metric(" Avaliação", media_avaliacao_loja2)
col2.metric(" Frete Médio", frete_medio_loja2)
col2.metric("Quantidade de Vendas", loja2['Produto'].count())

col3.metric(" Loja 3", format_faturamento_loja3)
col3.metric(" Avaliação", media_avaliacao_loja3)
col3.metric(" Frete Médio", frete_medio_loja3)
col3.metric("Quantidade de Vendas", loja3['Produto'].count())

col4.metric(" Loja 4", format_faturamento_loja4)
col4.metric(" Avaliação", media_avaliacao_loja4)
col4.metric(" Frete Médio", frete_medio_loja4)
col4.metric("Quantidade de Vendas", loja4['Produto'].count())

st.write("##")

st.write("### Comparativo de Vendas por Categoria")    
abas = st.tabs(["Loja 1", "Loja 2", "Loja 3", "Loja 4"])
with abas[0]:
    fig1, ax1 = plt.subplots()
    ax1.pie(venda_por_categoria_loja1, labels=venda_por_categoria_loja1.index, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)
with abas[1]:
    fig2, ax2 = plt.subplots()
    ax2.pie(venda_por_categoria_loja2, labels=venda_por_categoria_loja2.index, autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig2)
with abas[2]:
    fig3, ax3 = plt.subplots()
    ax3.pie(venda_por_categoria_loja3, labels=venda_por_categoria_loja3.index, autopct='%1.1f%%', startangle=90)
    ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig3)
with abas[3]:
    fig4, ax4 = plt.subplots()
    ax4.pie(venda_por_categoria_loja4, labels=venda_por_categoria_loja4.index, autopct='%1.1f%%', startangle=90)
    ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig4)
st.write("##")


st.write("### Produtos Mais Vendidos")  

abas2 = st.tabs(["Loja 1", "Loja 2", "Loja 3", "Loja 4"])
with abas2[0]:
    fig5 = px.bar(produtos_mais_vendidos_loja1, x='Produto', y='Quantidade')
    st.plotly_chart(fig5, use_container_width=True) 
with abas2[1]:
    fig6 = px.bar(produtos_mais_vendidos_loja2, x='Produto', y='Quantidade')
    st.plotly_chart(fig6, use_container_width=True)
with abas2[2]:
    fig7 = px.bar(produtos_mais_vendidos_loja3, x='Produto', y='Quantidade')
    st.plotly_chart(fig7, use_container_width=True)
with abas2[3]:
    fig8 = px.bar(produtos_mais_vendidos_loja4, x='Produto', y='Quantidade')
    st.plotly_chart(fig8, use_container_width=True)    
st.write("##")

st.write("### Produtos Menos Vendidos")
abas3 = st.tabs(["Loja 1", "Loja 2", "Loja 3", "Loja 4"])
with abas3[0]:
    fig9 = px.bar(produto_menos_vendidos_loja1, x='Produto', y='Quantidade')
    st.plotly_chart(fig9, use_container_width=True)
with abas3[1]:
    fig10 = px.bar(produto_menos_vendidos_loja2, x='Produto', y='Quantidade')
    st.plotly_chart(fig10, use_container_width=True)    
with abas3[2]:
    fig11 = px.bar(produto_menos_vendidos_loja3, x='Produto', y='Quantidade')
    st.plotly_chart(fig11, use_container_width=True)
with abas3[3]:
    fig12 = px.bar(prpoduto_menos_vendidos_loja4, x='Produto', y='Quantidade')
    st.plotly_chart(fig12, use_container_width=True)

st.write("##")

