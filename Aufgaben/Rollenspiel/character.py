# ## Teil 1: Neue Klassen hinzufügen (Vererbung und Abstraktion)
# - **Erstelle eine abstrakte Basisklasse `Charakter`:**
#   - Diese Klasse enthält die grundlegenden Attribute (z. B. `name`, `lebenspunkte`, `angriffskraft`, `ruestung`).
#   - Definiere die Methode `angreifen`, aber lasse sie abstrakt (`@abstractmethod`).
#   - Implementiere eine Methode `checkStatus`, die den Status eines Charakters ausgibt.


from abc import ABC, abstractmethod

class Character(ABC):
        def __init__(self, name: str, health_points: int, attack_power: int, armor: int):
                self._name = name
                self._health_points = health_points
                self._attack_power = attack_power
                self._armor = armor

        @abstractmethod
        def attack(self, target):
                # this method must bei implemented in subclasses.
                pass
        
        def check_status(self):
                status = (
                        f"Name: {self.name}\n"
                        f"Health Points: {self._health_points}\n"
                        f"Attack Power: {self._attack_power}\n"
                        f"Armor: {self._armor}\n"
                )
                return status