from Buch import Buch
from Kunde import Kunde

class Bibliothek:
    def __init__(self):
        self.__buecher = {}
        self.__kunden = []
    
    def buch_hinzufuegen(self, buch_ein):
        if isinstance(buch_ein, Buch):
            if buch_ein in self.__buecher:
                self.__buecher[buch_ein] += 1
            else:
                self.__buecher[buch_ein] = 1
            print(f"Das Buch mit dem Titel '{buch_ein.titel}' wurde hinzugefügt.")
        else:
            print("Fehler: Es wurde kein Buch hinzugefügt, da es sich nicht um ein Buch handelt.")
    
    def buch_hinzufuegen_objekt(self, buch_klasse, titel_ein, autor_ein, isbn_ein, *args):
        buch = buch_klasse(titel_ein, autor_ein, isbn_ein, *args)
        self.buch_hinzufuegen(buch)
        
    def buch_entfernen(self, buch):
        if buch in self.__buecher:
            if self.__buecher[buch] > 1:
                self.__buecher[buch] -= 1
            else:
                del self.__buecher[buch]
                print(f"{buch.titel} wurde entfernt.")
            print(f"Der Bestand vom Buch mit dem Titel {buch.titel} wurde um ein Exemplar verringert.")
        else:
            print(f"Fehler: Das Buch '{buch.titel}' ist nicht in der Bibliothek.")
    
    def alle_buecher(self):
        if not self.__buecher:
            print("Keine Bücher in der Bibliothek.")
        else:
            for buch, anzahl in self.__buecher.items():
                print(f"{buch.details()} (Anzahl: {anzahl})")
    
    def buch_lesen(self, buch):
        buch.lesen()
    
    def buch_suchen(self, titel):
        for buch in self.__buecher:
            if buch.titel == titel:
                return buch
        print("Buch nicht gefunden.")
        return None
    
    def kunde_hinzufuegen(self, kunde):
        if isinstance(kunde, Kunde):
            self.__kunden.append(kunde)
            print(f"Kunde {kunde.name} wurde hinzugefügt.")
        else:
            print("Fehler: Es wurde kein Kunde hinzugefügt, da es sich nicht um einen Kunden handelt.")
    
    def buch_zuruecknehmen(self, buch, kunde):
        if kunde in self.__kunden:
            self.buch_hinzufuegen(buch)
            print(f"{buch.titel} wurde von {kunde.name} zurückgenommen.")
        else:
            print("Fehler: Kunde nicht gefunden.")
            
    def buch_verleihen(self, buch, kunde):
        if kunde in self.__kunden:
            if buch in self.__buecher:
                kunde.buch_ausleihen(buch)
                self.buch_entfernen(buch)
                print(f"{buch.titel} wurde an {kunde.name} verliehen.")
            else:
                print("Fehler: Buch nicht gefunden.")
        else:
            print("Fehler: Kunde nicht gefunden.")