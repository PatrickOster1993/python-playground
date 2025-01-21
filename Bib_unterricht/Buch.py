from abc import ABC, abstractmethod

class Buch(ABC):
    def __init__(self, titel_ein, autor_ein, isbn_ein):
        self.titel = titel_ein
        self.autor = autor_ein
        self.isbn = isbn_ein

    def details(self):
        return f"Das Buch '{self.titel}' wurde vom Autor {self.autor} verfasst und ist über die ISBN {self.isbn} verfügbar!"
    
    @abstractmethod
    def lesen():
        print("Das Buch wird gelesen.")