from hilfsfunktionen import clear_screen

def shop():
    """Grafische Darstellung des Shops."""
    clear_screen()  # Bildschirm nur einmal zu Beginn leeren
    print("""
🛒 Willkommen im Shop 🛒

1. Tränke kaufen
2. Shop verlassen
""")
    aktion = input("Wähle eine Aktion: ")
    if aktion == "1":
        print("Du kaufst einen Heiltrank.")
    elif aktion == "2":
        print("Du verlässt den Shop.")
