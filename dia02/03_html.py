# %%
import pandas as pd

dfs = pd.read_html('https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil')
df_uf = dfs[1]
df_uf
# %%
df_uf.to_csv('ufs.csv', sep=';', index=False)
# %%
