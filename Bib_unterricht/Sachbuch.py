from Buch import Buch

class Sachbuch(Buch):
    def __init__(self, titel_ein, autor_ein, isbn_ein, thema_ein):
        super().__init__(titel_ein, autor_ein, isbn_ein)
        self.__thema = thema_ein

    def wissenVermitteln(self):
        print(f"Das Buch {self.titel} vermittelt Wissen zum Thema {self.__thema}.")
        
    def lesen(self):
        print("Ich lese, um zu lernen!")