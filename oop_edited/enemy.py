from player import Character

class GoblinMagier(Character):
    def __init__(self, name, hp, mp, atk, defense, magicattack, magicdefense):
        super().__init__(name, hp, mp, atk, defense, magicattack, magicdefense)

    
class Zombie(Character):
    def __init__(self, name, hp, mp, atk, defense, magicattack=0, magicdefense=0):
        super().__init__(name, hp, mp, atk, defense, magicattack, magicdefense)
        
