#%%

# 01 - Quantos clientes tem vínculo com a Twitch?

import pandas as pd

clientes = pd.read_csv('../data/clientes.csv')
clientes.head()

filtro = clientes['flTwitch'] == 1
clientes[filtro].shape[0]

#%%

# 02 - Quantos clientes tem um saldo de pontos maior que 1000?

filtro = clientes['qtdePontos'] > 1000
qtde_1000 = clientes[filtro].shape[0]
print(f'Temos {qtde_1000} clientes com mais de 1000 pontos.')

#%%

# 03 - Quantas transações ocorreram no dia 2025-02-01?

transacoes = pd.read_csv('../data/transacoes.csv')
transacoes.head()

filtro = (transacoes['dtCriacao'] >= '2025-02-01') & (transacoes['dtCriacao'] < '2025-02-02')
qtde_dia_2025_02_01 = transacoes[filtro].shape[0]
print(f'Tivemos {qtde_dia_2025_02_01} transações no dia 2025-02-01')

# %%
