#%%

import pandas as pd
import sqlalchemy

# %%

# criando conexão com banco de dados
engine = sqlalchemy.create_engine('sqlite:///../data/olist.db')

# gerando um df com a tabela de clientes
clientes = pd.read_sql_table(table_name='tb_customers', con=engine)
clientes

# %%

# fazendo uma query para evitar carregar toda a tabela e dar pau
 
query = 'SELECT * FROM tb_customers LIMIT 100'

df = pd.read_sql_query(query, con=engine)
df

# %%
