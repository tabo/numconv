# -*- coding: utf-8 -*-

"""Test numconv.py"""

import numconv
import unittest


class BaseconvI2s(unittest.TestCase):
    """tests for int2str()"""

    def test_i2s(self):
        """testing int2str: expected values"""
        self.assertEqual(numconv.int2str(3735928559, 16), 'DEADBEEF')
        self.assertEqual(numconv.int2str(238327, 62), 'zzz')
        self.assertEqual(numconv.int2str(14776335, 62), 'zzzz')
        self.assertEqual(numconv.int2str(466, 7), '1234')
        self.assertEqual(numconv.int2str(151880, 2), '100101000101001000')
        self.assertEqual(numconv.int2str(2693233728041137L, 85), '~123AFz@')
        self.assertEqual(numconv.int2str(543543, 40), '8JSN')
        self.assertEqual(numconv.int2str(1949459, 61), '8ZtL')
        self.assertEqual(numconv.int2str(19284, 2), '100101101010100')
        self.assertEqual(numconv.int2str(100, 10, 'abcdefghijklm'), 'baa')
        self.assertEqual(numconv.int2str(37, 4, 'rofl'), 'foo')

    def test_i2s_nonint_number(self):
        """testing int2str: error on non-integer number"""
        self.assertRaises(TypeError, numconv.int2str, 0.1, 8)

    def test_i2s_nonint_radix(self):
        """testing int2str: error on non-integer radix"""
        self.assertRaises(TypeError, numconv.int2str, 100, 0.1)

    def test_i2s_invalid_radix(self):
        """testing int2str: error on invalid radix"""
        self.assertRaises(ValueError, numconv.int2str, 100, -10)
        self.assertRaises(ValueError, numconv.int2str, 100, 10, 'abcde')

    def test_i2s_negative_number(self):
        """testing int2str: error on negative number"""
        self.assertRaises(ValueError, numconv.int2str, -100, 10)


class BaseconvS2i(unittest.TestCase):
    """tests for str2int()"""

    def test_s2i(self):
        """testing str2int: expected values"""
        self.assertEqual(numconv.str2int('DEADBEEF', 16), 3735928559L)
        self.assertEqual(numconv.str2int('zzz', 62), 238327)
        self.assertEqual(numconv.str2int('zzzz', 62), 14776335)
        self.assertEqual(numconv.str2int('1234', 7), 466)
        self.assertEqual(numconv.str2int('100101000101001000', 2), 151880)
        self.assertEqual(numconv.str2int('~123AFz@', 85), 2693233728041137L)
        self.assertEqual(numconv.str2int('8JSN', 40), 543543)
        self.assertEqual(numconv.str2int('8ZtL', 61), 1949459)
        self.assertEqual(numconv.str2int('100101101010100', 2), 19284)
        self.assertEqual(numconv.str2int('baa', 10, 'abcdefghijklm'), 100)
        self.assertEqual(numconv.str2int('foo', 4, 'rofl'), 37)

    def test_s2i_nonint_base(self):
        """testing str2int: error on non-integer base"""
        self.assertRaises(TypeError, numconv.str2int, '100', 0.1)

    def test_s2i_bad_number(self):
        """testing str2int: error on invalid number"""
        # raised by python
        self.assertRaises(ValueError, numconv.str2int, '1234z', 8)
        # raised by numconv.py
        self.assertRaises(ValueError, numconv.str2int, '1234z', 37)

    def test_s2i_invalid_radix(self):
        """testing str2int: error on invalid radix"""
        self.assertRaises(ValueError, numconv.str2int, 'abcd', -10)


class BaseconvCmap(unittest.TestCase):
    """tests for getcmap()"""

    def setUp(self):
        # clear the cmaps cache before every test
        numconv.CMAPS = {}

    def test_getcmap(self):
        """testing getcmap: expected values"""
        self.assertEqual(numconv.getcmap('0123456789'),
            {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
             '5': 5, '6': 6, '7': 7, '8': 8, '9': 9})
        self.assertEqual(numconv.getcmap('abcd'),
            {'a': 0, 'b': 1, 'c': 2, 'd': 3})

    def test_getcmap_dupechars(self):
        """testing getcmap: error on alphabet with duplicate chars"""
        self.assertRaises(ValueError, numconv.getcmap, 'abcdaf')

    def test_cmap_int2str(self):
        """tests that a call to int2str loads the cmap correctly"""
        numconv.int2str(10, 4, 'abcd')
        self.assertEqual(numconv.CMAPS['abcd'],
            {'a': 0, 'b': 1, 'c': 2, 'd': 3})

    def test_cmap_str2int(self):
        """tests that a call to str2int loads the cmap correctly"""
        numconv.str2int('aaaa', 4, 'abcd')
        self.assertEqual(numconv.CMAPS['abcd'],
            {'a': 0, 'b': 1, 'c': 2, 'd': 3})


class BaseconvSanity(unittest.TestCase):
    """sanity checks"""

    def test_sanity(self):
        """sanity check: testing a large interval and lots of radixes"""
        for num in range(1000) + [10**x for x in range(5, 15)]:
            for base in range(2, len(numconv.BASE85)):
                self.assertEqual(num,
                    numconv.str2int(numconv.int2str(num, base), base))

if __name__ == "__main__":
    unittest.main()
