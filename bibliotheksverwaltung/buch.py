from abc import ABC, abstractmethod

# Basisklasse Buch
class Buch(ABC):
    def __init__(self, titel, autor, isbn):
        self.titel = titel
        self.autor = autor
        # nur isbn als geschützt, da vielleicht später erweiterte Logik (= Erweiterbarkeit)
        # z. B. "überprüfen, ob Länge isbn korrekt" --> dann einfach bei Setter self._isbn = value
        # und schon Zugriff auch öffentlich über .isbn möglich (Setter)
        self._isbn = isbn 

    @abstractmethod
    def lesen(self):
        pass

    def details(self):
        return f"Titel: {self.titel}, Autor: {self.autor}, ISBN: {self._isbn}"