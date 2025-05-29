from setuptools import setup, find_packages

setup(
    name='zonos',
    version='0.1',
    packages=find_packages(include=['zonos', 'zonos.*']),
)