# ### Aufgabe 2
# Schreiben Sie ein Programm, das eine Temperatur in **Celsius** in **Fahrenheit** umrechnet und dann anschließend das Ergebnis in der Konsole ausgibt. Die Umrechnungsformel lautet wie folgt: `F = 1.8 * C + 32`

# mit F: Temperatur in **Fahrenheit**;
# sowie C: Temperatur in **Celsius**

# > **Anmerkung**: Geben Sie das Ergebnis bitte als Antwortsatz aus!

print("Aufgabe 2")
print("Bitte geben Sie die Temperatur in Celsius ein.")
print("Temperatur in Celsius:")
celsius = float(input())
fahrenheit = 1.8 * celsius + 32
print("Die Temperatur in Fahrenheit beträgt " + str(fahrenheit) + " Grad Fahrenheit.")
