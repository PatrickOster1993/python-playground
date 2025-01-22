# #### **1. Erstellung einer Basisklasse:**

# Erstelle eine Basisklasse `Buch`, die die gemeinsamen Attribute und Methoden für alle Bücher enthält.

# **Gemeinsame Attribute:**
# - `titel`: Der Titel des Buches.
# - `autor`: Der Autor des Buches.
# - `isbn`: Die ISBN des Buches.

# **Gemeinsame Methoden:**
# - `details`: Gibt eine kurze Beschreibung des Buches aus (Titel, Autor, ISBN).

class Buch:
    def __init__(self, titel_ein, autor_ein, isbn_ein):
        self.titel = titel_ein
        self.autor = autor_ein
        self.isbn = isbn_ein
    def details(self):
        print(f"Das Buch {self.titel}, vom Autor {self.autor}, mit der ISBN: {self.isbn}, wurde erfasst und ist verfügbar!")
        


# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-

# """
# Basis-Modul für die Bibliotheksverwaltung.
# Enthält die abstrakte Basisklasse für alle Arten von Büchern.
# """

# from abc import ABC, abstractmethod

# class Buch(ABC):
#     """
#     Abstrakte Basisklasse für alle Bücher.
#     Implementiert grundlegende Attribute und Methoden, die allen Büchern gemein sind.
    
#     Attributes:
#         __titel (str): Der Titel des Buches (private)
#         __autor (str): Der Autor des Buches (private)
#         __isbn (str): Die ISBN des Buches (private)
#     """
    
#     def __init__(self, titel: str, autor: str, isbn: str) -> None:
#         """
#         Initialisiert ein neues Buch mit den grundlegenden Attributen.
        
#         Args:
#             titel: Der Titel des Buches
#             autor: Der Autor des Buches
#             isbn: Die ISBN des Buches
#         """
#         self.__titel = titel
#         self.__autor = autor
#         self.__isbn = isbn
    
#     @property
#     def titel(self) -> str:
#         """Getter für den Titel des Buches."""
#         return self.__titel
    
#     @titel.setter
#     def titel(self, titel: str) -> None:
#         """Setter für den Titel des Buches."""
#         self.__titel = titel
    
#     @property
#     def autor(self) -> str:
#         """Getter für den Autor des Buches."""
#         return self.__autor
    
#     @autor.setter
#     def autor(self, autor: str) -> None:
#         """Setter für den Autor des Buches."""
#         self.__autor = autor
    
#     @property
#     def isbn(self) -> str:
#         """Getter für die ISBN des Buches."""
#         return self.__isbn
    
#     @isbn.setter
#     def isbn(self, isbn: str) -> None:
#         """Setter für die ISBN des Buches."""
#         self.__isbn = isbn
    
#     def details(self) -> str:
#         """
#         Gibt eine formatierte Beschreibung des Buches zurück.
        
#         Returns:
#             str: Formatierte Buchdetails mit Titel, Autor und ISBN
#         """
#         return f"Titel: {self.titel}, Autor: {self.autor}, ISBN: {self.isbn}"
    
#     @abstractmethod
#     def lesen(self) -> str:
#         """
#         Abstrakte Methode, die von erbenden Klassen implementiert werden muss.
        
#         Returns:
#             str: Eine Beschreibung des Lesevorgangs
#         """
#         pass