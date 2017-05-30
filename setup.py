#!/usr/bin/env python

"""
distutils/setuptools install script.
"""

from setuptools import setup

setup(name='vpc-free',
      version='1.0',
      description='Find free IP blocks in AWS EC2',
      url='http://github.com/cavaliercoder/vpc-free',
      author='Ryan Armstrong',
      author_email='ryan@cavaliercoder.com',
      license='Apache License 2.0',
      scripts=['bin/vpc-free'])
