# -*- coding: utf-8 -*-

"""Test numconv.py"""

from numconv import NumConv, int2str, str2int, BASE85
import unittest


class BaseconvI2s(unittest.TestCase):
    """tests for int2str()"""

    def test_i2s(self):
        """testing int2str: expected values"""
        self.assertEqual(int2str(3735928559, 16), 'DEADBEEF')
        self.assertEqual(int2str(238327, 62), 'zzz')
        self.assertEqual(int2str(14776335, 62), 'zzzz')
        self.assertEqual(int2str(466, 7), '1234')
        self.assertEqual(int2str(151880, 2), '100101000101001000')
        self.assertEqual(int2str(2693233728041137L, 85), '~123AFz@')
        self.assertEqual(int2str(543543, 40), '8JSN')
        self.assertEqual(int2str(1949459, 61), '8ZtL')
        self.assertEqual(int2str(19284, 2), '100101101010100')
        self.assertEqual(int2str(100, 10, 'abcdefghijklm'), 'baa')
        self.assertEqual(int2str(37, 4, 'rofl'), 'foo')

    def test_i2s_nonint_number(self):
        """testing int2str: error on non-integer number"""
        self.assertRaises(TypeError, int2str, 0.1, 8)

    def test_i2s_nonint_radix(self):
        """testing int2str: error on non-integer radix"""
        self.assertRaises(TypeError, int2str, 100, 0.1)

    def test_i2s_invalid_radix(self):
        """testing int2str: error on invalid radix"""
        self.assertRaises(ValueError, int2str, 100, -10)
        self.assertRaises(ValueError, int2str, 100, 10, 'abcde')

    def test_i2s_negative_number(self):
        """testing int2str: error on negative number"""
        self.assertRaises(ValueError, int2str, -100, 10)


class BaseconvS2i(unittest.TestCase):
    """tests for str2int()"""

    def test_s2i(self):
        """testing str2int: expected values"""
        self.assertEqual(str2int('DEADBEEF', 16), 3735928559L)
        self.assertEqual(str2int('zzz', 62), 238327)
        self.assertEqual(str2int('zzzz', 62), 14776335)
        self.assertEqual(str2int('1234', 7), 466)
        self.assertEqual(str2int('100101000101001000', 2), 151880)
        self.assertEqual(str2int('~123AFz@', 85), 2693233728041137L)
        self.assertEqual(str2int('8JSN', 40), 543543)
        self.assertEqual(str2int('8ZtL', 61), 1949459)
        self.assertEqual(str2int('100101101010100', 2), 19284)
        self.assertEqual(str2int('baa', 10, 'abcdefghijklm'), 100)
        self.assertEqual(str2int('foo', 4, 'rofl'), 37)

    def test_s2i_nonint_base(self):
        """testing str2int: error on non-integer base"""
        self.assertRaises(TypeError, str2int, '100', 0.1)

    def test_s2i_bad_number(self):
        """testing str2int: error on invalid number"""
        # raised by python
        self.assertRaises(ValueError, str2int, '1234z', 8)
        # raised by numconv.py
        self.assertRaises(ValueError, str2int, '1234z', 37)

    def test_s2i_invalid_radix(self):
        """testing str2int: error on invalid radix"""
        self.assertRaises(ValueError, str2int, 'abcd', -10)


class BaseconvCmap(unittest.TestCase):
    """tests for getcmap()"""

    def test_get_cmap(self):
        """testing get_cmap: expected values"""
        self.assertEqual(NumConv(alphabet='0123456789').cached_map,
            {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
             '5': 5, '6': 6, '7': 7, '8': 8, '9': 9})
        self.assertEqual(NumConv(radix=4, alphabet='abcd').cached_map,
            {'a': 0, 'b': 1, 'c': 2, 'd': 3})

    def test_getcmap_dupechars(self):
        """testing getcmap: error on alphabet with duplicate chars"""
        self.assertRaises(ValueError, NumConv, 6, 'abcdaf')


class BaseconvSanity(unittest.TestCase):
    """sanity checks"""

    def test_sanity(self):
        """sanity check: testing a large interval and lots of radixes"""
        for radix in range(2, len(BASE85)):
            ncobj = NumConv(radix)
            for num in range(1000) + [10**x for x in range(5, 15)]:
                self.assertEqual(num, ncobj.str2int(ncobj.int2str(num)))

if __name__ == "__main__":
    unittest.main()
