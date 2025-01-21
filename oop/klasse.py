"""
Rollenspiel-Charaktersystem mit objektorientierten Programmierungsprinzipien.

Dieses Modul implementiert ein komplexes Charaktersystem für ein Rollenspiel
mit verschiedenen Klassen, Vererbung, abstrakten Klassen und Polymorphismus.

Klassen:
    Waffe: Basisklasse für alle Waffen im Spiel
    Gilde: Organisationseinheit für Charaktere
    Charakter (ABC): Abstrakte Basisklasse für alle Spielercharaktere
    Krieger: Nahkampf-Spezialist
    Magier: Zauberkundiger mit Mana-System
    Schurke: Geschickter Kämpfer mit kritischen Treffern
    Heiler: Unterstützende Klasse mit Heilfähigkeiten
    Paladin: Hybridklasse aus Magier und Krieger

Funktionen:
    kampf_szenario: Simuliert einen Kampf zwischen zwei Charakteren

Konstanten:
    TRENNLINIE_LANG: 50 Zeichen für primäre Trennlinien
    TRENNLINIE_KURZ: 30 Zeichen für sekundäre Trennlinien
"""

from abc import ABC, abstractmethod
import random
import time

# Konstanten für einheitliche Trennlinien
TRENNLINIE_LANG = 50  # Für Hauptüberschriften und wichtige Trennungen
TRENNLINIE_KURZ = 30  # Für Unterabschnitte und weniger wichtige Trennungen

class Waffe:
    """
    Repräsentiert eine Waffe im Spiel.

    Eine Waffe verfügt über einen Namen, Grundschaden und eine begrenzte
    Haltbarkeit. Die Waffe kann nur verwendet werden, solange ihre
    Haltbarkeit größer als 0 ist.

    Attributes:
        _name (str): Name der Waffe
        _schaden (int): Grundschaden der Waffe
        _haltbarkeit (int): Verbleibende Nutzungen der Waffe

    Methods:
        ist_nutzbar: Prüft ob die Waffe noch verwendet werden kann
        nutzen: Reduziert die Haltbarkeit bei Verwendung
    """
    def __init__(self, name: str, schaden: int, haltbarkeit: int):
        """
        Initialisiert eine neue Waffe.

        Args:
            name (str): Der Name der Waffe
            schaden (int): Grundschaden der Waffe
            haltbarkeit (int): Anzahl möglicher Verwendungen
        """
        self._name = name
        self._schaden = schaden
        self._haltbarkeit = haltbarkeit

    @property
    def name(self) -> str:
        """
        Name der Waffe.

        Returns:
            str: Der Name der Waffe
        """
        return self._name

    @property
    def schaden(self) -> int:
        """
        Aktueller Schaden der Waffe.

        Returns:
            int: Schadenswert wenn die Waffe nutzbar ist, sonst 0
        """
        return self._schaden if self.ist_nutzbar() else 0

    @property
    def haltbarkeit(self) -> int:
        """
        Aktuelle Haltbarkeit der Waffe.

        Returns:
            int: Verbleibende Anzahl möglicher Verwendungen
        """
        return self._haltbarkeit

    def ist_nutzbar(self) -> bool:
        """
        Prüft ob die Waffe noch verwendet werden kann.

        Returns:
            bool: True wenn Haltbarkeit > 0, sonst False
        """
        return self._haltbarkeit > 0

    def nutzen(self) -> bool:
        """
        Reduziert die Haltbarkeit der Waffe bei Verwendung.

        Returns:
            bool: True wenn die Waffe genutzt werden konnte, sonst False
        """
        if self.ist_nutzbar():
            self._haltbarkeit -= 1
            return True
        return False

    def __add__(self, other):
        """
        Überladung des + Operators zum Kombinieren von Waffen.

        Args:
            other (Waffe): Eine andere Waffe zum Kombinieren

        Returns:
            Waffe: Eine neue Waffe mit kombinierten Eigenschaften

        Raises:
            TypeError: Wenn other keine Waffe ist
        """
        if not isinstance(other, Waffe):
            raise TypeError("Kann nur Waffen miteinander kombinieren!")
        
        neuer_name = f"{self.name} + {other.name}"
        neuer_schaden = self.schaden + other.schaden
        neue_haltbarkeit = self.haltbarkeit + other.haltbarkeit
        
        return Waffe(neuer_name, neuer_schaden, neue_haltbarkeit)

