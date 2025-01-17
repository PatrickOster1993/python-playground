import player as player
import random as rnd

def fight(self, gegner):
    """
    Führt einen Kampf zwischen dem Spielercharakter und dem Gegner durch.
    
    Args:
        self (Character): Der Spielercharakter.
        gegner (Character): Der Gegner.
    """
    while gegner.hp > 0 and self.hp > 0:
        # Zeige die Aktionsmöglichkeiten an
        print(f"\nWas möchtest du tun?")
        print("1. Status")
        print("2. Angreifen")
        if isinstance(self, player.Mage):
            print("3. Zaubern")
        print("4. Verteidigen")
        if isinstance(self, player.Warrior):
            print("5. Schildblock")

        # Eingabe des Spielers
        choose = input("Wählen Sie eine Option: ")
        
        # Verarbeite die Eingabe des Spielers
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
        
        # Überprüfe, ob der Gegner oder der Spieler besiegt wurde
        if gegner.hp == 0:
            print(f"{gegner.name} wurde besiegt!")
        elif self.hp == 0:
            print(f"{self.name} wurde besiegt!")
        
        # Gegnerzug nur ausführen, wenn nicht "Status" gewählt wurde
        if choose != "1":
            rndgegner = rnd.randint(1, 3)
            if rndgegner == 1:
                gegner.angreifen(self)
            elif rndgegner == 2:
                gegner.cast(self)
            elif rndgegner == 3:
                gegner.verteidigen()

def generate_map(length, width, start, end):
    """
    Generiere eine Karte mit Hindernissen (#) und Fallen ( ).
    
    Args:
        length (int): Die Länge der Karte.
        width (int): Die Breite der Karte.
        start (tuple): Die Startposition als (x, y).
        end (tuple): Die Endposition als (x, y).
    
    Returns:
        list: Die generierte Karte als 2D-Liste.
    """
    # Erstelle eine Karte mit Hindernissen (#)
    map = [["#" for _ in range(width)] for _ in range(length)]
    
    # Setze Start- und Endpunkte
    map[start[1]][start[0]] = "S"
    map[end[1]][end[0]] = "E"
    
    # Füge zufällige Fallen (leere Felder) hinzu
    for _ in range(rnd.randint(1, length * width // 4)):
        x = rnd.randint(0, width - 1)
        y = rnd.randint(0, length - 1)
        if map[y][x] == "#":
            map[y][x] = " "
    
    return map

def show_map(map):
    """
    Zeige die Karte in der Konsole an.
    
    Args:
        karte (list): Die Karte als 2D-Liste.
    """
    for row in map:
        print("".join(row))