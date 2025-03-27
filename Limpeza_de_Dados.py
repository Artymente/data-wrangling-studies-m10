import pandas as pd


# Setar Dados Iniciais
df = pd.read_csv('clientes.csv')

pd.set_option('display.width', None)

print(df.head(15))
print(df.tail(15))

#Remover dados
df.drop('pais',axis = 1 ,inplace = True) #Coluna
df.drop(2,axis = 0 ,inplace = True ) #Linha

#Normalizar Dados
df['nome'] = df['nome'].str.strip().str.upper()
df['endereco'] = df['endereco'].str.strip().str.upper()
df['estado'] = df['estado'].str.strip().str.upper()

#Converter tipos de Dados
df['idade'] = df['idade'].astype(int)


print('\nNormalizar textos:  \n\n', df.head())
#Tratar valores nulos

print(df)
print('\nValores nulos:  \n', df.isnull().sum().sum())


print('tratando valores nulos')


df = df.dropna(thresh=3)
df = df.dropna(subset=['data'])
df['estado']= df['estado'].fillna('Desconhecido')
df.fillna({'endereco':'Endereco não informado'})
df['idade-corrigida'] = df['idade'].fillna(df['idade'].mean())
df = df.fillna('Desconhecido')

print('\nValores nulos:  \n', df.isnull().sum().sum())

#tratar formato de dados
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')


#tratar dados duplicados
print('\nQuantidades de registros atuais:  \n', df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset='cpf', inplace= True)
print('\nQtd Registros removendo as duplicatas:  \n', len(df))
print(df.head())
#Formatando dados e gerando novo arquivo

df['idade'] = df['idade-corrigida']
df['data'] = df['data_corrigida']

df_salvar = df[['nome','cpf','idade','data','endereco','estado']]

print("\n\n\n\nDeseja Salvar o Arquivo \n")
print("\n(1)Sim desejo Salvar o Arquivo ")
print("(2)não desejo Salvar o Arquivo \n")

desisao = int(input("digite 1 ou 2:            "))

if desisao == 1:
    df_salvar.to_csv('clientes-limpeza.csv', index=False)
    print('Novo DataFrame: \n', pd.read_csv('clientes-limpeza.csv'))

else:
    print(df_salvar)
    print("Até logo")