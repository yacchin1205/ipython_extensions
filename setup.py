#!/usr/bin/env python

from setuptools import setup

setup(name='ToC nbextension',
      version='0.1',
      description='ToC extension for Jupyter Notebook',
      packages=['nbextension_toc'],
      package_data={'nbextension_toc/static': ['*']},
      include_package_data=True
     )