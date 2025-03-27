import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('Clientes2Tratados.csv')
pd.set_option('display.width',None)
pd.set_option('display.max_colwidth',None)

print(df.head())

#Codificação one-hot para estado-civil
df = pd.concat([df,pd.get_dummies(df['estado_civil'],prefix='estado_civil')],axis=1)
print(f'DF apos codificação one-hot: \n, {df.head()} \n')

#codificacao ordinal para nivel educacional
educacao_ordinal = {'Ensino Médio':2,'Ensino Fundamental':1, 'Ensino Superior':3, 'Pos-Graduação':4}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordinal)
print(f'DF apos codificação ordinal: \n, {df.head()} \n')


#codificacao label para estado
label_encoder = LabelEncoder()
df['estado'] = label_encoder.fit_transform(df['estado'])

print(f'DF apos codificação labelencoder: \n {df.head()}')