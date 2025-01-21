# #### **5. Aggregation:**

# Erstelle eine Klasse `Bibliothek`, die mehrere Bücher speichern kann. Die `Bibliothek` enthält eine Liste von `Buch`-Objekten. Sie soll Methoden zum Hinzufügen und Entfernen von Büchern haben.

from Aufgabe_1_Buch import Buch

class Bibliothek:
    
    def __init__(self):
        self.__buecher = []

    def buchHinzufuegen(self, buch_ein):
        if isinstance(buch_ein, Buch):
            self.__buecher.append(buch_ein)
            print("Das Buch wurde erfolhreich zu Bibliothek hinzugefügt")
        else:
            print("Es handelt sich dabei um kein Buch!")

    def buchEntfernen(self, buch_ein):
        if buch_ein in self.__buecher:
            self.__buecher.remove(buch_ein)
            print("Das Buch wurde erfolgreich entfernt!")
        else:
            print(f"Das buch{buch_ein.titel} ist noch nicht im Sortiment der Bibliothek!")

#meine_bib = Bibliothek()
#meine_bib_buecher.append(Buch("", "", ""))