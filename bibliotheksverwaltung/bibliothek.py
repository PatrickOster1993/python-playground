from buch import Buch

# Klasse Bibliothek
class Bibliothek:
    def __init__(self):
        # privates Attribut, da gewollter Zugriff vollumfänglich über Methoden gesteuert!
        self.__buecher = []

    def buchHinzufuegen(self, buch):
        if isinstance(buch, Buch):
            self.__buecher.append(buch)
            print(f"{buch.titel} wurde zur Bibliothek hinzugefügt.")
        else:
            print("Das Objekt ist kein Buch und kann nicht hinzugefügt werden.")

    def buchEntfernen(self, buch):
        if buch in self.__buecher:
            self.__buecher.remove(buch)
            print(f"{buch.titel} wurde aus der Bibliothek entfernt.")
        else:
            print("Das Buch ist nicht in der Bibliothek.")

    def buecherAnzeigen(self):
        if self.__buecher:
            print("Bücher in der Bibliothek:")
            for buch in self.__buecher:
                print(buch.details())
        else:
            print("Die Bibliothek ist leer.")
