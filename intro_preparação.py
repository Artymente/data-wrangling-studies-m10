import pandas as pd

#formatar display para tamanho Maximo

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#importar Data Frame
df = pd.read_csv('clientes-v2.csv')
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y' , errors='coerce')

#Exibir data frame

print(df.head().to_string())
print(df.tail().to_string())

#Verificar e identificar dados Nulos
print(f'Verificação inicial:\n ')
print(df.info())
print(f'\n Analizando dados nulos: \n {df.isnull().sum()}')
print(f'\n Total dados nulos: \n {df.isnull().sum().sum()}')
print(f'\n Total dados nulos em porcentagem ( % ): \n \n {df.isnull().mean() * 100}')

#Remover Dados Nulos
print("Removendo Dados Nulos.............\n")
df = df.dropna()
print("Dados Nulos Removidos - Reanalizando........")

#Verificar e identificar dados Nulos Novamente
print(f'\n Analizando dados nulos: \n ')
print(df.isnull().sum())
print(f'\n Total dados nulos: \n')
print(df.isnull().sum().sum())


print(f'Verificação secundaria:\n {df.info()}')
print(f'\n Analizando dados nulos: \n {df.isnull().sum()}')
print(f'\n Total dados nulos: \n {df.isnull().sum().sum()}')
print(f'\n Total dados nulos em porcentagem ( % ): \n \n {df.isnull().mean() * 100}')


#Verificar dados Nulos Novamente
print('\nAnalizando dados Duplicados: \n', df.duplicated().sum())
print('\nAnalizando dados Unicos: \n', df.nunique())
print('\nAnalizando Estatistica: \n\n', df.describe())


#Remover dados Sensiveis
df = df[['idade','estado','salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'anos_experiencia','area_atuacao']]

#Exibir data frame modificado
print('\n',df.head().to_string())
print('\n', df.tail().to_string())

