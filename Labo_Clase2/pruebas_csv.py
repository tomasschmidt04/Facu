
import pandas as pd
df = pd.read_csv("cronograma_sugerido.csv")
filtro = df["Cuatrimestre"] == 5
df_filatrado = df[filtro]
df.insert(3,"Nota",[8,6,5,3,2,1,3,4,5,3,2,1,1,3])
d2 = df.assign(notas=[8,6,5,3,2,1,3,4,5,3,2,1,1,3])
print(d2)