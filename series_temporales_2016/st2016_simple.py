# -*- coding: utf-8 -*-
# ---------------------------------- IMPORTS NECESARIOS ----------------------------------

# aca vas declarando todo lo que estaria en el .context en los test. ver la parte de arriba de imports de los test.
# aparecen amarillos pero porque no se usan directo en este archivo sino que se usan en los test
import pandas as pd
import random as rnd
import numpy as np
import matplotlib.pyplot as plt
import cmath
# a partir de aca voy poniendo lo relacionado con TPFinal ST2016
# idea incial: replicar lo mismo que R 
# este archivo tiene la declaracion de todas las funciones que vamos usando
# despues si vale la pena evolucionamos a objetos u otra cosa, por ahora con funciones a lo bruto basta.

# ---------------------------------- FUNCIONES QUE HACEN LA MAGIA  ----------------------------------

# pasos cargar archivo
def levantar_archivo_df():
    archivo_nombre = 'sensores_veralli_inner_join.txt'
    archivo_df =  pd.read_csv(archivo_path+'/'+archivo_nombre)
    return  archivo_df

# para levantar el archivo indexado por la columna de tiempo
def levantar_archivo_dfidx(archivo_path,archivo_nombre):
    archivo_df =  pd.read_csv(archivo_path+'/'+archivo_nombre,index_col=0)
    return  archivo_df

# para hacer el plot basico de x e y en funcion de t ( que esta tomado como indice )
def plotear_basico(dataframe_archivo,cant_rows ):
    df_reducido = dataframe_archivo.head(cant_rows)
    df_reducido.plot()
    plt.show()
  
def funcion_corre_levantador (num_muestras,path_archivo,nom_archivo):  
    n = num_muestras
    tmp_df=levantar_archivo_dfidx(archivo_path,nom_archivo)
    plotear_basico(tmp_df, n)    
# ---------------------------------- EJECUCION DE LA MAGIA ----------------------------------
# declaro el path global en este archivo que es donde estarian los datasets
# los nombres de los datasets se respetan tal cual se sube al drive.
archivo_path = '/home/julio/Dropbox/julio_box/educacion/maestria_explotacion_datos_uba/materias/cuat_3_secuencias_temporales/TP_grupal/sensores'
archivo_nombre = 'sensores_veralli_inner_join.txt'
cantidad_muestras= 5000
#archivo_path = 'C:\\SeriesTiempo'  
    
# codigo a ejecutar
#funcion_corre_levantador(cantidad_muestras,archivo_path,archivo_nombre)

# Ejercicios Clase 1: 
def funcion1_hacer_grafico_con_bandas():
    # codigo R a replicar
    #set.seed(12345)
    rnd.seed(12345)
#     tiempo = np.arange(0,11,0.1)
#     N = len(tiempo)
#   ``sigma * np.random.randn(...) + mu``
#     x = (np.random.randn (N) * cmath.sqrt(0.5) ) +2
        #tiempo <- seq(from=0 , to=10, by= 0.1 )  
#    http://mathesaurus.sourceforge.net/r-numpy.html
#    seq(from=10,to=1,by=-3) >>> arange(10,0,-3)
    #N <-  length(tiempo)
    #x <- rnorm (N , mean=2, sd=0.5)    
    #mean(x)
    #sd(x)    
    #plot(tiempo , x , type='l')
    #abline(h=mean(x), lty=2)
    #abline(h=mean(x)+2*sd(x), lty=3)
    #abline(h=mean(x)-2*sd(x), lty=3)

