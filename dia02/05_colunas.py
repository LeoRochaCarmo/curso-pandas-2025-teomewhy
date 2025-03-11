#%%

import pandas as pd

df = pd.read_csv('../data/transacoes.csv')
df
# %%

# renomear colunas
renamed_columns = {
        'qtdePontos': 'qtPontos',
        'descSistemaOrigem': 'SistemaOrigem'
}

df.rename(columns=renamed_columns, inplace=True)

# %%

# Acessando mais de uma coluna
df[['idCliente', 'qtPontos']]

# %%

# SELECT idCliente FROM df
df[['idCliente']]
# %%

# SELECT idCliente FROM df LIMIT 5
df[['idCliente']].head()
# %%

# SELECT idCliente, idTransacao, qtPontos FROM df LIMIT 5
df[['idCliente', 'idTransacao', 'qtPontos']].head()

# %%

# Ordenando as colunas
colunas = list(df.columns)
colunas.sort()
colunas

# %%

# Alterando a ordem das colunas
df = df[colunas]
df
# %%
