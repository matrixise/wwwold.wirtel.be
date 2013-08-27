:date: 2013-08-27
:title: Sphinx, Pygments and the logrotate format.
:slug: pylogrotate
:tags: python, sphinx, pygments, logrotate

PyLogrotate
===========

Introduction
------------

Yesterday, I have just noted there is logrotate lexer for Pygments. I just
developed this one for you.

If you want to contribute, please a simple Pull Request on the page of the
project.

Here is the repository of the project:
git://github.com/matrixise/pylogrotate.git

You are invited to contribute to this project ;-)

.. _installation:

Installation
------------

.. code-block:: bash

    git clone git://github.com/matrixise/pylogrotate.git

    virtualenv ~/.virtualenvs/pylogrotate
    source ~/.virtualenvs/pylogrotate

    cd pylogrotate
    python setup develop

Usage
-----

.. _pygmentize:

Pygmentize
~~~~~~~~~~

If you want to use it with ``pygmentize``, just download it and install it in a
VirtualEnv, see the "Installation" section.

    pygmentize -l logrotate -O full -f /tmp/test.html logrotate.conf

Sphinx
~~~~~~

In order to use it with Sphinx, just install it and define in your ``conf.py``
file a ``setup`` function as defined in the below example.

.. code-block:: python

    def setup(app):
       from pylogrotate.lexer import LogrotateLexer
       app.add_lexer('logrotate', LogrotateLexer())
