#%% 

import pandas as pd

clientes = pd.read_csv('../data/clientes.csv')
clientes


# %%

# Ignorando linhas que contêm QUALQUER NAs

clientes.dropna()

# %%

# Ignorando linhas que contêm NAs EM TODA LINHA

clientes.dropna(how='all')

# %%

# Remover NAs apenas da coluna idade

df = pd.DataFrame( 
    { 
        "nome": ["Téo", None, "Nah", "Marcio"], 
        "idade": [None, None, 43, 52], 
        "salario": [3453,4324,None,5423] 
    } 
)

df.dropna(how='all', subset='idade')

# %%

# Removendo idade E salario com NAs

df.dropna(how='all', subset=['idade', 'salario'])

# %%

# Trocando NAs para o valor 0

df['idade'] = df['idade'].fillna(0)
df

# %%

# Trocando NAs das colunas com critérios específicos

df.fillna({'nome': 'alguém', 'idade': 0, 'salario': 0})

# %%

# Trocando NAs com a média

medias = df[['idade', 'salario']].mean()
df.fillna(medias)

df

# %%

