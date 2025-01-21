from sachbuch import Sachbuch
from roman import Roman
from bibliothek import Bibliothek

def main():
    # Instanzen erzeugen
    mein_sachbuch = Sachbuch(
        titel_ein="Physik ist toll",
        autor_ein="Albert Zweistein",
        isbn_ein="123456789",
        thema_ein="Physik",
    )
    mein_roman = Roman(
        titel_ein="Der große Gatsby", 
        autor_ein="F. Scott Fitzgerald",
        isbn_ein="123456789",
        genre_ein="erotik"
        )

    # Methode der Basisklasse aufrufen:
    mein_sachbuch.details()
    mein_roman.details()
    print("######################################################")

    # Individuelle Methoden der Unterklassen / konkreten Klassen:
    mein_sachbuch.wissenVermitteln()
    print("######################################################")

    # Instanz der Klasse Bibliothek erstellen:
    meine_bibliothek = Bibliothek()

    # Methoden der Klasse Bibliothek aufrufen
    meine_bibliothek.buchHinzufuegen(mein_sachbuch)
    meine_bibliothek.buchHinzufuegen(mein_roman)

    meine_bibliothek.buchEntfernen(mein_roman)
    print("######################################################")

if __name__ == "__main__":
    main()