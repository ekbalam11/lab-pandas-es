# Laboratorio de Introducción a Pandas

# Completa el siguiente conjunto de ejercicios para consolidar tu conocimiento de los fundamentos de Pandas.

### 1. Importa Numpy y Pandas y asígnalos los alias `np` y `pd` respectivamente.
import pandas as pd

import numpy as np
### 2. Crea una Serie de Pandas que contenga los elementos de la lista a continuación.
lst = [5.7, 75.2, 74.4, 84.0, 66.5, 66.3, 55.8, 75.7, 29.1, 43.7]
serie = pd.Series(lst)
serie
### 3. Usa la indexación para devolver el tercer valor en la Serie anterior.

# Sugerencia: Recuerda que la indexación comienza en 0.*
# Tu código aquí
third_value = serie[3]
print(third_value)
### 4. Crea un DataFrame de Pandas a partir de la lista de listas a continuación. Cada sublista debe representarse como una fila.
b = [[53.1, 95.0, 67.5, 35.0, 78.4],
     [61.3, 40.8, 30.8, 37.8, 87.6],
     [20.6, 73.2, 44.2, 14.6, 91.8],
     [57.4, 0.1, 96.1, 4.2, 69.5],
     [83.6, 20.5, 85.4, 22.8, 35.9],
     [49.0, 69.0, 0.1, 31.8, 89.1],
     [23.3, 40.7, 95.0, 83.8, 26.9],
     [27.6, 26.4, 53.8, 88.8, 68.5],
     [96.6, 96.4, 53.4, 72.4, 50.1],
     [73.7, 39.0, 43.2, 81.6, 34.7]]
# Tu código aquí
df = pd.DataFrame(b)
print(df)
### 5. Renombra las columnas del DataFrame basándote en los nombres de la lista a continuación.
b = [[53.1, 95.0, 67.5, 35.0, 78.4],
     [61.3, 40.8, 30.8, 37.8, 87.6],
     [20.6, 73.2, 44.2, 14.6, 91.8],
     [57.4, 0.1, 96.1, 4.2, 69.5],
     [83.6, 20.5, 85.4, 22.8, 35.9],
     [49.0, 69.0, 0.1, 31.8, 89.1],
     [23.3, 40.7, 95.0, 83.8, 26.9],
     [27.6, 26.4, 53.8, 88.8, 68.5],
     [96.6, 96.4, 53.4, 72.4, 50.1],
     [73.7, 39.0, 43.2, 81.6, 34.7]]
# Tu código aquí
colnames = ['Score_1', 'Score_2', 'Score_3', 'Score_4', 'Score_5']
df = pd.DataFrame(b, columns=colnames)
print(df)
### 6. Crea un subconjunto de este DataFrame que contenga solo las columnas de Puntuación 1, 3 y 5.
# Tu código aquí
df_subset = df[['Score_1', 'Score_3', 'Score_5']]
print(df_subset)
### 7. Del DataFrame original, calcula el valor promedio de Score_3.
# Tu código aquí
mean_score_3 = df['Score_3'].mean()
print(mean_score_3)
### 8. Del DataFrame original, calcula el máximo valor del Score_4.
# Tu código aquí
max_score_4 = df['Score_4'].max()
print(max_score_4)
### 9. Del DataFrame original, calcula la media valor del Score_2.
# Tu código aquí
median_score_2 = df['Score_2'].median()
print(median_score_2)
### 10. Crea un DataFrame de Pandas a partir del diccionario de pedidos de productos a continuación.
orders = {'Description': ['LUNCH BAG APPLE DESIGN',
  'SET OF 60 VINTAGE LEAF CAKE CASES ',
  'RIBBON REEL STRIPES DESIGN ',
  'WORLD WAR 2 GLIDERS ASSTD DESIGNS',
  'PLAYING CARDS JUBILEE UNION JACK',
  'POPCORN HOLDER',
  'BOX OF VINTAGE ALPHABET BLOCKS',
  'PARTY BUNTING',
  'JAZZ HEARTS ADDRESS BOOK',
  'SET OF 4 SANTA PLACE SETTINGS'],
 'Quantity': [1, 24, 1, 2880, 2, 7, 1, 4, 10, 48],
 'UnitPrice': [1.65, 0.55, 1.65, 0.18, 1.25, 0.85, 11.95, 4.95, 0.19, 1.25],
 'Revenue': [1.65, 13.2, 1.65, 518.4, 2.5, 5.95, 11.95, 19.8, 1.9, 60.0]}
# Tu código aquí
df_orders = pd.DataFrame(orders)
print(df_orders)
### 11. Calcula la cantidad total pedida y los ingresos generados a partir de estos pedidos.
# Tu código aquí
total_quantity = df_orders['Quantity'].sum()
total_revenue = df_orders['Revenue'].sum()
print(total_quantity)
print(total_revenue)
### 12. Obten los precios del artículo más caro y del más barato pedidos e imprime la diferencia.
# Tu código aquí
max_price = df_orders['UnitPrice'].max()
min_price = df_orders['UnitPrice'].min()
price_diff = max_price - min_price
print(max_price)
print(min_price)
print(price_diff)

