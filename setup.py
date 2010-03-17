#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='goonsay',
      version='0.1',
      packages=find_packages(),
      package_data={'goonsay': ['bin/*.*', 'static/*.*', 'templates/*.*']},
      exclude_package_data={'goonsay': ['bin/*.pyc']},
      scripts=['goonsay/bin/manage.py'])
