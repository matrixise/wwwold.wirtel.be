:date: 2013-01-27
:slug: install-etherpadlite-debian-squeeze
:lang: fr
:status: draft

Installation d’Etherpad Lite sur Debian squeeze
###############################################

Introduction
============
Etherpad Lite est une réécriture de Etherpad en Node.JS.

Installation
============

Toute l’installation de Etherpad se fera dans le répertoire suivant: */home/www/etherpad.wirtel.be*::

    mkdir /home/www/etherpad.wirtel.be -p
    cd /home/www/etherpad.wirtel.be

Installation de NodeJS
----------------------
Dépendances
~~~~~~~~~~~
.. sourcecode:: bash

    apt-get install gzip git-core curl python libssl-dev pkg-config build-essential


Installation
~~~~~~~~~~~~

.. sourcecode:: bash

    wget http://nodejs.org/dist/v0.8.18/node-v0.8.18.tar.gz
    tar xfz node-v0.8.18.tar.gz
    
    cd node-v0.8.18/
    ./configure --prefix=/home/www/etherpad.wirtel.be/local
    make
    make install

EtherPad Lite
-------------

.. sourcecode:: bash

    git clone git://github.com/ether/etherpad-lite.git
    
    cd etherpad-lite/
    export PATH=/home/www/etherpad.wirtel.be/local/bin:$PATH
    ./bin/installDeps.sh

Dans le cas d’un accès non-root:

.. sourcecode:: bash

    ./bin/run.sh

Dans le cas d’un accès root, vous devrez spécifier le flag —root sur la ligne de commande:

.. sourcecode:: bash

    ./bin/run.sh --root
