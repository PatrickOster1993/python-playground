# Klassendiagramm

```mermaid
classDiagram
%% Charakter-Hierarchie
class Charakter {
    <<Abstract>>
    +name: str
    #_lebenspunkte: int
    #_angriffskraft: int
    #_ruestung: int
    +waffe: Waffe?
    +checkStatus() void
    +angreifen(ziel: Charakter) void
    +__eq__(andere: Charakter) bool
    +lebenspunkte: int
}

class Magier {
    #_mana: int
    +angreifen(ziel: Charakter) void
    +zaubern(ziel: Charakter) void
}

class Schurke {
    #_geschicklichkeit: int
    +angreifen(ziel: Charakter) void
    +verstecken() void
}

Charakter <|-- Magier
Charakter <|-- Schurke

%% Waffen-Komposition
class Waffe {
    +name: str
    +schaden: int
    +haltbarkeit: int
    +__add__(andereWaffe: Waffe) Waffe
}

Charakter *-- Waffe : Komposition

%% Gilde-Aggregation
class Gilde {
    +name: str
    +mitglieder: list[Charakter]
    +anfuehrer: Charakter?
    +hinzufuegen(charakter: Charakter) void
    +anzeigen() void
    +anfuehrerBestimmen(charakter: Charakter) void
}

Gilde o-- Charakter : Aggregation

%% Kampfszenario
class kampf_szenario {
    +kampf_szenario(char1: Charakter, char2: Charakter) void
}

kampf_szenario .. Charakter : Dependency