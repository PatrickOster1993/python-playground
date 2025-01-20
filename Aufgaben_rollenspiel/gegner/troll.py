from .gegner import Gegner

class Troll(Gegner):
    def __init__(self):
        super().__init__(
            "Troll",
            lebenspunkte=150,
            angriffskraft=18,
            ruestung=7,
            gold=30,
            loot=["Großer Heiltrank", "30 Gold", "Kriegshammer"]
        )
