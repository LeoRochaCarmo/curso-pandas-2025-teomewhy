#%%

import pandas as pd

transacoes = pd.read_csv('../data/transacoes.csv')
transacoes.head()

# %%

# Contagem por cliente

transacoes.groupby(by=['idCliente']).count()

# %%

# Quantidade de transações por cliente (retornando um dataframe)

transacoes.groupby(by=['idCliente'])[['idTransacao']].count()

# %%

# Retornar um dataframe com o idCliente sem ser o index

transacoes.groupby(by=['idCliente'], as_index=False)[['idTransacao']].count()

# %%

# Calcular, por cliente, a qtde de transações, total de ptos e média de ptos por transação

summary = (transacoes.groupby(by=['idCliente'], as_index=False)
            .agg({
                'idTransacao': ['count'],
                "qtdePontos": ['sum', 'mean']
                }))

summary

# %%

# Como acessar MultiIndex

summary['qtdePontos']['mean']

# OU

summary[('qtdePontos', 'mean')]

# %%

# Como se livrar do MultiIndex

summary.columns = ['idCliente', 'qtdeTransacao', 'totalPontos', 'avgPontos']
summary

# %%
