import player as player
import enemy as enemy
import utils

# Hauptprogramm
if __name__ == "__main__":
    # Generiere eine Karte mit den angegebenen Dimensionen und Start-/Endpunkten
    map = utils.generate_map(10, 10, (1, 1), (4, 4))
    
    # Zeige die generierte Karte an
    utils.show_map(map)
    
    # Erstelle Instanzen der Spielercharaktere
    mete = player.Warrior("Mete", hp=100, atk=30, mp=0, defense=0, magicdefense=10)
    pascal = player.Mage("Pascal", hp=80, atk=10, mp=100, defense=20, magicattack=30, magicdefense=15)
    
    # Erstelle eine Instanz des Gegners
    goblinmagier = enemy.GoblinMagier("GoblinMagier", hp=50, atk=20, mp=50, defense=10, magicattack=20, magicdefense=10)
    
    # Starte den Kampf zwischen dem Spielercharakter und dem Gegner
    utils.fight(mete, goblinmagier)