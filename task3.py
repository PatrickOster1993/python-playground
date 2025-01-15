# Aufgabe 3: Berechnung der Fakultät
# Der Benutzer gibt eine Zahl ein, und das Programm berechnet die Fakultät unter Verwendung von Exception-Handling.

def berechne_fakultaet(n):
    if n < 0:
        raise ValueError("Die Fakultät ist für negative Zahlen nicht definiert.")
    elif n == 0:
        return 1
    else:
        fakultaet = 1
        for i in range(1, n + 1):
            fakultaet *= i
        return fakultaet

while True:
    try:
        zahl = int(input("Bitte geben Sie eine positive ganze Zahl ein:"))
        if zahl < 0:
            print("Bitte eine positive Zahl eingeben.")
        else:
            break
    except ValueError:
        print("Bitte geben Sie eine gültige ganze Zahl ein.")

resultat = berechne_fakultaet(zahl)
print(f"Die Fakultät von {zahl} ist {resultat}.")
