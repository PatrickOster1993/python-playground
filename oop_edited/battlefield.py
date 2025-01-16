import player as player
import enemy as enemy
import utils

if __name__ == "__main__":
    karte = utils.generate_map(5, 5, (1, 1), (4, 4))
    utils.show_map(karte)
    mete = player.Warrior("Mete", hp = 100, atk = 30, mp = 0, defense = 30, magicdefense= 10)
    pascal = player.Mage("Pascal", hp = 80, atk = 10, mp = 100, defense = 20, magicattack = 30, magicdefense = 15)
    goblinmagier = enemy.GoblinMagier("GoblinMagier", hp = 50, atk = 20, mp = 50, defense = 10, magicattack = 20, magicdefense = 10)
    utils.fight(mete, goblinmagier)
