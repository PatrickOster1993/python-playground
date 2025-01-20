class Smartphone:
    @property
    def number(self):
        print("Getter wird aufgerufen")
        self.counter += 1
        return self._number

    @number.setter
    def number(self, text):
        print("Setter wird aufgerufen")
        self.counter += 1
        self._number = text

    def __init__(self, name, nummer):
        print("Konstruktor wird aufgerufen")
        self.counter = 0
        self._number = nummer
        if self.isIphone(name):
            self.counter += 1

    def isIphone(self, name):
        print("isIphone wird aufgerufen")
        self.counter += 1
        return "iphone" in name.lower()

# Test-Code
print("\n=== Test startet ===")
mein_smartphone = Smartphone("iPhone", "987654321")  # WICHTIG: Gleiche Nummer wie neue_number

try:
    print("\n=== Try-Block startet ===")
    neue_number = "987654321"  # WICHTIG: Gleiche Nummer wie in __init__
    alte_number = mein_smartphone.number
    print(f"alte_number: {alte_number}")
    print(f"neue_number: {neue_number}")
    if neue_number != alte_number:  # Diese Bedingung ist jetzt FALSE!
        print("Nummern sind unterschiedlich")
        mein_smartphone.number = neue_number  # Dies wird NICHT ausgeführt!
except:
    print("\n=== Exception-Block ===")
    mein_smartphone.counter += 1
else:
    print("\n=== Else-Block ===")
    mein_smartphone.counter += 1
finally:
    print("\n=== Finally-Block ===")
    print(f"Finaler Counter-Stand: {mein_smartphone.counter}")