class Gilde:
    """
    Organisationseinheit für Charaktere im Spiel.

    Die Gilde verwaltet eine Gruppe von Charakteren und deren Hierarchie.
    Sie ermöglicht das Hinzufügen von Mitgliedern, die Ernennung eines
    Anführers und die übersichtliche Darstellung der Gildenstruktur.

    Attributes:
        _name (str): Name der Gilde
        _mitglieder (list): Liste der Gildenmitglieder
        _anfuehrer (Optional[Charakter]): Anführer der Gilde, standardmäßig None

    Methods:
        hinzufuegen: Fügt einen Charakter zur Gilde hinzu
        anzeigen: Zeigt eine formatierte Liste aller Mitglieder
        anfuehrerBestimmen: Ernennt ein Mitglied zum Anführer
    """
    def __init__(self, name: str):
        """
        Initialisiert eine neue Gilde.

        Args:
            name (str): Name der Gilde
        """
        self._name = name
        self._mitglieder = []
        self._anfuehrer = None

    @property
    def name(self) -> str:
        """
        Name der Gilde.

        Returns:
            str: Der Name der Gilde
        """
        return self._name

    def hinzufuegen(self, charakter):
        """
        Fügt einen Charakter zur Gilde hinzu.

        Args:
            charakter (Charakter): Der hinzuzufügende Charakter

        Note:
            Ein Charakter kann nur einmal Mitglied einer Gilde sein.
            Bei Duplikaten wird eine Meldung ausgegeben.
        """
        if charakter not in self._mitglieder:
            self._mitglieder.append(charakter)
            print(f"{charakter.name} ist der Gilde '{self.name}' beigetreten!")
            print("=" * TRENNLINIE_KURZ)
        else:
            print(f"{charakter.name} ist bereits Mitglied der Gilde!")
            print("=" * TRENNLINIE_KURZ)

    def anzeigen(self):
        """
        Zeigt eine formatierte Liste aller Gildenmitglieder.

        Die Ausgabe ist hierarchisch gegliedert:
        1. Gildenname und Trennlinie
        2. Anführer (falls vorhanden)
        3. Alphabetisch sortierte Liste der übrigen Mitglieder
        """
        print(f"\nMitglieder der Gilde '{self.name}':")
        print("=" * TRENNLINIE_LANG)
        
        if self._anfuehrer:
            print(f"Anführer: {self._anfuehrer.name}")
            print("-" * TRENNLINIE_KURZ)
        
        print("\nMitglieder:")
        # Sortiere Mitglieder alphabetisch, außer dem Anführer
        for charakter in sorted(
            [c for c in self._mitglieder if c != self._anfuehrer],
            key=lambda x: x.name
        ):
            print(f"- {charakter.name}")
        print("=" * TRENNLINIE_LANG)

    def anfuehrerBestimmen(self, charakter):
        """
        Ernennt einen Charakter zum Anführer der Gilde.

        Args:
            charakter (Charakter): Der zum Anführer zu ernennende Charakter

        Note:
            Der Charakter muss bereits Mitglied der Gilde sein.
            Andernfalls wird eine entsprechende Meldung ausgegeben.
        """
        if charakter in self._mitglieder:
            self._anfuehrer = charakter
            print(f"{charakter.name} wurde zum Anführer der Gilde '{self.name}' ernannt!")
            print("=" * TRENNLINIE_LANG)
        else:
            print(f"{charakter.name} ist kein Mitglied der Gilde und kann nicht zum Anführer ernannt werden!")
            print("=" * TRENNLINIE_LANG)

