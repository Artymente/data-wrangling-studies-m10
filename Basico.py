import pandas as pd

df = pd.read_csv('clientes.csv')


#Verificar dados
print(df.head().to_string())

print(df.tail().to_string())


#verificar Quantidade de Dados
print("Qd:",df.shape)

#Verificar tipos de Dados
print("Tipagem:", df.dtypes)

print("Valores NULOS", df.isnull() )