from .gegner import Gegner

class Skelettmagier(Gegner):
    def __init__(self):
        super().__init__(
            "Skelettmagier",
            lebenspunkte=80,
            angriffskraft=12,
            ruestung=3,
            gold=15,
            loot=["Manatrank", "10 Gold", "Zauberstab der Flammen"]
        )
