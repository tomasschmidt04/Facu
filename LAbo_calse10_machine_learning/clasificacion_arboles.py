#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 18:07:30 2023

@author: mcerdeiro
"""


from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import tree
import pandas as pd

#%%######################

        ####            Análisis exploratorio

#########################
#%%        
data = pd.read_csv('arboles.csv')
#%%
nbins = 70

f, s = plt.subplots(1,2)
plt.suptitle('Histogramas de altura y diámetro', size = 'large')


sns.histplot(data = data, x = 'altura_tot', hue = 'nombre_com', bins = nbins, stat = 'probability', palette = 'viridis', ax=s[0])

sns.histplot(data = data, x = 'diametro', hue = 'nombre_com', bins = nbins, stat = 'probability', palette = 'viridis', ax=s[1])

#%%
f, s = plt.subplots(2,2)
plt.suptitle('Histogramas de los 4 atributos', size = 'large')


sns.histplot(data = data, x = 'altura_tot', hue = 'nombre_com', bins = nbins, stat = 'probability', ax=s[0,0], palette = 'viridis')

sns.histplot(data = data, x = 'sepal width (cm)', hue = 'target', bins = nbins, stat = 'probability', ax=s[0,1], palette = 'viridis')

sns.histplot(data = data, x = 'petal length (cm)', hue = 'target', bins = nbins, stat = 'probability', ax=s[1,0], palette = 'viridis')

sns.histplot(data = data, x = 'petal width (cm)', hue = 'target', bins = nbins, stat = 'probability', ax=s[1,1], palette = 'viridis')
#%%######################

        ####            Árboles de decisión

#########################
#%%

X = data[['altura_tot', 'diametro', 'inclinacio']]
Y = data['nombre_com']
#%%        
        
clf_info = tree.DecisionTreeClassifier(criterion = "entropy", max_depth= 4)
clf_info = clf_info.fit(X, Y)


plt.figure(figsize= [20,10])
tree.plot_tree(clf_info, feature_names = ['altura_tot', 'diametro', 'inclinacio'], class_names = ['Ceibo', 'Eucalipto', 'Jacarandá', 'Pindó'],filled = True, rounded = True, fontsize = 8)
#%%

datonuevo= pd.DataFrame([dict(zip(['altura_tot', 'diametro', 'inclinacio'], [22,56,8]))])
clf_info.predict(datonuevo)


#%%
# otra forma de ver el arbol
r = tree.export_text(clf_info, feature_names=['altura_tot', 'diametro', 'inclinacio'])
print(r)
#%%



