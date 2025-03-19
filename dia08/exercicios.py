#%%

# 06.04 - Quem teve mais transações de Streak(produto)?

import pandas as pd

transacoes = pd.read_csv('../data/transacoes.csv')

transacao_produto = pd.read_csv('../data/transacao_produto.csv')

produtos = pd.read_csv('../data/produtos.csv')

cliente_transacao_produtos = transacoes.merge(
    transacao_produto, 
    on='idTransacao', 
    how='left'
)

cliente_transacao_produtos[['idTransacao', 'idCliente', 'idProduto']]

df_full = cliente_transacao_produtos.merge(
    produtos, 
    on='idProduto',
    how='left'
    )

filtro = df_full['descProduto'] == 'Presença Streak'

df_full = df_full[filtro]

(df_full.groupby(by='idCliente')['idTransacao']
        .count()
        .sort_values(ascending=False)
        .head(1)
)

# %%

# Maneira mais avançada e perfomática

filtro = produtos['descProduto'] == 'Presença Streak'
produtos = produtos[filtro]
produtos

(transacoes.merge(transacao_produto,on='idTransacao', how='left')
           .merge(produtos, on='idProduto', how='right')
           .groupby(by='idCliente')['idTransacao']
           .count()
           .sort_values(ascending=False)
           .head(1)
)

# %%
