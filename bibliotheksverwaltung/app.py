from sachbuch import Sachbuch
from roman import Roman
from bibliothek import Bibliothek

# Bücher erstellen
sachbuch = Sachbuch("Python Programmierung", "Patrick Oster", "XXXXXXXXXX", "Programmieren")
roman = Roman("Der Hobbit", "J.R.R. Tolkien", "0987654321", "Fantasy")

# Bibliothek erstellen und verwalten
print("#####################################")
bibliothek = Bibliothek()
bibliothek.buchHinzufuegen(sachbuch)
bibliothek.buchHinzufuegen(roman)
print("#####################################")
bibliothek.buecherAnzeigen()

# Methoden aufrufen
print("#####################################")
print(sachbuch.wissenVermitteln())
print(roman.lesen())
print(f"FSK des Romans: {roman.fsk}")
print("#####################################")

bibliothek.buchEntfernen(roman)
print("#####################################")
bibliothek.buecherAnzeigen()