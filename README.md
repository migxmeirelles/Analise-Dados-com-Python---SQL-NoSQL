## Objetivo:
Seguindo meus estudos de Analise de Dados, usei um banco de dados SQL (SQL Server) e um NoSQL (MongoDB) para, no Python (com as bibliotecas SQLAlchemy, Pymongo, Pandas e Matplotlib Pyplot) "juntar" os dois em uma unica "Tabela", e assim criar gráficos e Analises.
## Contexto:
Dentro da pasta Origens, temos os scripts de criação dos dois bancos de dados.

* Banco SQL/SQL Server:
temos uma tabela simples, com informações das Agências de um Banco, nesse caso, apenas 3 Agências (os 3 estados da região sul do Brasil).
* Banco noSQL/MongoDB:
temos uma Collection com informações de Clientes desse Banco (Código da Agência, Nome do Cliente, CPF, Data de Nasc, etc...)
Essas informações de Clientes são **ficticias**, foram geradas com ajuda de IA.

A Junção das duas "tabelas" no Python é feito pela coluna em comum de Código da Agência.

## Código:

* primeiramente importamos as bibliotecas.
* criamos uma conexão com nosso banco de dados SQL Server, passando a Query e salvando em um DataFrame do Pandas (df_mssql).
* criamos a conexão com MongoDB e salvando o resultado da consulta em outro DataFrame (df_nosql).
* garantimos que a Chave da Relação (coluna "CD" dos dois DataFrames) estão no mesmo tipo: string.
* criamos um "join" entre as tabelas, atraves da função *pd.merge*.
* renomeamos apenas as colunas que vamos usar, e salvamos em um novo DataFrame (nw_df).
* executamos um *print(nw_df)* para visualizar os dados.

### Criando Gráficos:

* gráfico 1: antes de criar os gráficos, devemos agrupar usando *.nunique* para contar (de maneira única) os CPFs, e agrupamos por Agência.
* gráfico 2: o agrupamento de Renda Mensal por Agência é feita usando o *.sum()* para obter o total.
* definimos as propriedades do gráfico com .plot, inserindo cores, legenda, titulos, etc...
* usamos o *plt.savefig* para salvar em .jpg o resultado.