def kampf_szenario(charakter_1, charakter_2):
    """
    Simuliert einen Kampf zwischen zwei Charakteren.

    Diese Funktion führt einen rundenbasierten Kampf durch, bei dem beide
    Charaktere abwechselnd angreifen. Der Kampf endet, wenn mindestens
    einer der Charaktere keine Lebenspunkte mehr hat.

    Args:
        charakter_1 (Charakter): Erster kämpfender Charakter
        charakter_2 (Charakter): Zweiter kämpfender Charakter

    Note:
        Die Funktion demonstriert das Polymorphismus-Prinzip durch die
        Verwendung der abstrakten angreifen-Methode mit verschiedenen
        Charakterklassen.
    """
    runde = 1
    print("\nKampf beginnt!")
    print("=" * TRENNLINIE_LANG)
    
    while charakter_1.lebenspunkte > 0 and charakter_2.lebenspunkte > 0:
        print(f"\nRunde {runde}:")
        print("-" * TRENNLINIE_KURZ)
        
        # Charakter 1 greift an
        if charakter_1.lebenspunkte > 0:
            charakter_1.angreifen(charakter_2)
            time.sleep(1)  # Kurze Pause für bessere Lesbarkeit
            
        # Charakter 2 greift an
        if charakter_2.lebenspunkte > 0:
            charakter_2.angreifen(charakter_1)
            time.sleep(1)
            
        # Status anzeigen
        print(f"\nStatus nach Runde {runde}:")
        print("-" * TRENNLINIE_KURZ)
        charakter_1.checkStatus()
        print()
        charakter_2.checkStatus()
        
        runde += 1
    
    # Gewinner ermitteln
    print("\nKampf beendet!")
    print("=" * TRENNLINIE_LANG)
    if charakter_1.lebenspunkte <= 0 and charakter_2.lebenspunkte <= 0:
        print("Unentschieden! Beide Charaktere wurden besiegt!")
    elif charakter_1.lebenspunkte <= 0:
        print(f"{charakter_2.name} hat gewonnen!")
    else:
        print(f"{charakter_1.name} hat gewonnen!")
    print("=" * TRENNLINIE_LANG)

