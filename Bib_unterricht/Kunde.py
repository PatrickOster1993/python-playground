from Roman import Roman

class Kunde:
    def __init__(self, name_ein, kundennummer_ein):
        self.name = name_ein
        self.kundennummer = kundennummer_ein
        self.ausgeliehene_buecher = []
    
    def buch_ausleihen(self, buch):
        self.ausgeliehene_buecher.append(buch)
        print(f"{self.name} hat das Buch '{buch.titel}' ausgeliehen.")
    
    def buch_zurueckgeben(self, buch):
        if buch in self.ausgeliehene_buecher:
            self.ausgeliehene_buecher.remove(buch)
            print(f"{self.name} hat das Buch '{buch.titel}' zurückgegeben.")
        else:
            print(f"{self.name} hat das Buch '{buch.titel}' nicht ausgeliehen.")
    
    def geliehende_buecher_anzeigen(self):
        if not self.ausgeliehene_buecher:
            print(f"{self.name} hat keine Bücher ausgeliehen.")
        else:
            print(f"{self.name} hat folgende Bücher ausgeliehen:")
            for buch in self.ausgeliehene_buecher:
                print(buch.details())

