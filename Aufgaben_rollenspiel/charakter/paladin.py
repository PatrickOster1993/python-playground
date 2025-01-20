from .charakter import Charakter

class Paladin(Charakter):
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung, mana, gold=0):
        super().__init__(name, lebenspunkte, angriffskraft, ruestung, gold)
        self._mana = mana

    def angreifen(self, ziel):
        """Normale Angriffe des Paladins."""
        schaden = self._angriffskraft
        ziel.erleide_schaden(schaden)
        return f"{self.name} schlägt mit seinem Kolben zu und verursacht {schaden} Schaden!"

    def heilen(self, ziel):
        """Heilt ein einzelnes Ziel mit Mana."""
        kosten = 15
        heilung = 40
        if self._mana >= kosten:
            self._mana -= kosten
            ziel.heilen(heilung)
            return f"{self.name} heilt {ziel.name} um {heilung} HP!"
        return f"{self.name} hat nicht genug Mana für Heilung."

    def ausrüsten_schild(self, schild):
        """Der Paladin kann ein Schild ausrüsten."""
        if schild:
            self._ruestung += schild["basisverteidigung"]
            self.schild = schild
            return f"{self.name} hat das Schild {schild['name']} ausgerüstet! (+{schild['basisverteidigung']} Verteidigung)"
        return f"{self.name} kann kein Schild ausrüsten!"
