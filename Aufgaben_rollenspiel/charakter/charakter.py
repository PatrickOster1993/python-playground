from abc import ABC, abstractmethod

class Charakter(ABC):
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung, gold=0):
        self.name = name
        self._lebenspunkte = lebenspunkte
        self._max_lebenspunkte = lebenspunkte
        self._angriffskraft = angriffskraft
        self._ruestung = ruestung
        self.gold = gold
        self.waffe = None
        self.ruestung = None
        self.schild = None

    @abstractmethod
    def angreifen(self, ziel):
        pass

    def erleide_schaden(self, schaden):
        effektiv_schaden = max(0, schaden - self._ruestung)
        self._lebenspunkte = max(0, self._lebenspunkte - effektiv_schaden)
        return effektiv_schaden

    def heilen(self, menge):
        self._lebenspunkte = min(self._lebenspunkte + menge, self._max_lebenspunkte)

    def ausrüsten_waffe(self, waffe):
        self.waffe = waffe
        self._angriffskraft += waffe.schaden
        print(f"{self.name} hat {waffe.name} ausgerüstet! (+{waffe.schaden} Angriffskraft)")

    def ausrüsten_ruestung(self, ruestung):
        self.ruestung = ruestung
        self._ruestung += ruestung.verteidigung
        print(f"{self.name} hat {ruestung.name} ausgerüstet! (+{ruestung.verteidigung} Verteidigung)")

    def ausrüsten_schild(self, schild):
        self.schild = schild
        self._ruestung += schild["basisverteidigung"]
        print(f"{self.name} hat {schild['name']} ausgerüstet! (+{schild['basisverteidigung']} Verteidigung)")

    def ist_besiegt(self):
        return self._lebenspunkte <= 0
