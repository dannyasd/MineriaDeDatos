import pandas as pd
import numpy as np

#función para el muestro sistemático
def muestreo_sistematico(df, pasos):
    
    #np.arange muestra valores espaciados por pasos
    indices = np.arange(0,len(df),step=pasos)
    #iloc obtiene filas o columnas en posiciones particulares de un índice
    muestra_sistematica = df.iloc[indices]
    
    return muestra_sistematica

def muestreo_agrupamiento(df, num_de_clusters):
    
    try:
        # Divide en unidades de grupo de igual tamaño
        #np.repeat: repite los elementos de un arreglo
        df['cluster_id'] = np.repeat([range(1,num_de_clusters+1)],len(df)/num_de_clusters)

        # Crear una lista vacía
        indexes = []

        # Append the indexes from the clusters that meet the criteria
        #Añade los índices de grupos que satisfacen los criterios
        # Para esta fórmula los grupos deben de ser pares
        for i in range(0,len(df)):
            if df['cluster_id'].iloc[i]%2 == 0:
                indexes.append(i)
        muestra_cluster = df.iloc[indexes]
        return muestra_cluster
    
    except:
        return
    
