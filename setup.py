#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages


setup(name='pjg_sound',
      version='0.1',
      description='Sound processing utilities',
      author='Ethan Cowan',
      author_email='ethanc@poeticjustice.group',
      url='',
      install_requires=[
            'pydub',
            'scipy',
      ],
      packages=find_packages(exclude=['tests']),
)