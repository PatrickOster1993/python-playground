from Buch import Buch


class Roman(Buch):
    def __init__(self, titel_ein, autor_ein, isbn_ein, genre_ein):
        super().__init__(titel_ein, autor_ein, isbn_ein)
        self.genre = genre_ein

    def details(self):
        return f"{super().details()}, Genre: {self.genre}, FSK: {self.fsk}"
    
    def lesen(self):
        print("Ich lese, um in eine fesselnde Welt einzutauchen.")
    
    @property
    def fsk(self):
        # FSK basierend auf dem Genre setzen
        fsk_mapping = {
            "thriller": 18,
            "horror": 18,
            "drama": 12,
            "komödie": 6,
            "kinderbuch": 0
        }
        return fsk_mapping.get(self.genre.lower(), 0)  # Standardwert 0, falls Genre unbekannt ist
