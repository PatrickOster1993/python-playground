
# Erstelle eine Klasse Bibliothek, die mehrere Bücher speichern kann. Die Bibliothek enthält eine Liste von Buch-Objekten. 
# Sie soll Methoden zum Hinzufügen und Entfernen von Büchern haben.
# Aggregation bedeutet buch kann unabhängig von bib existieren
# Attribute:
# - List [Buch]

# Methoden:
# - Bücher hinzufügen
# - Bücher entfernen

from buch import Buch

class Bibliothek:
    def __init__(self):
        self.__buecher = []
    
    def buchHinzufuegen(self, buch_ein):
        if isinstance(buch_ein, Buch):
            self.__buecher.append(buch_ein)
            print(f"Das Buch mit dem Titel {buch_ein.titel} wurde erfolgreich zur Bib. hinzugefuegt!")
        else:
            print("Kein Buch!")

    def buchEntfernen(Self, buch_ein):
        if buch_ein in self.__buecher:
            self.__buecher.remove()
            print(f"Das Buch {buch_ein.titel} wurde entfernt.")
        else:
            print(f"Das Buch {buch_ein.titel} ist noch nicht im Sortiment der Bib.")
        
# meine_bib = Bibliothek()
# meine_bib.__buecher.append()