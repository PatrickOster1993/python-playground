from random import randint, choice
from hilfsfunktionen import clear_screen
from gruppen_inventar import GruppenInventar

class Gegner:
    def __init__(self, name, lebenspunkte, schaden):
        self.name = name
        self.lebenspunkte = lebenspunkte
        self.schaden = schaden

    def angreifen(self):
        """Der Gegner greift den Spieler an und verursacht Schaden."""
        return randint(1, self.schaden)  # Zufälliger Schaden des Gegners

    def erleide_schaden(self, schaden):
        """Der Gegner erleidet Schaden und verliert Lebenspunkte."""
        self.lebenspunkte -= schaden
        if self.lebenspunkte <= 0:
            return True  # Gegner besiegt
        return False

class Truhe:
    def __init__(self):
        """Die Truhe kann zufällige Belohnungen enthalten."""
        self.loot = self.loot_erzeugen()

    def loot_erzeugen(self):
        """Erzeugt zufällige Loot-Belohnungen."""
        loot_arten = [
            {"name": "Gold", "betrag": randint(20, 100)}, 
            {"name": "Heiltrank", "heilung": randint(25, 50)},
            {"name": "Mana-Trank", "mana": randint(25, 50)}
        ]
        return choice(loot_arten)  # Zufälliges Item auswählen

class BossGegner(Gegner):
    def __init__(self, name, lebenspunkte, schaden):
        super().__init__(name, lebenspunkte, schaden)
        self.name = name
        self.lebenspunkte = lebenspunkte * 2  # Boss hat mehr Lebenspunkte
        self.schaden = schaden * 2  # Boss verursacht mehr Schaden

class Dungeon:
    def __init__(self):
        # Die Karte des Dungeons (Text-Layout mit Zahlen zur Darstellung)
        self.karte = [
            ["⬛", "⬛", "⬛", "⬛", "⬛"],
            ["⬛", "🧙‍♂️", "🧛", "⬛", "⬛"],  # 🧙‍♂️ = Spieler, 🧛 = Gegner
            ["⬛", "⬛", "⬛", "💰", "⬛"],  # 💰 = Truhe
        ]
        self.spieler_pos = (1, 1)  # Startposition des Spielers
        self.gegner = Gegner("Troll", 20, 5)  # Gegner im Dungeon
        self.boss = BossGegner("Drachenlord", 100, 15)  # Boss-Gegner am Ende des Dungeons
        self.truhe = Truhe()  # Truhe im Dungeon

    def anzeigen(self):
        """Zeigt das Dungeon an."""
        clear_screen()  # Bildschirm löschen
        print("Dungeon:")
        for y, zeile in enumerate(self.karte):
            for x, feld in enumerate(zeile):
                # Zeigt die Position mit Zahlen an, um besser zu verstehen, wo der Spieler ist
                if (x, y) == self.spieler_pos:
                    print("🧙‍♂️", end=" ")  # Spieler
                else:
                    print(f"{feld} ", end="")  # Sonst das Icon aus der Karte
            print()  # Neue Zeile für die nächste Karte
        print("\nLegende:")
        print("🧙‍♂️: Spieler")
        print("🧛: Gegner")
        print("💰: Truhe")
        print("⬛: Wand")

    def bewegen(self, richtung):
        """Bewegt den Spieler im Dungeon basierend auf der Eingabe."""
        x, y = self.spieler_pos
        if richtung == "w" and x > 0:
            x -= 1  # Bewege nach oben
        elif richtung == "s" and x < len(self.karte) - 1:
            x += 1  # Bewege nach unten
        elif richtung == "a" and y > 0:
            y -= 1  # Bewege nach links
        elif richtung == "d" and y < len(self.karte[0]) - 1:
            y += 1  # Bewege nach rechts

        # Wenn der Spieler auf einen Gegner trifft, kommt es zum Kampf
        if self.karte[x][y] == "🧛":
            self.kampf()
        elif self.karte[x][y] == "💰":
            self.truhe_oeffnen()

        self.spieler_pos = (x, y)

    def kampf(self):
        """Simuliert den Kampf zwischen dem Spieler und dem Gegner."""
        print(f"Du kämpfst gegen {self.gegner.name}!")
        while self.gegner.lebenspunkte > 0:
            spieler_schaden = randint(5, 10)
            gegner_besiegt = self.gegner.erleide_schaden(spieler_schaden)
            print(f"Du verursachst {spieler_schaden} Schaden!")

            if gegner_besiegt:
                print(f"{self.gegner.name} wurde besiegt!")
                break

            gegner_schaden = self.gegner.angreifen()
            print(f"{self.gegner.name} greift an und verursacht {gegner_schaden} Schaden!")
            break

        print("Kampf beendet!")

    def truhe_oeffnen(self):
        """Öffnet die Truhe und gibt den Loot aus."""
        print("Du öffnest die Truhe!")
        loot = self.truhe.loot
        print(f"Du hast {loot['name']} gefunden: {loot}")

    def boss_kampf(self):
        """Kampf gegen den Boss-Gegner."""
        print(f"Du kämpfst gegen den Boss {self.boss.name}!")
        while self.boss.lebenspunkte > 0:
            spieler_schaden = randint(10, 20)
            boss_besiegt = self.boss.erleide_schaden(spieler_schaden)
            print(f"Du verursachst {spieler_schaden} Schaden!")

            if boss_besiegt:
                print(f"{self.boss.name} wurde besiegt!")
                print("Du hast das Dungeon abgeschlossen und gewinnst großartige Belohnungen!")
                break

            boss_schaden = self.boss.angreifen()
            print(f"{self.boss.name} greift an und verursacht {boss_schaden} Schaden!")
            break

        print("Kampf gegen den Boss beendet!")

def dungeon_starten(gruppe, gruppen_inventar):
    """Dungeon starten und logik für das Dungeon."""
    dungeon = Dungeon()
    while True:
        dungeon.anzeigen()
        richtung = input("Wähle: w (Hoch), s (Runter), a (Links), d (Rechts), q (Verlassen): ").lower()
        if richtung == "q":
            print("Du verlässt das Dungeon.")
            break
        elif richtung in ["w", "a", "s", "d"]:
            dungeon.bewegen(richtung)
        else:
            print("Ungültige Eingabe!")
