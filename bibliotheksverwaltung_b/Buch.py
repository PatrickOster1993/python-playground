from abc import ABC, abstractmethod


class Buch(ABC):
    ### Konstruktor ###
    def __init__(self, titel, autor, isbn):
        self.titel = titel
        self.autor = autor
        self.isbn = isbn

    ### Methoden ###
    def details(self):
        print(f"Titel: {self.titel}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")

    @abstractmethod
    def lesen():
        pass