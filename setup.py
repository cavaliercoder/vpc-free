#!/usr/bin/env python

"""
distutils/setuptools install script.
"""

import os
import re

from setuptools import setup

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')

def get_version():
    """
    get_version reads the version info from bin/vpc-free:__version__
    """

    init = open(os.path.join(ROOT, 'bin', 'vpc-free')).read()
    return VERSION_RE.search(init).group(1)

setup(name='vpc-free',
      version=get_version(),
      description='Find free IP address blocks in AWS EC2',
      long_description=open('README.rst').read(),
      url='http://github.com/cavaliercoder/vpc-free',
      author='Ryan Armstrong',
      author_email='ryan@cavaliercoder.com',
      license='Apache License 2.0',
      install_requires=['boto3'],
      scripts=['bin/vpc-free'])
