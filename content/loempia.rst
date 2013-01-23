:tags: project, loempia, openerp
:slug: loempia
:date: 2010-10-04
:title: Loempia

Loempia - Addons Registry for OpenERP
#####################################

Hi all,

I want to talk about a personal project for OpenERP. This project is Loempia.

Loempia will be the official repository for the modules of OpenERP, it allows to share the modules with the community.

Why Loempia?
------------

Currently, the community and OpenERP S.A. use LaunchPad to share the modules of OpenERP.

The problem with this way of working is that we don't know where a module is and if this module is up to date or not. Where are the certified modules ? etc...

I think Loempia can help everybody, because it will be the main repository for the modules of OpenERP.

With Loempia, you will have the capability to share your modules and comments. You could use the tag and rating systems.

You will have the capability to make some searchs with some specific criteria.

You will be able to look for the modules for the accounting for the version 5.0 of a specific contributor.

Do you want the certified modules for OpenERP 6.0, a small search on Loempia and you will get the results.

I think it's a very useful site and not only a marketing tool!

Why don't you want to use PyPi?
-------------------------------

PyPi is a very cool site if you want to share a python module, it's very useful and it works fine. But it's a technical site. Yes, we could use it to store the openerp's modules and after, what? You could show the best contributors, the most downloaded modules, and promote modules with screenshots.

Some features of Loempia:

* You could select a module of a given contributor.
* You could select a module for a specific version of OpenERP.
* How can I get the certified modules? Are these modules updated?

I hope that Loempia will help OpenERP, the Community and the developers.

What will we propose in Loempia?
--------------------------------

* Rating System
* Comment System
* Tag System
* User / Authentication system (OpenID, you will be able to connect with your LaunchPad ID account)
* Allows to register new launchpad branches or upload zip files
* Generate the documentation of the modules and integrate it into Sphinx
* Allows the screenshots (thanks to NaNtic)
* Produce sample of PDF reports
* Develop web-services for the API to register/browse addons
* Allows the possibility to register a branch or a module in the buildbot of OpenERP and add the results in the module statistics
* Fetch the specifications of a module in JSON, XML via an url
* Download the module via an url
* A python library and a command line client to handle the modules

.. sourcecode:: shell

  $ loempia search <module>
  $ loempia show <module+version>
  $ loempia fetch <module+version>
  $ loempia login <user> <version>
  $ loempia push <module>
  $ loempia install <module>
  $ loempia update {-all | <module> | <module+version> }
  $ loempia outdated
  
Currently, the project is hosted on `<http://www.loempia.org>`_, but you can see a mock-up on `<http://beta.loempia.org>`_.

Here is `the mock-up of the screens <http://www.loempia.org/website_modules.pdf>`_ with balsamic

If you have comments or suggestions, you can contact me.

