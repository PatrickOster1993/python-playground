##Vererbung:
# Erstelle zwei Unterklassen Sachbuch und Roman, die von der Klasse Buch erben.
# Roman:
# Zusätzlich zu den Attributen aus der Basisklasse soll es ein weiteres Attribut genre haben, das das Genre des Romans angibt (z. B. "Thriller", "Drama", ...).
# Auch soll die Klasse eine Property fsk beinhalten, welche sich (abhängig vom jeweiligen Genre auf 0, 6, 12 oder 18 setzt.
# 3. Abstraktion: 

from buch import Buch

class Roman(Buch):
    def __init__(self, titel_ein, autor_ein, isbn_ein, genre_ein):
       #super().__init__(...) = ruft Konstruktor der Elternklasse auf (= Zuweisung gemeinsamer Attribute)
       super().__init__(titel_ein, autor_ein, isbn_ein)
       #Zuweisung der spezifischen Attribute
       self.genre = genre_ein

    @property #eine Property ist ein "intelligentes Attribut" welches noch eine funktion hat /getter
    def fsk(self):
        FSK_MAPPING = {
            "kinderbuch": 0,
            "comedy": 6,
            "fantasy": 12,
            "thriller": 16,
            "erotik": 18
        }
        return FSK_MAPPING[self.genre.lower()]
    

#mein_roman = Roman(titel_ein="Bibel",autor_ein= "Gott",isbn_mein= "1",genre_mein="Fantasy")
    

