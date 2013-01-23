:slug: win32ole_le_retour
:tags: ruby, ole, word, automation
:lang: fr
:date: 2007-12-03

Win32OLE, le retour
===================

Suite à mon  `précédent article sur Win32OLE </2007/11/25/ruby_ole_and_word>`_

Je viens de découvrir une méthode de classe très intéressante, surtout qu'elle appartient à la classe WIN32OLE. Il s'agit de la méthode

.. sourcecode:: ruby

    WIN32OLE::const_load( ole_object, module_or_class )

Vous souvenez-vous du code de mon précédent article ? J'avais défini un ensemble de constantes hiérarchisées à l'aide de modules.

.. sourcecode:: ruby

    module Word 
        module PageSetup
            module Orientation
                Portrait = 0
                Landscape = 1
            end
        end
        # .....
    end
        
En découvrant cette méthode, j'ai pû refactoriser mon code, afin de le rendre plus lisible et d'utiliser directement les constantes définies par la couche OLE. Voici donc, un peu de refactorisation de mon précédent code.

.. sourcecode:: ruby

    # Définition d'un module qui va servir à agréger les différentes constantes 
    # qui sont définie dans le composant OLE de Word.
    module Word
    end

    begin
        word = WIN32OLE.new( "Word.Application" )
        # La méthode WIN32OLE::const_load charge les différentes constantes 
        # depuis l'instance Word.
        # De cette manière, il n'est pas nécessaire de créer une correspondance 
        # entre constante et valeur numérique
        WIN32OLE.const_load( word, Word )

        document = word.Documents.Add()
        document.PageSetup.PaperSize = Word::WdPaperA4
        document.PageSetup.Orientation = Word::WdOrientLandscape
    ensure
        word.Quit()
    end
    
Je vous donne un avis, je n'ai pas pû complètement la documentation lors de l'article précédent, ce qui m'a fait perdre du temps. Un conseil, lisez les exemples, la documentation et tout ce qui peut aider. Références

`WIN32OLE::const_load <http://ruby-doc.org/core/classes/WIN32OLE.html#M002844>`_
