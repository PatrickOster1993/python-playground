from charakter.charakter import Charakter
import random

class Gegner(Charakter):
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung, gold=0, loot=None):
        super().__init__(name, lebenspunkte, angriffskraft, ruestung, gold)
        self.loot = loot or []

    def angreifen(self, ziel):
        schaden = self._angriffskraft
        ziel.erleide_schaden(schaden)
        return f"{self.name} greift an und verursacht {schaden} Schaden!"

    def drop_loot(self):
        """Gibt ein zufälliges Item oder Gold aus dem Loot-Pool zurück."""
        if not self.loot:
            return None
        return random.choice(self.loot)
