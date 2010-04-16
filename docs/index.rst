numconv
=======

:synopsys: Convert strings to numbers and numbers to strings.
:copyright: 2008-2010 by Gustavo Picon
:license: Apache License 2.0
:version: 2.1
:url: http://code.tabo.pe/numconv/
:documentation:
   `numconv-docs
   <http://docs.tabo.pe/numconv/2.1/>`_
:examples:
   `numconv-tests
   <http://code.tabo.pe/numconv/src/2.1/tests.py>`_

:mod:`numconv` converts a string into a number and a number into a string
using default or user supplied encoding alphabets.


.. module:: numconv

.. autoclass:: NumConv
   :show-inheritance:

   .. automethod:: int2str

      **Examples** (taken from :file:`tests.py`):

        3735928559 to hexadecimal::

            >> NumConv(16).int2str(3735928559)
            'DEADBEEF'

        19284 to binary::

            >> NumConv(2).int2str(19284)
            '100101101010100'

        37 to base 4 using a custom dictionary::

            >> NumConv(4, 'rofl').int2str(37)
            'foo'

        Very large number to :data:`~numconv.BASE85`::

            >> NumConv(85).int2str(2693233728041137)
            '~123AFz@'

   .. automethod:: str2int

      **Examples** (taken from :file:`tests.py`):

        Hexadecimal 'DEADBEEF' to integer::

           >> NumConv(16).str2int('DEADBEEF')
           3735928559

        Binary '100101101010100' to integer::

            >> NumConv(2).str2int('100101101010100')
            19284

        Base 4 with custom encoding 'foo' to integer::

            >> NumConv(4, 'rofl').str2int('foo')
            37

        :data:`~numconv.BASE85` '~123AFz@' to integer::

            >> NumConv(85).str2int('~123AFz@')
            2693233728041137


.. data:: BASE85

   Alphabet defined in section 4 of :rfc:`1924`. Supposed to be a joke
   (it is an April's fools RFC after all), but is quite useful because
   it can be used as a base for the most common numeric conversions.

.. data:: BASE16
          BASE32
          BASE32HEX
          BASE64
          BASE64URL

   Alphabets defined in :rfc:`4648`. Not really for common numeric
   conversion use.

.. data:: BASE62

   Useful for URL shorteners.


functions
---------

.. autofunction:: int2str

.. autofunction:: str2int



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

