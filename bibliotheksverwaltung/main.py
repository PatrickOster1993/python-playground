#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Hauptprogramm der Bibliotheksverwaltung.
Demonstriert die Verwendung der implementierten Klassen.
"""

from bibliothek import Bibliothek
from sachbuch import Sachbuch
from roman import Roman
from kunde import Kunde

def main():
    """Hauptfunktion zum Testen der Bibliotheksverwaltung."""
    
    # Bibliothek erstellen
    print("Erstelle neue Bibliothek...")
    bibliothek = Bibliothek()
    
    # Beispielbücher erstellen
    print("\nErstelle Beispielbücher...")
    
    # Sachbücher
    python_buch = Sachbuch(
        "Python Programmierung",
        "Max Mustermann",
        "978-3-86680-192-1",
        "Programmierung"
    )
    
    kochen_buch = Sachbuch(
        "Gesunde Küche",
        "Lisa Koch",
        "978-3-86680-192-2",
        "Ernährung"
    )
    
    # Romane
    fantasy_roman = Roman(
        "Der Herr der Ringe",
        "J.R.R. Tolkien",
        "978-3-86680-192-3",
        "Fantasy"
    )
    
    thriller = Roman(
        "Das Schweigen der Lämmer",
        "Thomas Harris",
        "978-3-86680-192-4",
        "Thriller"
    )
    
    # Bücher mit mehreren Exemplaren zur Bibliothek hinzufügen
    print("\nFüge Bücher zur Bibliothek hinzu...")
    bibliothek.buch_hinzufuegen(python_buch, 2)  # 2 Exemplare
    bibliothek.buch_hinzufuegen(kochen_buch, 1)  # 1 Exemplar
    bibliothek.buch_hinzufuegen(fantasy_roman, 3)  # 3 Exemplare
    bibliothek.buch_hinzufuegen(thriller, 2)  # 2 Exemplare
    
    # Bestand anzeigen
    bibliothek.zeige_bestand()
    
    # Kunden erstellen und registrieren
    print("\nRegistriere Kunden...")
    kunde1 = Kunde("Anna Schmidt", "K001")
    kunde2 = Kunde("Bob Meyer", "K002")
    
    bibliothek.kunde_registrieren(kunde1)
    bibliothek.kunde_registrieren(kunde2)
    
    # Kundenübersicht
    bibliothek.zeige_kunden()
    
    # Bücher ausleihen
    print("\nBücher werden ausgeliehen...")
    bibliothek.buch_ausleihen("K001", "978-3-86680-192-1")  # Python-Buch
    bibliothek.buch_ausleihen("K001", "978-3-86680-192-3")  # Fantasy-Roman
    bibliothek.buch_ausleihen("K002", "978-3-86680-192-4")  # Thriller
    
    # Aktualisierte Übersichten
    print("\nAktualisierter Bestand:")
    bibliothek.zeige_bestand()
    print("\nAktualisierte Kundenübersicht:")
    bibliothek.zeige_kunden()
    
    # Ein Buch zurückgeben
    print("\nBuch wird zurückgegeben...")
    bibliothek.buch_zurueckgeben("K001", "978-3-86680-192-1")  # Python-Buch
    
    # Finale Übersichten
    print("\nFinaler Bestand:")
    bibliothek.zeige_bestand()
    print("\nFinale Kundenübersicht:")
    bibliothek.zeige_kunden()
    
    # Methoden der verschiedenen Buchtypen testen
    print("\nTeste spezifische Methoden der Bücher:")
    print("\nSachbuch:")
    print(python_buch.lesen())
    print(python_buch.wissenVermitteln())
    
    print("\nRoman:")
    print(fantasy_roman.lesen())
    print(f"FSK-Einstufung von '{fantasy_roman.titel}': {fantasy_roman.fsk}")
    print(f"FSK-Einstufung von '{thriller.titel}': {thriller.fsk}")
    
    # Versuche ein nicht verfügbares Buch auszuleihen
    print("\nVersuche ein weiteres Exemplar eines ausgeliehenen Buchs auszuleihen...")
    bibliothek.buch_ausleihen("K002", "978-3-86680-192-3")  # Fantasy-Roman

if __name__ == "__main__":
    main()