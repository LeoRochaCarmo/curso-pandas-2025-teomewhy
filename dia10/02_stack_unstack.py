#%%

import pandas as pd 

df = pd.read_csv('homicidios_consolidado.csv', sep=';')

df.head()

# %%

# stack -> transforma colunas em um índice hierárquico (MultiIndex), empilhando os dados de um DataFrame

df_stack = (df.set_index(['nome', 'período'])
             .stack())

# %%

# tipo series

type(df_stack)

# %%

# como ver em formato de DataFrame

df_stack = df_stack.reset_index()
df_stack.columns = ['nome', 'período', 'metrica', 'valor']
df_stack

# %%

# unstack -> transformar um índice de linha em colunas. 
# Ele desfaz o empilhamento de um índice hierárquico (MultiIndex), 
# convertendo uma parte do índice de linha para colunas.

df_unstack = (df_stack.set_index(['nome', 'período','metrica'])
                      .unstack()
                      .reset_index())

# %%

# como arrumar os nomes das colunas

metricas = df_unstack.columns.droplevel(0)[2:]
df_unstack.columns = ['nome', 'valor', *metricas]
df_unstack

# %%
