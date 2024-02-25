## Grafico para analisis univariado de variables cuantitativas
# Create a function that we can re-use
def show_distribution(var_data):
    from matplotlib import pyplot as plt

    # Get statistics
    min_val = var_data.min()
    max_val = var_data.max()
    mean_val = var_data.mean()
    med_val = var_data.median()
    mod_val = var_data.mode()[0]

    print('Minimum:{:.2f}\nMean:{:.2f}\nMedian:{:.2f}\nMode:{:.2f}\nMaximum:{:.2f}\n'.format(min_val,
                                                                                            mean_val,
                                                                                            med_val,
                                                                                            mod_val,
                                                                                            max_val))

    # Create a figure for 2 subplots (2 rows, 1 column)
    fig, ax = plt.subplots(2, 1, figsize = (10,4))

    # Plot the histogram   
    ax[0].hist(var_data)
    ax[0].set_ylabel('Frequencia')

    # Add lines for the mean, median, and mode
    ax[0].axvline(x=min_val, color = 'gray', linestyle='dashed', linewidth = 2)
    ax[0].axvline(x=mean_val, color = 'cyan', linestyle='dashed', linewidth = 2)
    ax[0].axvline(x=med_val, color = 'red', linestyle='dashed', linewidth = 2)
    ax[0].axvline(x=mod_val, color = 'yellow', linestyle='dashed', linewidth = 2)
    ax[0].axvline(x=max_val, color = 'gray', linestyle='dashed', linewidth = 2)

    # Plot the boxplot   
    ax[1].boxplot(var_data, vert=False)
    ax[1].set_xlabel(f'Valores de {var_data.name}')
    # Add a title to the Figure
    fig.suptitle(f'Distribution de la variable {var_data.name}')

    # Show the figure
    fig.show()


##################################
    
import seaborn as sns
from matplotlib import pyplot as plt

def graficar_boxplot(df, variable_target, variable_numerica):
  """
  Esta función grafica un boxplot para una variable categórica y una variable numérica.

  Argumentos:
    df: El DataFrame que contiene las variables a analizar.
    variable_target: La variable categórica.
    variable_numerica: La variable numérica.

  Devuelve:
    Un gráfico de boxplot.
  """

  # Crea un boxplot
  sns.boxplot(x=variable_target, y=variable_numerica, data=df)

  # Establece el título del gráfico
  plt.title("Boxplot de {} vs {}".format(variable_numerica, variable_target))

  # Muestra el gráfico
  plt.show()


#######################################
import seaborn as sns
import matplotlib.pyplot as plt

def graficar_barplot(df, variable_target, variable_categorica):
  """
  Esta función grafica un barplot para dos variables categóricas.

  Argumentos:
    df: El DataFrame que contiene las variables a analizar.
    variable_target: La variable categórica objetivo.
    variable_categorica: La variable categórica a analizar.

  Devuelve:
    Un gráfico de barplot.
  """
  df_group_to_graph = df[[variable_categorica, variable_target]].groupby([variable_categorica, variable_target]).size().to_frame().reset_index().rename(columns={0: 'count'}) 

  # Crea un barplot
  sns.barplot(x=variable_categorica, y="count", hue=variable_target, data=df_group_to_graph, palette="Set1")

  # Establece el título del gráfico
  plt.title("Barplot de {} vs {}".format(variable_categorica, variable_target))

  # Establece la etiqueta del eje y
  plt.ylabel("Conteo")

  # Rota las etiquetas del eje X verticalmente
  plt.xticks(rotation=90)

  # Muestra el gráfico
  plt.show()







