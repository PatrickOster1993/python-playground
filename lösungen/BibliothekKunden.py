
class Kunde:



    def __init__(self, vorname, nachname, alter, bankkontonr):
        self.vorname = vorname
        self.nachname = nachname
        self._alter = alter
        self.__bankkontonr = bankkontonr
        self.buecher = []


    def buchAusleihen(self, Buch):
        self.buecher.append(Buch.titel)