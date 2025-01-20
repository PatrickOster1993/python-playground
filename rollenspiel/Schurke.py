import random
from Charakter import Charakter

class Schurke(Charakter):
    ### Attribute ###
    # Getter und Setter für Attribut Geschicklichkeit
    @property
    def geschicklichkeit(self):
        return self._geschicklichkeit

    @geschicklichkeit.setter
    def geschicklichkeit(self, wert):
        if wert < 0:
            print("Geschicklichkeit kann nicht negativ sein!")
            print("#######################################")
        else:
            self._geschicklichkeit = wert
    ### Konstruktor ###
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung, geschicklichkeit):
        """Initialisiert einen Magier mit den angegebenen Attributen."""
        super().__init__(name, lebenspunkte, angriffskraft, ruestung)
        self.geschicklichkeit = geschicklichkeit

    ### Methoden ###
    def angreifen(self, gegner):
        """Führt einen Angriff auf einen Gegner aus und zieht dessen Lebenspunkte ab."""
        glücksliste = ["magier", "krieger", "priester", "schurke"]
        random.shuffle(glücksliste)

        if glücksliste[0] == "schurke":
            schaden = self.angriffskraft * 2 - gegner.ruestung
        else:
            schaden = self.angriffskraft - gegner.ruestung
        
        if schaden > 0:
            gegner.lebenspunkte -= schaden
            print(f"{self.name} greift {gegner.name} an und fügt {schaden} Schaden zu! {gegner.name} hat noch {gegner.lebenspunkte} Lebenspunkte.")
            print("#########################################################")
        else:
            print(f"{self.name} greift {gegner.name} an, aber der Angriff hat keinen Schaden verursacht!")
            print("###########################################################################")

    def verstecken(self):
        """Erhöht die Geschicklichkeit des Schurken."""
        self.geschicklichkeit += 5
        print(f"{self.name} versteckt sich und erhöht seine Geschicklichkeit auf {self.geschicklichkeit}.")
        print("#####################################################################")

    def verteidigen(self):
        """Erhöht die Rüstung des Magiers."""
        self.ruestung += 5
        print(f"{self.name} verteidigt sich und erhöht seine Rüstung auf {self.ruestung}.")
        print("#####################################################################")

    def heilen(self):
        """Erhöht die Lebenspunkte des Magiers."""
        self.lebenspunkte += 10
        print(f"{self.name} verteidigt sich und erhöht seine Rüstung auf {self.ruestung}.")
        print("#####################################################################")
    
    def checkStatus(self):
        print(f"############## {self.name} ###############")
        print("Lebenspunkte: ", self.lebenspunkte)
        print("Angriffskraft: ", self.angriffskraft)
        print("Rüstung: ", self.ruestung)
        print(f"##########################################")


    


# getter/setter für geschicklichkeit?
# getter/setter in Charakter?
# angreifen/verstecken