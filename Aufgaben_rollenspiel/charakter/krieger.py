from .charakter import Charakter

class Krieger(Charakter):
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung, gold=0):
        super().__init__(name, lebenspunkte, angriffskraft, ruestung, gold)

    def angreifen(self, ziel):
        schaden = self._angriffskraft
        ziel.erleide_schaden(schaden)
        return f"{self.name} greift an und verursacht {schaden} Schaden!"
