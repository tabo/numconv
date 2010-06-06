numconv
=======

`numconv <https://tabo.pe/projects/numconv/>`_ is a library that converts
strings to numbers and numbers to strings using default or user supplied
encoding alphabets, written by `Gustavo Picón <https://tabo.pe>`_ and
licensed under the Apache License 2.0.

Installation
------------

``numconv`` has been tested in Python 2.4, 2.5, 2.6, 2.7, 3.0 and 3.1. Other
versions may work but are not supported.

You have several ways to install ``numconv``. If you're not sure,
`just use pip <http://guide.python-distribute.org/pip.html>`_

pip (or easy_install)
~~~~~~~~~~~~~~~~~~~~~

You can install the release versions from
`numconv's PyPI page`_ using ``pip``::

  pip install numconv

or if for some reason you can't use ``pip``, you can try ``easy_install``::

  easy_install --always-unzip numconv


setup.py
~~~~~~~~

Download a release from the `numconv download page`_ and unpack it, then
run::

   python setup.py install


API
---

.. module:: numconv

.. autoclass:: NumConv

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


.. autofunction:: int2str

.. autofunction:: str2int



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`



.. _`numconv's PyPI page`:
   http://pypi.python.org/pypi/numconv
.. _`numconv download page`:
   http://code.tabo.pe/numconv/downloads/

