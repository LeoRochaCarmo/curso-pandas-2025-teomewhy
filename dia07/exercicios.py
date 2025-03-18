#%%

# 06.01 - Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?
# JEITO MAIS BRUTO


import pandas as pd

clientes = pd.read_csv('../data/clientes.csv')
clientes.head()

clientes['totalClientes'] = (clientes['flEmail']
                            + clientes['flTwitch']
                            + clientes['flYouTube']
                            + clientes['flBlueSky']
                            + clientes['flInstagram'])

media = clientes['totalClientes'].mean()
variancia = clientes['totalClientes'].var()
maximo = clientes['totalClientes'].max()

print('media:', media)
print('variancia:', variancia)
print('maximo:', maximo)

#%%
# 06.01 - Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?
# JEITO MAIS ELEGANTE E EFICAZ

redes = [
        'flEmail',
        'flTwitch',
        'flYouTube',
        'flBlueSky',
        'flInstagram',
]

clientes[redes].sum(axis=1).describe()

#%%

# 06.02 - Quais são os usuários que mais fizeram transações? Considere os 10 primeiros.

transacoes = pd.read_csv('../data/transacoes.csv')
transacoes.head()

(transacoes.groupby(by=['idCliente'])['idTransacao']
           .count()
           .sort_values(ascending=False)
           .head(10))

#%%

# 06.03 - Qual usuário teve maior quantidade de pontos debitados?

filtro = transacoes['qtdePontos'] < 0

(transacoes[filtro].groupby(by=['idCliente'])['qtdePontos']
                   .sum()
                   .sort_values()
                   .head(1))

#%%

# 06.04 - Qual a média de transações / dia?

transacoes.head()

transacoes['dtDia'] = pd.to_datetime(transacoes['dtCriacao']).dt.date

summary = transacoes.agg(
    {'idTransacao': 'count',
     'dtDia': 'nunique'
     })

transacoes_dia = summary['idTransacao'] / summary['dtDia']
transacoes_dia

#%%

# 06.05 - Como podemos calcular as estatísticas descritivas dos pontos das transações de cada usuário?

transacoes.groupby(by=['idCliente'], as_index=False)['qtdePontos'].describe()

# %%

# 06.06 - Obtenha a última linha de transação de cada usuário e depois a primeira.

import pandas as pd

df = pd.read_csv('../data/transacoes.csv')

ultima_transacao = (df.sort_values(by='dtCriacao')
                      .drop_duplicates(subset='idCliente', keep='last'))

primeira_transacao = (df.sort_values(by='dtCriacao')
                        .drop_duplicates(subset='idCliente', keep='first'))

# %%

primeira_transacao
# %%
