class Krieger:
    ### Attribute ###
    # Getter und Setter für Attribut Name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, text):
        self._name = text

    # Getter und Setter für Attribut Lebenspunkte
    @property
    def lebenspunkte(self):
        return self._lebenspunkte

    @lebenspunkte.setter
    def lebenspunkte(self, wert):
        if wert < 0:
            print("Lebenspunkte können nicht negativ sein!")
            print("#######################################")
        else:
            self._lebenspunkte = wert

    # Getter und Setter für Attribut Angriffskraft
    @property
    def angriffskraft(self):
        return self._angriffskraft

    @angriffskraft.setter
    def angriffskraft(self, wert):
        if wert < 0:
            print("Angriffskraft kann nicht negativ sein!")
            print("######################################")
        else:
            self._angriffskraft = wert

    # Getter und Setter für Attribut Rüstung
    @property
    def ruestung(self):
        return self._ruestung
    
    @ruestung.setter
    def ruestung(self, wert):
        if wert < 0:
            print("Rüstung kann nicht negativ sein!")
            print("################################")
        else:
            self._ruestung = wert

    ### Konstruktor ###
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung):
        """Initialisiert einen Krieger mit den angegebenen Attributen."""
        self.name = name
        self.lebenspunkte = lebenspunkte
        self.angriffskraft = angriffskraft
        self.ruestung = ruestung

    def angreifen(self, gegner):
        """Führt einen Angriff auf einen anderen Krieger aus und zieht dessen Lebenspunkte ab."""
        schaden = self.angriffskraft - gegner.ruestung
        if schaden > 0:
            gegner.lebenspunkte -= schaden
            print(f"{self.name} greift {gegner.name} an und fügt {schaden} Schaden zu!")
            print("#########################################################")
        else:
            print(f"{self.name} greift {gegner.name} an, aber der Angriff hat keinen Schaden verursacht!")
            print("###########################################################################")

    def verteidigen(self):
        """Erhöht die Rüstung des Kriegers."""
        self.ruestung += 5
        print(f"{self.name} verteidigt sich und erhöht seine Rüstung auf {self.ruestung}.")
        print("#####################################################################")
    
    def checkStatus(self):
        print(f"############## {self.name} ###############")
        print("Lebenspunkte: ", self.lebenspunkte)
        print("Angriffskraft: ", self.angriffskraft)
        print("Rüstung: ", self.ruestung)
        print(f"##########################################")


class Heiler(Krieger):
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung, heilkraft):
        """Initialisiert einen Heiler mit zusätzlicher Heilkraft."""
        super().__init__(name, lebenspunkte, angriffskraft, ruestung)
        self.heilkraft = heilkraft

    def heilen(self, ziel):
        """Heilt einen anderen Krieger oder sich selbst."""
        if ziel.lebenspunkte <= 0:
            print(f"{ziel.name} ist bereits besiegt und kann nicht geheilt werden!")
            return

        heilung = self.heilkraft
        ziel.lebenspunkte += heilung
        print(f"{self.name} heilt {ziel.name} um {heilung} Lebenspunkte!")
        print("#########################################################")

    def checkStatus(self):
        """Zeigt den Status des Heilers an, inklusive Heilkraft."""
        super().checkStatus()
        print("Heilkraft: ", self.heilkraft)
        print(f"##########################################")


class Magier(Krieger):
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung, magie_kraft):
        """Initialisiert einen Magier mit zusätzlicher Magiekraft."""
        super().__init__(name, lebenspunkte, angriffskraft, ruestung)
        self.magie_kraft = magie_kraft

    def zaubern(self, ziel):
        """Verwendet Magie, um einem Ziel Lebenspunkte zu geben oder zu nehmen."""
        if self.magie_kraft > 0:
            if ziel.lebenspunkte <= 0:
                print(f"{ziel.name} ist bereits besiegt und kann nicht verzaubert werden!")
                return
            
            effekt = self.magie_kraft
            ziel.lebenspunkte += effekt
            print(f"{self.name} verzaubert {ziel.name} und verändert die Lebenspunkte um {effekt}!")
            print("#########################################################")
        else:
            print(f"{self.name} hat keine Magiekraft mehr!")
            print("#########################################################")

    def verschwinden(self):
        """Lässt den Magier verschwinden und regeneriert etwas Lebenspunkte."""
        self.lebenspunkte += 10
        print(f"{self.name} verschwindet und regeneriert 10 Lebenspunkte!")
        print("#########################################################")

    def feuerball(self, ziel):
        """Wirft einen Feuerball auf das Ziel und verursacht Schaden."""
        schaden = self.magie_kraft * 2 - ziel.ruestung
        if schaden > 0:
            ziel.lebenspunkte -= schaden
            print(f"{self.name} wirft einen Feuerball auf {ziel.name} und fügt {schaden} Schaden zu!")
            print("#########################################################")
        else:
            print(f"{self.name}s Feuerball hat keinen Schaden verursacht!")
            print("#########################################################")

    def checkStatus(self):
        """Zeigt den Status des Magiers an, inklusive Magiekraft."""
        super().checkStatus()
        print("Magiekraft: ", self.magie_kraft)
        print(f"##########################################")


class Paladin(Magier):
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung, magie_kraft, reiter_kraft):
        """Initialisiert einen Paladin mit zusätzlicher Reiterkraft."""
        super().__init__(name, lebenspunkte, angriffskraft, ruestung, magie_kraft)
        self.reiter_kraft = reiter_kraft

    def reiten(self):
        """Der Paladin reitet und erhöht seine Angriffskraft und Rüstung."""
        self.angriffskraft += self.reiter_kraft
        self.ruestung += self.reiter_kraft
        print(f"{self.name} reitet und erhöht Angriffskraft und Rüstung um {self.reiter_kraft}!")
        print("#########################################################")

    def checkStatus(self):
        """Zeigt den Status des Paladins an, inklusive Reiterkraft."""
        super().checkStatus()
        print("Reiterkraft: ", self.reiter_kraft)
        print(f"##########################################")
