class Person:
    def __init__(self, name, hp, ang):				
        self.name = name
        self.hp = hp
        self.ang = ang
        
    def angriff(self,gegner):
        gegner.hp = gegner.hp - self.ang
        







