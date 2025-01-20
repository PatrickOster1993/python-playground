from abc import ABC, abstractmethod

class Charakter:
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
        self.name = name
        self.lebenspunkte = lebenspunkte
        self.angriffskraft = angriffskraft
        self.ruestung = ruestung
    
    @abstractmethod
    def angreifen():
        pass

    def checkStatus(self):
        print(f"{self.name} hat noch {self.lebenspunkte} Lebenspunkte.")