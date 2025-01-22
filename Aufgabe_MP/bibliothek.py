from buch import Buch

class Bibliothek:
    def __init__(self):
        self.buecher = []
    
    def buchHinzufuegen(self,buch_ein):
        if isinstance(buch_ein,Buch):
            self.buecher.append(buch_ein)
            print("Das buch {buch_ein.titel} wurde erfolgreich zur Bibliothek hinzugefügt!")
        else:
            print("Es handelt sich dabei um kein Buch")
            
    def buchEntfernen(self,buch_ein):
        if buch_ein in self.buecher:
            self.buecher.remove()
            print(f"Das Buch {buch_ein.titel} wurde erfolgreich entfernt!")
        else:
            print(f"Das buch {buch_ein.titel} ist noch nicht in der bibliothek")
    
meine_bib = Bibliothek()
meine_bib.buecher.append(Buch)


    