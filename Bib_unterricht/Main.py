from Bibliothek import Bibliothek
from Roman import Roman
from Sachbuch import Sachbuch
from Kunde import Kunde

# Erstelle eine Bibliothek
meine_bibliothek = Bibliothek()

# # Füge ein Sachbuch hinzu
# meine_bibliothek.buch_hinzufuegen_objekt(
#     Sachbuch,
#     "Physik ist toll",
#     "Albert Zweistein",
#     "123456789",
#     "Physik"
# )

# # Füge einen Roman hinzu
# meine_bibliothek.buch_hinzufuegen_objekt(
#     Roman,
#     "Drachen Chroniken",
#     "Peter Brand",
#     "123456789",
#     "Fantasy"
# )

# # Zeige alle Bücher in der Bibliothek an
# meine_bibliothek.alle_buecher()

# # Suche nach einem Buch und lese es
# buch = meine_bibliothek.buch_suchen("Drachen Chroniken")
# if buch:
#     meine_bibliothek.buch_lesen(buch)
    
    
    # Beispiel
ich = Kunde(
    name_ein="Pascal", 
    kundennummer_ein=0
)

mein_buch = Roman(
    titel_ein="Blabla", 
    autor_ein="Zweistein", 
    isbn_ein="21223456789",
    genre_ein="Fantasy"
)

ich.buch_ausleihen(mein_buch)
ich.geliehende_buecher_anzeigen()
ich.buch_zurueckgeben(mein_buch)
ich.geliehende_buecher_anzeigen()