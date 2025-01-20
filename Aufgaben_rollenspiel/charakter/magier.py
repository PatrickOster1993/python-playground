from .charakter import Charakter

class Magier(Charakter):
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung, mana, gold=0):
        super().__init__(name, lebenspunkte, angriffskraft, ruestung, gold)
        self._mana = mana

    def zaubern(self, ziel, tier=1):
        kosten = 10 if tier == 1 else 20
        schaden = self._angriffskraft * (1.5 if tier == 1 else 2.5)
        if self._mana >= kosten:
            self._mana -= kosten
            ziel.erleide_schaden(schaden)
            return f"{self.name} wirkt einen T{tier}-Zauber und verursacht {schaden} Schaden!"
        return f"{self.name} hat nicht genug Mana!"
