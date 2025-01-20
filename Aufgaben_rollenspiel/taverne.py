from hilfsfunktionen import clear_screen

def taverne_menu():
    """Grafische Darstellung der Taverne."""
    clear_screen()  # Bildschirm nur einmal zu Beginn leeren
    print("""
🍺 Willkommen in der Taverne 🍺

1. Neue Helden rekrutieren
2. Taverne verlassen
""")
    aktion = input("Wähle eine Aktion: ")
    if aktion == "1":
        print("Du hast einen neuen Helden rekrutiert!")
    elif aktion == "2":
        print("Du verlässt die Taverne.")