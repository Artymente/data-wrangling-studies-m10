import pandas as pd
from scipy import stats

df = pd.read_csv('clientes-limpeza.csv')

filtro_basico = df[df['idade'] > 80]


print("Filtro basico:   ", filtro_basico[['nome',"idade"]])


#Filtrando outliers com Z-score
z_scores = stats.zscore(df['idade'])
outliers_z = df[z_scores >= 3]

df_zscore = df[(stats.zscore(df['idade']) >3)]


print('Outliers z-score:   ',df_zscore)
15


# filtrar endereços invalidos