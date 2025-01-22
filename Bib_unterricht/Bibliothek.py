from Buch import Buch

class Bibliothek:
    def __init__(self):
        self.__buecher = []
    
    def buch_hinzufuegen(self, buch_ein):
        if isinstance(buch_ein, Buch):
            self.__buecher.append(buch_ein)
            print(f"Das Buch mit dem Titel {buch_ein.titel} wurde hinzugefügt.")
        else:
            print("Fehler: Es wurde kein Buch hinzugefügt, da es sich nicht um ein Buch handelt.")
    
    def buch_hinzufuegen_objekt(self, buch_klasse, titel_ein, autor_ein, isbn_ein, *args):
        buch = buch_klasse(titel_ein, autor_ein, isbn_ein, *args)
        self.__buecher.append(buch)
        
    def buch_entfernen(self, buch):
        self.__buecher.remove(buch)
    
    def alle_buecher(self):
        for buch in self.__buecher:
            print(buch.details())
    
    def buch_lesen(self, buch):
        buch.lesen()
    
    def buch_suchen(self, titel):
        for buch in self.__buecher:
            if buch.titel == titel:
                return buch
        print("Buch nicht gefunden.")
        return None