#!/usr/bin/python

try:
  from setuptools import setup, find_packages
except Exception:
  from distutils.core import setup, find_packages

packages = find_packages()

setup(
    name = 'render',
    version = '0.0.4',
    author = '@inconvergent',
    install_requires = ['numpy>=1.8.2'],
    license = 'MIT',
    packages = packages
)

