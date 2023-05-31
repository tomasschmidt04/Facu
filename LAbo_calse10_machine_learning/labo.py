import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score




data = [[0, 104], [50, 106], [100, 112],[200,117],[300,115.30],[400,117.30],[500,130.22],[750,139.80],[1000,140.60],
        [1250,154.12],[1750,170.50]]

df = pd.read_csv("data_alq_caba.csv", index_col = 'id')
x1 = (df[['surface_total']])
y =df[['price']]
rls = linear_model.LinearRegression()
rls.fit(x1,y)





rls.coef_
rls.intercept_
rls.score(x1,y)#Capacidad de predecir del modelo
y_pred = rls.predict(x1)


df = pd.read_csv("data_alq_caba.csv", index_col = 'id')
x3 = (df[['surface_total', 'surface_total']])
y3 =df[['price']]
rls2 = linear_model.LinearRegression()
rls2.fit(x3,y3)

rls2.coef_
rls2.intercept_
rls2.score(x3,y3)#Capacidad de predecir del modelo
y_pred3 = rls2.predict(x3)


grado = 3 # En grado 3 osea elevando a la 3 los elementos de x osea apoximando con una cubica. 
x4 = (df[['surface_total']])
y4 =df[['price']]
pol = PolynomialFeatures(grado)
X5= pol.fit_transform(x4) # Transformalo al cuadrado
rls3 = linear_model.LinearRegression() #1) Inicializo
rls3.fit(X5,y4)#2) Entreno el modelo

rls3.coef_
rls3.intercept_
rls3.score(X5,y4)
y_pred4 = rls3.predict(X5)#3) muestro los valores de y de mi recta de "prediccion"

grado = 3# Aca testeo cuan grande es el error(residuo) de mi prediccion con la regresion lineal 
pol = PolynomialFeatures(grado)
test= pd.read_csv('otra_data.csv',index_col = 'id')`
x6 = test[['price']]
x7 = pol.fit_transform(x6)

y_pred7 = rls3.predict(x7)
y_posta = test[['price']]
print('MSE del modelo polinomial, e test %.2f'% mean_squared_error(y_posta,y_pred7))



rls.score(x1,y)#Capacidad de predecir del modelo
y_pred = rls.predict(x1)
plt.scatter(x,y,color='black')
plt.plot(x,model.predict(x),color='blue',linewidth=3)
plt.xlabel('Dosis de RU(ug/huevo)')
plt.ylabel('Indice de daño')
plt.show()

print(model.score(x,y))


#

data1 = [[0, 104], [50, 106], [100, 112],[200,117],[300,115.30],[400,117.30],[500,130.22],[750,139.80],[1000,140.60],
        [1250,154.12],[1750,170.50]]

df1 = pd.read_csv('/home/clinux01/Descargas/datos_libreta_4622.csv')
print(df1)
x1 = pd.DataFrame(df1['RU'])
y1 = pd.DataFrame(df1['ID'])

model = linear_model.LinearRegression()
model.fit(x1,y1)

print(model.coef_)
print(model.intercept_)
print(model.score(x,y))