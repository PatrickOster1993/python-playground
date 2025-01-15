# Aufgabe 1

# Variablen deklarieren und als Eingabe initialisieren
Name = input("Gib deinen Namen ein. ")
Alter = input("Gib deinen Namen ein. ")
Lieblingsessen = input("Gib dein Lieblingsessen ein. ")
# In einem Satz ausgeben lassen
print(f"Mein Name ist {Name}, ich bin {Alter} Jahre alt und ich liebe {Lieblingsessen}")


# Aufgabe 2

def CelsiusToFahrenheit()
    return (1.8 * Celsiuszahl) + 32

def FahrenheitToCelsius()
    return (Fahrenheitszahl - 32) * 5/9

print("Entscheide dich für den Fahrenheitsrechner oder den Celsiusrechner. ")
print("A = Fahrenheitsrechner. ")
print("B = Celsiusrechner. ")
Eingabe = input("")


if Eingabe == "A"
    print("Du hast dich für den Fahrenheitsrechner entschieden.")
    Celsiuszahl = float(input("Bitte geben Sie Ihre Temperatur in Celsius ein. "))
    Ergebnis = CelsiusToFahrenheit()
    print(f"Deine eingegebene Celsius Zahl {Celsiuszahl} ist in Fahrenheit {Ergebnis}. ")

elif Eingabe == "B"
    print("Du hast dich für den Celsiusrechner entschieden.")
    Fahrenheitszahl = float(input("Bitte geben Sie Ihre Temperatur in Fahrenheit ein. "))
    Ergebnis2 = FahrenheitToCelsius()
    print(f"Deine eingegebene Fahrenheits Zahl {Fahrenheitszahl} ist in Celsius {Ergebnis2}. ")

else
    print("Ungültige Auswahl, bitte entscheide dich zwischen den beiden Optionen A oder B. ")
    break
