#!/usr/bin/env python
import os
import sys

from djlinkmobile import __version__
from setuptools import setup


# Publish to Pypi
if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

setup(
    name='django-linkmobile',
    version=__version__,
    description='Django application for receiving and saving callbacks from the Link Mobile MessageService API',
    long_description=open('README.md').read(),
    author='Funkbit',
    author_email='post@funkbit.no',
    url='https://github.com/funkbit/django-linkmobile',
    packages=['djlinkmobile'],
    license='BSD',
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    )
)
