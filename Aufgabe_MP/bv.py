# ### **Aufgabe: Bibliotheksverwaltung**

# Du sollst ein kleines Programm zur Verwaltung einer Bibliothek erstellen. Die Bibliothek enthält eine Sammlung von **Büchern**. Es gibt verschiedene Arten von Büchern, z. B. **Sachbücher** und **Romane**. Jedes Buch hat bestimmte Eigenschaften, aber es gibt auch Unterschiede zwischen den Bucharten.

# #### **1. Erstellung einer Basisklasse:**

# #Erstelle eine Basisklasse `Buch`, die die gemeinsamen Attribute und Methoden für alle Bücher enthält.

# #**Gemeinsame Attribute:**
# #- `titel`: Der Titel des Buches.
# #- `autor`: Der Autor des Buches.
# #- `isbn`: Die ISBN des Buches.

# **Gemeinsame Methoden:**
# - `details`: Gibt eine kurze Beschreibung des Buches aus (Titel, Autor, ISBN).

class Buch:
        
    def __init__(self,titel,autor,isbn,description):
        self.titel = titel 
        self.autor = autor 
        self.isbn = isbn
        self.description = description 
        
    def info_Buch(self):
        return f"Titel: {self.titel}, Autor: {self.autor}, Isbn: {self.isbn}, Beschreibung: {self.description}"
    
#Erstellung eines Objektes innerhalb der Klasse    
Buch1 = Buch("Pascal bringt mit klassen bei","Pascal","21-01-2025","Pascal <3")
 
    
# print(Buch1.info_Buch())


# #### **2. Vererbung:**

# Erstelle zwei Unterklassen `Sachbuch` und `Roman`, die von der Klasse `Buch` erben.

# - **Sachbuch**:
#   - Zusätzlich zu den Attributen aus der Basisklasse soll es ein weiteres Attribut `thema` haben, das das Thema des Sachbuches angibt.
#   - Eine Methode `wissenVermitteln`, die in der Konsole ausgibt, zu welchem Thema das Buch Wissen vermittelt (als Satz).
     

class Sachbuch(Buch):
    def __init__(self,titel,autor,isbn,description,thema):###Parameter der Klasse Sachbuch
        super().__init__(titel,autor,isbn,description) ## Parameter der Oberklasse Buch
        self.thema = thema
        
    def wissenVermitteln(self):
        return print(f"Das Aktuelle thema: {self.thema}") #f"Das Aktuelle thema: {self.thema}"
        
thema1= Sachbuch("mete versucht verzweifelt","Mete","21-01-2025","Wird es mete schaffen?","ich denke nicht")

# print(thema1.info_Buch())
# print(thema1.wissenVermitteln())


# - **Roman**:
#   - Zusätzlich zu den Attributen aus der Basisklasse soll es ein weiteres Attribut `genre` haben, das das Genre des Romans angibt (z. B. "Thriller", "Drama", ...).
#   - Auch soll die Klasse eine Property `fsk` beinhalten,  welche sich (abhängig vom jeweiligen Genre auf 0, 6, 12 oder 18 setzt.

class Roman(Buch):
    def __init__(self,titel,autor,isbn,description,genre):###Parameter der Klasse Genre
        super().__init__(titel,autor,isbn,description) ## Parameter der Oberklasse Buch
        self.genre = genre
        
        
    def info_Buch(self):
        return f"{super().info_Buch()},genre: {self.genre},fsk:{self.fsk}"
    
    @property
    def fsk(self):
        fsk_dict = {
            "Horror": 18,
            "Thriller": 16,
            "Kömödie" : 12,
            "Fantasy" : 6,
            "Kinderbuch" :0
        }
        return fsk_dict.get(self.genre,0)
        
genreAusgabe= Roman("mete versucht verzweifelt","Mete","21-01-2025","Wird es mete schaffen?","Horror")

print(genreAusgabe.info_Buch())

    
    
    

