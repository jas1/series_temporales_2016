# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath('..'))

# aca vas declarando todo lo que estaria en el .context en los test. ver la parte de arriba de imports de los test.
# aparecen amarillos pero porque no se usan directo en este archivo sino que se usan en los test
import pandas
import series_temporales_2016
from matplotlib import pyplot