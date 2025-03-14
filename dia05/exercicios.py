#%%

# 01 -> Selecione a primeira transação diária de cada cliente.

import pandas as pd

transacoes = pd.read_csv('../data/transacoes.csv')
transacoes.head()

# %%

transacoes['data'] = pd.to_datetime(transacoes['dtCriacao']).dt.date
(transacoes.sort_values('dtCriacao')
          .drop_duplicates(keep='first', subset=['idCliente', 'data']))

# %%

# 02 -> Selecione a primeira e última transação diária de cada cliente.

first =(transacoes.sort_values('dtCriacao')
          .drop_duplicates(keep='first', subset=['idCliente', 'data']))

last =(transacoes.sort_values('dtCriacao')
          .drop_duplicates(keep='last', subset=['idCliente', 'data']))

pd.concat([last, first])

# %%
