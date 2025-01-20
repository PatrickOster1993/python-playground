from stadt import Stadt
from hilfsfunktionen import clear_screen

def main():
    """Hauptprogramm für die Stadt."""
    clear_screen()  # Bildschirm zu Beginn leeren
    stadt = Stadt()

    while True:
        stadt.anzeigen()  # Stadt anzeigen
        print("\nBewege dich zu den verfügbaren Orten:")
        print("Taverne (1), Shop (2), Dungeon (3), Gilde (4), Q = Beenden")
        richtung = input("Wähle einen Ort oder Q zum Beenden: ").lower()

        if richtung == "q":
            print("Du verlässt die Stadt. Bis zum nächsten Mal!")
            break
        elif richtung == "1":
            stadt.bewegen("Taverne")  # Bewege dich zur Taverne
            stadt.interaktion()
        elif richtung == "2":
            stadt.bewegen("Shop")  # Bewege dich zum Shop
            stadt.interaktion()
        elif richtung == "3":
            stadt.bewegen("Dungeon")  # Bewege dich zum Dungeon
            stadt.interaktion()
        elif richtung == "4":
            stadt.bewegen("Gilde")  # Bewege dich zur Gilde
            stadt.interaktion()
        else:
            print("Ungültige Eingabe! Versuche es erneut.")

if __name__ == "__main__":
    main()
