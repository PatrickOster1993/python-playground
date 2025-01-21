# ### **Aufgabe: Bibliotheksverwaltung**

# Du sollst ein kleines Programm zur Verwaltung einer Bibliothek erstellen. Die Bibliothek enthält eine Sammlung von **Büchern**. Es gibt verschiedene Arten von Büchern, z. B. **Sachbücher** und **Romane**. Jedes Buch hat bestimmte Eigenschaften, aber es gibt auch Unterschiede zwischen den Bucharten.

# #### **1. Erstellung einer Basisklasse:**

# Erstelle eine Basisklasse `Buch`, die die gemeinsamen Attribute und Methoden für alle Bücher enthält.

# **Gemeinsame Attribute:**
# - `titel`: Der Titel des Buches.
# - `autor`: Der Autor des Buches.
# - `isbn`: Die ISBN des Buches.

# **Gemeinsame Methoden:**
# - `details`: Gibt eine kurze Beschreibung des Buches aus (Titel, Autor, ISBN).

# #### **3. Abstraktion:**

# Erstelle eine abstrakte Methode in der Klasse `Buch`, die in den Unterklassen implementiert werden muss. Die Methode `lesen()` soll in jeder Unterklasse unterschiedlich implementiert werden:
# - **Sachbuch**: Gibt "Ich lese, um zu lernen!" aus.
# - **Roman**: Gibt "Ich lese, um in eine fesselnde Welt einzutauchen." aus.


# #### **4. Kapselung:**

# Entscheiden Sie selbst, welche Attribute, Properties und Methoden für Sie als `privat (__)`, `protected (_)` oder `public` gelten. 



from abc import ABC, abstractmethod

class Buch(ABC): # Definition der Klasse Buch
    def __init__(self, titel_ein, autor_ein, isbn_ein):  # Konstruktor der Klasse
        self.titel = titel_ein  # Initialisiert das Attribut 'titel' mit dem übergebenen Wert
        self.autor = autor_ein  # Initialisiert das Attribut 'autor' mit dem übergebenen Wert
        self.isbn = isbn_ein    # Initialisiert das Attribut 'isbn' mit dem übergebenen Wert

    def details(self):  # Methode, um die Buchdetails auszugeben
        print(f"hard gecodeter string")  # Gibt einen festen, vordefinierten Text aus
        print(f"string mit einer Zahl {self.titel} ... denn dahinter kann ja auch noch was stehen")  # Gibt einen Text aus, der den Titel des Buches enthält
        print("Das Buch " + self.titel + " wurde vom Autor " + self.autor + " verfasst und ist über die ISBN " + self.isbn + " verfügbar!")  # Gibt eine formattierte Beschreibung des Buches aus

        #Aufgabe 3
        @abstractmethod
        def lesen(self):
            pass  

# # Erstellen eines Buchobjekts mit Titel, Autor und ISBN
# mein_buch = Buch(
#     titel_ein="Programmieren mit Python",  # Übergabe des Titels an den Konstruktor
#     autor_ein="Patrick Oster",             # Übergabe des Autors an den Konstruktor
#     isbn_ein="123456789",                  # Übergabe der ISBN an den Konstruktor
# )

# # Aufruf der Methode 'details', um die Buchdetails anzuzeigen
# mein_buch.details()


