from Bibliothek import Bibliothek
from Roman import Roman
from Sachbuch import Sachbuch
from Kunde import Kunde

    
# Erstelle eine Bibliothek
meine_bibliothek = Bibliothek()
    
# Erstelle einen Kunden
ich = Kunde(
    name_ein="Pascal", 
    kundennummer_ein=0
)

mein_buch = Roman(
    titel_ein="TestBuch", 
    autor_ein="Test", 
    isbn_ein="21223456789",
    genre_ein="Fantasy"
)

mein_buch2 = Roman(
    titel_ein="222TestBuch", 
    autor_ein="Test", 
    isbn_ein="21223456789",
    genre_ein="Fantasy"
)

if __name__ == "__main__":
    meine_bibliothek.buch_hinzufuegen(mein_buch)
    meine_bibliothek.buch_hinzufuegen(mein_buch)
    meine_bibliothek.buch_hinzufuegen(mein_buch)
    meine_bibliothek.buch_hinzufuegen(mein_buch2)
    # Zeige alle Bücher in der Bibliothek an
    meine_bibliothek.alle_buecher()

    meine_bibliothek.kunde_hinzufuegen(ich)
    meine_bibliothek.buch_verleihen(mein_buch, ich)
    meine_bibliothek.buch_zuruecknehmen(mein_buch, ich)
    meine_bibliothek.buch_zuruecknehmen(mein_buch2, ich)
    meine_bibliothek.alle_buecher()