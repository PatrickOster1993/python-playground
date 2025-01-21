from bibliotheksverwaltung_b.Buch import Buch


class Bibliothek:
    ### Konstruktor ###
    def __init__(self):
        self.buecher = []

    ### Methoden ###
    def buch_hinzufuegen(self, buch):
        if isinstance(buch, Buch):
            self.buecher.append(buch)
            print(f"Das Buch '{buch.titel}' wurde hinzugefügt.")
        else:
            print("Nur Objekte der Klasse 'Buch' oder ihrer Unterklassen können hinzugefügt werden.")

    def buch_entfernen(self, isbn):
        for buch in self.buecher:
            if buch.isbn == isbn:
                self.buecher.remove(buch)
                print(f"Das Buch '{buch.titel}' wurde entfernt.")
                return
        print("Kein Buch mit der angegebenen ISBN gefunden.")

    def alle_buecher_anzeigen(self):
        if not self.buecher:
            print("Die Bibliothek enthält keine Bücher.")
        else:
            print("Bücher in der Bibliothek:")
            for buch in self.buecher:
                buch.details()
