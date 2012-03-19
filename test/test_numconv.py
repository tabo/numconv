# -*- coding: utf-8 -*-

"""Test numconv.py"""

from numconv import NumConv, int2str, str2int, BASE85
import pytest


@pytest.mark.parametrize(("num", "radix", "expected"), [
    (3735928559, 16, 'DEADBEEF'),
    (238327, 62, 'zzz'),
    (14776335, 62, 'zzzz'),
    (466, 7, '1234'),
    (151880, 2, '100101000101001000'),
    (2693233728041137, 85, '~123AFz@'),
    (543543, 40, '8JSN'),
    (1949459, 61, '8ZtL'),
    (19284, 2, '100101101010100')])
def test_int2str(num, radix, expected):
    assert int2str(num, radix) == expected


def test_int2str_with_radix_and_alphabet():
    assert int2str(37, 4, 'rofl') == 'foo'


def test_int2str_with_alphabet():
    assert int2str(100, alphabet='abcdefghijklm') == 'baa'


def test_int2str_nonint_number():
    pytest.raises(TypeError, int2str, 0.1, 8)


def test_int2str_nonint_radix():
    pytest.raises(TypeError, int2str, 100, 0.1)


def test_int2str_negative_radix():
    pytest.raises(ValueError, int2str, 100, -10)


def test_int2str_big_radix():
    # the radix (10) is too big for a dictionary of 5 characters
    pytest.raises(ValueError, int2str, 100, 10, "abcde")


def test_int2str_negative_number():
    pytest.raises(ValueError, int2str, -100)


@pytest.mark.parametrize(("num", "radix", "expected"), [
    ('DEADBEEF', 16, 3735928559),
    ('zzz', 62, 238327),
    ('zzzz', 62, 14776335),
    ('1234', 7, 466),
    ('100101000101001000', 2, 151880),
    ('~123AFz@', 85, 2693233728041137),
    ('8JSN', 40, 543543),
    ('8ZtL', 61, 1949459),
    ('100101101010100', 2, 19284)])
def test_str2int(num, radix, expected):
    assert str2int(num, radix) == expected


def test_str2int_with_radix_and_alphabet():
    assert str2int('foo', 4, 'rofl') == 37


def test_str2int_with_alphabet():
    assert str2int('baa', alphabet='abcdefghijklm') == 100


def test_str2int_nonint_base():
    pytest.raises(TypeError, str2int, '100', 0.1)


def test_str2int_bad_number_raised_by_python():
    pytest.raises(ValueError, str2int, '1234z', 8)


def test_str2int_bad_number_raised_by_numconv():
    pytest.raises(ValueError, str2int, '1234z', 37)


def test_str2int_negative_radix():
    pytest.raises(ValueError, str2int, 'abcd', -10)


def test_cached_map_alphabet_with_numbers():
    expected = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    assert NumConv(alphabet='0123456789').cached_map == expected


def test_cached_map_alphabet_with_letters():
    expected = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
    assert NumConv(radix=4, alphabet='abcd').cached_map == expected


def test_cached_map_alphabet_with_duplicate_characters():
    pytest.raises(ValueError, NumConv, 6, 'abcdaf')


def test_sanity():
    """sanity check: testing a large interval and lots of radixes"""
    for radix in range(2, len(BASE85)):
        ncobj = NumConv(radix)
        for num in list(range(100)) + [10 ** x for x in range(3, 15)]:
            assert num == ncobj.str2int(ncobj.int2str(num))
