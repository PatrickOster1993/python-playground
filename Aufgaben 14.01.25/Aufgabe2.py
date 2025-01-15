

# Aufgabe 2 Schreiben Sie ein Programm, das eine Temperatur in Celsius in Fahrenheit umrechnet und dann anschließend
# das Ergebnis in der Konsole ausgibt. Die Umrechnungsformel lautet wie folgt: F = 1.8 * C + 32

while True:

    try:

        def fahrenheit_zu_celsius(fahrenheit):
            return((fahrenheit-32)/1.8)

        def celsius_zu_fahrenheit(celsius):
            return(1.8*celsius+32)

        print("Celsius - Fahrenheit Rechner:")
        print("1. Fahrenheit zu Celsius")
        print("2. Celsius zu Fahrenheit")
        print("3. Prgramm beenden.")
        Auswahl = input("Wie möchten Sie fortfahren? (1. 2. oder 3.)")

        if Auswahl =="1":

            fahrenheit = float(input("Temp. in Fahrenheit eingeben."))
            celsius = fahrenheit_zu_celsius(fahrenheit)
            print("Die Temp. in Celsius betrifft:", celsius, "Grad.")

        elif Auswahl =="2":

            celsius = float(input("Temp. in Celcius eingeben."))
            fahrenheit = celsius_zu_fahrenheit(celsius)
            print("Die Temp. in Fahrenheit betrifft:", fahrenheit, "Grad.")

        elif Auswahl =="3":
            print("Programm beendet.")
            break

        else:
            print("Ungültige Eingabe.")

    except ValueError:
        print("Fehler, gültige Zahl eingeben")

    except Exception as e:
        print(f"Ein unerwahrteter Fehler ist aufgetreten: {e}")

