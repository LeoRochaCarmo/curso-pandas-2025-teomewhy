#%%

import pandas as pd
import numpy as np

clientes = pd.read_csv('../data/clientes.csv')
clientes.head()

# %%

# Somando 100 ptos para cada cliente

clientes['qtdePontos'] + 100

# %%

# Criando coluna nova

clientes['pontos_100'] = clientes['qtdePontos'] + 100
clientes.head()

# %%

# Criar coluna que informa se a pessoa tem Email OU Twitch

clientes['emailTwitch']  = clientes['flEmail'] + clientes['flTwitch']
clientes.head()

# %%

# Criar coluna que informa se a pessoa tem Email OU Twitch

clientes['emaileTwitch']  = clientes['flEmail'] * clientes['flTwitch']
clientes.head()

# %%

# Criar coluna que informa quantas redes sociais clientes têm

clientes['qtde_social'] = clientes['flEmail'] + clientes['flTwitch'] + clientes['flYouTube'] + clientes['flBlueSky'] + clientes['flInstagram']

#%%

# Criar coluna que informa se cliente tem TODAS redes sociais clientes

clientes['todas_social']  = clientes['flEmail'] * clientes['flTwitch'] * clientes['flYouTube'] * clientes['flBlueSky'] * clientes['flInstagram']

#%%

import matplotlib.pyplot as plt

clientes['log_pontos'] = np.log(clientes['qtdePontos'] + 1)
clientes['log_pontos'].describe()

plt.hist(clientes['log_pontos'])
plt.grid(True)
plt.show()

# %%
