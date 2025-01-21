#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Modul für die Kundenklasse der Bibliotheksverwaltung.
Implementiert die Verwaltung von Bibliothekskunden und deren ausgeliehenen Büchern.
"""

from typing import List, Set
from buch import Buch

class Kunde:
    """
    Klasse zur Verwaltung von Bibliothekskunden.
    
    Attributes:
        __name (str): Name des Kunden (private)
        __kunden_id (str): Eindeutige Kundenidentifikation (private)
        __ausgeliehene_buecher (Set[str]): Set von ISBNs der ausgeliehenen Bücher (private)
    """
    
    def __init__(self, name: str, kunden_id: str) -> None:
        """
        Initialisiert einen neuen Bibliothekskunden.
        
        Args:
            name: Name des Kunden
            kunden_id: Eindeutige Kundenidentifikation
        """
        self.__name = name
        self.__kunden_id = kunden_id
        self.__ausgeliehene_buecher: Set[str] = set()  # Speichert ISBNs der ausgeliehenen Bücher
    
    @property
    def name(self) -> str:
        """Getter für den Namen des Kunden."""
        return self.__name
    
    @property
    def kunden_id(self) -> str:
        """Getter für die Kunden-ID."""
        return self.__kunden_id
    
    @property
    def anzahl_ausgeliehener_buecher(self) -> int:
        """
        Gibt die Anzahl der aktuell ausgeliehenen Bücher zurück.
        
        Returns:
            int: Anzahl ausgeliehener Bücher
        """
        return len(self.__ausgeliehene_buecher)
    
    def buch_ausleihen(self, buch: Buch) -> bool:
        """
        Markiert ein Buch als ausgeliehen für diesen Kunden.
        
        Args:
            buch: Das auszuleihende Buch
            
        Returns:
            bool: True wenn das Buch ausgeliehen wurde, False wenn es bereits ausgeliehen war
        """
        if buch.isbn not in self.__ausgeliehene_buecher:
            self.__ausgeliehene_buecher.add(buch.isbn)
            print(f"Kunde {self.name} hat '{buch.titel}' ausgeliehen.")
            return True
        return False
    
    def buch_zurueckgeben(self, buch: Buch) -> bool:
        """
        Markiert ein Buch als zurückgegeben.
        
        Args:
            buch: Das zurückzugebende Buch
            
        Returns:
            bool: True wenn das Buch zurückgegeben wurde, False wenn es nicht ausgeliehen war
        """
        if buch.isbn in self.__ausgeliehene_buecher:
            self.__ausgeliehene_buecher.remove(buch.isbn)
            print(f"Kunde {self.name} hat '{buch.titel}' zurückgegeben.")
            return True
        return False
    
    def hat_buch_ausgeliehen(self, isbn: str) -> bool:
        """
        Prüft, ob der Kunde ein bestimmtes Buch ausgeliehen hat.
        
        Args:
            isbn: Die ISBN des zu prüfenden Buchs
            
        Returns:
            bool: True wenn das Buch ausgeliehen ist, False sonst
        """
        return isbn in self.__ausgeliehene_buecher
    
    def zeige_ausgeliehene_buecher(self) -> None:
        """Gibt eine Liste aller ausgeliehenen Bücher des Kunden aus."""
        if not self.__ausgeliehene_buecher:
            print(f"Kunde {self.name} hat aktuell keine Bücher ausgeliehen.")
            return
        
        print(f"\nAusgeliehene Bücher von {self.name}:")
        print("-" * 40)
        for isbn in self.__ausgeliehene_buecher:
            print(f"ISBN: {isbn}")
        print(f"Gesamtanzahl: {len(self.__ausgeliehene_buecher)}")