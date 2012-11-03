#!/usr/bin/env python
""" toxhelper is a simple wrapper of pytest and coverage to be used with tox.

It is specially useful to avoid path and interpreter problems while running
tests with jenkins in OS X, Linux and Windows using the same configuration.

See https://tabo.pe/jenkins/ for the results.
"""

import sys

from coverage import coverage
import pytest


def run_the_tests():
    cov = coverage()
    cov.start()
    test_result = pytest.main(sys.argv[1:])
    cov.stop()
    cov.save()
    return test_result

if __name__ == '__main__':
    sys.exit(run_the_tests())
