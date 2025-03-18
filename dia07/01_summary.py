#%%

import pandas as pd

idades = [32, 44, 12, 54, 67, 32, 23, 34, 32, 12, 45, 43, 28, 73, 29]
idades = pd.Series(idades)
idades

# %%

# Sumerização com .describe

idades.describe()

# %%

clientes = pd.read_csv('../data/clientes.csv')
clientes.head()

# %%

# Quantos cliente têm Twitch?

clientes['flTwitch'].sum()

# %%

# Qual a média de clientes que têm Twitch?

clientes['flTwitch'].mean()

#%%

# Qual a média de todas as redes?

redes_sociais = ['flEmail', 'flTwitch', 'flYouTube', 'flBlueSky', 'flInstagram']
clientes[redes_sociais].mean()

# %%

# Obtendo colunas do tipo numérico de forma dinâmica

filtro = clientes.dtypes == 'object'
num_columns = clientes.dtypes[~filtro].index.to_list()
clientes[num_columns].mean()

# %%

# Retornando um dataframe com .describe

clientes[num_columns].describe()
# %%