class Charakter(ABC):
    """
    Abstrakte Basisklasse für alle Spielercharaktere.

    Diese Klasse definiert die grundlegende Struktur eines Charakters im Spiel.
    Sie implementiert die gemeinsamen Eigenschaften und das Interface für
    spezifische Charakterklassen.

    Attributes:
        _name (str): Name des Charakters
        _lebenspunkte (int): Aktuelle Gesundheit des Charakters
        _angriffskraft (int): Basis-Angriffsstärke ohne Waffenbonus
        _ruestung (int): Schadensreduzierung durch Rüstung
        _waffe (Optional[Waffe]): Aktuell ausgerüstete Waffe

    Methods:
        angreifen: Abstrakte Methode für Kampfaktionen
        checkStatus: Zeigt den aktuellen Status des Charakters
        waffe_ausruesten: Rüstet eine neue Waffe aus
    """
    def __init__(self, name: str, lebenspunkte: int, angriffskraft: int, ruestung: int):
        """
        Initialisiert einen neuen Charakter.

        Args:
            name (str): Name des Charakters
            lebenspunkte (int): Startmenge an Lebenspunkten
            angriffskraft (int): Basis-Angriffsstärke
            ruestung (int): Grundwert der Rüstung
        """
        self._name = name
        self._lebenspunkte = lebenspunkte
        self._angriffskraft = angriffskraft
        self._ruestung = ruestung
        self._waffe = None

    @property
    def name(self) -> str:
        """
        Name des Charakters.

        Returns:
            str: Der Name des Charakters
        """
        return self._name

    @name.setter
    def name(self, text: str) -> None:
        """
        Setzt den Namen des Charakters.

        Args:
            text (str): Der neue Name des Charakters
        """
        self._name = text

    @property
    def lebenspunkte(self) -> int:
        """
        Aktuelle Lebenspunkte des Charakters.

        Returns:
            int: Anzahl der verbleibenden Lebenspunkte
        """
        return self._lebenspunkte

        Args:
            wert (int): Neue Anzahl der Lebenspunkte

        Note:
            Negative Werte werden automatisch auf 0 gesetzt.
        """
        if wert < 0:
            print("Lebenspunkte können nicht negativ sein!")
            print("=" * TRENNLINIE_KURZ)
            self._lebenspunkte = 0
        else:
            self._lebenspunkte = wert

    @property
    def angriffskraft(self) -> int:
        """
        Aktuelle Angriffskraft des Charakters.

        Berücksichtigt sowohl die Basis-Angriffskraft als auch
        den zusätzlichen Schaden durch eine ausgerüstete Waffe.

        Returns:
            int: Gesamte Angriffskraft (Basis + Waffenschaden)
        """
        basis_kraft = self._angriffskraft
        if self._waffe and self._waffe.ist_nutzbar():
            return basis_kraft + self._waffe.schaden
        return basis_kraft

    @angriffskraft.setter
    def angriffskraft(self, wert: int) -> None:
        """
        Setzt die Basis-Angriffskraft des Charakters.

        Args:
            wert (int): Neue Basis-Angriffskraft

        Note:
            Negative Werte werden nicht akzeptiert.
        """
        if wert < 0:
            print("Angriffskraft kann nicht negativ sein!")
            print("=" * TRENNLINIE_KURZ)
        else:
            self._angriffskraft = wert

    @property
    def ruestung(self) -> int:
        """
        Aktuelle Rüstung des Charakters.

        Returns:
            int: Rüstungswert für Schadensreduzierung
        """
        return self._ruestung
    
    @ruestung.setter
    def ruestung(self, wert: int) -> None:
        """
        Setzt den Rüstungswert des Charakters.

        Args:
            wert (int): Neuer Rüstungswert

        Note:
            Negative Werte werden nicht akzeptiert.
        """
        if wert < 0:
            print("Rüstung kann nicht negativ sein!")
            print("=" * TRENNLINIE_KURZ)
        else:
            self._ruestung = wert

    def waffe_ausruesten(self, waffe: 'Waffe') -> None:
        """
        Rüstet eine neue Waffe aus.

        Args:
            waffe (Waffe): Die auszurüstende Waffe

        Note:
            Eine vorher ausgerüstete Waffe wird dabei überschrieben.
        """
        self._waffe = waffe
        print(f"{self.name} hat {waffe.name} ausgerüstet!")
        print("=" * TRENNLINIE_KURZ)

    @abstractmethod
    def angreifen(self, gegner: 'Charakter') -> None:
        """
        Abstrakte Methode für den Angriff auf einen anderen Charakter.

        Args:
            gegner (Charakter): Der anzugreifende Charakter

        Note:
            Muss von jeder Charakterklasse implementiert werden.
            Die konkrete Implementierung definiert die spezifische
            Kampfmechanik der jeweiligen Klasse.
        """
        pass

    def checkStatus(self) -> None:
        """
        Zeigt den aktuellen Status des Charakters an.

        Gibt alle relevanten Attribute in einem einheitlich
        formatierten Block aus.
        """
        print("=" * TRENNLINIE_LANG)
        print(f"# {self.name:^{TRENNLINIE_LANG-4}} #")
        print("=" * TRENNLINIE_LANG)
        print(f"# {'Lebenspunkte:':<20} {self.lebenspunkte:>25} #")
        print(f"# {'Angriffskraft:':<20} {self.angriffskraft:>25} #")
        print(f"# {'Rüstung:':<20} {self.ruestung:>25} #")
        if self._waffe:
            print(f"# {'Waffe:':<20} {self._waffe.name:>25} #")
            print(f"# {'Haltbarkeit:':<20} {self._waffe.haltbarkeit:>25} #")
        print("=" * TRENNLINIE_LANG)

    def __eq__(self, other) -> bool:
        """
        Vergleicht zwei Charaktere auf Gleichheit.

        Args:
            other (Charakter): Der zu vergleichende Charakter

        Returns:
            bool: True wenn die Charaktere in Name, Angriffskraft
                 und Rüstung übereinstimmen

        Note:
            Wird hauptsächlich für die Gildenverwaltung verwendet.
        """
        if not isinstance(other, Charakter):
            return False
        return (self.name == other.name and
                self.angriffskraft == other.angriffskraft and
                self.ruestung == other.ruestung)

