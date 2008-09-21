#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from distutils.core import setup

numconv = __import__('numconv')
version_tuple = numconv.VERSION
version = "%d.%d" % version_tuple[:2]
if version_tuple[2] is not None:
    svnf = os.path.join(os.path.dirname(os.path.abspath(numconv.__file__)),
                        '.svn/entries')
    gotdir = False
    version = '%s_%s' % (version, str(version_tuple[2]))
    if os.path.isfile(svnf):
        for ln in open(svnf):
            ln = ln.rstrip()
            if gotdir:
                version = '%s_rev%s' % (version, ln.replace(' ', ''))
                break
            if ln == 'dir':
                gotdir = True

setup(
    name = 'numconv',
    version = version,
    url = 'http://code.google.com/p/numconv/',
    author = 'Gustavo Picon',
    author_email = 'gpicon@gmail.com',
    license = 'Apache License 2.0',
    py_modules = ['numconv'],
    description = 'Python library to convert strings to numbers '
                  'and numbers to strings.',
)

