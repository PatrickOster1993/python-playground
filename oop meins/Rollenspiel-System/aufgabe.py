class Archer: ## Klasse Variable
    
    def __init__(self,name,hp,mana,arrows,angriff):
        self.name = name
        self.hp =hp
        self.mana =mana
        self.arrows = arrows
        self.angriff = angriff
    def walk(self):
        print(f"ich bin {self}und laufe")
    
    def status(self):
        print(f"Das leben von {self.name} beträgt: {self.hp} das mana beträgt : {self.mana}")    
    
    def attack(self,gegner) :
        gegner.hp -= self.angriff
        
        
        print(f"{self.name} greift mit {self.angriff} schaden  {gegner.name} an")   
    
archer1 = Archer("mete",100,0,3,50) # instanz
archer2 = Archer("pascal",50,0,3,50) # instanz

# print(archer1.hp)

# archer1.walk()
# archer1.status()
# archer2.shoot()
#
archer1.status()
archer2.status()
##########
archer2.attack(archer1)

archer1.status()
archer2.status()
##