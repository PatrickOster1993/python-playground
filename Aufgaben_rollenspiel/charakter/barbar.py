from .charakter import Charakter

class Barbar(Charakter):
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung, gold=0):
        super().__init__(name, lebenspunkte, angriffskraft, ruestung, gold)

    def angreifen(self, ziel):
        schaden = self._angriffskraft * 1.5
        ziel.erleide_schaden(schaden)
        return f"{self.name} schwingt seine Zweihandwaffe und verursacht {schaden} Schaden!"
