from gegner import Goblin, Ork, Skelettmagier, Bandit, Troll, Drachenlord
import random

def generiere_gegner_gruppe(max_gegner=3):
    """Erstellt eine Gruppe von Gegnern."""
    gegner_klassen = [Goblin, Ork, Skelettmagier, Bandit, Troll]
    return [random.choice(gegner_klassen)() for _ in range(random.randint(1, max_gegner))]

def generiere_boss():
    """Erstellt einen Bossgegner."""
    return Drachenlord()
