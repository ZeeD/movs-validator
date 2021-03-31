from setuptools import find_packages
from setuptools import setup

setup(name='movs-validator',
      version='0.0.1',
      author='Vito De Tullio',
      author_email='vito.detullio@gmail.com',
      description='movs validator',
      url='https://github.com/ZeeD/movs-validator',
      packages=find_packages(),
      python_requires='>=3.8',
      package_dir={'': 'src'},
      install_requires=[
          'movs'
      ],
      package_data={
          'movsvalidator': ['py.typed'],
      },
      entry_points={
          'console_scripts': [
              'movs-validator = movsvalidator:main'
          ]
      })
