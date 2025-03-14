#%% 

import pandas as pd

df = pd.read_csv('../data/clientes.csv')
df

# %%

# Converter inteiros para float e depois para string

df['qtdePontos'].astype(float).astype(str)


# %%

# Substituindo valor antigo por um novo (REPLACE)

df['dtCriacao'] = df['dtCriacao'].replace({
    '0000-00-00 00:00:00.000': '2024-02-01 09:00:00.000'
    })  

#%%

# Converter datas

pd.to_datetime(df['dtCriacao'])

# %%

# Jeito mais comum de encontrar no dia a dia

replace = {'0000-00-00 00:00:00.000': '2024-02-01 09:00:00.000'}

df['dtCriacao'] = pd.to_datetime(df['dtCriacao'].replace(replace))

df['dtCriacao']
# %%

# Obter apenas o ano

df['dtCriacao'].dt.year.astype(int)

# %%
