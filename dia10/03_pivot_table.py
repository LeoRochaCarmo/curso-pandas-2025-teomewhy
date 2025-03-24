#%%

import pandas as pd 

df = pd.read_csv('homicidios_consolidado.csv', sep=';')

df.head()

# %%

df_stack = (df.set_index(['nome', 'período'])
              .stack()
              .reset_index())

df_stack.columns = ['nome', 'periodo', 'metrica', 'valor']

df_stack

# %%

# pivot_table -> criar tabelas dinâmicas

df_pivot_table = df_stack.pivot_table(values='valor', 
                                      index=['nome', 'periodo'], 
                                      columns='metrica')

df_pivot_table

# %%

# Sumir com o período e gerar a média para cada estado

df_stack.pivot_table(values='valor', 
                     index='nome', 
                     columns='metrica',
                     aggfunc='mean' # já agrega a média como padrão
                     )

# %%

# como fazer pivot ao contrário? usar o stack

df_unpivot_table = (df_stack.pivot_table(values='valor', 
                                      index=['nome', 'periodo'], 
                                      columns='metrica')
                            .stack())

df_unpivot_table
# %%
