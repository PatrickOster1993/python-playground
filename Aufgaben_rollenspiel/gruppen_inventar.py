class GruppenInventar:
    def __init__(self):
        self.gold = 0  # Gesamtgold der Gruppe
        self.tränke = []  # Liste für Tränke oder andere Gegenstände

    def hinzufuegen(self, item):
        """Fügt einen Trank oder Gegenstand dem Inventar hinzu."""
        if "heilung" in item or "mana" in item:
            self.tränke.append(item)
            print(f"{item['name']} wurde zum Gruppeninventar hinzugefügt.")
        else:
            print("Unbekannter Gegenstand.")

    def anzeigen(self):
        """Zeigt den Inhalt des Gruppeninventars."""
        print(f"\nGold: {self.gold}")
        print("Tränke und Gegenstände:")
        for trank in self.tränke:
            print(f"- {trank['name']} ({trank.get('heilung', 0)} Heilung, {trank.get('mana', 0)} Mana)")
