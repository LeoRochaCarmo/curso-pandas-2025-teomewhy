#%%

# 01 - Crie uma coluna nova “twitch_points” que e resultado da multiplicação do saldo de pontos e a marcação da twitch

import pandas as pd

clientes = pd.read_csv('../data/clientes.csv')

clientes['twitch_points'] = clientes['qtdePontos'] * clientes['flTwitch']
clientes.head()

#%%

# 02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova

import numpy as np

clientes['log_pontos'] = np.log(clientes['qtdePontos'])
clientes.head()

#%%

# 03 - Crie uma coluna que sinalize se a pessoa tem vínculo com alguma (qualquer uma) plataforma de rede social.

clientes['tem_uma_social'] = clientes['flEmail'] | clientes['flTwitch'] | clientes['flYouTube'] | clientes['flBlueSky'] | clientes['flInstagram']
clientes.head()

#%%

# 04 - Qual é o id de cliente que tem maior saldo de pontos? E o menor?

clientes.sort_values(by='qtdePontos', ascending=False).head(1)
clientes.sort_values(by='qtdePontos', ascending=True).head(1)

#%%