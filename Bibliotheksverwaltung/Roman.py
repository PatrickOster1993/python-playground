from Basebook import Book

class Roman(Book):
    def __init__(self, titel, autor, isbn, genre):
        super().__init__(titel, autor, isbn)
        self.genre = genre

    def details(self):
        return f"{super().details()}, Subject: {self.genre}, FSK: {self.fsk}"
    
    @property
    def fsk(self):
        # FSK basierend auf dem Genre setzen
        fsk_mapping = {
            "Thriller": 18,
            "Horror": 18,
            "Drama": 12,
            "Komödie": 6,
            "Kinderbuch": 0
        }
        return fsk_mapping.get(self.genre, 0)  # Standardwert 0, falls Genre unbekannt ist
