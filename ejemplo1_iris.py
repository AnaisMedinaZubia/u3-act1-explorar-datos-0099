## Anais Medina NC 0099 fecha 04 noviembre 2026
import pandas as pd
import os
# URL del dataset público para leer datos de iris.csv
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
# Descargar y cargar el CSV
datos = pd.read_csv(url)

print(datos)
# Guardar una copia local en la carpeta datasets
datos.to_csv("datasets/iris.csv", index=False)
# Explorar los datos
print("PRIMERAS 5 FILAS")
print(datos.head()) 
print()
print("\\CANTIDAD DE FILAS Y COLUMNAS")
print(datos.shape)
print("mostrando nombre de las columnas")
print("\\NOMBRES DE LAS COLUMNAS")
print(datos.columns.tolist())

print("\\INFORMACION DEL DATASET (conjunto de datos)")
print(datos.info())

print("\\CARACTERISTICAS (X) tumba la columna especiales con drop")
X = datos.drop(columns=["species"])
print(X.head())

print("\\VARIABLE OBJETIVO (y)")
y = datos["species"]
print(y.head())

print("\\nESPECIES REGISTRADAS con la opcion unica")
print(y.unique())
print()
print("Anais Medina NC 0099")