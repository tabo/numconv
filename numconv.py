# -*- coding: utf-8 -*-
"""

numconv
-------

:synopsys: Python library to convert strings to numbers and numbers to
           strings.
:copyright: 2008 by Gustavo Picon
:license: Apache License 2.0
:version: 1.1
:url: http://code.google.com/p/numconv/
:documentation:
   `numconv-docs
   <http://code.google.com/p/numconv/source/browse/trunk/docs/html/index.html>`_
:examples:
   `numconv-tests
   <http://numconv.googlecode.com/svn/docs/index.html>`_


:mod:`numconv` converts a string into a number and a number into a string using
default or user supplied encoding alphabets.

constants
~~~~~~~~~

.. data:: BASE85

   Alphabet defined in section 4 of :rfc:`1924`. Supposed to be a joke (it is
   an April's fools RFC after all), but is quite useful because can be used as
   a base for the most common numeric conversions.

.. data:: BASE16
          BASE32
          BASE32HEX
          BASE64
          BASE64URL

   Alphabets defined in :rfc:`4648`. Not really for common numeric conversion
   use.

"""

VERSION = (1, 1)

# from april fool's rfc 1924
BASE85 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
         '!#$%&()*+-;<=>?@^_`{|}~'

# rfc4648 alphabets
BASE16 = BASE85[:16]
BASE32 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567'
BASE32HEX = BASE85[:32]
BASE64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
BASE64URL = BASE64[:62] + '-_'

# cached maps
CMAPS = {}


def int2str(num, radix=10, alphabet=BASE85):
    """Converts an integer into a string.

    :param num: A numeric value to be converted to another base as a string.
    :param radix: The base that will be used in the conversion.
       The default value is 10 for decimal conversion.
    :param alphabet: A string that will be used as a encoding alphabet.

       The length of the alphabet can be longer than the radix. In this case
       the alphabet will be internally truncated.

       The default value is :data:`numconv.BASE85`

    :rtype: string

    :raise TypeError: when *num* isn't an integer
    :raise ValueError: when *num* isn't positive
    :raise TypeError: when *radix* isn't an integer
    :raise ValueError: when *radix* is invalid
    :raise ValueError: when *alphabet* has duplicated characters

    **Examples** (taken from :file:`tests.py`):
       
       3735928559 to hexadecimal::

           >> numconv.int2str(3735928559, 16)
           'DEADBEEF'

       10284 to binary::

           >> numconv.int2str(19284, 2)
           '100101101010100'

       37 to base 4 using a custom dictionary::

           >> numconv.int2str(37, 4, 'rofl')
           'foo'

       Very large number to :data:`~numconv.BASE85`::

           >> numconv.int2str(2693233728041137L, 85)
           '~123AFz@'

    """
    if alphabet not in CMAPS:
        # just to validate the alphabet
        getcmap(alphabet)
    if int(num) != num:
        raise TypeError, 'number must be an integer'
    if num < 0:
        raise ValueError, 'number must be positive'
    if int(radix) != radix:
        raise TypeError, 'radix must be an integer'
    if not 2 <= radix <= len(alphabet):
        raise ValueError, 'radix must be >= 2 and <= %d' % (len(alphabet),)
    ret = ''
    while True:
        ret = alphabet[num % radix] + ret
        if num < radix:
            break
        num //= radix
    return ret


def str2int(num, radix=10, alphabet=BASE85):
    """Converts a string into an integer.

    If possible, the built-in python conversion will be used for speed
    porpuses.

    :param num: A string that will be converted to an integer.
    :param radix: The base that will be used in the conversion.
       The default value is 10 for decimal conversion.
    :param alphabet: A string that will be used as a encoding alphabet.

       The length of the alphabet can be longer than the radix. In this case
       the alphabet will be internally truncated.

       The default value is :data:`numconv.BASE85`

    :rtype: integer

    :raise TypeError: when *radix* isn't an integer
    :raise ValueError: when *radix* is invalid
    :raise ValueError: when *num* is invalid
    :raise ValueError: when *alphabet* has duplicated characters

    **Examples** (taken from :file:`tests.py`):
       
       Hexadecimal 'DEADBEEF' to integer::

          >> numconv.str2int('DEADBEEF', 16)
          3735928559L

       Binary '100101101010100' to integer::

           >> numconv.str2int('100101101010100', 2)
           19284

       Base 4 with custom encoding 'foo' to integer::

           >> numconv.str2int('foo', 4, 'rofl')
           37

       :data:`~numconv.BASE85` '~123AFz@' to integer::

           >> numconv.str2int('~123AFz@', 85)
           2693233728041137L

    """
    if alphabet not in CMAPS:
        getcmap(alphabet)
    if int(radix) != radix:
        raise TypeError, 'radix must be an integer'
    if not 2 <= radix <= len(alphabet):
        raise ValueError, 'radix must be >= 2 and <= %d' % (len(alphabet),)
    if radix <= 36 and alphabet[:radix].lower() == BASE85[:radix].lower():
        return int(num, radix)
    ret = 0
    lmap = CMAPS[alphabet]
    lalphabet = alphabet[:radix]
    for char in num:
        if char not in lalphabet:
            raise ValueError, "invalid literal for radix2int() " \
                "with radix %d: '%s'" % (radix, num)
        ret = ret * radix + lmap[char]
    return ret


def getcmap(alphabet):
    """Builds an internal alphabet lookup table, to be stored in CMAPS"""
    ret = dict(zip(alphabet, range(len(alphabet))))
    if len(ret) != len(alphabet):
        raise ValueError, "duplicate characters found in '%s'" % (alphabet,)
    CMAPS[alphabet] = ret
    return ret

