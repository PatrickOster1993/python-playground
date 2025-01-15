# Aufgabe 4: Einfache Kalkulation
# Der Benutzer gibt zwei Zahlen ein und wählt eine Operation (Addition, Subtraktion, Multiplikation, Division).

print("Wählen Sie eine Operation:")
print("1: Addition")
print("2: Subtraktion")
print("3: Multiplikation")
print("4: Division")
wahl = input("Bitte wählen Sie 1, 2, 3 oder 4:")

# Exception-Handling für die Wahl der Operation
while wahl not in ["1", "2", "3", "4"]:
    print("Ungültige Eingabe. Bitte wählen Sie 1, 2, 3 oder 4.")
    wahl = input("Bitte wählen Sie 1, 2, 3 oder 4:")

# Eingabe der Zahlen
while True:
    try:
        zahl1 = float(input("Bitte geben Sie die erste Zahl ein:"))
        zahl2 = float(input("Bitte geben Sie die zweite Zahl ein:"))
        break
    except ValueError:
        print("Bitte geben Sie gültige Zahlen ein.")

# Durchführung der gewählten Operation
if wahl == "1":
    ergebnis = zahl1 + zahl2
    operation = "Addition"
elif wahl == "2":
    ergebnis = zahl1 - zahl2
    operation = "Subtraktion"
elif wahl == "3":
    ergebnis = zahl1 * zahl2
    operation = "Multiplikation"
else:
    if zahl2 == 0:
        print("Division durch Null ist nicht erlaubt.")
    else:
        ergebnis = zahl1 / zahl2
        operation = "Division"
        print(f"Das Ergebnis der {operation} von {zahl1} und {zahl2} ist {ergebnis}.")
