#!/usr/bin/env python

import os
from setuptools import setup
from setuptools.command.test import test


def root_dir():
    rd = os.path.dirname(__file__)
    if rd:
        return rd
    return '.'


class pytest_test(test):
    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        pytest.main([])


setup_args = dict(
    name='numconv',
    version='2.1.2-dev',
    url='https://tabo.pe/projects/numconv/',
    author='Gustavo Picon',
    author_email='tabo@tabo.pe',
    license='Apache License 2.0',
    py_modules=['numconv'],
    description='Python library to convert strings to numbers '
                'and numbers to strings.',
    long_description=open(root_dir() + '/README').read(),
    cmdclass={'test': pytest_test},
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries'])

if __name__ == '__main__':
    setup(**setup_args)
