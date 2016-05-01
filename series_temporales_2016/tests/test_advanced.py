# -*- coding: utf-8 -*-

from .context import series_temporales_2016 as st2016
from .context import pandas as pd
from .context import pyplot as plt

import unittest

# esta clase es para ir probando las funciones
# se pueden ejecutar casos completos desde aca
# o se pueden ir ejecutando partes a travez de una consola python
class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    # levanta archivo y muestra los primeros 5 y describe los cmapos tipo summary de R        
    # vuelve a hacer lo mismo pero acotado a los 1ros 5000
    def test_cargar_archivo(self):
        tmp_df=st2016.levantar_archivo_dfidx()
        tmp_df_chico = tmp_df.head(5000)

        pd.set_option('display.float_format', lambda x: '%.3f' % x)
        print(tmp_df.head(5))
        print(tmp_df.describe())
        
        print('\n---- achicado ---- \n')
        print(tmp_df_chico.head(5))
        print(tmp_df_chico.describe())
    
    # estoy hace el plot base levanta el archivo y hace el plot acotado a una muestra de 5000
    def test_plotear_base(self):
        n = 5000
        tmp_df=st2016.levantar_archivo_dfidx()
        st2016.plotear_basico(tmp_df, n)
        

    # intento nro 0 carga de archivo: VIEJO !
    # no lo borro porque tiene referencias a donde fui sacando info de como hacer las cosas 
    def test_cargar_archivo_old(self):
        tmp_df=st2016.levantar_archivo_dfidx()
#    para acotar la muestra
#    http://pandas.pydata.org/pandas-docs/stable/10min.html
#         plt.figure(1) # sin esto no me aparece el output visual :U solo codigos en consola.
        tmp_df_chico = tmp_df.head(5000)
        tmp_df_chico.plot()
        plt.show()
#    para el plot
#    http://matplotlib.org/users/pyplot_tutorial.html
#         plt.figure(1) # sin esto no me aparece el output visual :U solo codigos en consola. 
#         plt.plot(tmp_df_chico) 
#         plt.ylabel('some numbers')
#         plt.plot(tmp_df_chico['t'], tmp_df_chico['valor.x'], linewidth=2.0)
#         plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
#         plt.plot(tmp_df_chico['t'], tmp_df_chico['valor.x'], 'k')
#         plt.show()
#     para el formato no cientifico 
#     http://stackoverflow.com/questions/21137150/format-suppress-scientific-notation-from-python-pandas-aggregation-results
        pd.set_option('display.float_format', lambda x: '%.3f' % x)
        print(tmp_df.head(5))
        print(tmp_df.describe())
        
        print('\n---- achicado ---- \n')
        print(tmp_df_chico.head(5))
        print(tmp_df_chico.describe())

if __name__ == '__main__':
    unittest.main()