
import pandas as pd

def eleva_cubo(x):
        return x**3


df = pd.DataFrame({'numeros':[1,2,3,4,5,6,7,8,9,10]})

df["cubo_funcao"] = df['numeros'].apply(eleva_cubo)
df['Lambda'] = df['numeros'].apply(lambda x: x ** 3)

print(df)
