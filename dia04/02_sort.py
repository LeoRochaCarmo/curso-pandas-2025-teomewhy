#%%

import pandas as pd


clientes = pd.read_csv('../data/clientes.csv')
clientes['qtdePontos'].sort_values()

# %%

# Descobrir cliente com maior pontos

max_ponto = clientes['qtdePontos'].max()
filtro = clientes['qtdePontos'] == max_ponto
clientes[filtro]

# %%

# Descobrir 5 clientes com mais pontos (Usando SORT_VALUES)

clientes.sort_values(by='qtdePontos', ascending=False).head()


# %%

# PARENTESES SERVEM PARA DIZER QUE COMANDO NÃO TERMINOU

top_5 = (clientes.sort_values(by='qtdePontos', ascending=False)
                 .head()['idCliente'])

# %%



brinquedo = pd.DataFrame( 
    { 
        "nome": ["teo", "ana", "nah", "jose"], 
        "idade": [32, 43, 35, 42], 
        "salario":[2345, 4533, 3245, 4533], 
    } 
)

# Primeiro ordenando pelo salário e depois pela idade (os dois decrescentes)

brinquedo.sort_values(by=['salario', 'idade'], ascending=False)

# %%

# Primeiro ordenando pelo salário (decrescente) e depois pela idade (crescente) 

brinquedo.sort_values(by=['salario', 'idade'], ascending=[False, True])