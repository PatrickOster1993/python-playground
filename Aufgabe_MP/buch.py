# #### **1. Erstellung einer Basisklasse:**

# Erstelle eine Basisklasse `Buch`, die die gemeinsamen Attribute und Methoden für alle Bücher enthält.

# **Gemeinsame Attribute:**
# - `titel`: Der Titel des Buches.
# - `autor`: Der Autor des Buches.
# - `isbn`: Die ISBN des Buches.

# **Gemeinsame Methoden:**
# - `details`: Gibt eine kurze Beschreibung des Buches aus (Titel, Autor, ISBN).

from abc import ABC, abstractmethod
class Buch:
    ##__init__ Konstruktor
    def __init__(self, titel_ein, autor_ein, isbn_ein):#Attribute im Parameter
        self.titel = titel_ein
        #attribut    #argument
        self.autor = autor_ein
        self.isbn = isbn_ein
    def details(self):
        #return f"Titel:{self.titel},Autor:{self.autor},isbn:{self.isbn}"
        print(f"Das buch {self.titel}, ist vom Autor{self.autor} verfasst und hat die isbn: {self.isbn}   ")
    
    @abstractmethod
    def lesen(self):
        pass
    
# mein_buch = Buch(
#     titel_ein="Prommieren mit python",
#     autor_ein="Patrick oster",
#     isbn_ein="123456789"
#     )

# mein_buch = Buch(
#     "Prommieren mit python",
#     "Patrick oster",    #soo besser
#     "123456789"
#     )
       
# mein_buch.details() 


