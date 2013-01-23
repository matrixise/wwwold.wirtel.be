:date: 2007-12-05
:tags: soap, delphi, c++
:title: Après la SOAP, le dessert
:slug: apres_la_soap-le_dessert
:lang: fr

Après la SOAP, le dessert !
===========================

Vous souvenez-vous, dans `mon précédent billet </2007/12/04/la-soap>`_,
j'indiquais que j'allais devoir utiliser `mouseHole <http://code.whytheluckystiff.net/mouseHole/>`_ 
afin de vérifier le bon fonctionnement d'un connecteur SOAP. 

J'étais prêt à mettre la main à la pate, quand tout à coup, 
j'ai trouvé `soapUI <http://www.soapui.org/>`_. 

Il s'agit d'un outil de test pour WebServices. 

A première vue, il avait l'air simple, mais j'ai pû constater qu'il était
génial. Importer mon WSDL, générer un mock webservice et tester mon connecteur
en quelques minutes, sans écrire une seule ligne. 

Je ne vous dis pas la joie que j'ai pû ressentir en me disant que j'avais gagné
quelques jours de développement à cause d'un manque d'outil pour debugger mes
messages SOAP. 

La chose vraiment intéressante, il est possible de scripter cet outil via
Groovy afin de modifier les responses à la volée.  Sincèrement, j'avais la
bouche ouverte :d

