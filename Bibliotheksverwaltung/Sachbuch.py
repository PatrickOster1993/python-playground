from Basebook import Book

class Sachbuch(Book):
    def __init__(self, titel, autor, isbn, thema):
        super().__init__(titel, autor, isbn)
        self.thema = thema

    def wissen_vermitteln(self):
        print(f"Das Sachbuch '{self.titel}' vermittelt Wissen zum Thema: {self.thema}")
