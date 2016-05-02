# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='series_temporales_2016',
    version='0.0.1',
    description='series temporales dmkd uba tpfinal 2016',
    long_description=readme,
    author='JAS1/EV/EG/NC/DA',
    author_email='jspairani.registros@gmail.com',
    url='https://github.com/jas1/series_temporales_2016',
    license=MIT,
    packages=find_packages(exclude=('tests', 'docs'))
)

