from .gegner import Gegner

class Drachenlord(Gegner):
    def __init__(self):
        super().__init__(
            "Drachenlord",
            lebenspunkte=300,
            angriffskraft=25,
            ruestung=10,
            gold=100,
            loot=["Legendäres Schwert", "100 Gold", "Flammenring"]
        )

    def feuerschlag(self, ziel):
        """Spezieller Angriff des Drachenlords."""
        schaden = self._angriffskraft * 2
        ziel.erleide_schaden(schaden)
        return f"{self.name} entfesselt einen Feuerschlag und verursacht {schaden} Schaden!"
