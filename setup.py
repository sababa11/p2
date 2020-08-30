#!/usr/bin/env python

from setuptools import setup

setup(
    name='p2',
    version='0.1',
    description='Python Distribution Utilities',
    author='Adam Ta',
    author_email='notrelevant@gmail.net',
    url='https://github.com/sababa11/p1.git',
    install_requires=['boto==1.14.51', 'p1==0.1'],
    packages=['p2'],
    )

print("OK")
