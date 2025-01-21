from bibliotheksverwaltung_b.Buch import Buch

class Roman(Buch):
    ### Attribute ###
    # Getter und Setter für Attribut FSK
    @property
    def fsk(self):
        return self._fsk
    
    @fsk.setter
    def fsk(self, genre):
        if genre == "Kinderbuch":
            self._fsk = 0
        elif genre == "Jugendbuch":
            self._fsk = 12 
        elif genre == "Krimi":
            self._fsk = 16
        elif genre == "Thriller":
            self._fsk = 18
        else:
            self._fsk = 0

    ### Konstruktor ###
    def __init__(self, titel, autor, isbn, genre, fsk):
        super().__init__(titel, autor, isbn)
        self.genre = genre
        self.fsk = fsk

    ### Methoden ###
    def lesen():
        print("Ich lese, um in eine fesselnde Welt einzutauchen.")