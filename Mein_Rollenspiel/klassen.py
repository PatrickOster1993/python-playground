from abc import ABC, abstractmethod
from random import randint

# Basisklasse Charakter
class Charakter(ABC):
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung):
        self._name = name
        self._lebenspunkte = lebenspunkte
        self._angriffskraft = angriffskraft
        self._ruestung = ruestung

    @abstractmethod
    def angreifen(self, ziel):
        pass

    def check_status(self):
        return f"{self._name} - LP: {self._lebenspunkte}, Angriff: {self._angriffskraft}, Rüstung: {self._ruestung}"

    @property
    def lebenspunkte(self):
        return self._lebenspunkte

    @lebenspunkte.setter
    def lebenspunkte(self, value):
        self._lebenspunkte = max(0, value)

    @property
    def name(self):
        return self._name


# Magier-Klasse
class Magier(Charakter):
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung, mana):
        super().__init__(name, lebenspunkte, angriffskraft, ruestung)
        self._mana = mana

    def angreifen(self, ziel):
        if self._mana >= 5:
            schaden = self._angriffskraft
            self._mana -= 5
            ziel.lebenspunkte -= max(0, schaden - ziel._ruestung)
            return f"{self._name} greift {ziel.name} mit Magie an und verursacht {schaden} Schaden."
        else:
            return f"{self._name} hat nicht genug Mana, um anzugreifen."


# Schurke-Klasse
class Schurke(Charakter):
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung, geschicklichkeit):
        super().__init__(name, lebenspunkte, angriffskraft, ruestung)
        self._geschicklichkeit = geschicklichkeit

    def angreifen(self, ziel):
        krit = randint(1, 100) <= self._geschicklichkeit
        schaden = self._angriffskraft * (2 if krit else 1)
        ziel.lebenspunkte -= max(0, schaden - ziel._ruestung)
        return f"{self._name} greift {ziel.name} an und verursacht {schaden} Schaden{' (kritischer Treffer)' if krit else ''}."


# Gegner-Klassen
class Goblin(Charakter):
    def angreifen(self, ziel):
        schaden = self._angriffskraft
        ziel.lebenspunkte -= max(0, schaden - ziel._ruestung)
        return f"Goblin greift {ziel.name} an und verursacht {schaden} Schaden."


class GoblinKoenig(Charakter):
    def angreifen(self, ziel):
        schaden = self._angriffskraft * 2
        ziel.lebenspunkte -= max(0, schaden - ziel._ruestung)
        return f"Goblin-König greift {ziel.name} mit brutaler Stärke an und verursacht {schaden} Schaden."


# Kampf-Logik
class Kampf:
    @staticmethod
    def kampf_szenario(charakter_1, charakter_2):
        while charakter_1.lebenspunkte > 0 and charakter_2.lebenspunkte > 0:
            print(charakter_1.angreifen(charakter_2))
            if charakter_2.lebenspunkte <= 0:
                return f"{charakter_2.name} wurde besiegt! {charakter_1.name} gewinnt!"

            print(charakter_2.angreifen(charakter_1))
            if charakter_1.lebenspunkte <= 0:
                return f"{charakter_1.name} wurde besiegt! {charakter_2.name} gewinnt!"
