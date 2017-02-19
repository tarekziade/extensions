# -*- coding: utf8 -*-
import os
from distutils.core import setup

README = os.path.join(os.path.dirname(__file__),
                      'extensions', 'README.txt')

setup(name='extensions',
      version='0.5',
      description='Simple plugin system',
      long_description=open(README).read(),
      author='Tarek Ziade',
      author_email='tarek@ziade.org',
      url='http://pypi.python.org/pypi/extensions',
      packages=['extensions', 'extensions.command']
      )

