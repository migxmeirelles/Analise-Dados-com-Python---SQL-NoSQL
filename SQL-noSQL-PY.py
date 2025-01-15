from sqlalchemy import create_engine
from pymongo import MongoClient
import matplotlib.pyplot as plt
import pandas as pd

#conexao sqlserver
engine = create_engine('mssql+pyodbc://user:senha@localhost/dw?driver=ODBC+Driver+17+for+SQL+Server')
query = '''
    SELECT * FROM AGENCIAS
'''
df_mssql = pd.read_sql(query, engine)

#conexao mongodb
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['dw']
collection = db['clientes']
df_nosql = pd.DataFrame(list(collection.find()))

#garantindo tipo das pk iguais
df_nosql['CD'] = df_nosql['CD'].astype(str)
df_mssql['CD'] = df_mssql['CD'].astype(str)

#join
df_merge = pd.merge(df_mssql, df_nosql, on='CD', how='inner')
nw_df = df_merge[['SG', 'nome', 'cpf', 'dt_nasc', 'renda_mensal']]
nw_df.rename(columns={'SG': 'AGENCIA', 'nome': 'CLIENTE', 'cpf': 'CPF', 'dt_nasc': 'NASC', 'renda_mensal': 'RENDA_MENSAL'}, inplace=True)

print(nw_df)



#grafico de pizza, clientes por agencia
graf_ag = nw_df.groupby('AGENCIA')['CPF'].nunique().sort_index()
print(f"contagem de clientes por agencia:{graf_ag}")

plt.figure(figsize=(10,6))
graf_ag.plot(
             kind='pie', autopct='%1.1f%%', shadow=True, 
             colors=['green', 'orange', 'skyblue'], 
             wedgeprops={'edgecolor': 'black', 'linewidth': 1.5}
            )
plt.title("N° de Clientes por Agência:", fontsize=14, fontweight='bold')
plt.legend(
             handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) 
                     for color in ['green', 'orange', 'blue']], 
             labels=[f"{int(val)} clientes" for val in graf_ag],
             loc="center left", bbox_to_anchor=(1, 0.5), fontsize=8
          )
plt.ylabel("")
plt.xlabel("")
plt.subplots_adjust(left=0.048, bottom=0.107, right=0.879, top=0.795)
plt.savefig("TotalClientes_ag.jpg")
plt.show()



#grafico de barra, renda total por agencia
graf_renda = nw_df.groupby('AGENCIA')['RENDA_MENSAL'].sum()
print(f"Renda Total por Agências: {graf_renda}")

plt.figure(figsize=(10,6))
graf_renda.plot(kind='bar', color='skyblue', edgecolor='darkblue', alpha=0.7)
plt.title("Renda Total por Agência:", fontsize=14, fontweight='bold')
plt.ylabel("Renda Total", fontsize=10, fontweight='bold')
plt.xlabel("Agências", fontsize=10, fontweight='bold')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.subplots_adjust(left=0.11, bottom=0.136, right=0.962, top=0.898)
plt.savefig("RendaTotal_ag.jpg")
plt.show()