from .charakter import Charakter

class Priester(Charakter):
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung, mana, gold=0):
        super().__init__(name, lebenspunkte, angriffskraft, ruestung, gold)
        self._mana = mana

    def heilen(self, ziel=None, gruppe=None):
        kosten = 15
        heilung = 50
        if ziel and self._mana >= kosten:
            self._mana -= kosten
            ziel.heilen(heilung)
            return f"{self.name} heilt {ziel.name} um {heilung} HP!"
        elif gruppe and self._mana >= kosten:
            self._mana -= kosten
            for mitglied in gruppe:
                mitglied.heilen(heilung // len(gruppe))
            return f"{self.name} heilt die Gruppe um {heilung // len(gruppe)} HP pro Person!"
        return f"{self.name} hat nicht genug Mana!"
