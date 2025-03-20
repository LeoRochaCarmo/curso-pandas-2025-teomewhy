#%%

import pandas as pd
import sqlalchemy
from sklearn import cluster

with open ('etl.sql') as open_file:
    query = open_file.read()

print(query)

# %%

# criando df com query

engine = sqlalchemy.create_engine('sqlite:///../data/olist.db')
df = pd.read_sql_query(query, con=engine)
df

# %%

# criando nova coluna com o cluster que cada cliente pertence

kmean = cluster.KMeans(n_clusters=4)
kmean.fit(df[['totalRevenue', 'qtSalles']])

df['cluster'] = kmean.labels_
df

#%%

# enviando uma nova tabela para o banco de dados

df.to_sql('sellers_cluster', con=engine, index=False)

# %%

# garantindo que tabela atualizada substituirá tabela já existente

df.to_sql('sellers_cluster', 
          con=engine, 
          index=False, 
          if_exists='replace')

#%%

# verificando essa nova tabela

query = 'select * from sellers_cluster LIMIT 10'
df = pd.read_sql_query(query, con=engine)
df

# %%
