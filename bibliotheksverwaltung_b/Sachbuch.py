from bibliotheksverwaltung_b.Buch import Buch

class Sachbuch(Buch):
    ### Konstruktor ###
    def __init__(self, titel, autor, isbn, thema):
        super().__init__(titel, autor, isbn)
        self.thema = thema
    
    ### Methoden ###
    def wissenVermitteln(self):
        print(f"{self.titel} vermittelt Wissen zum Thema {self.thema}.")

    def lesen(self):
        print("Ich lese, um zu lernen!")