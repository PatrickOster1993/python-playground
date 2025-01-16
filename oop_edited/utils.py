import player as player
import random as rnd

def fight(self, gegner):
    while gegner.hp > 0 and self.hp > 0:
        print(f"\n Was möchtest du tun?")
        print("1. Status")
        print("2. Angreifen")
        if isinstance(self, player.Mage):
            print("3. Zaubern")
        print("4. Verteidigen")
        if isinstance(self, player.Warrior):
            print("5. Schildblock")

        choose = input("Wählen Sie eine Option: ")
        
        if choose == "1":
            self.status()
        elif choose == "2":
            self.angreifen(gegner)
        elif choose == "3" and isinstance(self, player.Mage):
            self.cast(gegner)
        elif choose == "4":
            self.verteidigen()
        elif choose == "5" and isinstance(self, player.Warrior):
            self.schildblock()
        else:
            print("Ungültige Eingabe! Bitte wählen Sie eine der Optionen aus.")
            

        if gegner.hp == 0:
            print(f"{gegner.name} wurde besiegt!")
        elif self.hp == 0:
            print(f"{self.name} wurde besiegt!")
            
            
        if choose != "1":  # Gegnerzug nur ausführen, wenn nicht "Status" gewählt wurde
            rndgegner = rnd.randint(1, 3)
            if rndgegner == 1:
                gegner.angreifen(self)
            elif rndgegner == 2:
                gegner.cast(self)
            elif rndgegner == 3:
                gegner.verteidigen()
                
def generate_map(length, width, start, end):
    # Erstelle eine Karte mit Hindernissen (#)
    karte = [["#" for _ in range(width)] for _ in range(length)]
    
    # Setze Start- und Endpunkte
    karte[start[1]][start[0]] = "S"
    karte[end[1]][end[0]] = "E"
    
    # Füge zufällige Fallen (leere Felder) hinzu
    for _ in range(rnd.randint(1, length * width // 4)):
        x = rnd.randint(0, width - 1)
        y = rnd.randint(0, length - 1)
        if karte[y][x] == "#":
            karte[y][x] = " "
    
    return karte

def show_map(karte):
    for row in karte:
        print("".join(row))