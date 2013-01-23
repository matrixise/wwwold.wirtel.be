:tags: ruby, ole, word, automation
:slug: ruby_ole_and_word
:lang: fr
:date: 2007-11-25

Ruby, OLE et Word
=================

Comment générer des documents Words avec OLE et Ruby ?
------------------------------------------------------

Je vais être honnête avec vous, je ne suis pas pour l'utilisation de Word, mais
les personnes travaillant avec moi, utilisent majoritairement cet outil et ne
jurent que par celui-ci. Afin d'utiliser correctement OLE avec Ruby, il faut
avoir à sa disposition plusieurs outils, :-)

* win32ole Elle fait partie de la librairie standard de Ruby et d'une très
  grande utilité ;-) sans ça, il est impossible de pouvoir utiliser Word via
  OLE.

* `ole_browser.rb <http://dave.burt.id.au/ruby/ole_browser.rb>`_ qui est un
  script permettant d'introspecter les objets disponibles. Cet outil a été
  écrit par Dave Burt et Masaki Suketa.

.. sourcecode:: ruby
    
    #!/usr/bin/env ruby

    require "win32ole"

Définition d'une nouvelle méthode basée sur l'opérateur '/' afin de sucharger
la classe String.

.. sourcecode:: ruby

    class String
        def / (other)
            File.join(self, other)
        end
    end

Etant donné que je n'avais pas envie d'écrire tout le temps du code
inutilement, et que j'adore refactoriser, j'ai ajouté une petite méthode au
module Kernel. Celle me permet de gagner un peu de lisibilité, mais pas grand
chose, je la met dans la zone des Helpers.o

.. sourcecode:: ruby

    module Kernel
        def with(obj)
            yield obj
        end
    end

Bon, commençons par le plus intéressant, je pense que le plus intéressant est
tout de même de charger Word :D donc, voici comment charger cet outil.

.. sourcecode:: ruby
    
    word = WIN32OLE.new( "Word.Application" )

Dans mon exemple, je ne veux pas voir l'interface de Word, de ce fait, je
n'active pas sa visibilité.

.. sourcecode:: ruby
    
    word.Visible = false
    
Etant donné que cet article parle de la création de document, il ne s'agit pas
d'ouvrir un document Word et de lui rajouter des infos, on part de zéro.

.. sourcecode:: ruby
    
    document = word.Documents.Add()

Afin que vous ne soyez pas perdu dans des nombres magiques, j'ai ajouté une
petite liste de constantes, permettant de cette manière une utilisation plus
aisée des composants.

.. sourcecode:: ruby
    
    module Word
        module PageSetup
            module Orientation
                Portrait = 0
                Landscape = 1
            end
            module Size
                PaperA4 = 7
            end
        end

        module Font
            module ColorIndex
                Black = 1
                Blue = 2
                Turquoise = 3
                BrightGreen = 4
                Pink = 5
                Red = 6
                Yellow = 7
                White = 8
                DarkBlue = 9
                Teal = 10
                Green = 11
                Violet = 12
                DarkRed = 13
                DarkYellow = 14
            end
        end

        module ParagraphAlignment
            Left = 0
            Center = 1
            Right = 2
            Justify = 3
            Distribute = 4
            JustifyMed = 5
            JustifyHi = 7
            JustifyLow = 8
            ThaiJustify = 9
        end
    end
    
    
Cette partie est bête, mais spécifie le format de la page, de cette manière
j'indique le format A4 en Paysage ( LandScape )

.. sourcecode:: ruby
   
    document.PageSetup.PaperSize = Word::PageSetup::Size::PaperA4
    document.PageSetup.Orientation = Word::PageSetup::Orientation::Landscape

Pour toutes les sections se trouvant dans le document, nous allons ajoutés un
en-tête et un pied de page. Création de l'entête avec une police de caractères
ayant la couleur Violet, et dont le contenu sera "En-tête d'exemple"

.. sourcecode:: ruby

    for section in document.Sections
        with section.Headers( 1 ).Range do |range|
            range.Font.ColorIndex = Word::Font::ColorIndex::Violet
            range.Text = "En-tête d'exemple"
        end
        with section.Footers( 1 ).Range do |range|
            range.ParagraphFormat.Alignment = Word::ParagraphAligment::Right
            range.Font.ColorIndex = Word::Font::ColorIndex::DarkRed
            range.Text = "Stephane Wirtel < stephane DOT wirtel AT gmail DOT com>"
        end
    end
    with word.Selection do |sel|
        # Ajout d'une image,
        picture = sel.InlineShapes.AddPicture( Dir.pwd() / 'change_directory.png', nil, true )

        # Bon, on insère un break, c'est à dire une nouvelle page
        sel.InsertBreak()

        [ "Je ne suis pas Superman, mais j'y arrive :D",
        "Une option en plus que les autres :D" ].each do |line|
            sel.TypeText( "#{line}\n" )
        end
        sel.InsertBreak()

        # Spécification de la taille de la police à utiliser
        with sel.Font do |font|
            font.Name = "Bitstream Vera Sans Mono"
            font.Size = 10
            font.Bold = false
        end

        # On ajoute l'heure avec la date de cette manière, on peut déjà savoir la date de création du document
        sel.TypeText( Time.now.to_s )
        sel.InsertBreak()
    end
    
    
Et si on enregistrait le document, ça serait cool, vous ne pensez pas ? Tout ce
travail pour ne pas le sauver, ça serait débile :D Donc, tadaaaaam

.. sourcecode:: ruby

    document.SaveAs( Dir.pwd() / 'test.doc' )
    document.close()

Maintenant il ne reste plus qu'à fermer l'application Word, si nous ne le
faisons pas, il restera une instance Word ouverte, ce qui peut provoquer des
problèmes.

.. sourcecode:: ruby

    word.Quit()


Imaginez maintenant la création d'un DSL pour simplifier tout ce code, ou aussi
l'utilisation de Textile
