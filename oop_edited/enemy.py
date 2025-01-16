class Character:
    def __init__(self, name, hp, mp, atk, defense, magicattack, magicdefense):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.defense = defense
        self.magicattack = magicattack
        self.magicdefense = magicdefense
        
    def angreifen(self, gegner):
        schaden = max(0, self.atk - gegner.defense)
        gegner.hp -= schaden
        gegner.hp = max(0, gegner.hp - schaden)
        print(f"{self.name} greift {gegner.name} an und fügt {schaden} Schaden zu!")
        if gegner.hp == 0:
            print(f"{gegner.name} wurde besiegt!")
        
    def heilen(self, value):
        self.hp += value
        print(f"{self.name} hat sich um {value} Lebenspunkte geheilt.")

    
    def status(self):
        print(f"Name: {self.name}, HP: {self.hp}, MP: {self.mp}, ATK: {self.atk}, DEF: {self.defense}, Magic ATK: {self.magicattack}, Magic DEF: {self.magicdefense}")
        print(f"#############################################")
        
    def verteidigen(self):
        self.defense += 2
        print(f"{self.name} erhöht seine Verteidigung um 2.")
            
        def mp_reg(self, value):
            self.mp = min(100, self.mp + value)
            print(f"{self.name} hat {value} Mana regeneriert.")
    
    
class Zombie(Character):
    def __init__(self, name, hp, mp, atk, defense, magicattack=0, magicdefense=0):
        super().__init__(name, hp, mp, atk, defense, magicattack, magicdefense)
        

            
class GoblinMagier(Character):
    def __init__(self, name, hp, mp, atk, defense, magicattack, magicdefense):
        super().__init__(name, hp, mp, atk, defense, magicattack, magicdefense)

    def cast(self, gegner):
        schaden = max(0, self.magicattack - gegner.magicdefense)
        gegner.hp -= schaden
        print(f"{self.name} greift {gegner.name} mit Magie an und fügt {schaden} Schaden zu!")
        