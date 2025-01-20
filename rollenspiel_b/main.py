from Magier import Magier
from Schurke import Schurke

def kampf_szenario(charakter_1, charakter_2):
    """Simuliert einen Kampf zwischen zwei Charakteren."""
    while charakter_1.lebenspunkte > 0 and charakter_2.lebenspunkte > 0:
        charakter_1.angreifen(charakter_2)
        if charakter_2.lebenspunkte <= 0:
            print(f"{charakter_2.name} wurde besiegt!")
            break
        charakter_2.angreifen(charakter_1)
        if charakter_1.lebenspunkte <= 0:
            print(f"{charakter_1.name} wurde besiegt!")
            break


sven = Magier("Sven", 100, 20, 10, 100)
maser = Schurke("Maser", 100, 20, 10, 100)

kampf_szenario(sven, maser)
