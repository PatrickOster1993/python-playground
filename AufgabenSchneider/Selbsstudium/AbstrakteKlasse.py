from abc import ABC, abstractmethod

class Tier(ABC):
    @abstractmethod
    def bewegen(self):
        pass  # Abstrakte Methode

class Hund(Tier):
    def bewegen(self):
        print("Der Hund rennt.")

class Katze(Tier):
    def bewegen(self):
        print("Die Katze schleicht.")

# Jetzt funktioniert alles
tiere = [Hund(), Katze()]
for tier in tiere:
    tier.bewegen()
