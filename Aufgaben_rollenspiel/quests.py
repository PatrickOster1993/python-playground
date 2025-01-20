class Quest:
    def __init__(self, name, beschreibung, belohnung):
        self.name = name
        self.beschreibung = beschreibung
        self.belohnung = belohnung
        self.abgeschlossen = False

    def abschließen(self):
        self.abgeschlossen = True
        return self.belohnung
