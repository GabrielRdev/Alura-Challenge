# 📊 Análise de Desempenho de Lojas – Projeto Sr. João

## 🧾 Contexto

O Sr. João é proprietário de uma rede com 4 lojas espalhadas por diferentes regiões. Com o objetivo de diversificar seus investimentos, ele está avaliando a possibilidade de **vender uma das lojas**. No entanto, essa decisão precisa ser tomada com base em dados confiáveis para **evitar prejuízos financeiros** e **manter a sustentabilidade de seu negócio**.

Este projeto tem como objetivo **analisar o desempenho de cada loja** com base em critérios relevantes para identificar qual delas apresenta menor impacto ao ser vendida.

---

## 🎯 Objetivo

Realizar uma **análise comparativa entre as quatro lojas**, considerando indicadores como:

- Faturamento das lojas
- Avaliações dos clientes
- Categorias dos produtos
- Custo médio do frete
- Quantidade de vendas
- Produtos mais vendidos
- Produtos menos vendidos

Com base nesses dados, identificar **qual loja pode ser vendida** com menor impacto financeiro e estratégico para o negócio do Sr. João.

---

## 📊 Análise dos indicadores

A análise dos principais indicadores das quatro lojas do Sr. João revelou os seguintes pontos:

- **🔝 Faturamento Total:**  
  A **Loja 1** possui o maior faturamento (R$1.534.509,12), seguida pela Loja 2 e Loja 3. A **Loja 4 tem o menor faturamento** (R$1.384.497,58), o que pode indicar menor potencial de receita."

- **⭐ Média das Avaliações:**  
  A **Loja 3 é a melhor avaliada pelos clientes** (nota 4.05), enquanto a **Loja 1 apresenta a pior avaliação** (nota 3.98). A percepção do cliente é um fator crucial para a reputação e continuidade do negócio.

- **🚚 Custo Médio do Frete:**  
  A **Loja 4 apresenta o menor custo médio de frete** (R$31,28), o que pode indicar melhor localização logística ou eficiência operacional. A **Loja 1 tem o maior custo médio de frete** (R$34,69), impactando na margem de lucro.

  ![](./images/tela.gif)

  [Clique aqui para visualizar os gráficos](https://alura-challenge-one-kwvpbbtc4jpfmmwqpvyc9q.streamlit.app/)

---

### 📌 Considerações

Apesar da **Loja 1 ter o maior faturamento**, ela **tem a pior avaliação dos clientes e o maior custo de frete**. Já a **Loja 4 apresenta o menor faturamento**, mas possui **melhor custo logístico e avaliação razoável**, o que pode indicar uma operação mais enxuta.

---

## ✅ Recomendação Final

### 🔻 Pontos Negativos da Loja 1:

- **Pior avaliação dos clientes** (nota 3.98), indicando possíveis problemas na operação ou experiência de compra.
- **Maior custo médio de frete** (R$34,69), o que impacta negativamente a lucratividade.
- Apesar de possuir o **maior faturamento**, esses custos e avaliações indicam **menor eficiência operacional**.

### 📌 Conclusão:

**Vender a Loja 1** é a decisão mais estratégica, pois:

- Reduz custos operacionais e risco reputacional;
- Provavelmente mantém a lucratividade geral da rede;
- Pode atrair compradores interessados devido ao alto faturamento, **sem gerar prejuízo** para o Sr. João.

---

## 🛠️ Tecnologias Utilizadas

- Python 🐍
- Pandas
- Matplotlib / Seaborn (gráficos)
- Plotly (para gráficos interativos)
- Streamlit (para visualização e dashboard)

---

## 📁 Estrutura do Projeto

```bash
📂 analise-lojas-sr-joao/
├── .venv/
├── app/            # Análises exploratórias
 ├── main.py                # Aplicação principal em Streamlit
├── requirements.txt      # Dependências do projeto
├── bd-lojas              #Dados em .csv
└── README.md             # Documentação do projeto

```

---

## 🧪 Como Executar o Projeto

1. Clone o repositório:

```bash
  git clone https://github.com/seu-usuario/analise-lojas-sr-joao.git
  cd analise-lojas-sr-joao
```

2. Crie um ambiente virtual e instale as dependências:

```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
```

3. Execute o dashboard com Streamlit:

```bash
   streamlit run ./app/main.py
```

## 👨‍💻 Autor

Projeto desenvolvido por Gabriel Ricardo.<br>
