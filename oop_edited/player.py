class Character:
    def __init__(self, name: str, hp: int, mp: int, atk: int, defense: int, magicattack: int, magicdefense:int):
        self.name = name
        self.hp = hp
        self.max_hp = hp if hp > 0 else 1  # Stelle sicher, dass max_hp nicht 0 ist
        self.mp = mp
        self.max_mp = mp if mp > 0 else 1  # Stelle sicher, dass max_mp nicht 0 ist
        self.atk = atk
        self.defense = defense
        self.magicattack = magicattack
        self.magicdefense = magicdefense
        
    def angreifen(self, gegner):
        schaden = max(0, self.atk - gegner.defense)
        gegner.hp = max(0, gegner.hp - schaden)
        print(f"{self.name} greift {gegner.name} an und fügt {schaden} Schaden zu!")
        
    def cast(self, gegner):
        schaden = self.magicattack
        gegner.hp = max(0, gegner.hp - schaden)
        print(f"{self.name} zaubert und fügt {gegner.name} {schaden} Schaden zu!")
        if gegner.hp == 0:
            print(f"{gegner.name} wurde besiegt!")
            
    def heilen(self, value):
        self.hp += value
        print(f"{self.name} hat sich um {value} Lebenspunkte geheilt.")
        
    def show_bar(self, current, maximum, bar_length=20):
        if maximum == 0:
            maximum = 1  # Vermeide Division durch 0
        ratio = current / maximum
        filled_length = int(bar_length * ratio)
        bar = "█" * filled_length + "_" * (bar_length - filled_length)
        return bar
    
    def status(self):
        status_line = f"Name: {self.name}, HP: [{self.show_bar(self.hp, self.max_hp)}] {self.hp}/{self.max_hp}"
        if self.mp > 1:
            status_line += f", MP: [{self.show_bar(self.mp, self.max_mp)}] {self.mp}/{self.max_mp}"
        status_line += f", ATK: {self.atk}, DEF: {self.defense}, Magic ATK: {self.magicattack}, Magic DEF: {self.magicdefense}"
        print(status_line)
        
    def verteidigen(self):
        self.defense += 2
        print(f"{self.name} erhöht seine Verteidigung um 2.")
            
    def mp_reg(self, value):
        self.mp = min(self.max_mp, self.mp + value)
        print(f"{self.name} hat {value} Mana regeneriert.")

class Warrior(Character):
    def __init__(self, name, hp, mp, atk, defense, magicattack=0, magicdefense=0):
        super().__init__(name, hp, mp, atk, defense, magicattack, magicdefense)
        
    def schildblock(self):
        self.defense += 5
        print(f"{self.name} erhöht seine Verteidigung um 5.")

class Mage(Character):
    def __init__(self, name, hp, mp, atk, defense, magicattack, magicdefense=0):
        super().__init__(name, hp, mp, atk, defense, magicattack, magicdefense)