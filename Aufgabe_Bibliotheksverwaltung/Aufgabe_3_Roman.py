from Aufgabe_1_Buch import Buch

class Roman(Buch):
    def __init__(self, titel_ein, autor_ein, isbn_ein, genre_ein):
        super().__init__(titel_ein, autor_ein, isbn_ein)
        self.genre = genre_ein
    
    @property
    def fsk(self):
        FSK_MAPPING = {
            "kinderbuch": 0,
            "comedy": 6,
            "fantasy": 12,
            "thriller": 16,
            "erotik": 18
            }
        return FSK_MAPPING[self.genre.lower()]
    
mein_roman = Roman(
    titel_ein="Der große Gatsby",
    autor_ein="F. Scott Fritzgerald",
    isbn_ein="123456789",
    genre_ein="erotik"
)
        
