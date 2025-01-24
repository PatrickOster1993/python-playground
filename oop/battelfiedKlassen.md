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
    +angreifen(ziel: Charakter)* void
    +waffe_ausruesten(waffe: Waffe) void
    +lebenspunkte: int property
    +angriffskraft: int property
    +ruestung: int property
}

class Krieger {
    +angreifen(ziel: Charakter) void
    +blocken() void
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

class Heiler {
    #_heilungskraft: int
    +angreifen(ziel: Charakter) void
    +heilen(ziel: Charakter) void
}

class Paladin {
    #_glaube: int
    +angreifen(ziel: Charakter) void
    +segnen() void
}

Charakter <|-- Krieger
Charakter <|-- Magier
Charakter <|-- Schurke
Charakter <|-- Heiler
Charakter <|-- Paladin
Krieger <|-- Paladin
Magier <|-- Paladin

%% Waffen-Komposition
class Waffe {
    +name: str
    +schaden: int
    +haltbarkeit: int
    +ist_nutzbar() bool
    +nutzen() bool
    +__add__(other: Waffe) Waffe
}

Charakter *-- Waffe : Komposition

%% Gilde-Struktur
class Gilde {
    +name: str
    +mitglieder: List~Charakter~
    +anfuehrer: Charakter?
    +hinzufuegen(c: Charakter) void
    +anzeigen() void
    +anfuehrerBestimmen(c: Charakter) void
}

Gilde o-- Charakter : Aggregation

%% Kampflogik
class kampf_szenario {
    +kampf_szenario(c1: Charakter, c2: Charakter) void
}

kampf_szenario ..> Charakter : Dependency
kampf_szenario ..> Waffe : Indirect Usage

%% Besondere Beziehungen
note for Paladin "Kombiniert Eigenschaften\nvon Krieger und Magier\n(Multiple Vererbung)"
note for Waffe "Operatorüberladung:\n__add__ für Waffenkombination"
note for kampf_szenario "Verwendet Polymorphismus\nüber Charakter.angreifen()"