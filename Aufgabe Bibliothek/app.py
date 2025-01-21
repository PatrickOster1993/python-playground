from sachbuch import Sachbuch
from roman import Roman
from bibliothek import Bibliothek

def main():
    #Instanz erzeugen
    mein_sachbuch = Sachbuch(
        titel_ein="physik ist toll",
        autor_ein="Albert ZweiKohle",
        isbn_ein="1123335364",
        thema_ein="Physik"
    )


    # Methode der Basisklasse aufrufen:
    mein_sachbuch.details()
    #mein_roman.details()
    print("#################")

    # Individuelle methoden der Unterklassen konkreten Klassen:
    mein_sachbuch.wissenVermitteln()
    print("#################")

    # instanz der Klasse Bib erstellen
    meine_bibliothek.buchHinzufuegen(mein_sachbuch)

if __name__ == "__main__":
    main()
    