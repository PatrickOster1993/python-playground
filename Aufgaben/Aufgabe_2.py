# ### Aufgabe 2
# Schreiben Sie ein Programm, das eine Temperatur in **Celsius** in **Fahrenheit** umrechnet und dann anschließend das Ergebnis in der Konsole ausgibt. Die Umrechnungsformel 
# lautet wie folgt: `F = 1.8 * C + 32`

# mit F: Temperatur in **Fahrenheit**;
# sowie C: Temperatur in **Celsius**

# > **Anmerkung**: Geben Sie das Ergebnis bitte als Antwortsatz aus!

print("Wählen Sie die Umrechnungsrichtung:")
print("1: Fahrenheit in Celsius")
print("2: Celsius in Fahrenheit")

wahl = input("Geben Sie 1 für fahrenheit in celsius oder 2 für celsius in fahrenheit ein: ")

if wahl == "1":
    fahrenheit = float(input("Geben Sie die Temperatur in Fahrenheit ein: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{fahrenheit}°F sind umgerechnet {celsius}°C.")
elif wahl == "2":
    celsius = float(input("Geben Sie die Temperatur in Celsius ein: "))
    fahrenheit = 1.8 * celsius + 32
    print(f"{celsius}°C sind umgerechnet {fahrenheit}°F.")
else:
    print("Ungültige Eingabe. Geben Sie 1 oder 2 ein.")