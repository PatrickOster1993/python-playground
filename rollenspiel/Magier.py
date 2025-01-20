from Charakter import Charakter

class Magier(Charakter):
    ### Attribute ###
    # Getter und Setter für Attribut Mana
    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, wert):
        if wert < 0:
            print("Mana kann nicht negativ sein!")
            print("################################")
        else:
            self._mana = wert

    ### Konstruktor ###
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung, mana):
        """Initialisiert einen Magier mit den angegebenen Attributen."""
        super().__init__(name, lebenspunkte, angriffskraft, ruestung)
        self.mana = mana

    ### Methoden ###
    def angreifen(self, gegner, mana_kosten=5, schadensfaktor=1):
        """Führt einen Angriff auf einen Gegner aus und zieht dessen Lebenspunkte ab."""
        schaden = (self.angriffskraft * schadensfaktor) - gegner.ruestung
        if schaden > 0:
            gegner.lebenspunkte -= schaden
            self.mana -= mana_kosten
            print(f"{self.name} greift {gegner.name} an und fügt {schaden} Schaden zu! {gegner.name} hat noch {gegner.lebenspunkte} Lebenspunkte. {self.name} hat noch {self.mana} Mana.")
            print("#########################################################")
        else:
            print(f"{self.name} greift {gegner.name} an, aber der Angriff hat keinen Schaden verursacht!")
            print("###########################################################################")

    def zaubern(self, gegner):
        """Verursacht mehr Schaden als "angreifen", kostet aber mehr Mana."""
        self.angreifen(gegner, mana_kosten=10, schadensfaktor=2)

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


    


