# def fahrenheit_zu_celsius(fahrenheit):
#     return (fahrenheit - 32) / 1.8

# def celsius_zu_fahrenheit(celsius):
#     return 1.8 * celsius + 32

# print("Celsius - Fahrenheit Rechner:")
# print("1. Fahrenheit zu Celsius")
# print("2. Celsius zu Fahrenheit")
# auswahl = input("Wie möchten Sie fortfahren? (1 oder 2): ")

# if auswahl == "1":
#     fahrenheit = float(input("Temperatur in Fahrenheit eingeben: "))
#     celsius = fahrenheit_zu_celsius(fahrenheit)
#     print(f"Die Temperatur in Celsius beträgt: {celsius:.2f} Grad.")
# elif auswahl == "2":
#     celsius = float(input("Temperatur in Celsius eingeben: "))
#     fahrenheit = celsius_zu_fahrenheit(celsius)
#     print(f"Die Temperatur in Fahrenheit beträgt: {fahrenheit:.2f} Grad.")
# else:
#     print("Ungültige Eingabe.")

get_fahrenheit_by_celsius = lambda celsius: 1.8 * celsius + 32

try:

    celsius = float(input("Bitte geben Sie die Temperatur in Celsius ein: ") )
    fahrenheit = get_fahrenheit_by_celsius(celsius)

    print(f"Die Temperafur von {celsius}C entspricht {fahrenheit :. 2f}°F.")

except ValueError:
    print("Fehler: Bitte geben Sie eine gültige Zahl ein.")

except Exception as e:
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")