from klasse import Krieger, Heiler, Magier, Schurke, Paladin, Waffe, Gilde, kampf_szenario
import os
import sys
import keyboard
import time

def clear_screen():
    """Löscht die Konsole"""
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_input():
    """Wartet auf Leertaste-Eingabe"""
    print("\nDrücke die LEERTASTE zum Fortfahren...")
    keyboard.wait('space')  # Wartet bis Leertaste gedrückt und losgelassen wird
    clear_screen()
    time.sleep(0.1)  # Kurze Verzögerung um versehentliches Überspringen zu verhindern

# Waffen erstellen
schwert = Waffe("Eisenschwert", schaden=10, haltbarkeit=5)
dolch = Waffe("Vergifteter Dolch", schaden=8, haltbarkeit=3)
zauberstab = Waffe("Kristallstab", schaden=12, haltbarkeit=4)
streitkolben = Waffe("Heiliger Streitkolben", schaden=15, haltbarkeit=6)

# Charaktere erstellen
heroes = [
    Krieger(name="Herbert", lebenspunkte=100, angriffskraft=20, ruestung=10),
    Krieger(name="Maximilian", lebenspunkte=80, angriffskraft=25, ruestung=15),
    Heiler("Merlin", 100, 20, 10, 30),
    Magier("Gandalf", 80, 15, 5, 100),
    Schurke("Aragorn", 90, 22, 8, 30),
    Paladin("Arthur", 120, 30, 20, 50, 10)
]

# Gilde erstellen
gilde = Gilde("Die Beschützer des Lichts")

# Storyline
clear_screen()
print("""
==========================================
           Die Schlacht der Helden
==========================================

In einer fernen Welt bereiten sich die Helden
auf eine epische Schlacht vor...
""")
wait_for_input()

print("Die Helden rüsten sich mit Waffen aus...")
heroes[0].waffe_ausruesten(schwert)  # Herbert bekommt das Schwert
heroes[4].waffe_ausruesten(dolch)    # Aragorn bekommt den Dolch
heroes[3].waffe_ausruesten(zauberstab)  # Gandalf bekommt den Zauberstab
heroes[5].waffe_ausruesten(streitkolben)  # Arthur bekommt den Streitkolben
wait_for_input()

print("Die Helden schließen sich der Gilde an...")
for hero in heroes:
    gilde.hinzufuegen(hero)
wait_for_input()

print("Arthur wird zum Anführer der Gilde ernannt...")
gilde.anfuehrerBestimmen(heroes[5])
wait_for_input()

print("Die Gildenmitglieder:")
gilde.anzeigen()
wait_for_input()

print("Demonstration der Waffenkombination:")
kombinierte_waffe = schwert + dolch
print(f"Kombination aus {schwert.name} und {dolch.name}:")
print(f"Name: {kombinierte_waffe.name}")
print(f"Schaden: {kombinierte_waffe.schaden}")
print(f"Haltbarkeit: {kombinierte_waffe.haltbarkeit}")
wait_for_input()

print("Ein epischer Kampf beginnt!")
print("Aragorn gegen Gandalf...")
wait_for_input()

# Kampfdemonstration mit der kampf_szenario Funktion
kampf_szenario(heroes[4], heroes[3])
wait_for_input()

print("""
==========================================
           Finaler Status der Helden
==========================================
""")
for hero in heroes:
    hero.checkStatus()
    print()

print("""
Die Schlacht ist vorbei...
Die Helden kehren erschöpft nach Hause zurück.
""")
