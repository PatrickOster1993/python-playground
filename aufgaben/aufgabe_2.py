#Neuer Code
# Lambda-Funktionen zur Umrechnung
get_fahrenheit_by_celsius = lambda celsius: 1.8 * celsius + 32
get_celsius_by_fahrenheit = lambda fahrenheit: (fahrenheit - 32) / 1.8

# Hauptprogramm mit Abfrage
def main():
    print("Willkommen zum Temperaturumrechner!")
    print("1: Celsius in Fahrenheit umrechnen")
    print("2: Fahrenheit in Celsius umrechnen")

    try:
        auswahl = int(input("Bitte geben Sie 1 oder 2 ein: "))

        if auswahl == 1:
            celsius = float(input("Bitte geben Sie die Temperatur in Celsius ein: "))
            fahrenheit = get_fahrenheit_by_celsius(celsius)
            print(f"Die Temperatur von {celsius}°C entspricht {fahrenheit:.2f}°F.")

        elif auswahl == 2:
            fahrenheit = float(input("Bitte geben Sie die Temperatur in Fahrenheit ein: "))
            celsius = get_celsius_by_fahrenheit(fahrenheit)
            print(f"Die Temperatur von {fahrenheit}°F entspricht {celsius:.2f}°C.")

        else:
            print("Fehler: Bitte geben Sie entweder 1 oder 2 ein.")

    except ValueError:
        print("Fehler: Bitte geben Sie eine gültige Zahl ein.")

    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

# Programm starten
if __name__ == "__main__":
    main()

"""
Alter Code
# get_fahrenheit_by_celsius = lambda celsius: 1.8 * celsius + 32

# # Alternative:
# # def get_fahrenheit_by_celsius(celsius):
#     # return (1.8 * celsius + 32)

# try:
#     celsius = float(input("Bitte geben Sie die Temperatur in Celsius ein: "))
#     fahrenheit = get_fahrenheit_by_celsius(celsius)

#     print(f"Die Temperatur von {celsius}°C entspricht {fahrenheit:.2f}°F.")

# except ValueError:
#     print("Fehler: Bitte geben Sie eine gültige Zahl ein.")
    
# except Exception as e:
#     print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
"""