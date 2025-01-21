#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Modul für die Bibliotheksklasse der Bibliotheksverwaltung.
Implementiert die Verwaltung der Buchsammlung, Exemplare und Kunden.
"""

from typing import List, Optional, Dict
from buch import Buch
from kunde import Kunde

class Bibliothek:
    """
    Klasse zur Verwaltung einer Bibliothek mit Büchern und Kunden.
    
    Attributes:
        __buecher (Dict[str, Buch]): Dictionary mit ISBN als Schlüssel und Buch als Wert (private)
        __exemplare (Dict[str, int]): Anzahl der verfügbaren Exemplare pro ISBN (private)
        __kunden (Dict[str, Kunde]): Dictionary mit Kunden-ID als Schlüssel und Kunde als Wert (private)
    """
    
    def __init__(self) -> None:
        """Initialisiert eine neue Bibliothek."""
        self.__buecher: Dict[str, Buch] = {}
        self.__exemplare: Dict[str, int] = {}
        self.__kunden: Dict[str, Kunde] = {}
    
    def buch_hinzufuegen(self, buch: Buch, anzahl: int = 1) -> None:
        """
        Fügt ein neues Buch mit Anzahl der Exemplare zur Bibliothek hinzu.
        
        Args:
            buch: Das hinzuzufügende Buch
            anzahl: Anzahl der Exemplare (Standard: 1)
        """
        self.__buecher[buch.isbn] = buch
        self.__exemplare[buch.isbn] = self.__exemplare.get(buch.isbn, 0) + anzahl
        print(f"Buch '{buch.titel}' wurde mit {anzahl} Exemplar(en) zur Bibliothek hinzugefügt.")
    
    def buch_entfernen(self, isbn: str) -> bool:
        """
        Entfernt alle Exemplare eines Buchs aus der Bibliothek.
        
        Args:
            isbn: Die ISBN des zu entfernenden Buchs
            
        Returns:
            bool: True wenn das Buch gefunden und entfernt wurde, False sonst
        """
        if isbn in self.__buecher:
            buch = self.__buecher[isbn]
            del self.__buecher[isbn]
            del self.__exemplare[isbn]
            print(f"Buch '{buch.titel}' wurde aus der Bibliothek entfernt.")
            return True
        print(f"Buch mit ISBN {isbn} wurde nicht gefunden.")
        return False
    
    def kunde_registrieren(self, kunde: Kunde) -> bool:
        """
        Registriert einen neuen Kunden in der Bibliothek.
        
        Args:
            kunde: Der zu registrierende Kunde
            
        Returns:
            bool: True wenn die Registrierung erfolgreich war, False wenn die ID bereits existiert
        """
        if kunde.kunden_id not in self.__kunden:
            self.__kunden[kunde.kunden_id] = kunde
            print(f"Kunde {kunde.name} wurde erfolgreich registriert.")
            return True
        print(f"Kunde mit ID {kunde.kunden_id} existiert bereits.")
        return False
    
    def kunde_entfernen(self, kunden_id: str) -> bool:
        """
        Entfernt einen Kunden aus der Bibliothek.
        
        Args:
            kunden_id: Die ID des zu entfernenden Kunden
            
        Returns:
            bool: True wenn der Kunde gefunden und entfernt wurde, False sonst
        """
        if kunden_id in self.__kunden:
            kunde = self.__kunden[kunden_id]
            if kunde.anzahl_ausgeliehener_buecher > 0:
                print(f"Kunde {kunde.name} hat noch Bücher ausgeliehen und kann nicht entfernt werden.")
                return False
            del self.__kunden[kunden_id]
            print(f"Kunde {kunde.name} wurde aus der Bibliothek entfernt.")
            return True
        print(f"Kunde mit ID {kunden_id} wurde nicht gefunden.")
        return False
    
    def buch_ausleihen(self, kunden_id: str, isbn: str) -> bool:
        """
        Lässt einen Kunden ein Buch ausleihen.
        
        Args:
            kunden_id: Die ID des Kunden
            isbn: Die ISBN des auszuleihenden Buchs
            
        Returns:
            bool: True wenn das Ausleihen erfolgreich war, False sonst
        """
        if kunden_id not in self.__kunden:
            print(f"Kunde mit ID {kunden_id} nicht gefunden.")
            return False
            
        if isbn not in self.__buecher:
            print(f"Buch mit ISBN {isbn} nicht gefunden.")
            return False
            
        if self.__exemplare[isbn] <= 0:
            print(f"Keine Exemplare von '{self.__buecher[isbn].titel}' verfügbar.")
            return False
            
        kunde = self.__kunden[kunden_id]
        buch = self.__buecher[isbn]
        
        if kunde.buch_ausleihen(buch):
            self.__exemplare[isbn] -= 1
            return True
        return False
    
    def buch_zurueckgeben(self, kunden_id: str, isbn: str) -> bool:
        """
        Nimmt ein ausgeliehenes Buch zurück.
        
        Args:
            kunden_id: Die ID des Kunden
            isbn: Die ISBN des zurückzugebenden Buchs
            
        Returns:
            bool: True wenn die Rückgabe erfolgreich war, False sonst
        """
        if kunden_id not in self.__kunden:
            print(f"Kunde mit ID {kunden_id} nicht gefunden.")
            return False
            
        if isbn not in self.__buecher:
            print(f"Buch mit ISBN {isbn} nicht gefunden.")
            return False
            
        kunde = self.__kunden[kunden_id]
        buch = self.__buecher[isbn]
        
        if kunde.buch_zurueckgeben(buch):
            self.__exemplare[isbn] += 1
            return True
        return False
    
    def zeige_bestand(self) -> None:
        """Gibt eine Übersicht über alle Bücher und deren verfügbare Exemplare aus."""
        if not self.__buecher:
            print("Die Bibliothek ist leer.")
            return
        
        print("\nAktueller Bibliotheksbestand:")
        print("-" * 50)
        for isbn, buch in self.__buecher.items():
            print(f"{buch.details()} | Verfügbare Exemplare: {self.__exemplare[isbn]}")
        print("-" * 50)
        print(f"Verschiedene Titel: {len(self.__buecher)}")
    
    def zeige_kunden(self) -> None:
        """Gibt eine Übersicht über alle registrierten Kunden aus."""
        if not self.__kunden:
            print("Keine Kunden registriert.")
            return
        
        print("\nRegistrierte Kunden:")
        print("-" * 40)
        for kunde in self.__kunden.values():
            print(f"Name: {kunde.name} (ID: {kunde.kunden_id})")
            kunde.zeige_ausgeliehene_buecher()
        print("-" * 40)
        print(f"Gesamtanzahl Kunden: {len(self.__kunden)}")
    
    def finde_buch(self, isbn: str) -> Optional[Buch]:
        """
        Sucht ein Buch anhand seiner ISBN.
        
        Args:
            isbn: Die ISBN des gesuchten Buchs
            
        Returns:
            Optional[Buch]: Das gefundene Buch oder None wenn nicht gefunden
        """
        return self.__buecher.get(isbn)
    
    @property
    def anzahl_buecher(self) -> int:
        """
        Gibt die Anzahl verschiedener Bücher in der Bibliothek zurück.
        
        Returns:
            int: Anzahl der verschiedenen Bücher
        """
        return len(self.__buecher)