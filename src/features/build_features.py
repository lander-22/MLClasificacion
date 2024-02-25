
import pandas as pd

def mostrar_datos_faltantes(df):
    """
    Muestra la cantidad y el porcentaje de datos faltantes en un DataFrame como un nuevo DataFrame.

    Argumentos:
        df: El DataFrame a analizar.

    Devuelve:
        Un DataFrame con la información sobre los datos faltantes.
    """

    total_datos = df.shape[0]

    columnas = ["Columna", "Número de datos nulos", "Porcentaje de datos nulos"]
    datos = []

    for columna in df.columns:
        numero_nulos = df[columna].isnull().sum()
        porcentaje_nulos = round((numero_nulos / total_datos) * 100, 2)
        datos.append([columna, numero_nulos, porcentaje_nulos])

    return pd.DataFrame(datos, columns=columnas)


def imputar_promedio(df, variables):
    """
    Imputa los datos faltantes de un listado de variables en un DataFrame utilizando el promedio de cada variable.

    Argumentos:
        df: El DataFrame a analizar.
        variables: Un iterable con las variables a imputar.

    Devuelve:
        Un DataFrame con los datos faltantes imputados.
    """

    for variable in variables:
        df[variable] = df[variable].fillna(df[variable].mean())

    return df


from sklearn.impute import KNNImputer

def imputar_knn_completo(df, variables, n_neighbors=5):
    """
    Imputa los datos faltantes de un listado de variables en un DataFrame utilizando el algoritmo KNN (K-Nearest Neighbors) y devuelve todas las variables.

    Argumentos:
        df: El DataFrame a analizar.
        variables: Un iterable con las variables a imputar.
        n_neighbors: El número de vecinos a utilizar en el algoritmo KNN.

    Devuelve:
        Un DataFrame con las variables imputadas y las que no lo fueron.
    """

    imputador = KNNImputer(n_neighbors=n_neighbors)

    df_imputado = pd.DataFrame(imputador.fit_transform(df[variables]), columns=variables)

    df_completo = pd.concat([df.drop(columns=variables), df_imputado], axis=1)

    return df_completo


from sklearn.impute import KNNImputer

def imputar_knn(df, variables, n_neighbors=5):
    """
    Imputa los datos faltantes de un listado de variables en un DataFrame utilizando el algoritmo KNN (K-Nearest Neighbors).

    Argumentos:
        df: El DataFrame a analizar.
        variables: Un iterable con las variables a imputar.
        n_neighbors: El número de vecinos a utilizar en el algoritmo KNN.

    Devuelve:
        Un DataFrame con los datos faltantes imputados.
    """

    imputador = KNNImputer(n_neighbors=n_neighbors)

    df_imputado = pd.DataFrame(imputador.fit_transform(df[variables]), columns=variables)

    return df_imputado



### Funcion para identificar y reemplazar atipicos

import numpy as np
import pandas as pd

def identificar_tratar_atipicos(df, variable, imputar_atipicos=False):
  """
  Esta función identifica los puntos atípicos en una variable de un DataFrame utilizando un boxplot y permite imputarlos o eliminarlos.

  Argumentos:
    df: El DataFrame que contiene la variable a analizar.
    variable: La variable a analizar.
    imputar_atipicos: Un booleano que indica si se deben imputar o eliminar los valores atípicos.

  Devuelve:
    Un DataFrame con la variable original, una columna con los valores atípicos y el número total de atípicos.
  """

  df_atipicos = df.copy()

  # Calcula el rango intercuartílico (IQR)
  iqr = df[variable].quantile(0.75) - df[variable].quantile(0.25)

  # Calcula el límite inferior y superior
  limite_inferior = df[variable].quantile(0.25) - (1.5 * iqr)
  limite_superior = df[variable].quantile(0.75) + (1.5 * iqr)

  # Identifica los valores atípicos
  df_atipicos[f"{variable}_atipico"] = np.where(df[variable] < limite_inferior, "Atipico", np.where(df[variable] > limite_superior, "Atipico", "Normal"))

  # Cuenta el número de valores atípicos
  numero_atipicos = df_atipicos[f"{variable}_atipico"].value_counts().get("Atipico", 0)

  # Calcula el porcentaje de valores atípicos
  porcentaje_atipicos = numero_atipicos / len(df) * 100

  # Imprime información sobre los valores atípicos
  print(f"Variable: {variable}")
  print(f"Número de valores atípicos: {numero_atipicos}")
  print(f"Porcentaje de valores atípicos: {porcentaje_atipicos:.2f}%")

  if imputar_atipicos:
    # Imputa los valores atípicos con el valor máximo
    df_atipicos[variable] = np.where(df[variable] < limite_inferior, limite_inferior, np.where(df[variable] > limite_superior, limite_superior,df[variable]))
    #df_atipicos[variable].where(df_atipicos[f"{variable}_atipico"] != "Atipico", limite_superior)
    print("Los valores atípicos se han imputado con el valor del limite superior e inferior respectivamente.")
  else:
    # Elimina los valores atípicos
    df_atipicos = df_atipicos[df_atipicos[f"{variable}_atipico"] != "Atipico"]
    print("Los valores atípicos se han eliminado.")

  return df_atipicos[variable]
