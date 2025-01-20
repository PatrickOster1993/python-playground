import random
from .charakter import Charakter

class Schurke(Charakter):
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung, gold=0):
        super().__init__(name, lebenspunkte, angriffskraft, ruestung, gold)

    def angreifen(self, ziel):
        """Schurke greift an und verursacht Schaden."""
        schaden = self._angriffskraft + random.randint(1, 5)
        ziel.erleide_schaden(schaden)
        return f"{self.name} greift mit Dolchen an und verursacht {schaden} Schaden!"

    def stehlen(self, ziel):
        """Schurke bestiehlt den Gegner."""
        if hasattr(ziel, "gestohlen") and ziel.gestohlen:
            return f"{ziel.name} wurde bereits bestohlen!"
        ziel.gestohlen = True

        loot = ziel.loot if hasattr(ziel, "loot") else None
        if loot:
            item = random.choice(loot)
            if isinstance(item, int):  # Gold
                self.gold += item
                return f"{self.name} hat {item} Gold gestohlen!"
            elif isinstance(item, dict):  # Gegenstand
                return f"{self.name} hat {item['name']} gestohlen!"
        return f"{self.name} hat nichts Wertvolles gefunden!"
