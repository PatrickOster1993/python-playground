# ### Aufgabe 2
# Schreiben Sie ein Programm, das eine Temperatur in **Celsius** in **Fahrenheit** umrechnet und dann anschließend das Ergebnis in der Konsole ausgibt. Die Umrechnungsformel 
# lautet wie folgt: `F = 1.8 * C + 32`

# mit F: Temperatur in **Fahrenheit**;
# sowie C: Temperatur in **Celsius**

# > **Anmerkung**: Geben Sie das Ergebnis bitte als Antwortsatz aus!

def celsius_in_fahrenheit(celsius):
    return 1.8 * celsius + 32

def fahrenheit_in_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

print("Wählen Sie die Umrechnungsrichtung:")
print("1: Celsius in Fahrenheit")
print("2: Fahrenheit in Celsius")

wahl = input("Geben Sie 1 oder 2 ein: ")

if wahl == "1":
    celsius = float(input("Geben Sie die Temperatur in Celsius ein: "))
    fahrenheit = celsius_in_fahrenheit(celsius) 
elif wahl == "2":
    fahrenheit = float(input("Geben Sie die Temperatur in Fahrenheit ein: "))
    celsius = fahrenheit_in_celsius(fahrenheit)  
    print(f"{fahrenheit}°F entsprechen {celsius}°C.")
else:
    print("Ungültige Eingabe. Bitte starten Sie das Programm neu und wählen Sie 1 oder 2.")
