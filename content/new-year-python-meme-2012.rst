:date: 2013-01-09
:tags: python
:slug: new-year-python-meme-2012
:title: New Year's Python Meme 2012

New Years' Python Meme 2012
###########################

1. What’s the coolest Python application, framework or libraries you have discovered in 2012 ?
==============================================================================================


* VirtualEnv (virtualenvwrapper), this tool is really awesome, you can create a
  new environment for your test and your development. really useful if you want
  to contribute to a python project. just python setup develop and let's go.

* Requests (by `Kenneth Reitz`_) is a real advantage when you develop a http
  client because urllib is really bullshit.

* Python-RQ (by `Vincent Driessen`_), we can create a PubSub with Redis and it's
  easy.

* Gunicorn (by `Benoit Chesneau`_), a very good WSGI server, I use it for my own
  project, this wsgi server can be included in your own project via the python
  api.

If you want to monitor your processes you can use these tools.

* Circus (by `Tarek Ziade`_ and the `Mozilla Foundation`_)

* Gaffer (by `Benoit Chesneau`_)

2. What new programming technique did you learn in 2012 ?
=========================================================

* I learned the asynchronous programming with gevent and python-rq, these
  libraries are really awesome.

* before december 2012, I didn't use Github excepted to fetch the sources of
  several projects.

3. Which open source project did you contribute to the most in 2012 ? What did you do ?
=======================================================================================

`OpenERP`_  I am a core dev for 5 years.  Python via `PythonFOSDEM`_.

I organize with some friends a python devroom at `FOSDEM2013`_. It's really
great for the Python community, we want to improve the visibility of Python.

If you want to contribute, the repository is on `GitHub`_

4. Which Python blog or website did you read the most in 2012 ?
===============================================================

The python section of `Reddit`_ and `HackerNews`_ and sometimes you can find a
lot of great articles on `HumanCoders`_

5. What are the three top things you want to learn in 2013 ?
============================================================

* `Gateway`_ , based on python-rq, this library is a tool to exchange the data
  from one source to one destination via the concept of Workers.
  
* `PrintUs`_ , this is a prototype, but this is a printing server based on
  pyzmq.

* `LLVM`_ I implemented a small interpreter for a minimalist lisp language and I
  would like to compile it with LLVM.

* The foundation of the python network programming.

* Erlang
* Go
* Scala


6. What is the top software, application or library you wish someone would write in 2013 ?
==========================================================================================

* A CMS based on Python and Flask
* a wiki based on git and python (flask) and with the reStructuredText support


Want to do your own list? Here's how:
=====================================

* copy-paste the questions and answer to them in your blog
* tweet it with the `#2012pythonmeme`_ hashtag.


.. _#2012pythonmeme: https://twitter.com/search/realtime?q=%232012pythonmeme
.. _Benoit Chesneau: http://twitter.com/benoitc
.. _FOSDEM2013: http://fosdem.org/2013
.. _Gateway: http://github.com/matrixise/gateway
.. _GitHub: http://github.com/matrixise/python-fosdem.org
.. _HackerNews: http://news.ycombinator.com
.. _HumanCoders: http://news.humancoders.com/
.. _Kenneth Reitz: http://kennethreitz.com
.. _LLVM: http://llvm.org
.. _Mozilla Foundation: http://mozilla.org
.. _OpenERP: http://openerp.com
.. _PrintUs: http://github.com/matrixise/printus
.. _PythonFOSDEM: http://python-fosdem.org
.. _Reddit: http://reddit.com
.. _Tarek Ziade: http://ziade.org
.. _Vincent Driessen: http://nvie.com
