#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Modul für die Sachbuch-Klasse der Bibliotheksverwaltung.
Implementiert die spezifische Funktionalität für Sachbücher.
"""

from buch import Buch

class Sachbuch(Buch):
    """
    Klasse für Sachbücher, erbt von der Basisklasse Buch.
    Erweitert die Grundfunktionalität um sachbuchspezifische Eigenschaften.
    
    Attributes:
        __thema (str): Das Thema des Sachbuchs (private)
    """
    
    def __init__(self, titel: str, autor: str, isbn: str, thema: str) -> None:
        """
        Initialisiert ein neues Sachbuch.
        
        Args:
            titel: Der Titel des Buchs
            autor: Der Autor des Buchs
            isbn: Die ISBN des Buchs
            thema: Das Thema des Sachbuchs
        """
        super().__init__(titel, autor, isbn)
        self.__thema = thema
    
    @property
    def thema(self) -> str:
        """Getter für das Thema des Sachbuchs."""
        return self.__thema
    
    @thema.setter
    def thema(self, thema: str) -> None:
        """Setter für das Thema des Sachbuchs."""
        self.__thema = thema
    
    def lesen(self) -> str:
        """
        Implementiert die abstrakte Methode der Basisklasse.
        
        Returns:
            str: Eine Beschreibung des Lesevorgangs für Sachbücher
        """
        return "Ich lese, um zu lernen!"
    
    def wissenVermitteln(self) -> str:
        """
        Spezifische Methode für Sachbücher zur Wissensvermittlung.
        
        Returns:
            str: Eine Beschreibung des vermittelten Wissensgebiets
        """
        return f"Dieses Buch vermittelt Wissen zum Thema {self.thema}."
    
    def details(self) -> str:
        """
        Erweitert die details-Methode der Basisklasse um das Thema.
        
        Returns:
            str: Erweiterte Buchdetails inklusive Thema
        """
        basis_details = super().details()
        return f"{basis_details}, Thema: {self.thema}"