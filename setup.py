import glob
import os
import typing

import setuptools


setuptools.setup(name='movs-validator',
                 version='0.0.1',
                 author='Vito De Tullio',
                 author_email='vito.detullio@gmail.com',
                 description='movs validator',
                 url='https://github.com/ZeeD/movs-validator',
                 packages=setuptools.find_packages(),
                 python_requires='>=3.8',
                 install_requires=[
                     'movs'
                 ])
