#%%
# Leia o arquivo transacoes.csv com a formatação correta;
# Adicione uma coluna com valores 1;
# Salve o dataframe com nome: transacoes_1.csv

import pandas as pd

df = pd.read_csv('../../data/transacoes.csv')

df['valor 1'] = 1

df.head(5)

df.to_csv('transacoes.csv', index=False)
# %%

# 03.01 - Quantas linhas há no arquivo clientes.csv ?
df = pd.read_csv('../../data/clientes.csv')
df.shape[0]

#%%

# 03.02 - Quantas colunas do tipo int há no arquivo transacoes.csv ?
df = pd.read_csv('../../data/transacoes.csv')
tipos_df = df.dtypes
num_colunas_int = sum(tipos_df == 'int64')
num_colunas_int

#%%

# 03.03 - Quantas colunas do tipo object há no arquivo produtos.csv ?
df = pd.read_csv('../../data/produtos.csv')
tipos_df = df.dtypes
num_colunas_object = sum(tipos_df == 'object')
num_colunas_object

#%%

# 03.04 - Qual o id do cliente no índice 4 no arquivo clientes.csv ?
df = pd.read_csv('../../data/clientes.csv')
df['idCliente'][4]
df.loc[4]['idCliente']
#%%

# 03.05 - Qual o saldo de pontos do cliente na 10a posição (sem ordenar) do arquivo clientes.csv ?
df = pd.read_csv('../../data/clientes.csv')
df.iloc[9]['qtdePontos']

# %%
