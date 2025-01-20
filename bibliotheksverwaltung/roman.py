from buch import Buch

# Unterklasse Roman
class Roman(Buch):
    def __init__(self, titel, autor, isbn, genre):
        super().__init__(titel, autor, isbn)
        # öffentliches Attribut
        self.genre = genre

    @property
    def fsk(self):
        # Großschreibung, da dies in Python der Notation für eine "Konstante" entspricht
        GENRE_FSK_MAPPING = {
            "Erotik": 18,
            "Thriller": 16,
            "Fantasy": 12,
            "Komödie": 6,
            "Kinderbuch": 0
        }
        return GENRE_FSK_MAPPING[self.genre]

    def lesen(self):
        return "Ich lese, um in eine fesselnde Welt einzutauchen."