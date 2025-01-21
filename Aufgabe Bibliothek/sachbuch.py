##Vererbung:
# Erstelle zwei Unterklassen Sachbuch und Roman, die von der Klasse Buch erben.

# Sachbuch:

# Zusätzlich zu den Attributen aus der Basisklasse soll es ein weiteres Attribut thema haben, das das Thema des Sachbuches angibt.
# Eine Methode wissenVermitteln, die in der Konsole ausgibt, zu welchem Thema das Buch Wissen vermittelt (als Satz).
# Roman:

# Zusätzlich zu den Attributen aus der Basisklasse soll es ein weiteres Attribut genre haben, das das Genre des Romans angibt (z. B. "Thriller", "Drama", ...).
# Auch soll die Klasse eine Property fsk beinhalten, welche sich (abhängig vom jeweiligen Genre auf 0, 6, 12 oder 18 setzt.
# 3. Abstraktion: 

from buch import Buch

class Sachbuch(Buch):
    def __init__(self, titel_ein, autor_ein, isbn_ein, thema_ein):
       #super().__init__(...) = ruft Konstruktor der Elternklasse auf (= Zuweisung gemeinsamer Attribute)
       super().__init__(titel_ein, autor_ein, isbn_ein)
       #Zuweisung der spezifischen Attribute
       self.thema = thema_ein

    def wissenVermitteln(self):
        print(f"das Buch {self.titel} vermittelt Wissen zum thema {self.thema}.")

mein_sachbuch = Sachbuch(
    titel_ein="physik ist toll",
    autor_ein="Albert ZweiKohle",
    isbn_ein="1123335364",
    thema_ein="Physik"
)

mein_sachbuch.wissenVermitteln()