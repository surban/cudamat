#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name="cudamat",
    version="0.3",
    description="CUBLAS for Python",
    license="BSD",
    keywords="CUDA CUBLAS",
    packages=find_packages(exclude=['examples', 'test']),
    include_package_data=True,
	author='Volodymyr Mnih',
	author_email='vlad.mnih@gmail.com',
)
