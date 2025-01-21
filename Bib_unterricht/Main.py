from Bibliothek import Bibliothek
from Roman import Roman
from Sachbuch import Sachbuch

# Erstelle eine Bibliothek
meine_bibliothek = Bibliothek()

# Füge ein Sachbuch hinzu
meine_bibliothek.buch_hinzufuegen(
    Sachbuch,
    "Physik ist toll",
    "Albert Zweistein",
    "123456789",
    "Physik"
)

# Füge einen Roman hinzu
meine_bibliothek.buch_hinzufuegen(
    Roman,
    "Drachen Chroniken",
    "Peter Brand",
    "123456789",
    "Fantasy"
)

# Zeige alle Bücher in der Bibliothek an
meine_bibliothek.alle_buecher()

# Suche nach einem Buch und lese es
buch = meine_bibliothek.buch_suchen("Drachen Chroniken")
if buch:
    meine_bibliothek.buch_lesen(buch)