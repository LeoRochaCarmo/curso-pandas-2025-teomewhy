#%%

import pandas as pd

transacoes = pd.read_csv('../data/transacoes.csv')
transacoes.head()

#%%


clientes = pd.read_csv('../data/clientes.csv')
clientes.head()

# %%

# Como juntar os dois dataframes usando .merge (como o JOIN no SQL)

transacoes.merge(clientes, how='left', on=['idCliente'])

# %%

# Trocando o sufixo de colunas repetidas

transacoes.merge(right=clientes, 
                 how='left', 
                 on=['idCliente'],
                 suffixes=['Pransacao', 'Cliente'])

# %%

# E se as chaves têm nomes diferentes nas tabelas?

df_1 = pd.DataFrame({ 
            "transacao": [1,2,3,4,5], 
            "idCliente": [1,2,3,2,2], 
            "valor": [10,45,32,17,87], 
})

df_2 = pd.DataFrame({ 
            "id": [1,2,3,4],   
            "nome": ["teo", "nah", "mah", "jose"] 
})

df_1.merge(df_2, 
           left_on=['idCliente'], 
           right_on=['id'], 
           how='left')

# %%

df_1 = pd.DataFrame({ 
            "transacao": [1,2,3,4,5], 
            "idCliente": [1,2,3,2,2], 
            "valor": [10,45,32,17,87], 
})

df_2 = pd.DataFrame({ 
            "idCliente": [1,2,3,4],   
            "nome": ["teo", "nah", "mah", "jose"] 
})

df_1.set_index('idCliente').merge(df_2.set_index('idCliente'), how='left')
# %%
