from .gegner import Gegner

class Bandit(Gegner):
    def __init__(self):
        super().__init__(
            "Bandit",
            lebenspunkte=60,
            angriffskraft=14,
            ruestung=3,
            gold=12,
            loot=["10 Gold", "Wurfmesser"]
        )
