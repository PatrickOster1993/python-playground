import os
import time

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def zeichne_hp_herzen(name, lebenspunkte, max_lebenspunkte):
    """Erstellt eine grafische Anzeige für Lebenspunkte."""
    gefüllte_herzen = "❤️" * (lebenspunkte // 10)
    leere_herzen = "♡" * ((max_lebenspunkte - lebenspunkte) // 10)
    return f"{name:10}: {gefüllte_herzen}{leere_herzen} ({lebenspunkte}/{max_lebenspunkte} HP)"

def zeige_status(gruppe, gegner_gruppe):
    """Zeigt den Status der Spielergruppe und Gegnergruppe."""
    print("Spielergruppe:")
    print("=" * 20)
    for char in gruppe:
        print(zeichne_hp_herzen(char.name, char._lebenspunkte, char._max_lebenspunkte))
    print("\nGegnergruppe:")
    print("=" * 20)
    for gegner in gegner_gruppe:
        print(zeichne_hp_herzen(gegner.name, gegner._lebenspunkte, gegner._max_lebenspunkte))
    print()

def kampf_szenario_grafisch(gruppe, gegner_gruppe, gruppen_inventar):
    """Kampfszenario zwischen Spieler- und Gegnergruppe mit grafischer Anzeige."""
    runde = 1
    while True:
        clear_screen()
        print(f"{'=' * 30}\nRunde {runde}\n{'=' * 30}")
        zeige_status(gruppe, gegner_gruppe)

        # Spielergruppe greift an
        for spieler in gruppe:
            if gegner_gruppe and not spieler.ist_besiegt():
                gegner = gegner_gruppe[0]
                print(f"{spieler.name} greift an!")
                schaden = spieler.angreifen(gegner)
                print(f"{gegner.name} verliert {schaden} HP.\n")
                time.sleep(1)
                if gegner.ist_besiegt():
                    print(f"{gegner.name} wurde besiegt!")
                    gegner_gruppe.remove(gegner)
                    if not gegner_gruppe:
                        print("\nSpielergruppe hat gewonnen! 🏆")
                        return

        # Gegnergruppe greift an
        for gegner in gegner_gruppe:
            if gruppe and not gegner.ist_besiegt():
                spieler = gruppe[0]
                print(f"{gegner.name} greift an!")
                schaden = gegner.angreifen(spieler)
                print(f"{spieler.name} verliert {schaden} HP.\n")
                time.sleep(1)
                if spieler.ist_besiegt():
                    print(f"{spieler.name} wurde besiegt!")
                    gruppe.remove(spieler)
                    if not gruppe:
                        print("\nGegnergruppe hat gewonnen! 💀")
                        return

        runde += 1
        time.sleep(2)
