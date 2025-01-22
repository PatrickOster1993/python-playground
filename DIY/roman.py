from buch import Inhaltsverzeichnis

class Roman(Inhaltsverzeichnis):
    def __init__(self, ein_Autor, ein_Titel, ein_jahr, ein_Genre):
        super().__init__(ein_Autor, ein_Titel, ein_jahr)
        self.Genre = ein_Genre
        
    def hinzufügenRoman(self):
        print(f"Es wurde {self.Genre} hinzugefügt")
        
        
# Objekt der Klasse Roman erstellen
hey1 = Roman(
    ein_Autor="Döner",
    ein_Titel="Es heißt eigentlich Gyros",
    ein_jahr="2015",
    ein_Genre="Roman"
)

# Methode hinzufügenRoman aufrufen
hey1.hinzufügenRoman()
