from hilfsfunktionen import clear_screen
from quests import Quest

boss_quest = Quest(
    "Besiege den Boss",
    "Gehe in den Dungeon und besiege den Boss, um die Stadt zu retten.",
    {"gold": 100}
)

def gilde_menu():
    clear_screen()  # Bildschirm nur einmal zu Beginn leeren
    while True:
        print("""
🏰 Willkommen in der Gilde 🏰

📜 [Quests]    🏆 [Erfolge]

1. Quest ansehen
2. Gilde verlassen
""")
        aktion = input("Wähle eine Aktion: ")
        if aktion == "1":
            print(f"Quest: {boss_quest.name}")
            print(f"Beschreibung: {boss_quest.beschreibung}")
            print(f"Status: {'Abgeschlossen ✅' if boss_quest.abgeschlossen else 'Noch offen ❌'}")
        elif aktion == "2":
            print("Du verlässt die Gilde.")
            break
