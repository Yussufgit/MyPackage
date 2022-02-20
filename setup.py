from gettext import install
import opcode
from unicodedata import name
import numpy
from setuptools import setup, find_packages

setup(
    name='MyPackage',
    version='1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/yussufgit/MyPackage',
    author='Yussuf Abdiwali',
    author_email='yussufmohamed608@gmail.com'

)