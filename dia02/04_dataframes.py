#%% 
import pandas as pd

df_clientes = pd.read_csv('../data/clientes.csv')
df_clientes
# %%

# Igual o LIMIT 5 do SQL
df_clientes.head()
# %%

df_clientes.head(10)

# %%

# Ver as últimas 5 linhas
df_clientes.tail()

# %%

# Amostra aleatória com 10 registros
df_clientes.sample(10)

# %%

# retorna números de colunas e linhas
df_clientes.shape

# %%

# retorna nomes das colunas
df_clientes.columns

# %%

# retorna os índices
df_clientes.index

# %%

# retorna informações do dataframe
df_clientes.info()

# %%

# retorna o uso real de memória
df_clientes.info(memory_usage='deep')

# %%

# retorna a tipagem de cada coluna
df_clientes.dtypes

# %%

df_clientes.dtypes['qtdePontos']

# %%

