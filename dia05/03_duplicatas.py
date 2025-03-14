#%%

import pandas as pd

# %%

df = pd.DataFrame(
    { 
        "nome": ['teo', 'lara', 'nah', 'bia', 'mah', 'lara', 'mah', 'mah'], 
        "sobrenome": ['calvo', 'calvo', 'ataide', 'ataide', 'silva', 'silva', 'silva', 'silva'],
        "salario": [2132, 1231, 454, 6543, 6532, 4322, 987, 2134]
    }
)

df
# %%

# Removendo duplicatas (MANTÉM A PRIMEIRA POR DEFAULT)

df.drop_duplicates()

# %%

# Removendo duplicatas mas mantendo a última

df.drop_duplicates(keep='last')

# %%

# Removendo duplicatas de colunas específicas

df.drop_duplicates(subset=['nome', 'sobrenome'])

# %%

# Removendo duplicatas mantendo o salário maior

df.sort_values(by='salario', ascending=False)
df.drop_duplicates(subset=['nome', 'sobrenome'], keep='last')

# %%

df = (df.sort_values(by='salario', ascending=False)
        .drop_duplicates(subset=['nome', 'sobrenome'], keep='last'))

df

# %%

