#%%

import pandas as pd

# %%

# Filtrar transações maiores de 50 pontos (usando for)
pontos = [10, 1, 1, 50, 100, 130, 30, 25, 50]

valores_50_mais = []
for i in pontos:
    if i > 50:
        valores_50_mais.append(i)

valores_50_mais

# %%

# Filtrar transações maiores de 50 pontos (usando list comprehension)
valores_50_mais = [i for i in valores_50_mais if i > 50]
valores_50_mais

# %%

# Filtrar idade maior de 18 anos (usando Pandas)

brinquedo = pd.DataFrame(
    {'nome': ['Teo', 'Nah', 'Mah'],
     'idade': [32, 35, 14],
     'uf': ['sp', 'pr', 'rj']
     }
)

filtro = brinquedo['idade'] > 18
filtro

brinquedo[filtro]

# %%

df = pd.read_csv('../data/transacoes.csv')
df.head()
# %%

# Filtrar transações maiores ou iguais a 50

filtro = df['qtdePontos'] >= 50
df[filtro]
# %%

# Filtrar transações maiores ou iguais a 50 e menores que 100

# PRECISAM ESTAR DENTRO DOS PARENTESES
filtro = (df['qtdePontos'] >= 50) & (df['qtdePontos'] < 100)
df[filtro]

#%%

# Filtrar transações 1 ou 100

# PRECISAM ESTAR DENTRO DOS PARENTESES
filtro = (df['qtdePontos'] == 1) | (df['qtdePontos'] == 100)
df[filtro]

# %%

# Filtrar pontos entre 0 E 50 OU de 2025 para frente

filtro = ((df['qtdePontos'] > 0 ) & (df['qtdePontos'] <= 50)) | (df['dtCriacao'] >= '2025-01-01')
df[filtro]
# %%
