from buch import Buch

class Roman(Buch):
    def __init__(self,titel_ein, autor_ein, isbn_ein, genre_ein):
        super().__init__(titel_ein, autor_ein,isbn_ein)
        self.genre = genre_ein
        
    @property
    def fsk(self):
        FSK_MAPPING = {
            "Kinderbuch": 0,
            "Comedy": 6,
            "Fantasy": 12,
            "Thriller": 16,
            "Erotik": 18
        }
        return FSK_MAPPING.get(self.genre.lower(),0)
    
    def lesen (self):
        print("ich wowli,um zu lernen!")
        
        
    
mein_roman =Roman(
    titel_ein="Pizza oder Döner",
    autor_ein="Gandalf",
    isbn_ein="024012",
    genre_ein="comedy"
)
        
print(mein_roman.fsk)

        