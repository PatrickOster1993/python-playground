#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Modul für die Roman-Klasse der Bibliotheksverwaltung.
Implementiert die spezifische Funktionalität für Romane.
"""

from buch import Buch

class Roman(Buch):
    """
    Klasse für Romane, erbt von der Basisklasse Buch.
    Erweitert die Grundfunktionalität um romanspezifische Eigenschaften.
    
    Attributes:
        __genre (str): Das Genre des Romans (private)
        __genre_fsk_mapping (dict): Zuordnung von Genres zu FSK-Einstufungen
    """
    
    # Mapping von Genres zu FSK-Einstufungen
    __genre_fsk_mapping = {
        "Kinderbuch": 0,
        "Jugendliteratur": 6,
        "Fantasy": 12,
        "Abenteuer": 12,
        "Drama": 12,
        "Thriller": 18,
        "Horror": 18
    }
    
    def __init__(self, titel: str, autor: str, isbn: str, genre: str) -> None:
        """
        Initialisiert einen neuen Roman.
        
        Args:
            titel: Der Titel des Buchs
            autor: Der Autor des Buchs
            isbn: Die ISBN des Buchs
            genre: Das Genre des Romans
        """
        super().__init__(titel, autor, isbn)
        self.__genre = genre
    
    @property
    def genre(self) -> str:
        """Getter für das Genre des Romans."""
        return self.__genre
    
    @genre.setter
    def genre(self, genre: str) -> None:
        """Setter für das Genre des Romans."""
        self.__genre = genre
    
    @property
    def fsk(self) -> int:
        """
        Ermittelt die FSK-Einstufung basierend auf dem Genre.
        
        Returns:
            int: FSK-Einstufung (0, 6, 12 oder 18)
        """
        return self.__genre_fsk_mapping.get(self.genre, 0)
    
    def lesen(self) -> str:
        """
        Implementiert die abstrakte Methode der Basisklasse.
        
        Returns:
            str: Eine Beschreibung des Lesevorgangs für Romane
        """
        return "Ich lese, um in eine fesselnde Welt einzutauchen."
    
    def details(self) -> str:
        """
        Erweitert die details-Methode der Basisklasse um Genre und FSK.
        
        Returns:
            str: Erweiterte Buchdetails inklusive Genre und FSK
        """
        basis_details = super().details()
        return f"{basis_details}, Genre: {self.genre}, FSK: {self.fsk}"