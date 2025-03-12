#%%

import pandas as pd

clientes = pd.read_csv('../data/clientes.csv')
clientes.head()

# %%

# Em Pandas, uma view é uma referência a uma parte do DataFrame original, sem copiar os dados para um novo objeto. 
# Isso significa que alterações feitas na view podem afetar o DataFrame original.

filtro = clientes['qtdePontos'] == 0
clientes_0 = clientes[filtro]
clientes_0['flag_1'] = 1 # -> isso gera um erro

# %%

# .copy() -> cria um novo objeto com dados separados
clientes_0 = clientes[filtro].copy()
clientes_0['flag_1'] = 1
clientes_0

# %%
