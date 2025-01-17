from abc import ABC, abstractmethod 

class Charakter(ABC):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, text):
        self._name = text


    def __init__(self, name, lebenspunkte, angriffskraft, ruestung):
        self.name = name
        self.lebenspunkte = lebenspunkte
        self.angriffskraft = angriffskraft
        self.ruestung = ruestung

    @abstractmethod
    def angreifen():
        pass

    def checkStatus():
        return self.lebenspunkte()


class Magier(Charakter):
    def __init__(self, name, lebenspunkte, angriffskraft, ruestung, mana):
        super().__init__(name, lebenspunkte, angriffskraft, ruestung)
        self.mana = mana

