from setuptools import find_packages
from setuptools import setup

setup(name='movs-validator',
      version='0.0.0',
      url='https://github.com/ZeeD/movs-validator',
      author='Vito De Tullio',
      author_email='vito.detullio@gmail.com',
      packages=find_packages(),
      install_requires=[
          'movs'
      ],
      package_data={
          'movsvalidator': ['py.typed'],
      },
      entry_points={
          'console_scripts': [
              'movs-validator = movsvalidator.__main__:main'
          ]
      })
