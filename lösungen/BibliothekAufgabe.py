from abc import ABC, abstractmethod

class Buch(ABC):
    def __init__(self, titel, autor, isbn):
        self.titel = titel
        self.autor = autor
        self.isbn = isbn

    @abstractmethod
    def lesen(self):
        pass
    

    def detailsAusgeben(self):
        print(f"Titel des Buchs: {self.titel}")
        print(f"Autor des Buchs: {self.autor}")
        print(f"ISBN des Buchs: {self.isbn}")

class Sachbuch(Buch):
    def __init__(self, titel, autor, isbn, thema):
        super().__init__(titel, autor, isbn)
        self.thema = thema
    
    def wissenVermitteln(self):
        print(f"Dieses Buch antwortet al Ihre Fragen über {self.thema}")

    def lesen(self):
        print("Ich lese, um zu lernen!")
    

class Roman(Buch):
    def __init__(self, titel, autor, isbn, genre):
        super().__init__(titel, autor, isbn)
        self.genre = genre
    
    @property
    def fskVergabe(self):
        if self.genre == "Thriller":
            self.fsk = 18
        elif self.genre == "Drama":
            self.fsk = 12
    
    def lesen(self):
        print("Ich lese, um zu lesen :)")