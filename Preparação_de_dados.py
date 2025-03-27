#explorar e analisar Dados
import pandas as pd

pd.set_option('display.max_rows', None)  # Mostra todas as linhas
pd.set_option('display.max_columns', None)  # Mostra todas as colunas
pd.set_option('display.width', 1000)  # Ajusta a largura da saída
pd.set_option('display.max_colwidth', None)  # Exibe todo o conteúdo das células


df = pd.read_csv('clientes-v2.csv')
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

print(df.head().to_string())
print(df.tail().to_string())

print('\nVerificação Inicial:\n')
print(df.info())


print('\nVerificação Dados nulos:\n')
print(df.isnull().sum())
print('\nPorcentagem(%) Dados nulos:\n',df.isnull().mean() * 100 )

#Tratar dados Nulos
df.dropna(inplace=True)

print('\nConfirmação de remoção dados nulos ou incompletos:\n',df.isnull().sum().sum() )

print('Analise Dados Duplicados:\n', df.duplicated().sum(),'\n')

print('Analise Dados unicoa:\n', df.nunique())

print('Estatisticas Dados:\n', df.describe())


df = df[['idade','data','estado','salario','nivel_educacao','numero_filhos','estado_civil', 'area_atuacao']]

print(df.head())
print(df.tail())

df.to_csv('Clientes2Tratados.csv', index= False)
