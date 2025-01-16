class Magier:
    # Getter und Setter für das Attribut 'name'
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, text):
        self._name = text

    # Getter und Setter für das Attribut 'lebenspunkte'
    @property
    def lebenspunkte(self):
        return self._lebenspunkte

    @lebenspunkte.setter
    def lebenspunkte(self, wert):
        if wert < 0:
            print("Lebenspunkte können nicht negativ sein!")
        else:
            self._lebenspunkte = wert

    # Getter und Setter für das Attribut 'angriffskraft'
    @property
    def angriffskraft(self):
        return self._angriffskraft

    @angriffskraft.setter
    def angriffskraft(self, wert):
        if wert < 0:
            print("Angriffskraft kann nicht negativ sein!")
        else:
            self._angriffskraft = wert

    # Getter und Setter für das Attribut 'ruestung'
    @property
    def ruestung(self):
        return self._ruestung

    @ruestung.setter
    def ruestung(self, wert):
        if wert < 0:
            print("Rüstung kann nicht negativ sein!")
        else:
            self._ruestung = wert

    # Konstruktor zum Initialisieren der Magier-Instanz
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung):
        """Initialisiert einen Magier mit den angegebenen Attributen."""
        self.name = name
        self.lebenspunkte = lebenspunkte
        self.angriffskraft = angriffskraft
        self.ruestung = ruestung

    # Methode für den Angriff auf einen Gegner
    def angreifen(self, gegner):
        """Führt einen Angriff auf einen anderen Gegner aus und zieht dessen Lebenspunkte ab."""
        schaden = self.angriffskraft - gegner.ruestung  # Schaden berechnen
        if schaden > 0:
            gegner.lebenspunkte -= schaden  # Lebenspunkte des Gegners verringern
            print(f"{self.name} greift {gegner.name} an und fügt {schaden} Schaden zu!")
            print("#########################################################")
        else:
            print(f"{self.name} greift {gegner.name} an, aber der Angriff hat keinen Schaden verursacht!")
            print("###########################################################################")

    # Methode für die Verteidigung des Magiers (erhöht Rüstung)
    def verteidigen(self):
        """Erhöht die Rüstung des Magiers."""
        self.ruestung += 5
        print(f"{self.name} verteidigt sich und erhöht seine Rüstung auf {self.ruestung}.")
        print("#####################################################################")
    
    # Methode zur Anzeige des aktuellen Status des Magiers
    def checkStatus(self):
        print(f"############## {self.name} ###############")
        print("Lebenspunkte: ", self.lebenspunkte)
        print("Angriffskraft: ", self.angriffskraft)
        print("Rüstung: ", self.ruestung)
        print(f"##########################################")
