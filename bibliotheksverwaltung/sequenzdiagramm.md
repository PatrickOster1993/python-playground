# Sequenzdiagramm Buchausleihe

```mermaid
sequenceDiagram
    participant Kunde as Kundenoberfläche
    participant Bibliothek as Bibliothekssystem
    participant KundenDB as Kundenverwaltung
    participant BuecherDB as Buchbestand

    Kunde->>Bibliothek: Ausleihanfrage(kunden_id, isbn)
    activate Bibliothek
    
    Bibliothek->>KundenDB: Prüfe Kundenexistenz(kunden_id)
    KundenDB-->>Bibliothek: Kundenstatus
    
    alt Kunde nicht registriert
        Bibliothek-->>Kunde: Fehlermeldung: Unbekannter Kunde
    else
        Bibliothek->>BuecherDB: Prüfe Verfügbarkeit(isbn)
        BuecherDB-->>Bibliothek: Exemplarzahl
        
        alt Exemplare = 0
            Bibliothek-->>Kunde: "Buch nicht verfügbar"
        else
            Bibliothek->>BuecherDB: Reduziere Exemplar
            Bibliothek->>KundenDB: Füge Ausleihe hinzu
            Bibliothek-->>Kunde: Ausleihe bestätigt
        end
    end
    deactivate Bibliothek
```

## Erklärung der Interaktionen

1. **Ausleihanfrage Initiation**  
   Der Kunde sendet eine Anfrage mit seiner ID und der Buch-ISBN

2. **Kundenvalidierung**  
   Das System prüft in der Kunden-DB die Registrierung

3. **Buchverfügbarkeitscheck**  
   Bei gültigem Kunden wird der Buchbestand geprüft

4. **Kritische Pfade**  
   - Rote Route: Ungültige Kunden-ID
   - Gelbe Route: Keine verfügbaren Exemplare
   - Grüne Route: Erfolgreiche Ausleihe

5. **Transaktionsabschluss**  
   Bei Erfolg wird der Bestand aktualisiert und die Ausleihe registriert