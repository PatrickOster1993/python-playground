from klasse import Krieger
from klasse import Magier
# Beispiel: Erstellen von zwei Kriegern und ein Kampf
krieger1 = Krieger(name="Herbert", lebenspunkte=100, angriffskraft=20, ruestung=10)
magier = Magier(name="Gandalf", lebenspunkte=50, angriffskraft=100, ruestung=1)

# Krieger 1 greift Krieger 2 an
krieger1.angreifen(gegner=krieger2)

# Krieger 2 verteidigt sich
magier.verteidigen()

# Status von Krieger 2 checken
krieger2.checkStatus()
magier.checkStatus()
# Beispiel für Setter-Methoden
krieger2.lebenspunkte = 90  # Lebenspunkte ändern
krieger2.angriffskraft = 30  # Angriffskraft ändern
krieger2.ruestung = 20      # Rüstung ändern