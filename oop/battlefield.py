from klasse import Krieger, Heiler, Magier, Paladin
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

# Charaktere erstellen
heroes = [
    Krieger(name="Herbert", lebenspunkte=100, angriffskraft=20, ruestung=10),
    Krieger(name="Maximilian", lebenspunkte=80, angriffskraft=25, ruestung=15),
    Heiler("Merlin", 100, 20, 10, 30),
    Magier("Gandalf", 80, 15, 5, 25),
    Paladin("Arthur", 120, 30, 20, 15, 10)
]

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

print("""
Unsere Helden:

1. Herbert - Der tapfere Krieger
2. Maximilian - Der starke Krieger  
3. Merlin - Der weise Heiler
4. Gandalf - Der mächtige Magier
5. Arthur - Der edle Paladin
""")
wait_for_input()

print("""
Die Schlacht beginnt!

Herbert greift Maximilian an!
""")
wait_for_input()

# Kampfsequenz 1
heroes[0].angreifen(heroes[1])
wait_for_input()

print("""
Maximilian verteidigt sich!
""")
wait_for_input()

heroes[1].verteidigen()
wait_for_input()

print("""
Merlin eilt zur Hilfe und heilt Maximilian!
""")
wait_for_input()

heroes[2].heilen(heroes[1])
wait_for_input()

print("""
Gandalf betritt das Schlachtfeld und wirft
einen mächtigen Feuerball!
""")
wait_for_input()

heroes[3].feuerball(heroes[0])
wait_for_input()

print("""
Arthur reitet in die Schlacht und zeigt seine
Kraft als Paladin!
""")
wait_for_input()

heroes[4].reiten()
heroes[4].feuerball(heroes[1])
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
