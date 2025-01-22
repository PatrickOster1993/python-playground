# Klassendiagramm Bibliotheksverwaltung

```mermaid
classDiagram

%% Abstrakte Basisklasse Buch
class Buch {
    <<abstract>>
    -titel: str
    -autor: str
    -isbn: str
    +getTitel() str
    +getAutor() str
    +getIsbn() str
    +setTitel(titel: str)
    +setAutor(autor: str)
    +setIsbn(isbn: str)
    +details() str
    +lesen()* str
}

%% Sachbuch erbt von Buch
class Sachbuch {
    -thema: str
    +getThema() str
    +setThema(thema: str)
    +lesen() str
    +wissenVermitteln() str
}

%% Roman erbt von Buch
class Roman {
    -genre: str
    -genre_fsk_mapping: dict
    +getGenre() str
    +setGenre(genre: str)
    +getFsk() int
    +lesen() str
}

%% Bibliothek verwaltet Bücher und Kunden
class Bibliothek {
    -buecher: Dict[str, Buch]
    -exemplare: Dict[str, int]
    -kunden: Dict[str, Kunde]
    +buch_hinzufuegen(buch: Buch, anzahl: int)
    +buch_entfernen(isbn: str) bool
    +kunde_registrieren(kunde: Kunde) bool
    +kunde_entfernen(kunden_id: str) bool
    +buch_ausleihen(kunden_id: str, isbn: str) bool
    +buch_zurueckgeben(kunden_id: str, isbn: str) bool
    +zeige_bestand()
    +zeige_kunden()
    +finde_buch(isbn: str) Buch
    +getAnzahlBuecher() int
}

%% Kundenklasse
class Kunde {
    -name: str
    -kunden_id: str
    -ausgeliehene_buecher: Set[str]
    +getName() str
    +getKundenId() str
    +getAnzahlAusgeliehenerBuecher() int
    +buch_ausleihen(buch: Buch) bool
    +buch_zurueckgeben(buch: Buch) bool
    +hat_buch_ausgeliehen(isbn: str) bool
    +zeige_ausgeliehene_buecher()
}

%% Vererbungsbeziehungen
Buch <|-- Sachbuch : erbt von
Buch <|-- Roman : erbt von

%% Aggregationsbeziehungen
Bibliothek o-- Buch : verwaltet
Bibliothek o-- Kunde : verwaltet
Kunde o-- Buch : leiht aus