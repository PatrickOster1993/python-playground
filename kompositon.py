# Zweck: Komposition von Klassen
class Zimmer:
    def __init__(self, art, flaeche): # Konstuktor
        self.art = art # Attribut von Zimmer
        self.flaeche = flaeche	# Attribut von Zimmer

    # Formatiert den Text zu String Objekt
    def __str__(self):
        return f"Zimmer: {self.art} mit {self.flaeche} m²"	# Methode 

class Haus:
    def __init__(self, adresse): # Konstruktor
        self.zimmer = []  	# Attribut > Liste von Zimmer Objekten erbet von Zimmer Klasse
        self.adresse = adresse	# Attribut von Haus


# Haus bau

if __name__ == "__main__":
    zimmer1 = Zimmer(art="Schlafzimmer", flaeche=20) # Zimmer Objekt
    zimmer2 = Zimmer(art="Küche", flaeche=15) # Zimmer Objekt
    zimmer3 = Zimmer(art="Wohnzimmer", flaeche=30) # Zimmer Objekt

    haus = Haus(adresse="Musterstraße 1") # Haus Objekt
    haus.zimmer.append(zimmer1) # Zimmer Objekt hinzufügen
    haus.zimmer.append(zimmer2) # Zimmer Objekt hinzufügen
    haus.zimmer.append(zimmer3) # Zimmer Objekt hinzufügen

    print(f"Das Haus in der {haus.adresse} hat folgende Zimmer:")
    for zimmer in haus.zimmer:
        print(zimmer) # Ausgabe der Zimmer Objekte


# Kompositon Beispiel
class Auto:
    def __init__(self, motor, reifen):
        self.motor = motor # Attribut > Kompositon Objekt von Motor
        self.reifen = reifen # Attribut > Komposition Objekt von Reifen

class Motor:
    def __init__(self, typ):
        self.typ = typ # Attribut

class Reifen:
    def __init__(self, groesse):
        self.groesse = groesse # Attribut

# Beispiel Objekte
if __name__ == "__main__":
    motor = Motor(typ="V8")
    reifen = Reifen(groesse="22 Zoll")
    auto = Auto(motor=motor, reifen=reifen) # Ergebniss der Komposition = Auto Objekt mit Motor und Reifen

    print(f"Das Auto mit dem Motor: {auto.motor.typ} und den Reifen: {auto.reifen.groesse}")


myAuto = Auto()