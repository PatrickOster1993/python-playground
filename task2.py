# Aufgabe 2: Temperaturumrechnung
# Der Benutzer kann entscheiden, ob er von Celsius nach Fahrenheit oder umgekehrt umrechnen möchte.

print("Wählen Sie die Umrechnung:")
print("1: Celsius nach Fahrenheit")
print("2: Fahrenheit nach Celsius")
wahl = input("Bitte wählen Sie 1 oder 2:")

# Exception-Handling für die Eingabe der Wahl
while wahl not in ["1", "2"]:
    print("Ungültige Eingabe. Bitte wählen Sie 1 oder 2.")
    wahl = input("Bitte wählen Sie 1 oder 2:")

# Temperaturabfrage
while True:
    try:
        temperatur = float(input("Bitte geben Sie die Temperatur ein:"))
        break
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl für die Temperatur ein.")

if wahl == "1":
    # Umrechnung von Celsius nach Fahrenheit
    fahrenheit = (temperatur * 9/5) + 32
    print(f"{temperatur} °C sind {fahrenheit} °F")
else:
    # Umrechnung von Fahrenheit nach Celsius
    celsius = (temperatur - 32) * 5/9
    print(f"{temperatur} °F sind {celsius} °C")
