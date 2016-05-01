# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

# a partir de aca voy poniendo lo relacionado con TPFinal ST2016
# idea incial: replicar lo mismo que R 
# este archivo tiene la declaracion de todas las funciones que vamos usando
# despues si vale la pena evolucionamos a objetos u otra cosa, por ahora con funciones a lo bruto basta.

# declaro el path global en este archivo que es donde estarian los datasets
# los nombres de los datasets se respetan tal cual se sube al drive.
archivo_path = 'C:/Users/julio/Dropbox/julio_box/educacion/maestria_explotacion_datos_uba/materias/cuat_3_secuencias_temporales/TP_grupal/sensores'

# pasos cargar archivo
def levantar_archivo_df():
    archivo_nombre = 'sensores_veralli_inner_join.txt'
    archivo_df =  pd.read_csv(archivo_path+'/'+archivo_nombre)
    return  archivo_df

def levantar_archivo_dfidx():
    archivo_nombre = 'sensores_veralli_inner_join.txt'
    archivo_df =  pd.read_csv(archivo_path+'/'+archivo_nombre,index_col=0)
    return  archivo_df

def plotear_basico(dataframe_archivo,cant_rows ):
    df_reducido = dataframe_archivo.head(cant_rows)
    df_reducido.plot()
    plt.show()