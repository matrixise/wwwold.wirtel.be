:date: 2013-01-21
:title: Test your SMTP connection within your projects
:slug: dsmtpd-0.2
:tags: python, tools

dsmtpd - a SMTP server for debugging
####################################

Sometimes I have to use a smtp server to check my outgoing emails but I don't
want to pollute the internet with some useless emails.

So in this case, I just developped this small tools for me but you will may be
interested by this project. I called dsmtpd for debugger smtp server (the last
'd' comes from the smtpd python lib)

Installation
------------

This package is on pypi, so you can use pip to install it::
    
    pip install dsmtpd


Use it
------

To use it, it's very simple::
    
    dsmtpd

.. code-block:: text

    2013-01-13 14:00:07,346 INFO: Starting SMTP server at 127.0.0.1:1025

By default the server will run on the port 1025 and on the loopback interface.
It's pretty easy.

Indeed, there is a small help::

    dsmtpd --help

.. code-block:: text

    dsmtpd: A small SMTP server for the smart developer

    Usage:
        dsmtpd [-i <iface>] [-p <port>] [-d <directory>]

    Options:
        -p <port>      Specify the port for the SMTP server [default: 1025]
        -i <iface>     Specify the interface [default: 127.0.0.1]
        -d <directory> Specify the directory to save the incoming emails
        -h --help
        --version


Change the port
~~~~~~~~~~~~~~~
If you want to change the default port, you can do it with the '-p' option::

    sudo dsmtpd -p 25

.. code-block:: text

    2013-01-13 14:00:07,346 INFO: Starting SMTP server at 127.0.0.1:25

Change the interface
~~~~~~~~~~~~~~~~~~~~

By default, dsmtpd listens to the loopback but you can change that with the '-i' option::

    dsmtpd -i YOUR_IP

.. code-block:: text

    2013-01-13 14:00:07,346 INFO: Starting SMTP server at YOUR_IP:1025

    2013-01-13 14:00:19,634 INFO: 127.0.0.1:55549: stephane@wirtel.be -> stephane@wirtel.be [test Sun, 13 Jan 2013 14:00:19 +0100]

You can store the incoming emails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is a cool feature with dsmtpd, all the emails can be caught by the mail server with the '-d' parameter::

    dsmtpd -d store_directory

This store directory is a maildir directory, so you will be able to use the mutt software to see the emails.
It's really useful if you want to see all the emails with the description of the headers. ::

    mutt -f store_directory


Contributions
-------------

The project is hosted on `github <http://github.com/matrixise/dsmtpd>`_

