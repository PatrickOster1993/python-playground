from buch import Buch

# Unterklasse Sachbuch
class Sachbuch(Buch):
    def __init__(self, titel, autor, isbn, thema):
        super().__init__(titel, autor, isbn)
        # privates Attribut, da Zugriff nach Außen nicht notwendig ...
        # Datenkapselung: wir verhindern somit, dass Attribut überschrieben wird ...
        # Zugriff nach Außen hin über wissenVermitteln() --> nur das möchte Nutzer wissen:)
        self.__thema = thema

    def lesen(self):
        return "Ich lese, um zu lernen!"

    def wissenVermitteln(self):
        return f"Dieses Buch vermittelt Wissen zum Thema: {self.__thema}"