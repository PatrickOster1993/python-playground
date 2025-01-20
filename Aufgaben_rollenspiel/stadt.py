from hilfsfunktionen import clear_screen
from taverne import taverne_menu
from shop import shop
from gilde import gilde_menu
from dungeon import dungeon_starten
from gruppen_inventar import GruppenInventar

class Stadt:
    def __init__(self):
        self.spieler_pos = "Mitte der Stadt"
        self.orte = {
            "Taverne": "🍺",
            "Shop": "🛒",
            "Dungeon": "⚔️",
            "Gilde": "🏰"
        }

    def anzeigen(self):
        """Zeigt die Stadt an."""
        clear_screen()  # Bildschirm löschen
        print(f"Du befindest dich an der {self.spieler_pos}.")
        print("\nVerfügbare Orte in der Stadt:")
        for ort, emoji in self.orte.items():
            print(f"{emoji} {ort}")
        
        print("\nLegende:")
        print("🧙‍♂️: Spieler")
        print("🍺: Taverne, 🛒: Shop, ⚔️: Dungeon, 🏰: Gilde")

    def bewegen(self, richtung):
        """Bewegt den Spieler in der Stadt."""
        if richtung in self.orte:
            self.spieler_pos = richtung
            print(f"\nDu gehst zur {self.spieler_pos}.")
        else:
            print("\nUngültige Eingabe!")

    def interaktion(self):
        """Öffnet das Menü, wenn der Spieler auf das entsprechende Feld kommt."""
        if self.spieler_pos == "Taverne":
            taverne_menu()
        elif self.spieler_pos == "Shop":
            shop()
        elif self.spieler_pos == "Dungeon":
            dungeon_starten([], GruppenInventar())
        elif self.spieler_pos == "Gilde":
            gilde_menu()
