from buch import Buch

class Sachbuch(Buch): #Vererbung
    def __init__(self,titel_ein, autor_ein, isbn_ein, thema_ein): #<-- bezieht sich auf sachbuch
        
        super().__init__(titel_ein, autor_ein, isbn_ein) #<- bezieht sich auf klasse Buch Elternklasse
       #hinzufügen von neuer Attribute für Buch  
        self.thema = thema_ein


    def wissenVermitteln(self):
        print(f"Das Buch {self.titel} vermittelt wissen zum thema {self.thema}")
    
    def lesen(self):
        print("ich lese,um zu lernen!")
        
    
mein_sachbuch = Sachbuch(
    titel_ein="Döner ist Toll",
    autor_ein="Mehmet Dönermann",
    isbn_ein="0505052152",
    thema_ein="Physik",
)

mein_sachbuch.wissenVermitteln()

mein_sachbuch.lesen()