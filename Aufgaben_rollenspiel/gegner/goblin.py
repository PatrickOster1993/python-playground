from .gegner import Gegner

class Goblin(Gegner):
    def __init__(self):
        super().__init__(
            "Goblin",
            lebenspunkte=50,
            angriffskraft=10,
            ruestung=2,
            gold=10,
            loot=["Kleiner Heiltrank", "5 Gold", "Dolch"]
        )
