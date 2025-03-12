#%%

import pandas as pd

df = pd.read_csv('../data/transacao_produto.csv')
df.head()

# %%

# Filtrar vendas que tiveram dois tipos de produtos (5 e 11)

filtro = (df['idProduto'] == 5) | (df['idProduto'] == 11)
df[filtro]

# %%

# Outra maneira (isin)

filtro = df['idProduto'].isin([5, 11])
df[filtro]

# %%

# Quais clientes têm a data de criação registrada (notna)

clientes = pd.read_csv('../data/clientes.csv')
clientes.head()

filtro = clientes['dtCriacao'].notna() 
clientes[filtro]

# %%

# Invertando os valores booleanos (usando ~)
filtro = ~ clientes['dtCriacao'].notna() 
clientes[filtro]