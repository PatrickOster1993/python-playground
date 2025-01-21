# #### **2. Vererbung:**

# Erstelle zwei Unterklassen `Sachbuch` und `Roman`, die von der Klasse `Buch` erben.

# - **Sachbuch**:
#   - Zusätzlich zu den Attributen aus der Basisklasse soll es ein weiteres Attribut `thema` haben, das das Thema des Sachbuches angibt.
#   - Eine Methode `wissenVermitteln`, die in der Konsole ausgibt, zu welchem Thema das Buch Wissen vermittelt (als Satz).

# - **Roman**:
#   - Zusätzlich zu den Attributen aus der Basisklasse soll es ein weiteres Attribut `genre` haben, das das Genre des Romans angibt (z. B. "Thriller", "Drama", ...).
#   - Auch soll die Klasse eine Property `fsk` beinhalten,  welche sich (abhängig vom jeweiligen Genre auf 0, 6, 12 oder 18 setzt.

from Aufgabe_1_Buch import Buch # importiert aus der Datei "Aufgabe_1_Buch" und nimmt sich die Basisklasse "Class Buch"

class Sachbuch(Buch): # Erstellt die Klasse 'Sachbuch_buch', die von der Basisklasse 'Buch' erbt(befindet sich in Aufgabe_1_Buch)
    def __init__(self, titel_ein, autor_ein, isbn_ein, thema_ein):
        super().__init__(titel_ein, autor_ein, isbn_ein)
        self.thema = thema_ein

    def wissenVermitteln(self):
        print (f"Das Buch {self.titel} vermittelt Wissen zum Them {self.thema}.")


mein_sachbuch = Sachbuch(
    titel_ein="Physik ist toll",
    autor_ein="Albert Zweistein",
    isbn_ein="123456789",
    thema_ein="Physik",

)

mein_sachbuch.wissenVermitteln
    