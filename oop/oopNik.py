class Auto:

    def __init__(self, in_ps): #Constructor
        # in das self Objekt bauen wir eine Instanzvariable "ps" ein
        self.ps = in_ps # Instanzvariable
        self.farbe = "leer"
        self.tueren = 0
        self.km = 0
        self.besitzer = "leer"
        self.marke = "leer"

    def werBistDu( auto_obj):
        print("Ich bin ein Auto der Marke ", auto_obj.marke, " und gehöre ", auto_obj.besitzer, "mit ", str(auto_obj.ps, " PS")
# neues Auto erzeugen
a1 = Auto( 200 ); # Instanz von Auto
a1.marke = "Opel"
a1.farbe = "rot"
a1.tueren = 4
a1.km = 10000
a1.besitzer = "Hans"
a1.werBistDu()

# neues Auto erzeugen
a2 = Auto(); # Instanz von Auto
a2.ps = 100
a2.marke = "BMW"
a2.farbe = "blau"
a2.tueren = 2
a2.km = 5000
a2.besitzer = "Peter"
a2.werBistDu()

