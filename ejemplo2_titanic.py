import pandas as pd
import os

# URL del conjunto de datos
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
# Descargar y cargar
datos = pd.read_csv(url)
# Guardar archivo titanic.csv en carpeta datasets
datos.to_csv("datasets/titanic.csv", index=False)

# Explorar información
print("PRIMEROS 5 PASAJEROS")
print(datos.head())
print("\\DIMENSIONES")
print(datos.shape)
print("\\COLUMNAS")
print(datos.columns.tolist())
print("\\INFORMACION GENERAL")
print(datos.info())
# Identificar características
columnas = ["pclass", "sex", "age", "fare", "sibsp", "parch"]

X = datos[columnas]

# Identificar variable objetivo
y = datos["survived"]

print("\\CARACTERISTICAS (X)")
print(X.head())
print("\\VARIABLE OBJETIVO (y)")
print(y.head())
print("\\CANTIDAD DE SUPERVIVIENTES")
print(y.value_counts())
print("\\VALORES FALTANTES")
print(datos.isnull().sum())

print("Anais Medina NC 009")