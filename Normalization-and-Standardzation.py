import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('Clientes2Tratados.csv')

print(df.head())

df = df[['idade','salario']]


#Normalizacao - min_max_scaler
scaler = MinMaxScaler()

df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1,1))
df['idadeMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['salario']])

#Padronização StandardScaler (media)

scaler = StandardScaler()
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])

#padronização RobustScaler(mediana)
scaler = RobustScaler()
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])

print(df.head(15))

print('MinMaxScaler de (de 0 a 1):\n')

print('Idade Min = {:.4f}. '
      'Max = {:.4f}. '
      'Mean = {:.4f} . '
      'STD = {:.4f}'
      .format(df['idadeMinMaxScaler'].min(),
    df['idadeMinMaxScaler'].max(),
    df['idadeMinMaxScaler'].mean(),
    df['idadeMinMaxScaler'].std()))

print('Salario Min = {:.4f}.'
      ' Max = {:.4f} .  '
      'Mean = {:.4f} . '
      'STD = {:.4f}'
      .format(df['salarioMinMaxScaler'].min(),
              df['salarioMinMaxScaler'].max(),
              df['salarioMinMaxScaler'].mean(),
              df['salarioMinMaxScaler'].std()))

print('MinMaxScaler  (de -1 a 1):\n')
print('Idade Min = {:.4f}. '
      'Max = {:.4f} .  '
      'Mean = {:.4f} . '
      'STD = {:.4f}'
      .format(df['idadeMinMaxScaler_mm'].min(),
              df['idadeMinMaxScaler_mm'].max(),
              df['idadeMinMaxScaler_mm'].mean(),
              df['idadeMinMaxScaler_mm'].std()))

print('Salario Min = {:.4f}.'
      ' Max = {:.4f} . '
      ' Mean = {:.4f} .'
      ' STD = {:.4f}'
      .format(df['salarioMinMaxScaler_mm'].min(),
              df['salarioMinMaxScaler_mm'].max(),
              df['salarioMinMaxScaler_mm'].mean(),
              df['salarioMinMaxScaler_mm'].std()))

print('StandardScaler (Ajusta a media a 0):\n')
print('Idade Min = {:.4f}.'
      ' Max = {:.4f} .'
      '  Mean = {:.4f} .'
      ' STD = {:.4f}'
      .format(df['idadeStandardScaler'].min(),
              df['idadeStandardScaler'].max(),
              df['idadeStandardScaler'].mean(),
              df['idadeStandardScaler'].std()))

print('Salario Min = {:.4f}.'
      ' Max = {:.4f} . '
      ' Mean = {:.4f} . '
      'STD = {:.4f}'
      .format(df['salarioStandardScaler'].min(),
              df['salarioStandardScaler'].max(),
              df['salarioStandardScaler'].mean(),
              df['salarioStandardScaler'].std()))

print('RobustScaler  (Ajusta a media a IQR):\n')

print('Idade Min = {:.4f}.'
      ' Max = {:.4f} . '
      ' Mean = {:.4f} .'
      ' STD = {:.4f}'
      .format(df['idadeRobustScaler'].min(),
              df['idadeRobustScaler'].max(),
              df['idadeRobustScaler'].mean(),
              df['idadeRobustScaler'].std()))

print('Salario Min = {:.4f}. '
      'Max = {:.4f} .'
      '  Mean = {:.4f} . '
      'STD = {:.4f}'
      .format(df['salarioRobustScaler'].min(),
              df['salarioRobustScaler'].max(),
              df['salarioRobustScaler'].mean(),
              df['salarioRobustScaler'].std()))

