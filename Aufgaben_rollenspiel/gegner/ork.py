from .gegner import Gegner

class Ork(Gegner):
    def __init__(self):
        super().__init__(
            "Ork",
            lebenspunkte=100,
            angriffskraft=15,
            ruestung=5,
            gold=20,
            loot=["Kleiner Heiltrank", "20 Gold", "Zweihandhammer"]
        )
