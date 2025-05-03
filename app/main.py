import pandas as pd
import locale
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px



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
st.title("Análise de Vendas por Loja")
st.subheader("Faturamento Total por Loja")
st.write("Faturamento total da loja 1: ", format_faturamento_loja1)     
st.write("Faturamento total da loja 2: ", format_faturamento_loja2)     
st.write("Faturamento total da loja 3: ", format_faturamento_loja3)
st.write("Faturamento total da loja 4: ", format_faturamento_loja4)


st.subheader("Vendas por Categoria")


