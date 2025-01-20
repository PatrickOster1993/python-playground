# ## Teil 1: Neue Klassen hinzufügen (Vererbung und Abstraktion)
# - **Erstelle eine abstrakte Basisklasse `Charakter`:**
#   - Diese Klasse enthält die grundlegenden Attribute (z. B. `name`, `lebenspunkte`, `angriffskraft`, `ruestung`).
#   - Definiere die Methode `angreifen`, aber lasse sie abstrakt (`@abstractmethod`).
#   - Implementiere eine Methode `checkStatus`, die den Status eines Charakters ausgibt.


from abc import ABC, abstractmethod
import random

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
        
class Mage(Character):
    def __init__(self, name: str, health_points: int, attack_power: int, armor: int, mana: int):
        super().__init__(name, health_points, attack_power, armor)
        self._mana = mana

    def attack(self, target):
        if self._mana > 0:
            damage = self._attack_power
            self._mana -= 10  # Reduce mana by a fixed amount
            print(f"{self._name} attacks {target._name} with magic for {damage} damage!")
        else:
            print(f"{self._name} has no mana left to attack!")

    def cast_spell(self, target):
        if self._mana >= 20:
            damage = self._attack_power * 2
            self._mana -= 20  # Reduce mana by a larger amount
            print(f"{self._name} casts a powerful spell on {target._name} for {damage} damage!")
        else:
            print(f"{self._name} doesn't have enough mana to cast a spell!")

class Rogue(Character):
    def __init__(self, name: str, health_points: int, attack_power: int, armor: int, dexterity: int):
        super().__init__(name, health_points, attack_power, armor)
        self._dexterity = dexterity

    def attack(self, target):
        critical_hit = random.random() < 0.2  # 20% chance for a critical hit
        damage = self._attack_power * 2 if critical_hit else self._attack_power
        if critical_hit:
            print(f"{self._name} lands a critical hit on {target._name} for {damage} damage!")
        else:
            print(f"{self._name} attacks {target._name} for {damage} damage!")

    def hide(self):
        print(f"{self._name} hides in the shadows, increasing evasion chance!")
