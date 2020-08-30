#!/usr/bin/env python

from setuptools import setup

setup(
    name='p2',
    version='0.1',
    description='Python Package 2',
    author='Adam Ta',
    author_email='notrelevant@mail.net',
    url='https://github.com/sababa11/p2.git',
    install_requires=['boto3==1.14.51', 'p1==0.1'],
    packages=['p2'],
    )

print("OK")
