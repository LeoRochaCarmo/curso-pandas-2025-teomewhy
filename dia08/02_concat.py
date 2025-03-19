#%% 


import pandas as pd

df = pd.DataFrame({ 
        "cliente": [1,2,3,4,5], 
        "nome": ["teo", "jose", "nah", "mah", "lah"] 
})

df_02 = pd.DataFrame({ 
        "cliente": [6,7,8],    
        "nome": ["kozato", "laura", "dan",], 
        "idade":[32,29,31], 
})

df_03 = pd.DataFrame({
    'idade': [32,34,19,54,33]
})

# %%

# Concatenar 2 dfs 

pd.concat([df, df_02], ignore_index=True)

# %%

# Concatenar um do lado do outro com axis=1

pd.concat([df, df_03], axis=1)

# %%

# Concatenando depois de uma ordenação

df_03 = df_03.sort_values('idade').reset_index(drop=True)
pd.concat([df, df_03], axis=1)

# %%
