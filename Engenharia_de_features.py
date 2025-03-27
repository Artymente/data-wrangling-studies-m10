import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('Clientes2Tratados.csv')

print(f'Primeiro Print DF:\n{df.head()}\n')

#transformação logaritmica

df['salario_log'] = np.log1p(df['salario'])

print(f'Transformação Logaritima DF:\n{df.head()}\n')

#transformação Boxcox

df['salario_Boxcox'], _ = stats.boxcox(df['salario'] + 1)

print(f'Transformação Boxcox DF:\n{df.head()}\n')


