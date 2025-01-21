# Erstellung einer Basisklasse:
# Erstelle eine Basisklasse Buch, die die gemeinsamen Attribute und Methoden für alle Bücher enthält.

# Gemeinsame Attribute:

# titel: Der Titel des Buches.
# autor: Der Autor des Buches.
# isbn: Die ISBN des Buches.
# Gemeinsame Methoden:

# details: Gibt eine kurze Beschreibung des Buches aus (Titel, Autor, ISBN).

class Buch:
    def __init__(self, titel_ein, autor_ein, isbn_ein): #"_ein" zur Unterscheidung
        self.titel = titel_ein
        self.autor = autor_ein
        self.isbn = isbn_ein
        
    def details(self):
        print(f"Das Buch {self.titel} wurde vom Autor {self.autor} verfasst und ist über die ISBN {self.isbn} verfügbar.")

mein_buch = Buch(
    titel_ein = "Programmieren mit Python",
    autor_ein = "Patrick Oster",
    isbn_ein = "24577989"
    )

mein_buch.details()
  


    