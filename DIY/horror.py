from buch import Inhaltsverzeichnis

class horror(Inhaltsverzeichnis):
    def __init__(self,ein_Autor , ein_Titel, ein_jahr, ein_neuesBuch):
        super().__init__(ein_Autor,ein_Titel,ein_jahr)
        self.neuesBuch = ein_neuesBuch
        
    def buchHinzufügen1(self):
        print(f"es wurde ein neues buch hinzugefügt{self.neuesBuch}")
        
        
hey2 = horror(
    ein_Autor= "Pizza" ,
    ein_Titel="Pizza sind brötchen" ,
    ein_jahr= "2025" ,
    ein_neuesBuch="Horror"
)


hey2.buchHinzufügen1()
        