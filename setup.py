#!/usr/bin/env python

from distutils.core import setup

version = '2.0'

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries",
]

setup(
    name='numconv',
    version=version,
    url='http://code.tabo.pe/numconv/',
    author='Gustavo Picon',
    author_email='tabo@tabo.pe',
    license='Apache License 2.0',
    py_modules=['numconv'],
    description='Python library to convert strings to numbers '
                'and numbers to strings.',
    classifiers=classifiers,
    #long_description=__doc__,
)
