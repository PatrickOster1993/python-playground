import Charakter 


p1= Charakter.Person("Pascal", 100,25)
p2= Charakter.Person("Mete",100,25)

print(p1.hp,p1.name)
print(p2.hp,p2.name)
print(p1.angriff(p2))
print(p2.angriff(p1))
print(p1.hp,p1.name)
print(p2.hp,p2.name)

